Exceptions
==========

imdbio defines a clean exception hierarchy for predictable error handling.

.. code-block:: python

    from imdbio import ImdbioError, HTTPError, WAFError, GraphQLError, ParseError

    try:
        movie = get_movie("tt0133093")
    except WAFError as e:
        print(f"WAF blocked: {e.status_code}")
    except HTTPError as e:
        print(f"HTTP error: {e.status_code}")
    except ParseError as e:
        print(f"Parse failed: {e}")
    except ImdbioError as e:
        print(f"Generic imdbio error: {e}")

Hierarchy
---------

- :class:`~imdbio.exceptions.ImdbioError` (base)
   - :class:`~imdbio.exceptions.HTTPError` — non-200 HTTP responses
      - :class:`~imdbio.exceptions.WAFError` — HTTP 202 from AWS WAF
   - :class:`~imdbio.exceptions.GraphQLError` — GraphQL API failures
   - :class:`~imdbio.exceptions.ParseError` — HTML/JSON parsing failures
