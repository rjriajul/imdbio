
from imdbio import set_proxy, get_proxy, get_movie

# Configure a proxy for all requests. Format: scheme://user:pass@host:port
set_proxy("http://user:pass@proxy.example.com:8080")

print(f"Active proxy: {get_proxy()}")

try:
    movie = get_movie("tt0133093")  # The Matrix
    print(f"\nFetched via proxy: {movie.title} ({movie.year}) - {movie.rating}")
except Exception as e:
    print(f"Error: {e}")

# Disable the proxy again — later requests go out directly.
set_proxy(None)
print(f"\nProxy after reset: {get_proxy()}")

# Invalid proxy URLs raise ValueError immediately, so you find out at
# configuration time rather than on the first request.
try:
    set_proxy("not-a-valid-proxy")
except ValueError as e:
    print(f"\nRejected invalid proxy: {e}")
