People
======

Get person details
------------------

.. code-block:: python

    from imdbio import get_name

    person = get_name("nm0000206")  # Brad Pitt
    print(person.name, person.birth_date, person.death_date)
    print(person.bio, person.primary_profession)
    print(person.knownfor)

Filmography
-----------

.. code-block:: python

    from imdbio import get_filmography

    filmography = get_filmography("nm0000206")
    for role, films in filmography.items():
        print(f"\nRole: {role}")
        for film in films:
            print(f"  {film.title} ({film.year}) [{film.imdbId}]")
