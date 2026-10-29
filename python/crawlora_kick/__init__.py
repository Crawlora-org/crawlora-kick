"""Typed Kick client for the Crawlora hosted API."""

from .platform import KickClient, AsyncKickClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = KickClient
AsyncClient = AsyncKickClient
__version__ = '0.1.0'
DISPLAY_NAME = 'Kick'
PLATFORM = 'kick'
CONTRACT_REVISION = 'sha256:21aa0d1aad656980f5ea6effcebad59951eac7af94ef33ab23888a3707f0ba5a'

__all__ = [
    "KickClient", "AsyncKickClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
