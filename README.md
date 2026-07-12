[![PyPI Downloads](https://static.pepy.tech/badge/imdbio)](https://pepy.tech/projects/imdbio)
[![PyPI Version](https://img.shields.io/pypi/v/imdbio?style=flat-square)](https://pypi.org/project/imdbio/)
[![Python Versions](https://img.shields.io/pypi/pyversions/imdbio?style=flat-square)](https://pypi.org/project/imdbio/)

# imdbio

**Your personal gateway to IMDb data** — no API keys required.

## Features

- Search movies, series, and people by name or title
- Detailed movie info: cast, crew, ratings, box office, company credits
- TV series support with seasons and episodes
- Person details with biography, filmography and images
- Localized results in multiple languages (global or per-request)
- User reviews, trivia, parental guide, awards info
- Typed Pydantic models
- Built-in caching

## Installation

```bash
pip install imdbio
```

## Quick Start

```python
from imdbio import search_title, get_movie, get_name

# Search for a title
results = search_title("The Matrix")
for movie in results.titles:
    print(f"{movie.title} ({movie.year}) - {movie.imdb_id}")

# Get movie details
movie = get_movie("0133093")
print(movie.title, movie.year, movie.rating, movie.kind)

# Get person details
person = get_name("nm0000206")
print(person.name, person.birth_date)

# Series example
from imdbio import get_season_episodes
episodes = get_season_episodes("tt1520211", season=1)  # Walking Dead
for ep in episodes[:3]:
    print(ep.title, ep.rating)
```

📝 More examples in the [examples](examples/) folder.

## Using a proxy

Route **all** imdbio requests — including the AWS WAF challenge solver — through
a proxy with `set_proxy`. This is handy for rotating IPs or getting around an IP
that IMDb's WAF has started blocking (HTTP 202).

```python
from imdbio import set_proxy, get_movie

# scheme://user:pass@host:port  (credentials optional)
set_proxy("http://user:pass@proxy.example.com:8080")

movie = get_movie("tt0133093")  # fetched through the proxy

# Disable proxying again
set_proxy(None)
```

Supported schemes: `http`, `https`, `socks4`, `socks5`, `socks5h`
(socks proxies require the socks extras of niquests / curl_cffi). Invalid proxy
URLs raise `ValueError` immediately. See [examples/example_proxy.py](examples/example_proxy.py).

## Why choose imdbio?

- Clean structured data via Pydantic models
- No API keys or external dependencies
- Powered by niquests and lxml
- Ideal for scripts and data analysis

## Disclaimer

Not affiliated with IMDb Inc. See [DISCLAIMER](DISCLAIMER.txt).

## License

MIT — see [LICENSE](LICENSE).
