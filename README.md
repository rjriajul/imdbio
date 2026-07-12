[![PyPI Downloads](https://static.pepy.tech/badge/imdbio)](https://pepy.tech/projects/imdbio)
[![PyPI Version](https://img.shields.io/pypi/v/imdbio?style=flat-square)](https://pypi.org/project/imdbio/)
[![Python Versions](https://img.shields.io/pypi/pyversions/imdbio?style=flat-square)](https://pypi.org/project/imdbio/)
[![Docs](https://img.shields.io/badge/docs-imdbio-blue?style=flat-square)](https://rjriajul.github.io/imdbio/)

# imdbio

**Your personal gateway to IMDb data** — no API keys required.

imdbio is a Python library for querying movie, TV series, and celebrity
information from IMDb. It provides structured, typed results without
requiring any API keys or external services.

- Search movies, TV series, and people by title or name
- Cast, crew, ratings, box office, and company credits
- TV series seasons and episode listings
- User reviews, trivia, parental guide, and awards
- Localized results in multiple languages
- Proxy support for IP rotation
- Typed Pydantic models with built-in caching

```bash
pip install imdbio
```

```python
from imdbio import search_title

results = search_title("The Matrix")
print(results.titles[0].title, results.titles[0].year)
```

📘 Full docs: https://rjriajul.github.io/imdbio/
📝 Examples: [examples/](examples/)

## Why choose imdbio?

- Clean structured data via Pydantic models
- No API keys or external dependencies
- Powered by niquests and lxml
- Ideal for scripts and data analysis

## Disclaimer

Not affiliated with IMDb Inc. See [DISCLAIMER](DISCLAIMER.txt).

## License

MIT — see [LICENSE](LICENSE).
