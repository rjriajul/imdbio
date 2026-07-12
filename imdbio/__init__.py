import logging

from .services import (
    get_movie,
    search_title,
    get_name,
    get_episodes,
    get_all_episodes,
    get_season_episodes,
    get_akas,
    get_reviews,
    get_trivia,
    get_parental_guide,
    get_filmography,
    get_all_interests,
    get_media_gallery,
    TitleType,
)
from .proxy import (
    set_proxy,
    get_proxy,
)
from .models import (
    TitleMediaGallery,
    TitleMediaItem,
)
from .exceptions import (
    ImdbioError,
    HTTPError,
    WAFError,
    GraphQLError,
    ParseError,
)

__all__ = [
    "get_movie",
    "search_title",
    "get_name",
    "get_episodes",
    "get_all_episodes",
    "get_season_episodes",
    "get_akas",
    "get_reviews",
    "get_trivia",
    "get_parental_guide",
    "get_filmography",
    "get_all_interests",
    "get_media_gallery",
    "TitleMediaGallery",
    "TitleMediaItem",
    "TitleType",
    # exceptions
    "ImdbioError",
    "HTTPError",
    "WAFError",
    "GraphQLError",
    "ParseError",
    # proxy
    "set_proxy",
    "get_proxy",
]

# setup library logging
logging.getLogger(__name__).addHandler(logging.NullHandler())
