Proxy Support
=============

Route all imdbio requests — including the AWS WAF challenge solver —
through a proxy. This is useful for rotating IPs or bypassing IP blocks.

.. code-block:: python

    from imdbio import set_proxy, get_movie

    # scheme://user:pass@host:port  (credentials optional)
    set_proxy("http://user:pass@proxy.example.com:8080")

    movie = get_movie("tt0133093")  # fetched through the proxy

    # Disable proxying again
    set_proxy(None)

Check the current proxy:

.. code-block:: python

    from imdbio import get_proxy

    print(get_proxy())  # None or the proxy URL

Supported proxy schemes:

- ``http``
- ``https``
- ``socks4``
- ``socks5``
- ``socks5h``

Socks proxies require the ``socks`` extras (install with
``pip install niquests[socks]``).

Invalid proxy URLs raise ``ValueError`` immediately.
