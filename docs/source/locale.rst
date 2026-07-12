Localization
============

imdbio supports fetching localized content from IMDb in multiple languages.

Per-request locale
------------------

.. code-block:: python

    from imdbio import get_movie, search_title

    movie = get_movie("tt0133093", locale="it")
    results = search_title("The Matrix", locale="es")

Global locale
-------------

Set a default locale so you don't have to pass it every time:

.. code-block:: python

    from imdbio.locale import set_locale

    set_locale("it")  # All subsequent requests use Italian

    movie = get_movie("tt0133093")  # Italian
    person = get_name("nm0000206")  # Italian
