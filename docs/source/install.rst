Installation
============

.. code-block:: bash

    pip install imdbio

Dependencies
------------

imdbio requires **Python 3.10+** and uses:

- ``niquests`` — HTTP client
- ``lxml`` — HTML parsing
- ``pydantic`` — typed models
- ``jmespath`` — JSON querying
- ``curl_cffi`` — TLS fingerprinting for the AWS WAF solver
- ``cryptography`` — challenge payload encryption

Development
-----------

.. code-block:: bash

    git clone https://github.com/rjriajul/imdbio
    cd imdbio
    pip install uv
    uv sync --frozen --extra dev
    uv run poe test
