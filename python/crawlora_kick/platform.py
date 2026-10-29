"""Platform-specific convenience clients."""
from __future__ import annotations
from typing import Any
from .client import CrawloraClient
from .async_client import AsyncCrawloraClient

class KickClient(CrawloraClient):
    """Synchronous Kick API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-kick-python/0.1.0')
        super().__init__(*args, **kwargs)

    def categories(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('kick-categories', params, response_type=response_type, timeout=timeout, headers=headers)

    def category_clips(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('kick-category-clips', params, response_type=response_type, timeout=timeout, headers=headers)

    def channel(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('kick-channel', params, response_type=response_type, timeout=timeout, headers=headers)

    def channel_chatroom(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('kick-channel-chatroom', params, response_type=response_type, timeout=timeout, headers=headers)

    def channel_clips(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('kick-channel-clips', params, response_type=response_type, timeout=timeout, headers=headers)

    def channel_emotes(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('kick-channel-emotes', params, response_type=response_type, timeout=timeout, headers=headers)

    def channel_links(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('kick-channel-links', params, response_type=response_type, timeout=timeout, headers=headers)

    def channel_streams(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('kick-channel-streams', params, response_type=response_type, timeout=timeout, headers=headers)

    def channel_videos(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('kick-channel-videos', params, response_type=response_type, timeout=timeout, headers=headers)

    def clip(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('kick-clip', params, response_type=response_type, timeout=timeout, headers=headers)

    def clips(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('kick-clips', params, response_type=response_type, timeout=timeout, headers=headers)

    def drops(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('kick-drops', params, response_type=response_type, timeout=timeout, headers=headers)

    def gifts(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('kick-gifts', params, response_type=response_type, timeout=timeout, headers=headers)

    def languages(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('kick-languages', params, response_type=response_type, timeout=timeout, headers=headers)

    def livestreams(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('kick-livestreams', params, response_type=response_type, timeout=timeout, headers=headers)

    def search_categories(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('kick-search-categories', params, response_type=response_type, timeout=timeout, headers=headers)

    def search_channels(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('kick-search-channels', params, response_type=response_type, timeout=timeout, headers=headers)

    def subcategories(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('kick-subcategories', params, response_type=response_type, timeout=timeout, headers=headers)

    def subcategory(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('kick-subcategory', params, response_type=response_type, timeout=timeout, headers=headers)

    def top_channels(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('kick-top-channels', params, response_type=response_type, timeout=timeout, headers=headers)

    def video(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('kick-video', params, response_type=response_type, timeout=timeout, headers=headers)

class AsyncKickClient(AsyncCrawloraClient):
    """Asynchronous Kick API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-kick-python/0.1.0')
        super().__init__(*args, **kwargs)

    async def categories(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('kick-categories', params, response_type=response_type, timeout=timeout, headers=headers)

    async def category_clips(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('kick-category-clips', params, response_type=response_type, timeout=timeout, headers=headers)

    async def channel(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('kick-channel', params, response_type=response_type, timeout=timeout, headers=headers)

    async def channel_chatroom(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('kick-channel-chatroom', params, response_type=response_type, timeout=timeout, headers=headers)

    async def channel_clips(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('kick-channel-clips', params, response_type=response_type, timeout=timeout, headers=headers)

    async def channel_emotes(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('kick-channel-emotes', params, response_type=response_type, timeout=timeout, headers=headers)

    async def channel_links(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('kick-channel-links', params, response_type=response_type, timeout=timeout, headers=headers)

    async def channel_streams(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('kick-channel-streams', params, response_type=response_type, timeout=timeout, headers=headers)

    async def channel_videos(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('kick-channel-videos', params, response_type=response_type, timeout=timeout, headers=headers)

    async def clip(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('kick-clip', params, response_type=response_type, timeout=timeout, headers=headers)

    async def clips(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('kick-clips', params, response_type=response_type, timeout=timeout, headers=headers)

    async def drops(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('kick-drops', params, response_type=response_type, timeout=timeout, headers=headers)

    async def gifts(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('kick-gifts', params, response_type=response_type, timeout=timeout, headers=headers)

    async def languages(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('kick-languages', params, response_type=response_type, timeout=timeout, headers=headers)

    async def livestreams(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('kick-livestreams', params, response_type=response_type, timeout=timeout, headers=headers)

    async def search_categories(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('kick-search-categories', params, response_type=response_type, timeout=timeout, headers=headers)

    async def search_channels(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('kick-search-channels', params, response_type=response_type, timeout=timeout, headers=headers)

    async def subcategories(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('kick-subcategories', params, response_type=response_type, timeout=timeout, headers=headers)

    async def subcategory(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('kick-subcategory', params, response_type=response_type, timeout=timeout, headers=headers)

    async def top_channels(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('kick-top-channels', params, response_type=response_type, timeout=timeout, headers=headers)

    async def video(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('kick-video', params, response_type=response_type, timeout=timeout, headers=headers)
