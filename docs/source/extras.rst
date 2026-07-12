Extras
======

Alternate titles (AKAs)
-----------------------

.. code-block:: python

    from imdbio import get_akas

    akas = get_akas("tt0133093")
    for aka in akas["akas"][:5]:
        print(f"{aka.title} ({aka.country_name})")

User reviews
------------

.. code-block:: python

    from imdbio import get_reviews

    reviews = get_reviews("tt0133093")
    for review in reviews[:3]:
        print(f"Rating: {review['authorRating']}/10")
        print(f"Summary: {review['summary']}")
        print(f"Spoiler: {review['spoiler']}")
        print("---")

Trivia
------

.. code-block:: python

    from imdbio import get_trivia

    trivia = get_trivia("tt0133093")
    for fact in trivia[:3]:
        print(fact['body'][:200] + "...")

Parental guide
--------------

.. code-block:: python

    from imdbio import get_parental_guide

    pg = get_parental_guide("tt0133093")
    for cat in pg.categories:
        print(cat)
        for txt in cat.category_texts_list(spolier=True):
            print(f"  - {txt.text}")

Awards
------

.. code-block:: python

    from imdbio import get_movie

    movie = get_movie("tt0133093")
    if movie.awards:
        print("Wins:", movie.awards.wins)
        print("Nominations:", movie.awards.nominations)
        if movie.awards.prestigious_award:
            print("Prestigious:", movie.awards.prestigious_award)

Media gallery
-------------

.. code-block:: python

    from imdbio import get_media_gallery

    gallery = get_media_gallery("tt0133093")
    for item in gallery.items:
        print(item.url, item.type, item.caption)

Interests
---------

.. code-block:: python

    from imdbio import get_all_interests

    interests = get_all_interests("tt0133093")
    print(interests)
