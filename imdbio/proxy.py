import logging
from typing import Optional, Dict
from urllib.parse import urlparse

logger = logging.getLogger(__name__)

# Schemes we accept for a proxy URL. http/https are always usable; socks
# schemes require the optional socks extras of niquests / curl_cffi.
_ALLOWED_SCHEMES = {"http", "https", "socks4", "socks5", "socks5h"}

# Process-wide proxy URL. None means "no proxy".
_proxy: Optional[str] = None


def _validate_proxy(proxy_url: str) -> str:
    """Validate a proxy URL and return it normalized (stripped).

    Raises ValueError if the URL is malformed or uses an unsupported scheme.
    """
    if not isinstance(proxy_url, str) or not proxy_url.strip():
        raise ValueError(
            "Proxy must be a non-empty string, e.g. "
            "'http://user:pass@host:port'."
        )
    proxy_url = proxy_url.strip()
    parsed = urlparse(proxy_url)

    scheme = (parsed.scheme or "").lower()
    if scheme not in _ALLOWED_SCHEMES:
        raise ValueError(
            f"Unsupported proxy scheme {parsed.scheme!r}. "
            f"Use one of: {', '.join(sorted(_ALLOWED_SCHEMES))}."
        )
    if not parsed.hostname:
        raise ValueError(f"Proxy URL {proxy_url!r} is missing a host.")
    if parsed.port is None:
        raise ValueError(f"Proxy URL {proxy_url!r} is missing a port.")

    return proxy_url


def set_proxy(proxy_url: Optional[str]) -> None:
    """Set (or clear) the global proxy used for all imdbio requests.

    Args:
        proxy_url: A proxy URL such as ``"http://user:pass@host:port"``. Supported
            schemes are http, https, socks4, socks5 and socks5h. Pass ``None`` to
            disable proxying.

    Raises:
        ValueError: If ``proxy_url`` is not ``None`` and is not a valid proxy URL.
    """
    global _proxy
    if proxy_url is None:
        _proxy = None
        logger.debug("Proxy disabled")
        return
    _proxy = _validate_proxy(proxy_url)
    logger.debug("Proxy set to %s", _proxy)


def get_proxy() -> Optional[str]:
    """Return the currently configured proxy URL, or ``None`` if unset."""
    return _proxy


def get_proxies() -> Optional[Dict[str, str]]:
    """Return a ``proxies`` mapping suitable for niquests / curl_cffi.

    Returns ``None`` when no proxy is configured, so callers can pass the result
    straight through as ``proxies=...`` without changing behaviour.
    """
    if not _proxy:
        return None
    return {"http": _proxy, "https": _proxy}
