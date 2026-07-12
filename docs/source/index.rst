imdbio
======

**Your personal gateway to IMDb data** — no API keys required.

``imdbio`` is a Python library for querying IMDb data. Search for movies,
series and people, get detailed information, reviews, trivia, parental
guides, and more — all through a clean typed API.

.. code-block:: python

    from imdbio import search_title, get_movie

    results = search_title("The Matrix")
    for movie in results.titles:
        print(f"{movie.title} ({movie.year}) - {movie.rating}")

    movie = get_movie("tt0133093")
    print(movie.title, movie.year, movie.kind)

.. toctree::
    :maxdepth: 2
    :caption: Getting Started

    install
    quickstart

.. toctree::
    :maxdepth: 2
    :caption: Usage Guide

    movies
    people
    extras
    locale
    proxy
    exceptions

.. toctree::
    :maxdepth: 2
    :caption: API Reference

    api
