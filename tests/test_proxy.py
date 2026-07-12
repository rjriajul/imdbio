import pytest
from types import SimpleNamespace

import imdbio
from imdbio import proxy
from imdbio import services


@pytest.fixture(autouse=True)
def _reset_proxy():
    """Ensure every test starts and ends with no proxy configured."""
    proxy.set_proxy(None)
    yield
    proxy.set_proxy(None)


# ── set_proxy / get_proxy / get_proxies ──────────────────────────────────────


def test_set_and_get_proxy():
    proxy.set_proxy("http://user:pass@host:8080")
    assert proxy.get_proxy() == "http://user:pass@host:8080"


def test_set_proxy_none_clears():
    proxy.set_proxy("http://host:8080")
    assert proxy.get_proxy() is not None
    proxy.set_proxy(None)
    assert proxy.get_proxy() is None


def test_get_proxies_returns_none_when_unset():
    assert proxy.get_proxies() is None


def test_get_proxies_maps_http_and_https():
    proxy.set_proxy("http://host:8080")
    assert proxy.get_proxies() == {
        "http": "http://host:8080",
        "https": "http://host:8080",
    }


def test_set_proxy_strips_whitespace():
    proxy.set_proxy("  http://host:8080  ")
    assert proxy.get_proxy() == "http://host:8080"


@pytest.mark.parametrize("scheme", ["http", "https", "socks4", "socks5", "socks5h"])
def test_set_proxy_accepts_supported_schemes(scheme):
    proxy.set_proxy(f"{scheme}://host:1080")
    assert proxy.get_proxy() == f"{scheme}://host:1080"


# ── validation errors ────────────────────────────────────────────────────────


@pytest.mark.parametrize(
    "bad",
    [
        "",
        "   ",
        "host:8080",             # missing scheme
        "ftp://host:8080",       # unsupported scheme
        "http://host",           # missing port
        "http://:8080",          # missing host
        123,                     # not a string
    ],
)
def test_set_proxy_rejects_invalid(bad):
    with pytest.raises(ValueError):
        proxy.set_proxy(bad)


def test_invalid_proxy_does_not_mutate_state():
    proxy.set_proxy("http://good:8080")
    with pytest.raises(ValueError):
        proxy.set_proxy("bad")
    # previous valid value is preserved
    assert proxy.get_proxy() == "http://good:8080"


# ── proxy is forwarded to niquests ───────────────────────────────────────────


def test_request_handler_forwards_proxy(monkeypatch):
    captured = {}

    def fake_get(url, headers=None, cookies=None, proxies=None):
        captured["proxies"] = proxies
        return SimpleNamespace(status_code=200, text="", content=b"")

    monkeypatch.setattr(services.niquests, "get", fake_get)
    proxy.set_proxy("http://host:8080")

    services.request_handler("https://www.imdb.com/title/tt0133093/reference")

    assert captured["proxies"] == {
        "http": "http://host:8080",
        "https": "http://host:8080",
    }


def test_request_handler_no_proxy_by_default(monkeypatch):
    captured = {}

    def fake_get(url, headers=None, cookies=None, proxies=None):
        captured["proxies"] = proxies
        return SimpleNamespace(status_code=200, text="", content=b"")

    monkeypatch.setattr(services.niquests, "get", fake_get)

    services.request_handler("https://www.imdb.com/title/tt0133093/reference")

    assert captured["proxies"] is None


def test_request_graphql_forwards_proxy(monkeypatch):
    captured = {}

    def fake_post(url, headers=None, json=None, proxies=None):
        captured["proxies"] = proxies
        return SimpleNamespace(status_code=200, json=lambda: {"data": {}})

    monkeypatch.setattr(services.niquests, "post", fake_post, raising=False)
    proxy.set_proxy("socks5://host:1080")

    services.request_graphql_url({}, "matrix", {"query": "{}"}, services.GRAPHQL_URL)

    assert captured["proxies"] == {
        "http": "socks5://host:1080",
        "https": "socks5://host:1080",
    }


# ── proxy is passed to the AWS solver ─────────────────────────────────────────


def test_get_cookies_passes_proxy_to_solver(monkeypatch):
    captured = {}

    class FakeSolver:
        def __init__(self, user_agent, domain, proxies=None):
            captured["proxies"] = proxies

        def solve(self, text):
            return "fake-token"

    monkeypatch.setattr(services, "AwsSolver", FakeSolver)
    proxy.set_proxy("http://host:8080")

    result = services.get_cookies("<html></html>", services.USER_AGENT)

    assert result == {"aws-waf-token": "fake-token"}
    assert captured["proxies"] == {
        "http": "http://host:8080",
        "https": "http://host:8080",
    }


# ── public API surface ───────────────────────────────────────────────────────


def test_set_proxy_exported_from_package():
    assert imdbio.set_proxy is proxy.set_proxy
    assert imdbio.get_proxy is proxy.get_proxy
    assert "set_proxy" in imdbio.__all__
    assert "get_proxy" in imdbio.__all__
