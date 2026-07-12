Quick Start
===========

Search for a title
------------------

.. code-block:: python

    from imdbio import search_title

    results = search_title("The Matrix")
    for movie in results.titles:
        print(f"{movie.title} ({movie.year}) - {movie.rating} - {movie.imdb_id}")

Get movie details
-----------------

.. code-block:: python

    from imdbio import get_movie

    movie = get_movie("tt0133093")
    print(movie.title, movie.year, movie.rating, movie.kind)
    print(movie.genres, movie.duration, movie.mpaa)

Get person details
------------------

.. code-block:: python

    from imdbio import get_name

    person = get_name("nm0000206")  # Brad Pitt
    print(person.name, person.birth_date, person.primary_profession)

Work with series
----------------

.. code-block:: python

    from imdbio import get_season_episodes

    episodes = get_season_episodes("tt1520211", season=1)  # Walking Dead
    for ep in episodes.episodes[:3]:
        print(ep.title, ep.rating, ep.plot[:80] + "...")
