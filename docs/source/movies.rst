Movies, Series & Episodes
=========================

Searching
---------

Use :func:`~imdbio.services.search_title` to find titles by name:

.. code-block:: python

    from imdbio import search_title, TitleType

    # Basic search
    results = search_title("The Matrix")

    # Exact match
    results = search_title("The Matrix", exact_match=True)

    # Filter by year
    results = search_title("The Matrix", year=1999)

    # Filter by type
    results = search_title("The Matrix", title_type=TitleType.Movies)

    # Multiple types
    results = search_title("The Matrix", title_type=(TitleType.Movies, TitleType.Series))

The result object contains both ``titles`` and ``names``.

Getting movie details
---------------------

.. code-block:: python

    from imdbio import get_movie

    movie = get_movie("tt0133093")

    # Basic info
    print(movie.title, movie.year, movie.rating, movie.kind)
    print(movie.genres, movie.duration, movie.mpaa)
    print(movie.languages, movie.countries)
    print(movie.stars, movie.directors)

    # Series detection
    if movie.is_series():
        print("Series:", movie.info_series)
    elif movie.is_episode():
        print("Episode:", movie.info_episode)

    # Company credits
    for company in movie.company_credits.get("production", []):
        print(f"  {company.name} ({company.country})")

Series and episodes
-------------------

.. code-block:: python

    from imdbio import get_season_episodes, get_all_episodes

    # Episodes for a specific season
    eps = get_season_episodes("tt1520211", season=1)

    # All episodes ever
    all_eps = get_all_episodes("tt1520211")
