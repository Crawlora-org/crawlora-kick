from __future__ import annotations

import sys
from typing import Any, Callable, Iterable, Iterator, Literal, Mapping, overload

if sys.version_info >= (3, 11):
    from typing import NotRequired, Required, TypedDict, Unpack
else:
    from typing_extensions import NotRequired, Required, TypedDict, Unpack

ResponseType = Literal["auto", "json", "text", "stream"]

class CrawloraError(Exception):
    status: int
    code: int | None
    body: Any
    raw_body: str
    headers: Mapping[str, str]
    request_id: str | None
    def __init__(self, message: str, *, status: int = ..., code: int | None = ..., body: Any = ..., raw_body: str = ..., headers: Mapping[str, str] | None = ..., request_id: str | None = ..., cause: BaseException | None = ...) -> None: ...

class CrawloraClientError(CrawloraError): ...
class CrawloraServerError(CrawloraError): ...
class CrawloraNetworkError(CrawloraError): ...

class _RequestOptions(TypedDict, total=False):
    _response_type: ResponseType
    _timeout: float
    _headers: Mapping[str, str]

ModelAppResponse = TypedDict('ModelAppResponse', {
    'code': NotRequired[int],
    'data': NotRequired[Any],
    'msg': NotRequired[Any],
}, total=False)

ModelKickVideoResponseDoc = TypedDict('ModelKickVideoResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelKickVideoResponse],
    'msg': NotRequired[str],
}, total=False)

ModelKickVideoResponse = TypedDict('ModelKickVideoResponse', {
    'categories': NotRequired[list[ModelKickCategoryRef]],
    'channel': NotRequired[ModelKickChannelRef],
    'created_at': NotRequired[str],
    'duration_ms': NotRequired[int],
    'id': NotRequired[int],
    'language': NotRequired[str],
    'mature': NotRequired[bool],
    'started_at': NotRequired[str],
    'status': NotRequired[str],
    'tags': NotRequired[list[str]],
    'thumbnail_url': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
    'uuid': NotRequired[str],
    'viewer_count': NotRequired[int],
    'views': NotRequired[int],
}, total=False)

ModelKickChannelRef = TypedDict('ModelKickChannelRef', {
    'id': NotRequired[int],
    'profile_picture': NotRequired[str],
    'slug': NotRequired[str],
    'url': NotRequired[str],
    'username': NotRequired[str],
    'verified': NotRequired[bool],
}, total=False)

ModelKickCategoryRef = TypedDict('ModelKickCategoryRef', {
    'id': NotRequired[int],
    'name': NotRequired[str],
    'slug': NotRequired[str],
}, total=False)

ModelKickTopChannelsResponseDoc = TypedDict('ModelKickTopChannelsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelKickTopChannelsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelKickTopChannelsResponse = TypedDict('ModelKickTopChannelsResponse', {
    'channels': NotRequired[list[ModelKickChannelHit]],
}, total=False)

ModelKickChannelHit = TypedDict('ModelKickChannelHit', {
    'followers': NotRequired[int],
    'id': NotRequired[int],
    'live': NotRequired[bool],
    'profile_picture': NotRequired[str],
    'slug': NotRequired[str],
    'url': NotRequired[str],
    'username': NotRequired[str],
    'verified': NotRequired[bool],
}, total=False)

ModelKickSubcategoryResponseDoc = TypedDict('ModelKickSubcategoryResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelKickSubcategoryResponse],
    'msg': NotRequired[str],
}, total=False)

ModelKickSubcategoryResponse = TypedDict('ModelKickSubcategoryResponse', {
    'subcategory': NotRequired[ModelKickSubcategory],
}, total=False)

ModelKickSubcategory = TypedDict('ModelKickSubcategory', {
    'banner_url': NotRequired[str],
    'description': NotRequired[str],
    'followers': NotRequired[int],
    'id': NotRequired[int],
    'mature': NotRequired[bool],
    'name': NotRequired[str],
    'parent_id': NotRequired[int],
    'parent_name': NotRequired[str],
    'parent_slug': NotRequired[str],
    'slug': NotRequired[str],
    'tags': NotRequired[list[str]],
    'url': NotRequired[str],
    'viewers': NotRequired[int],
}, total=False)

ModelKickSubcategoriesResponseDoc = TypedDict('ModelKickSubcategoriesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelKickSubcategoriesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelKickSubcategoriesResponse = TypedDict('ModelKickSubcategoriesResponse', {
    'category': NotRequired[str],
    'limit': NotRequired[int],
    'page': NotRequired[int],
    'reachable': NotRequired[int],
    'subcategories': NotRequired[list[ModelKickSubcategory]],
    'total': NotRequired[int],
}, total=False)

ModelKickSearchChannelsResponseDoc = TypedDict('ModelKickSearchChannelsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelKickSearchChannelsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelKickSearchChannelsResponse = TypedDict('ModelKickSearchChannelsResponse', {
    'channels': NotRequired[list[ModelKickChannelHit]],
    'query': NotRequired[str],
}, total=False)

ModelKickSearchCategoriesResponseDoc = TypedDict('ModelKickSearchCategoriesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelKickSearchCategoriesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelKickSearchCategoriesResponse = TypedDict('ModelKickSearchCategoriesResponse', {
    'categories': NotRequired[list[ModelKickCategoryHit]],
    'query': NotRequired[str],
}, total=False)

ModelKickCategoryHit = TypedDict('ModelKickCategoryHit', {
    'id': NotRequired[int],
    'mature': NotRequired[bool],
    'name': NotRequired[str],
    'slug': NotRequired[str],
    'tags': NotRequired[list[str]],
    'thumbnail_url': NotRequired[str],
    'url': NotRequired[str],
    'viewers': NotRequired[int],
}, total=False)

ModelKickLivestreamsResponseDoc = TypedDict('ModelKickLivestreamsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelKickLivestreamsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelKickLivestreamsResponse = TypedDict('ModelKickLivestreamsResponse', {
    'category_id': NotRequired[int],
    'language': NotRequired[str],
    'livestreams': NotRequired[list[ModelKickDirectoryStream]],
    'next_cursor': NotRequired[str],
    'sort': NotRequired[str],
}, total=False)

ModelKickDirectoryStream = TypedDict('ModelKickDirectoryStream', {
    'category': NotRequired[ModelKickCategoryRef],
    'channel': NotRequired[ModelKickChannelRef],
    'id': NotRequired[str],
    'language': NotRequired[str],
    'mature': NotRequired[bool],
    'started_at': NotRequired[str],
    'tags': NotRequired[list[str]],
    'thumbnail_url': NotRequired[str],
    'title': NotRequired[str],
    'viewers': NotRequired[int],
}, total=False)

ModelKickLanguagesResponseDoc = TypedDict('ModelKickLanguagesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelKickLanguagesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelKickLanguagesResponse = TypedDict('ModelKickLanguagesResponse', {
    'languages': NotRequired[list[ModelKickLanguage]],
}, total=False)

ModelKickLanguage = TypedDict('ModelKickLanguage', {
    'code': NotRequired[str],
    'name': NotRequired[str],
}, total=False)

ModelKickGiftsResponseDoc = TypedDict('ModelKickGiftsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelKickGiftsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelKickGiftsResponse = TypedDict('ModelKickGiftsResponse', {
    'gifts': NotRequired[list[ModelKickGift]],
}, total=False)

ModelKickGift = TypedDict('ModelKickGift', {
    'character_limit': NotRequired[int],
    'id': NotRequired[str],
    'kicks': NotRequired[int],
    'name': NotRequired[str],
    'pinned_seconds': NotRequired[int],
    'tier': NotRequired[str],
    'type': NotRequired[str],
}, total=False)

ModelKickDropsResponseDoc = TypedDict('ModelKickDropsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelKickDropsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelKickDropsResponse = TypedDict('ModelKickDropsResponse', {
    'campaigns': NotRequired[list[ModelKickDropCampaign]],
    'status': NotRequired[str],
    'total': NotRequired[int],
}, total=False)

ModelKickDropCampaign = TypedDict('ModelKickDropCampaign', {
    'category': NotRequired[ModelKickCategoryRef],
    'channel_count': NotRequired[int],
    'channels': NotRequired[list[ModelKickDropChannel]],
    'ends_at': NotRequired[str],
    'id': NotRequired[str],
    'name': NotRequired[str],
    'organization': NotRequired[ModelKickDropOrganization],
    'rewards': NotRequired[list[ModelKickDropReward]],
    'rule': NotRequired[str],
    'starts_at': NotRequired[str],
    'status': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelKickDropReward = TypedDict('ModelKickDropReward', {
    'category_id': NotRequired[int],
    'id': NotRequired[str],
    'image_url': NotRequired[str],
    'name': NotRequired[str],
    'required_units': NotRequired[int],
}, total=False)

ModelKickDropOrganization = TypedDict('ModelKickDropOrganization', {
    'id': NotRequired[str],
    'logo_url': NotRequired[str],
    'name': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelKickDropChannel = TypedDict('ModelKickDropChannel', {
    'id': NotRequired[int],
    'profile_picture': NotRequired[str],
    'slug': NotRequired[str],
    'url': NotRequired[str],
    'username': NotRequired[str],
}, total=False)

ModelKickClipsResponseDoc = TypedDict('ModelKickClipsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelKickClipsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelKickClipsResponse = TypedDict('ModelKickClipsResponse', {
    'category': NotRequired[str],
    'clips': NotRequired[list[ModelKickClip]],
    'next_cursor': NotRequired[str],
    'slug': NotRequired[str],
    'sort': NotRequired[str],
    'time': NotRequired[str],
}, total=False)

ModelKickClip = TypedDict('ModelKickClip', {
    'category': NotRequired[ModelKickCategoryRef],
    'channel': NotRequired[ModelKickChannelRef],
    'created_at': NotRequired[str],
    'duration_seconds': NotRequired[int],
    'id': NotRequired[str],
    'likes': NotRequired[int],
    'mature': NotRequired[bool],
    'started_at': NotRequired[str],
    'thumbnail_url': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
    'video_id': NotRequired[str],
    'video_offset_seconds': NotRequired[int],
    'views': NotRequired[int],
}, total=False)

ModelKickClipResponseDoc = TypedDict('ModelKickClipResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelKickClipResponse],
    'msg': NotRequired[str],
}, total=False)

ModelKickClipResponse = TypedDict('ModelKickClipResponse', {
    'clip': NotRequired[ModelKickClip],
}, total=False)

ModelKickChannelVideosResponseDoc = TypedDict('ModelKickChannelVideosResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelKickChannelVideosResponse],
    'msg': NotRequired[str],
}, total=False)

ModelKickChannelVideosResponse = TypedDict('ModelKickChannelVideosResponse', {
    'slug': NotRequired[str],
    'videos': NotRequired[list[ModelKickVideo]],
}, total=False)

ModelKickVideo = TypedDict('ModelKickVideo', {
    'categories': NotRequired[list[ModelKickCategoryRef]],
    'duration_ms': NotRequired[int],
    'id': NotRequired[int],
    'language': NotRequired[str],
    'live': NotRequired[bool],
    'mature': NotRequired[bool],
    'started_at': NotRequired[str],
    'tags': NotRequired[list[str]],
    'thumbnail_url': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
    'uuid': NotRequired[str],
    'views': NotRequired[int],
}, total=False)

ModelKickChannelStreamsResponseDoc = TypedDict('ModelKickChannelStreamsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelKickChannelStreamsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelKickChannelStreamsResponse = TypedDict('ModelKickChannelStreamsResponse', {
    'slug': NotRequired[str],
    'streams': NotRequired[list[ModelKickStreamSession]],
}, total=False)

ModelKickStreamSession = TypedDict('ModelKickStreamSession', {
    'categories': NotRequired[list[ModelKickCategoryRef]],
    'duration_ms': NotRequired[int],
    'id': NotRequired[int],
    'language': NotRequired[str],
    'live': NotRequired[bool],
    'mature': NotRequired[bool],
    'started_at': NotRequired[str],
    'tags': NotRequired[list[str]],
    'thumbnail_url': NotRequired[str],
    'title': NotRequired[str],
    'video_url': NotRequired[str],
    'video_uuid': NotRequired[str],
    'video_views': NotRequired[int],
    'viewer_count': NotRequired[int],
}, total=False)

ModelKickChannelLinksResponseDoc = TypedDict('ModelKickChannelLinksResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelKickChannelLinksResponse],
    'msg': NotRequired[str],
}, total=False)

ModelKickChannelLinksResponse = TypedDict('ModelKickChannelLinksResponse', {
    'links': NotRequired[list[ModelKickChannelLink]],
    'slug': NotRequired[str],
}, total=False)

ModelKickChannelLink = TypedDict('ModelKickChannelLink', {
    'description': NotRequired[str],
    'id': NotRequired[int],
    'image_url': NotRequired[str],
    'kind': NotRequired[str],
    'order': NotRequired[int],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelKickChannelEmotesResponseDoc = TypedDict('ModelKickChannelEmotesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelKickChannelEmotesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelKickChannelEmotesResponse = TypedDict('ModelKickChannelEmotesResponse', {
    'channel': NotRequired[list[ModelKickEmote]],
    'emoji': NotRequired[list[ModelKickEmote]],
    'global': NotRequired[list[ModelKickEmote]],
    'slug': NotRequired[str],
}, total=False)

ModelKickEmote = TypedDict('ModelKickEmote', {
    'id': NotRequired[int],
    'image_url': NotRequired[str],
    'name': NotRequired[str],
    'subscribers_only': NotRequired[bool],
}, total=False)

ModelKickChannelClipsResponseDoc = TypedDict('ModelKickChannelClipsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelKickClipsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelKickChannelChatroomResponseDoc = TypedDict('ModelKickChannelChatroomResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelKickChannelChatroomResponse],
    'msg': NotRequired[str],
}, total=False)

ModelKickChannelChatroomResponse = TypedDict('ModelKickChannelChatroomResponse', {
    'account_age': NotRequired[ModelKickChatMode],
    'chatroom_id': NotRequired[int],
    'emotes_only': NotRequired[ModelKickChatMode],
    'followers_only': NotRequired[ModelKickChatMode],
    'gifts_enabled': NotRequired[bool],
    'rules': NotRequired[str],
    'slow_mode': NotRequired[ModelKickChatMode],
    'slug': NotRequired[str],
    'subscribers_only': NotRequired[ModelKickChatMode],
}, total=False)

ModelKickChatMode = TypedDict('ModelKickChatMode', {
    'enabled': NotRequired[bool],
    'interval_seconds': NotRequired[int],
    'minutes': NotRequired[int],
}, total=False)

ModelKickChannelResponseDoc = TypedDict('ModelKickChannelResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelKickChannelResponse],
    'msg': NotRequired[str],
}, total=False)

ModelKickChannelResponse = TypedDict('ModelKickChannelResponse', {
    'affiliate': NotRequired[bool],
    'banned': NotRequired[bool],
    'banner_url': NotRequired[str],
    'bio': NotRequired[str],
    'followers': NotRequired[int],
    'id': NotRequired[int],
    'live': NotRequired[ModelKickLiveStream],
    'profile_picture': NotRequired[str],
    'recent_categories': NotRequired[list[ModelKickCategoryRef]],
    'slug': NotRequired[str],
    'socials': NotRequired[ModelKickSocials],
    'subscription_enabled': NotRequired[bool],
    'url': NotRequired[str],
    'username': NotRequired[str],
    'verified': NotRequired[bool],
    'vod_enabled': NotRequired[bool],
}, total=False)

ModelKickSocials = TypedDict('ModelKickSocials', {
    'discord': NotRequired[str],
    'facebook': NotRequired[str],
    'instagram': NotRequired[str],
    'tiktok': NotRequired[str],
    'twitter': NotRequired[str],
    'youtube': NotRequired[str],
}, total=False)

ModelKickLiveStream = TypedDict('ModelKickLiveStream', {
    'categories': NotRequired[list[ModelKickCategoryRef]],
    'id': NotRequired[int],
    'language': NotRequired[str],
    'mature': NotRequired[bool],
    'started_at': NotRequired[str],
    'tags': NotRequired[list[str]],
    'thumbnail_url': NotRequired[str],
    'title': NotRequired[str],
    'viewers': NotRequired[int],
}, total=False)

ModelKickCategoryClipsResponseDoc = TypedDict('ModelKickCategoryClipsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelKickClipsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelKickCategoriesResponseDoc = TypedDict('ModelKickCategoriesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelKickCategoriesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelKickCategoriesResponse = TypedDict('ModelKickCategoriesResponse', {
    'categories': NotRequired[list[ModelKickCategory]],
}, total=False)

ModelKickCategory = TypedDict('ModelKickCategory', {
    'icon': NotRequired[str],
    'id': NotRequired[int],
    'name': NotRequired[str],
    'slug': NotRequired[str],
}, total=False)

KickCategoriesResponse = ModelKickCategoriesResponseDoc
KickCategoriesParams = TypedDict('KickCategoriesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

KickCategoryClipsResponse = ModelKickCategoryClipsResponseDoc
KickCategoryClipsParams = TypedDict('KickCategoryClipsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'slug': Required[str],
    'cursor': NotRequired[str],
}, total=False)

KickChannelResponse = ModelKickChannelResponseDoc
KickChannelParams = TypedDict('KickChannelParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'slug': Required[str],
}, total=False)

KickChannelChatroomResponse = ModelKickChannelChatroomResponseDoc
KickChannelChatroomParams = TypedDict('KickChannelChatroomParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'slug': Required[str],
}, total=False)

KickChannelClipsResponse = ModelKickChannelClipsResponseDoc
KickChannelClipsParams = TypedDict('KickChannelClipsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'slug': Required[str],
    'cursor': NotRequired[str],
}, total=False)

KickChannelEmotesResponse = ModelKickChannelEmotesResponseDoc
KickChannelEmotesParams = TypedDict('KickChannelEmotesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'slug': Required[str],
}, total=False)

KickChannelLinksResponse = ModelKickChannelLinksResponseDoc
KickChannelLinksParams = TypedDict('KickChannelLinksParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'slug': Required[str],
}, total=False)

KickChannelStreamsResponse = ModelKickChannelStreamsResponseDoc
KickChannelStreamsParams = TypedDict('KickChannelStreamsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'slug': Required[str],
}, total=False)

KickChannelVideosResponse = ModelKickChannelVideosResponseDoc
KickChannelVideosParams = TypedDict('KickChannelVideosParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'slug': Required[str],
}, total=False)

KickClipResponse = ModelKickClipResponseDoc
KickClipParams = TypedDict('KickClipParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

KickClipsResponse = ModelKickClipsResponseDoc
KickClipsParams = TypedDict('KickClipsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'sort': NotRequired[Literal['date', 'views']],
    'time': NotRequired[Literal['day', 'week', 'month', 'all']],
    'cursor': NotRequired[str],
}, total=False)

KickDropsResponse = ModelKickDropsResponseDoc
KickDropsParams = TypedDict('KickDropsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'status': NotRequired[Literal['active', 'expired', 'all']],
}, total=False)

KickGiftsResponse = ModelKickGiftsResponseDoc
KickGiftsParams = TypedDict('KickGiftsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

KickLanguagesResponse = ModelKickLanguagesResponseDoc
KickLanguagesParams = TypedDict('KickLanguagesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

KickLivestreamsResponse = ModelKickLivestreamsResponseDoc
KickLivestreamsParams = TypedDict('KickLivestreamsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'sort': NotRequired[Literal['viewer_count_desc', 'featured']],
    'language': NotRequired[str],
    'category_id': NotRequired[int],
    'limit': NotRequired[int],
    'after': NotRequired[str],
}, total=False)

KickSearchCategoriesResponse = ModelKickSearchCategoriesResponseDoc
KickSearchCategoriesParams = TypedDict('KickSearchCategoriesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'query': Required[str],
    'limit': NotRequired[int],
}, total=False)

KickSearchChannelsResponse = ModelKickSearchChannelsResponseDoc
KickSearchChannelsParams = TypedDict('KickSearchChannelsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'query': Required[str],
    'live': NotRequired[bool],
    'limit': NotRequired[int],
}, total=False)

KickSubcategoriesResponse = ModelKickSubcategoriesResponseDoc
KickSubcategoriesParams = TypedDict('KickSubcategoriesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'category': NotRequired[Literal['games', 'irl', 'music', 'gambling', 'creative', 'alternative', 'chat-roulette']],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

KickSubcategoryResponse = ModelKickSubcategoryResponseDoc
KickSubcategoryParams = TypedDict('KickSubcategoryParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'slug': Required[str],
}, total=False)

KickTopChannelsResponse = ModelKickTopChannelsResponseDoc
KickTopChannelsParams = TypedDict('KickTopChannelsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

KickVideoResponse = ModelKickVideoResponseDoc
KickVideoParams = TypedDict('KickVideoParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

class KickGroup:
    @overload
    def categories(self, **params: Unpack[KickCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def categories(self, **params: Unpack[KickCategoriesTextResponseParams]) -> str: ...
    @overload
    def categories(self, **params: Unpack[KickCategoriesDefaultParams]) -> KickCategoriesResponse: ...
    @overload
    def category_clips(self, **params: Unpack[KickCategoryClipsStreamParams]) -> BinaryIO: ...
    @overload
    def category_clips(self, **params: Unpack[KickCategoryClipsTextResponseParams]) -> str: ...
    @overload
    def category_clips(self, **params: Unpack[KickCategoryClipsDefaultParams]) -> KickCategoryClipsResponse: ...
    @overload
    def channel(self, **params: Unpack[KickChannelStreamParams]) -> BinaryIO: ...
    @overload
    def channel(self, **params: Unpack[KickChannelTextResponseParams]) -> str: ...
    @overload
    def channel(self, **params: Unpack[KickChannelDefaultParams]) -> KickChannelResponse: ...
    @overload
    def channel_chatroom(self, **params: Unpack[KickChannelChatroomStreamParams]) -> BinaryIO: ...
    @overload
    def channel_chatroom(self, **params: Unpack[KickChannelChatroomTextResponseParams]) -> str: ...
    @overload
    def channel_chatroom(self, **params: Unpack[KickChannelChatroomDefaultParams]) -> KickChannelChatroomResponse: ...
    @overload
    def channel_clips(self, **params: Unpack[KickChannelClipsStreamParams]) -> BinaryIO: ...
    @overload
    def channel_clips(self, **params: Unpack[KickChannelClipsTextResponseParams]) -> str: ...
    @overload
    def channel_clips(self, **params: Unpack[KickChannelClipsDefaultParams]) -> KickChannelClipsResponse: ...
    @overload
    def channel_emotes(self, **params: Unpack[KickChannelEmotesStreamParams]) -> BinaryIO: ...
    @overload
    def channel_emotes(self, **params: Unpack[KickChannelEmotesTextResponseParams]) -> str: ...
    @overload
    def channel_emotes(self, **params: Unpack[KickChannelEmotesDefaultParams]) -> KickChannelEmotesResponse: ...
    @overload
    def channel_links(self, **params: Unpack[KickChannelLinksStreamParams]) -> BinaryIO: ...
    @overload
    def channel_links(self, **params: Unpack[KickChannelLinksTextResponseParams]) -> str: ...
    @overload
    def channel_links(self, **params: Unpack[KickChannelLinksDefaultParams]) -> KickChannelLinksResponse: ...
    @overload
    def channel_streams(self, **params: Unpack[KickChannelStreamsStreamParams]) -> BinaryIO: ...
    @overload
    def channel_streams(self, **params: Unpack[KickChannelStreamsTextResponseParams]) -> str: ...
    @overload
    def channel_streams(self, **params: Unpack[KickChannelStreamsDefaultParams]) -> KickChannelStreamsResponse: ...
    @overload
    def channel_videos(self, **params: Unpack[KickChannelVideosStreamParams]) -> BinaryIO: ...
    @overload
    def channel_videos(self, **params: Unpack[KickChannelVideosTextResponseParams]) -> str: ...
    @overload
    def channel_videos(self, **params: Unpack[KickChannelVideosDefaultParams]) -> KickChannelVideosResponse: ...
    @overload
    def clip(self, **params: Unpack[KickClipStreamParams]) -> BinaryIO: ...
    @overload
    def clip(self, **params: Unpack[KickClipTextResponseParams]) -> str: ...
    @overload
    def clip(self, **params: Unpack[KickClipDefaultParams]) -> KickClipResponse: ...
    @overload
    def clips(self, **params: Unpack[KickClipsStreamParams]) -> BinaryIO: ...
    @overload
    def clips(self, **params: Unpack[KickClipsTextResponseParams]) -> str: ...
    @overload
    def clips(self, **params: Unpack[KickClipsDefaultParams]) -> KickClipsResponse: ...
    @overload
    def drops(self, **params: Unpack[KickDropsStreamParams]) -> BinaryIO: ...
    @overload
    def drops(self, **params: Unpack[KickDropsTextResponseParams]) -> str: ...
    @overload
    def drops(self, **params: Unpack[KickDropsDefaultParams]) -> KickDropsResponse: ...
    @overload
    def gifts(self, **params: Unpack[KickGiftsStreamParams]) -> BinaryIO: ...
    @overload
    def gifts(self, **params: Unpack[KickGiftsTextResponseParams]) -> str: ...
    @overload
    def gifts(self, **params: Unpack[KickGiftsDefaultParams]) -> KickGiftsResponse: ...
    @overload
    def languages(self, **params: Unpack[KickLanguagesStreamParams]) -> BinaryIO: ...
    @overload
    def languages(self, **params: Unpack[KickLanguagesTextResponseParams]) -> str: ...
    @overload
    def languages(self, **params: Unpack[KickLanguagesDefaultParams]) -> KickLanguagesResponse: ...
    @overload
    def livestreams(self, **params: Unpack[KickLivestreamsStreamParams]) -> BinaryIO: ...
    @overload
    def livestreams(self, **params: Unpack[KickLivestreamsTextResponseParams]) -> str: ...
    @overload
    def livestreams(self, **params: Unpack[KickLivestreamsDefaultParams]) -> KickLivestreamsResponse: ...
    @overload
    def search_categories(self, **params: Unpack[KickSearchCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def search_categories(self, **params: Unpack[KickSearchCategoriesTextResponseParams]) -> str: ...
    @overload
    def search_categories(self, **params: Unpack[KickSearchCategoriesDefaultParams]) -> KickSearchCategoriesResponse: ...
    @overload
    def search_channels(self, **params: Unpack[KickSearchChannelsStreamParams]) -> BinaryIO: ...
    @overload
    def search_channels(self, **params: Unpack[KickSearchChannelsTextResponseParams]) -> str: ...
    @overload
    def search_channels(self, **params: Unpack[KickSearchChannelsDefaultParams]) -> KickSearchChannelsResponse: ...
    @overload
    def subcategories(self, **params: Unpack[KickSubcategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def subcategories(self, **params: Unpack[KickSubcategoriesTextResponseParams]) -> str: ...
    @overload
    def subcategories(self, **params: Unpack[KickSubcategoriesDefaultParams]) -> KickSubcategoriesResponse: ...
    @overload
    def subcategory(self, **params: Unpack[KickSubcategoryStreamParams]) -> BinaryIO: ...
    @overload
    def subcategory(self, **params: Unpack[KickSubcategoryTextResponseParams]) -> str: ...
    @overload
    def subcategory(self, **params: Unpack[KickSubcategoryDefaultParams]) -> KickSubcategoryResponse: ...
    @overload
    def top_channels(self, **params: Unpack[KickTopChannelsStreamParams]) -> BinaryIO: ...
    @overload
    def top_channels(self, **params: Unpack[KickTopChannelsTextResponseParams]) -> str: ...
    @overload
    def top_channels(self, **params: Unpack[KickTopChannelsDefaultParams]) -> KickTopChannelsResponse: ...
    @overload
    def video(self, **params: Unpack[KickVideoStreamParams]) -> BinaryIO: ...
    @overload
    def video(self, **params: Unpack[KickVideoTextResponseParams]) -> str: ...
    @overload
    def video(self, **params: Unpack[KickVideoDefaultParams]) -> KickVideoResponse: ...

OperationId = Literal[
    'kick-categories',
    'kick-category-clips',
    'kick-channel',
    'kick-channel-chatroom',
    'kick-channel-clips',
    'kick-channel-emotes',
    'kick-channel-links',
    'kick-channel-streams',
    'kick-channel-videos',
    'kick-clip',
    'kick-clips',
    'kick-drops',
    'kick-gifts',
    'kick-languages',
    'kick-livestreams',
    'kick-search-categories',
    'kick-search-channels',
    'kick-subcategories',
    'kick-subcategory',
    'kick-top-channels',
    'kick-video',
]

class CrawloraClient:
    kick: KickGroup
    api_key: str
    jwt_token: str
    base_url: str
    timeout: float
    retries: int
    retry_delay: float
    max_retry_delay: float
    retry_statuses: frozenset[int] | None
    retry_predicate: Callable[[int, BaseException | None], bool] | None
    on_retry: Callable[[int, BaseException, float], None] | None
    request_id: bool
    idempotency_keys: bool
    rate_limit: float | None
    max_concurrency: int | None
    logger: Callable[[Mapping[str, Any]], None] | None
    before_request: list[Callable[[dict[str, Any]], None]]
    after_response: list[Callable[[str, int, Mapping[str, str], Any], Any]]
    headers: dict[str, str]
    user_agent: str
    def _is_retryable(self, status: int, exc: BaseException | None) -> bool: ...
    def _compute_retry_delay(self, attempt: int, headers: Mapping[str, str]) -> float: ...
    def _log(self, event: Mapping[str, Any]) -> None: ...
    def __init__(
        self,
        *,
        api_key: str | None = ...,
        jwt_token: str | None = ...,
        base_url: str | None = ...,
        timeout: float = ...,
        retries: int = ...,
        retry_delay: float = ...,
        max_retry_delay: float = ...,
        retry_statuses: Iterable[int] | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
        on_retry: Callable[[int, BaseException, float], None] | None = ...,
        request_id: bool = ...,
        idempotency_keys: bool = ...,
        rate_limit: float | None = ...,
        max_concurrency: int | None = ...,
        logger: Callable[[Mapping[str, Any]], None] | None = ...,
        before_request: Callable[[dict[str, Any]], None] | Iterable[Callable[[dict[str, Any]], None]] | None = ...,
        after_response: Callable[[str, int, Mapping[str, str], Any], Any] | Iterable[Callable[[str, int, Mapping[str, str], Any], Any]] | None = ...,
        headers: Mapping[str, str] | None = ...,
        user_agent: str | None = ...,
        transport: Callable[..., Any] | None = ...,
    ) -> None: ...
    def close(self) -> None: ...
    def __enter__(self) -> CrawloraClient: ...
    def __exit__(self, *exc: Any) -> None: ...
    def paginate(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    def paginate_items(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        items: Callable[[Any], Any] | None = ...,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    @overload
    def operation(
        self,
        operation_id: Literal['kick-categories'],
        params: KickCategoriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> KickCategoriesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['kick-category-clips'],
        params: KickCategoryClipsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> KickCategoryClipsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['kick-channel'],
        params: KickChannelParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> KickChannelResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['kick-channel-chatroom'],
        params: KickChannelChatroomParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> KickChannelChatroomResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['kick-channel-clips'],
        params: KickChannelClipsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> KickChannelClipsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['kick-channel-emotes'],
        params: KickChannelEmotesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> KickChannelEmotesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['kick-channel-links'],
        params: KickChannelLinksParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> KickChannelLinksResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['kick-channel-streams'],
        params: KickChannelStreamsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> KickChannelStreamsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['kick-channel-videos'],
        params: KickChannelVideosParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> KickChannelVideosResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['kick-clip'],
        params: KickClipParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> KickClipResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['kick-clips'],
        params: KickClipsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> KickClipsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['kick-drops'],
        params: KickDropsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> KickDropsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['kick-gifts'],
        params: KickGiftsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> KickGiftsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['kick-languages'],
        params: KickLanguagesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> KickLanguagesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['kick-livestreams'],
        params: KickLivestreamsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> KickLivestreamsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['kick-search-categories'],
        params: KickSearchCategoriesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> KickSearchCategoriesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['kick-search-channels'],
        params: KickSearchChannelsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> KickSearchChannelsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['kick-subcategories'],
        params: KickSubcategoriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> KickSubcategoriesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['kick-subcategory'],
        params: KickSubcategoryParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> KickSubcategoryResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['kick-top-channels'],
        params: KickTopChannelsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> KickTopChannelsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['kick-video'],
        params: KickVideoParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> KickVideoResponse: ...
    @overload
    def operation(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...
    @overload
    def request(
        self,
        operation_id: Literal['kick-categories'],
        params: KickCategoriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> KickCategoriesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['kick-category-clips'],
        params: KickCategoryClipsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> KickCategoryClipsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['kick-channel'],
        params: KickChannelParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> KickChannelResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['kick-channel-chatroom'],
        params: KickChannelChatroomParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> KickChannelChatroomResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['kick-channel-clips'],
        params: KickChannelClipsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> KickChannelClipsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['kick-channel-emotes'],
        params: KickChannelEmotesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> KickChannelEmotesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['kick-channel-links'],
        params: KickChannelLinksParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> KickChannelLinksResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['kick-channel-streams'],
        params: KickChannelStreamsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> KickChannelStreamsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['kick-channel-videos'],
        params: KickChannelVideosParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> KickChannelVideosResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['kick-clip'],
        params: KickClipParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> KickClipResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['kick-clips'],
        params: KickClipsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> KickClipsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['kick-drops'],
        params: KickDropsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> KickDropsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['kick-gifts'],
        params: KickGiftsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> KickGiftsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['kick-languages'],
        params: KickLanguagesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> KickLanguagesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['kick-livestreams'],
        params: KickLivestreamsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> KickLivestreamsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['kick-search-categories'],
        params: KickSearchCategoriesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> KickSearchCategoriesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['kick-search-channels'],
        params: KickSearchChannelsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> KickSearchChannelsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['kick-subcategories'],
        params: KickSubcategoriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> KickSubcategoriesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['kick-subcategory'],
        params: KickSubcategoryParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> KickSubcategoryResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['kick-top-channels'],
        params: KickTopChannelsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> KickTopChannelsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['kick-video'],
        params: KickVideoParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> KickVideoResponse: ...
    @overload
    def request(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...

VERSION: str

# Internal helpers reused by the async client; not part of the public API.
def _build_request(base_url: str, operation: Mapping[str, Any], params: dict[str, Any]) -> tuple[Any, Any, dict[str, str]]: ...
def _merge_headers(*sources: Mapping[str, str]) -> dict[str, str]: ...
def _auth_headers(security: list[str], api_key: str, jwt_token: str) -> dict[str, str]: ...
def _ensure_request_id(headers: dict[str, str]) -> str: ...
def _header_value(headers: Mapping[str, str], name: str) -> str: ...
def _parse_response(body: bytes, content_type: str, response_type: str) -> Any: ...
def _validate_response_type(response_type: str) -> ResponseType: ...
def _api_error_class(status: int) -> type[CrawloraError]: ...
def _run_before_request(hooks: list[Any], ctx: dict[str, Any]) -> None: ...
def _run_after_response(hooks: list[Any], operation_id: Any, status: int, headers: Mapping[str, str], body: Any) -> Any: ...
def _allowed_params(operation_id: str) -> set[str]: ...

from typing import BinaryIO

class AsyncCrawloraClient:
    def __init__(self, **kwargs: Any) -> None: ...
    async def aclose(self) -> None: ...
    async def __aenter__(self) -> AsyncCrawloraClient: ...
    async def __aexit__(self, *exc: Any) -> None: ...
    async def request(self, operation_id: str, params: Mapping[str, Any] | None = ..., *, response_type: ResponseType = ..., timeout: float | None = ..., headers: Mapping[str, str] | None = ..., retries: int | None = ..., retry_predicate: Callable[[int, BaseException | None], bool] | None = ...) -> Any: ...

class KickClient(CrawloraClient):
    def __enter__(self) -> KickClient: ...
    @overload
    def categories(self, **params: Unpack[KickCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def categories(self, **params: Unpack[KickCategoriesTextResponseParams]) -> str: ...
    @overload
    def categories(self, **params: Unpack[KickCategoriesDefaultParams]) -> KickCategoriesResponse: ...
    @overload
    def category_clips(self, **params: Unpack[KickCategoryClipsStreamParams]) -> BinaryIO: ...
    @overload
    def category_clips(self, **params: Unpack[KickCategoryClipsTextResponseParams]) -> str: ...
    @overload
    def category_clips(self, **params: Unpack[KickCategoryClipsDefaultParams]) -> KickCategoryClipsResponse: ...
    @overload
    def channel(self, **params: Unpack[KickChannelStreamParams]) -> BinaryIO: ...
    @overload
    def channel(self, **params: Unpack[KickChannelTextResponseParams]) -> str: ...
    @overload
    def channel(self, **params: Unpack[KickChannelDefaultParams]) -> KickChannelResponse: ...
    @overload
    def channel_chatroom(self, **params: Unpack[KickChannelChatroomStreamParams]) -> BinaryIO: ...
    @overload
    def channel_chatroom(self, **params: Unpack[KickChannelChatroomTextResponseParams]) -> str: ...
    @overload
    def channel_chatroom(self, **params: Unpack[KickChannelChatroomDefaultParams]) -> KickChannelChatroomResponse: ...
    @overload
    def channel_clips(self, **params: Unpack[KickChannelClipsStreamParams]) -> BinaryIO: ...
    @overload
    def channel_clips(self, **params: Unpack[KickChannelClipsTextResponseParams]) -> str: ...
    @overload
    def channel_clips(self, **params: Unpack[KickChannelClipsDefaultParams]) -> KickChannelClipsResponse: ...
    @overload
    def channel_emotes(self, **params: Unpack[KickChannelEmotesStreamParams]) -> BinaryIO: ...
    @overload
    def channel_emotes(self, **params: Unpack[KickChannelEmotesTextResponseParams]) -> str: ...
    @overload
    def channel_emotes(self, **params: Unpack[KickChannelEmotesDefaultParams]) -> KickChannelEmotesResponse: ...
    @overload
    def channel_links(self, **params: Unpack[KickChannelLinksStreamParams]) -> BinaryIO: ...
    @overload
    def channel_links(self, **params: Unpack[KickChannelLinksTextResponseParams]) -> str: ...
    @overload
    def channel_links(self, **params: Unpack[KickChannelLinksDefaultParams]) -> KickChannelLinksResponse: ...
    @overload
    def channel_streams(self, **params: Unpack[KickChannelStreamsStreamParams]) -> BinaryIO: ...
    @overload
    def channel_streams(self, **params: Unpack[KickChannelStreamsTextResponseParams]) -> str: ...
    @overload
    def channel_streams(self, **params: Unpack[KickChannelStreamsDefaultParams]) -> KickChannelStreamsResponse: ...
    @overload
    def channel_videos(self, **params: Unpack[KickChannelVideosStreamParams]) -> BinaryIO: ...
    @overload
    def channel_videos(self, **params: Unpack[KickChannelVideosTextResponseParams]) -> str: ...
    @overload
    def channel_videos(self, **params: Unpack[KickChannelVideosDefaultParams]) -> KickChannelVideosResponse: ...
    @overload
    def clip(self, **params: Unpack[KickClipStreamParams]) -> BinaryIO: ...
    @overload
    def clip(self, **params: Unpack[KickClipTextResponseParams]) -> str: ...
    @overload
    def clip(self, **params: Unpack[KickClipDefaultParams]) -> KickClipResponse: ...
    @overload
    def clips(self, **params: Unpack[KickClipsStreamParams]) -> BinaryIO: ...
    @overload
    def clips(self, **params: Unpack[KickClipsTextResponseParams]) -> str: ...
    @overload
    def clips(self, **params: Unpack[KickClipsDefaultParams]) -> KickClipsResponse: ...
    @overload
    def drops(self, **params: Unpack[KickDropsStreamParams]) -> BinaryIO: ...
    @overload
    def drops(self, **params: Unpack[KickDropsTextResponseParams]) -> str: ...
    @overload
    def drops(self, **params: Unpack[KickDropsDefaultParams]) -> KickDropsResponse: ...
    @overload
    def gifts(self, **params: Unpack[KickGiftsStreamParams]) -> BinaryIO: ...
    @overload
    def gifts(self, **params: Unpack[KickGiftsTextResponseParams]) -> str: ...
    @overload
    def gifts(self, **params: Unpack[KickGiftsDefaultParams]) -> KickGiftsResponse: ...
    @overload
    def languages(self, **params: Unpack[KickLanguagesStreamParams]) -> BinaryIO: ...
    @overload
    def languages(self, **params: Unpack[KickLanguagesTextResponseParams]) -> str: ...
    @overload
    def languages(self, **params: Unpack[KickLanguagesDefaultParams]) -> KickLanguagesResponse: ...
    @overload
    def livestreams(self, **params: Unpack[KickLivestreamsStreamParams]) -> BinaryIO: ...
    @overload
    def livestreams(self, **params: Unpack[KickLivestreamsTextResponseParams]) -> str: ...
    @overload
    def livestreams(self, **params: Unpack[KickLivestreamsDefaultParams]) -> KickLivestreamsResponse: ...
    @overload
    def search_categories(self, **params: Unpack[KickSearchCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def search_categories(self, **params: Unpack[KickSearchCategoriesTextResponseParams]) -> str: ...
    @overload
    def search_categories(self, **params: Unpack[KickSearchCategoriesDefaultParams]) -> KickSearchCategoriesResponse: ...
    @overload
    def search_channels(self, **params: Unpack[KickSearchChannelsStreamParams]) -> BinaryIO: ...
    @overload
    def search_channels(self, **params: Unpack[KickSearchChannelsTextResponseParams]) -> str: ...
    @overload
    def search_channels(self, **params: Unpack[KickSearchChannelsDefaultParams]) -> KickSearchChannelsResponse: ...
    @overload
    def subcategories(self, **params: Unpack[KickSubcategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def subcategories(self, **params: Unpack[KickSubcategoriesTextResponseParams]) -> str: ...
    @overload
    def subcategories(self, **params: Unpack[KickSubcategoriesDefaultParams]) -> KickSubcategoriesResponse: ...
    @overload
    def subcategory(self, **params: Unpack[KickSubcategoryStreamParams]) -> BinaryIO: ...
    @overload
    def subcategory(self, **params: Unpack[KickSubcategoryTextResponseParams]) -> str: ...
    @overload
    def subcategory(self, **params: Unpack[KickSubcategoryDefaultParams]) -> KickSubcategoryResponse: ...
    @overload
    def top_channels(self, **params: Unpack[KickTopChannelsStreamParams]) -> BinaryIO: ...
    @overload
    def top_channels(self, **params: Unpack[KickTopChannelsTextResponseParams]) -> str: ...
    @overload
    def top_channels(self, **params: Unpack[KickTopChannelsDefaultParams]) -> KickTopChannelsResponse: ...
    @overload
    def video(self, **params: Unpack[KickVideoStreamParams]) -> BinaryIO: ...
    @overload
    def video(self, **params: Unpack[KickVideoTextResponseParams]) -> str: ...
    @overload
    def video(self, **params: Unpack[KickVideoDefaultParams]) -> KickVideoResponse: ...

class AsyncKickClient(AsyncCrawloraClient):
    async def __aenter__(self) -> AsyncKickClient: ...
    kick: _AsyncKickGroup
    @overload
    async def categories(self, **params: Unpack[KickCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def categories(self, **params: Unpack[KickCategoriesTextResponseParams]) -> str: ...
    @overload
    async def categories(self, **params: Unpack[KickCategoriesDefaultParams]) -> KickCategoriesResponse: ...
    @overload
    async def category_clips(self, **params: Unpack[KickCategoryClipsStreamParams]) -> BinaryIO: ...
    @overload
    async def category_clips(self, **params: Unpack[KickCategoryClipsTextResponseParams]) -> str: ...
    @overload
    async def category_clips(self, **params: Unpack[KickCategoryClipsDefaultParams]) -> KickCategoryClipsResponse: ...
    @overload
    async def channel(self, **params: Unpack[KickChannelStreamParams]) -> BinaryIO: ...
    @overload
    async def channel(self, **params: Unpack[KickChannelTextResponseParams]) -> str: ...
    @overload
    async def channel(self, **params: Unpack[KickChannelDefaultParams]) -> KickChannelResponse: ...
    @overload
    async def channel_chatroom(self, **params: Unpack[KickChannelChatroomStreamParams]) -> BinaryIO: ...
    @overload
    async def channel_chatroom(self, **params: Unpack[KickChannelChatroomTextResponseParams]) -> str: ...
    @overload
    async def channel_chatroom(self, **params: Unpack[KickChannelChatroomDefaultParams]) -> KickChannelChatroomResponse: ...
    @overload
    async def channel_clips(self, **params: Unpack[KickChannelClipsStreamParams]) -> BinaryIO: ...
    @overload
    async def channel_clips(self, **params: Unpack[KickChannelClipsTextResponseParams]) -> str: ...
    @overload
    async def channel_clips(self, **params: Unpack[KickChannelClipsDefaultParams]) -> KickChannelClipsResponse: ...
    @overload
    async def channel_emotes(self, **params: Unpack[KickChannelEmotesStreamParams]) -> BinaryIO: ...
    @overload
    async def channel_emotes(self, **params: Unpack[KickChannelEmotesTextResponseParams]) -> str: ...
    @overload
    async def channel_emotes(self, **params: Unpack[KickChannelEmotesDefaultParams]) -> KickChannelEmotesResponse: ...
    @overload
    async def channel_links(self, **params: Unpack[KickChannelLinksStreamParams]) -> BinaryIO: ...
    @overload
    async def channel_links(self, **params: Unpack[KickChannelLinksTextResponseParams]) -> str: ...
    @overload
    async def channel_links(self, **params: Unpack[KickChannelLinksDefaultParams]) -> KickChannelLinksResponse: ...
    @overload
    async def channel_streams(self, **params: Unpack[KickChannelStreamsStreamParams]) -> BinaryIO: ...
    @overload
    async def channel_streams(self, **params: Unpack[KickChannelStreamsTextResponseParams]) -> str: ...
    @overload
    async def channel_streams(self, **params: Unpack[KickChannelStreamsDefaultParams]) -> KickChannelStreamsResponse: ...
    @overload
    async def channel_videos(self, **params: Unpack[KickChannelVideosStreamParams]) -> BinaryIO: ...
    @overload
    async def channel_videos(self, **params: Unpack[KickChannelVideosTextResponseParams]) -> str: ...
    @overload
    async def channel_videos(self, **params: Unpack[KickChannelVideosDefaultParams]) -> KickChannelVideosResponse: ...
    @overload
    async def clip(self, **params: Unpack[KickClipStreamParams]) -> BinaryIO: ...
    @overload
    async def clip(self, **params: Unpack[KickClipTextResponseParams]) -> str: ...
    @overload
    async def clip(self, **params: Unpack[KickClipDefaultParams]) -> KickClipResponse: ...
    @overload
    async def clips(self, **params: Unpack[KickClipsStreamParams]) -> BinaryIO: ...
    @overload
    async def clips(self, **params: Unpack[KickClipsTextResponseParams]) -> str: ...
    @overload
    async def clips(self, **params: Unpack[KickClipsDefaultParams]) -> KickClipsResponse: ...
    @overload
    async def drops(self, **params: Unpack[KickDropsStreamParams]) -> BinaryIO: ...
    @overload
    async def drops(self, **params: Unpack[KickDropsTextResponseParams]) -> str: ...
    @overload
    async def drops(self, **params: Unpack[KickDropsDefaultParams]) -> KickDropsResponse: ...
    @overload
    async def gifts(self, **params: Unpack[KickGiftsStreamParams]) -> BinaryIO: ...
    @overload
    async def gifts(self, **params: Unpack[KickGiftsTextResponseParams]) -> str: ...
    @overload
    async def gifts(self, **params: Unpack[KickGiftsDefaultParams]) -> KickGiftsResponse: ...
    @overload
    async def languages(self, **params: Unpack[KickLanguagesStreamParams]) -> BinaryIO: ...
    @overload
    async def languages(self, **params: Unpack[KickLanguagesTextResponseParams]) -> str: ...
    @overload
    async def languages(self, **params: Unpack[KickLanguagesDefaultParams]) -> KickLanguagesResponse: ...
    @overload
    async def livestreams(self, **params: Unpack[KickLivestreamsStreamParams]) -> BinaryIO: ...
    @overload
    async def livestreams(self, **params: Unpack[KickLivestreamsTextResponseParams]) -> str: ...
    @overload
    async def livestreams(self, **params: Unpack[KickLivestreamsDefaultParams]) -> KickLivestreamsResponse: ...
    @overload
    async def search_categories(self, **params: Unpack[KickSearchCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def search_categories(self, **params: Unpack[KickSearchCategoriesTextResponseParams]) -> str: ...
    @overload
    async def search_categories(self, **params: Unpack[KickSearchCategoriesDefaultParams]) -> KickSearchCategoriesResponse: ...
    @overload
    async def search_channels(self, **params: Unpack[KickSearchChannelsStreamParams]) -> BinaryIO: ...
    @overload
    async def search_channels(self, **params: Unpack[KickSearchChannelsTextResponseParams]) -> str: ...
    @overload
    async def search_channels(self, **params: Unpack[KickSearchChannelsDefaultParams]) -> KickSearchChannelsResponse: ...
    @overload
    async def subcategories(self, **params: Unpack[KickSubcategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def subcategories(self, **params: Unpack[KickSubcategoriesTextResponseParams]) -> str: ...
    @overload
    async def subcategories(self, **params: Unpack[KickSubcategoriesDefaultParams]) -> KickSubcategoriesResponse: ...
    @overload
    async def subcategory(self, **params: Unpack[KickSubcategoryStreamParams]) -> BinaryIO: ...
    @overload
    async def subcategory(self, **params: Unpack[KickSubcategoryTextResponseParams]) -> str: ...
    @overload
    async def subcategory(self, **params: Unpack[KickSubcategoryDefaultParams]) -> KickSubcategoryResponse: ...
    @overload
    async def top_channels(self, **params: Unpack[KickTopChannelsStreamParams]) -> BinaryIO: ...
    @overload
    async def top_channels(self, **params: Unpack[KickTopChannelsTextResponseParams]) -> str: ...
    @overload
    async def top_channels(self, **params: Unpack[KickTopChannelsDefaultParams]) -> KickTopChannelsResponse: ...
    @overload
    async def video(self, **params: Unpack[KickVideoStreamParams]) -> BinaryIO: ...
    @overload
    async def video(self, **params: Unpack[KickVideoTextResponseParams]) -> str: ...
    @overload
    async def video(self, **params: Unpack[KickVideoDefaultParams]) -> KickVideoResponse: ...

class _AsyncKickGroup:
    @overload
    async def categories(self, **params: Unpack[KickCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def categories(self, **params: Unpack[KickCategoriesTextResponseParams]) -> str: ...
    @overload
    async def categories(self, **params: Unpack[KickCategoriesDefaultParams]) -> KickCategoriesResponse: ...
    @overload
    async def category_clips(self, **params: Unpack[KickCategoryClipsStreamParams]) -> BinaryIO: ...
    @overload
    async def category_clips(self, **params: Unpack[KickCategoryClipsTextResponseParams]) -> str: ...
    @overload
    async def category_clips(self, **params: Unpack[KickCategoryClipsDefaultParams]) -> KickCategoryClipsResponse: ...
    @overload
    async def channel(self, **params: Unpack[KickChannelStreamParams]) -> BinaryIO: ...
    @overload
    async def channel(self, **params: Unpack[KickChannelTextResponseParams]) -> str: ...
    @overload
    async def channel(self, **params: Unpack[KickChannelDefaultParams]) -> KickChannelResponse: ...
    @overload
    async def channel_chatroom(self, **params: Unpack[KickChannelChatroomStreamParams]) -> BinaryIO: ...
    @overload
    async def channel_chatroom(self, **params: Unpack[KickChannelChatroomTextResponseParams]) -> str: ...
    @overload
    async def channel_chatroom(self, **params: Unpack[KickChannelChatroomDefaultParams]) -> KickChannelChatroomResponse: ...
    @overload
    async def channel_clips(self, **params: Unpack[KickChannelClipsStreamParams]) -> BinaryIO: ...
    @overload
    async def channel_clips(self, **params: Unpack[KickChannelClipsTextResponseParams]) -> str: ...
    @overload
    async def channel_clips(self, **params: Unpack[KickChannelClipsDefaultParams]) -> KickChannelClipsResponse: ...
    @overload
    async def channel_emotes(self, **params: Unpack[KickChannelEmotesStreamParams]) -> BinaryIO: ...
    @overload
    async def channel_emotes(self, **params: Unpack[KickChannelEmotesTextResponseParams]) -> str: ...
    @overload
    async def channel_emotes(self, **params: Unpack[KickChannelEmotesDefaultParams]) -> KickChannelEmotesResponse: ...
    @overload
    async def channel_links(self, **params: Unpack[KickChannelLinksStreamParams]) -> BinaryIO: ...
    @overload
    async def channel_links(self, **params: Unpack[KickChannelLinksTextResponseParams]) -> str: ...
    @overload
    async def channel_links(self, **params: Unpack[KickChannelLinksDefaultParams]) -> KickChannelLinksResponse: ...
    @overload
    async def channel_streams(self, **params: Unpack[KickChannelStreamsStreamParams]) -> BinaryIO: ...
    @overload
    async def channel_streams(self, **params: Unpack[KickChannelStreamsTextResponseParams]) -> str: ...
    @overload
    async def channel_streams(self, **params: Unpack[KickChannelStreamsDefaultParams]) -> KickChannelStreamsResponse: ...
    @overload
    async def channel_videos(self, **params: Unpack[KickChannelVideosStreamParams]) -> BinaryIO: ...
    @overload
    async def channel_videos(self, **params: Unpack[KickChannelVideosTextResponseParams]) -> str: ...
    @overload
    async def channel_videos(self, **params: Unpack[KickChannelVideosDefaultParams]) -> KickChannelVideosResponse: ...
    @overload
    async def clip(self, **params: Unpack[KickClipStreamParams]) -> BinaryIO: ...
    @overload
    async def clip(self, **params: Unpack[KickClipTextResponseParams]) -> str: ...
    @overload
    async def clip(self, **params: Unpack[KickClipDefaultParams]) -> KickClipResponse: ...
    @overload
    async def clips(self, **params: Unpack[KickClipsStreamParams]) -> BinaryIO: ...
    @overload
    async def clips(self, **params: Unpack[KickClipsTextResponseParams]) -> str: ...
    @overload
    async def clips(self, **params: Unpack[KickClipsDefaultParams]) -> KickClipsResponse: ...
    @overload
    async def drops(self, **params: Unpack[KickDropsStreamParams]) -> BinaryIO: ...
    @overload
    async def drops(self, **params: Unpack[KickDropsTextResponseParams]) -> str: ...
    @overload
    async def drops(self, **params: Unpack[KickDropsDefaultParams]) -> KickDropsResponse: ...
    @overload
    async def gifts(self, **params: Unpack[KickGiftsStreamParams]) -> BinaryIO: ...
    @overload
    async def gifts(self, **params: Unpack[KickGiftsTextResponseParams]) -> str: ...
    @overload
    async def gifts(self, **params: Unpack[KickGiftsDefaultParams]) -> KickGiftsResponse: ...
    @overload
    async def languages(self, **params: Unpack[KickLanguagesStreamParams]) -> BinaryIO: ...
    @overload
    async def languages(self, **params: Unpack[KickLanguagesTextResponseParams]) -> str: ...
    @overload
    async def languages(self, **params: Unpack[KickLanguagesDefaultParams]) -> KickLanguagesResponse: ...
    @overload
    async def livestreams(self, **params: Unpack[KickLivestreamsStreamParams]) -> BinaryIO: ...
    @overload
    async def livestreams(self, **params: Unpack[KickLivestreamsTextResponseParams]) -> str: ...
    @overload
    async def livestreams(self, **params: Unpack[KickLivestreamsDefaultParams]) -> KickLivestreamsResponse: ...
    @overload
    async def search_categories(self, **params: Unpack[KickSearchCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def search_categories(self, **params: Unpack[KickSearchCategoriesTextResponseParams]) -> str: ...
    @overload
    async def search_categories(self, **params: Unpack[KickSearchCategoriesDefaultParams]) -> KickSearchCategoriesResponse: ...
    @overload
    async def search_channels(self, **params: Unpack[KickSearchChannelsStreamParams]) -> BinaryIO: ...
    @overload
    async def search_channels(self, **params: Unpack[KickSearchChannelsTextResponseParams]) -> str: ...
    @overload
    async def search_channels(self, **params: Unpack[KickSearchChannelsDefaultParams]) -> KickSearchChannelsResponse: ...
    @overload
    async def subcategories(self, **params: Unpack[KickSubcategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def subcategories(self, **params: Unpack[KickSubcategoriesTextResponseParams]) -> str: ...
    @overload
    async def subcategories(self, **params: Unpack[KickSubcategoriesDefaultParams]) -> KickSubcategoriesResponse: ...
    @overload
    async def subcategory(self, **params: Unpack[KickSubcategoryStreamParams]) -> BinaryIO: ...
    @overload
    async def subcategory(self, **params: Unpack[KickSubcategoryTextResponseParams]) -> str: ...
    @overload
    async def subcategory(self, **params: Unpack[KickSubcategoryDefaultParams]) -> KickSubcategoryResponse: ...
    @overload
    async def top_channels(self, **params: Unpack[KickTopChannelsStreamParams]) -> BinaryIO: ...
    @overload
    async def top_channels(self, **params: Unpack[KickTopChannelsTextResponseParams]) -> str: ...
    @overload
    async def top_channels(self, **params: Unpack[KickTopChannelsDefaultParams]) -> KickTopChannelsResponse: ...
    @overload
    async def video(self, **params: Unpack[KickVideoStreamParams]) -> BinaryIO: ...
    @overload
    async def video(self, **params: Unpack[KickVideoTextResponseParams]) -> str: ...
    @overload
    async def video(self, **params: Unpack[KickVideoDefaultParams]) -> KickVideoResponse: ...

KickCategoriesDefaultParams = TypedDict('KickCategoriesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

KickCategoriesTextResponseParams = TypedDict('KickCategoriesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

KickCategoriesStreamParams = TypedDict('KickCategoriesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

KickCategoryClipsDefaultParams = TypedDict('KickCategoryClipsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'slug': Required[str],
    'cursor': NotRequired[str],
}, total=False)

KickCategoryClipsTextResponseParams = TypedDict('KickCategoryClipsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'slug': Required[str],
    'cursor': NotRequired[str],
}, total=False)

KickCategoryClipsStreamParams = TypedDict('KickCategoryClipsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'slug': Required[str],
    'cursor': NotRequired[str],
}, total=False)

KickChannelDefaultParams = TypedDict('KickChannelDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'slug': Required[str],
}, total=False)

KickChannelTextResponseParams = TypedDict('KickChannelTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'slug': Required[str],
}, total=False)

KickChannelStreamParams = TypedDict('KickChannelStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'slug': Required[str],
}, total=False)

KickChannelChatroomDefaultParams = TypedDict('KickChannelChatroomDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'slug': Required[str],
}, total=False)

KickChannelChatroomTextResponseParams = TypedDict('KickChannelChatroomTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'slug': Required[str],
}, total=False)

KickChannelChatroomStreamParams = TypedDict('KickChannelChatroomStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'slug': Required[str],
}, total=False)

KickChannelClipsDefaultParams = TypedDict('KickChannelClipsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'slug': Required[str],
    'cursor': NotRequired[str],
}, total=False)

KickChannelClipsTextResponseParams = TypedDict('KickChannelClipsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'slug': Required[str],
    'cursor': NotRequired[str],
}, total=False)

KickChannelClipsStreamParams = TypedDict('KickChannelClipsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'slug': Required[str],
    'cursor': NotRequired[str],
}, total=False)

KickChannelEmotesDefaultParams = TypedDict('KickChannelEmotesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'slug': Required[str],
}, total=False)

KickChannelEmotesTextResponseParams = TypedDict('KickChannelEmotesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'slug': Required[str],
}, total=False)

KickChannelEmotesStreamParams = TypedDict('KickChannelEmotesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'slug': Required[str],
}, total=False)

KickChannelLinksDefaultParams = TypedDict('KickChannelLinksDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'slug': Required[str],
}, total=False)

KickChannelLinksTextResponseParams = TypedDict('KickChannelLinksTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'slug': Required[str],
}, total=False)

KickChannelLinksStreamParams = TypedDict('KickChannelLinksStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'slug': Required[str],
}, total=False)

KickChannelStreamsDefaultParams = TypedDict('KickChannelStreamsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'slug': Required[str],
}, total=False)

KickChannelStreamsTextResponseParams = TypedDict('KickChannelStreamsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'slug': Required[str],
}, total=False)

KickChannelStreamsStreamParams = TypedDict('KickChannelStreamsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'slug': Required[str],
}, total=False)

KickChannelVideosDefaultParams = TypedDict('KickChannelVideosDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'slug': Required[str],
}, total=False)

KickChannelVideosTextResponseParams = TypedDict('KickChannelVideosTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'slug': Required[str],
}, total=False)

KickChannelVideosStreamParams = TypedDict('KickChannelVideosStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'slug': Required[str],
}, total=False)

KickClipDefaultParams = TypedDict('KickClipDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

KickClipTextResponseParams = TypedDict('KickClipTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

KickClipStreamParams = TypedDict('KickClipStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

KickClipsDefaultParams = TypedDict('KickClipsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'sort': NotRequired[Literal['date', 'views']],
    'time': NotRequired[Literal['day', 'week', 'month', 'all']],
    'cursor': NotRequired[str],
}, total=False)

KickClipsTextResponseParams = TypedDict('KickClipsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'sort': NotRequired[Literal['date', 'views']],
    'time': NotRequired[Literal['day', 'week', 'month', 'all']],
    'cursor': NotRequired[str],
}, total=False)

KickClipsStreamParams = TypedDict('KickClipsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'sort': NotRequired[Literal['date', 'views']],
    'time': NotRequired[Literal['day', 'week', 'month', 'all']],
    'cursor': NotRequired[str],
}, total=False)

KickDropsDefaultParams = TypedDict('KickDropsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'status': NotRequired[Literal['active', 'expired', 'all']],
}, total=False)

KickDropsTextResponseParams = TypedDict('KickDropsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'status': NotRequired[Literal['active', 'expired', 'all']],
}, total=False)

KickDropsStreamParams = TypedDict('KickDropsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'status': NotRequired[Literal['active', 'expired', 'all']],
}, total=False)

KickGiftsDefaultParams = TypedDict('KickGiftsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

KickGiftsTextResponseParams = TypedDict('KickGiftsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

KickGiftsStreamParams = TypedDict('KickGiftsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

KickLanguagesDefaultParams = TypedDict('KickLanguagesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

KickLanguagesTextResponseParams = TypedDict('KickLanguagesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

KickLanguagesStreamParams = TypedDict('KickLanguagesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

KickLivestreamsDefaultParams = TypedDict('KickLivestreamsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'sort': NotRequired[Literal['viewer_count_desc', 'featured']],
    'language': NotRequired[str],
    'category_id': NotRequired[int],
    'limit': NotRequired[int],
    'after': NotRequired[str],
}, total=False)

KickLivestreamsTextResponseParams = TypedDict('KickLivestreamsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'sort': NotRequired[Literal['viewer_count_desc', 'featured']],
    'language': NotRequired[str],
    'category_id': NotRequired[int],
    'limit': NotRequired[int],
    'after': NotRequired[str],
}, total=False)

KickLivestreamsStreamParams = TypedDict('KickLivestreamsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'sort': NotRequired[Literal['viewer_count_desc', 'featured']],
    'language': NotRequired[str],
    'category_id': NotRequired[int],
    'limit': NotRequired[int],
    'after': NotRequired[str],
}, total=False)

KickSearchCategoriesDefaultParams = TypedDict('KickSearchCategoriesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'query': Required[str],
    'limit': NotRequired[int],
}, total=False)

KickSearchCategoriesTextResponseParams = TypedDict('KickSearchCategoriesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'query': Required[str],
    'limit': NotRequired[int],
}, total=False)

KickSearchCategoriesStreamParams = TypedDict('KickSearchCategoriesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'query': Required[str],
    'limit': NotRequired[int],
}, total=False)

KickSearchChannelsDefaultParams = TypedDict('KickSearchChannelsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'query': Required[str],
    'live': NotRequired[bool],
    'limit': NotRequired[int],
}, total=False)

KickSearchChannelsTextResponseParams = TypedDict('KickSearchChannelsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'query': Required[str],
    'live': NotRequired[bool],
    'limit': NotRequired[int],
}, total=False)

KickSearchChannelsStreamParams = TypedDict('KickSearchChannelsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'query': Required[str],
    'live': NotRequired[bool],
    'limit': NotRequired[int],
}, total=False)

KickSubcategoriesDefaultParams = TypedDict('KickSubcategoriesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'category': NotRequired[Literal['games', 'irl', 'music', 'gambling', 'creative', 'alternative', 'chat-roulette']],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

KickSubcategoriesTextResponseParams = TypedDict('KickSubcategoriesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'category': NotRequired[Literal['games', 'irl', 'music', 'gambling', 'creative', 'alternative', 'chat-roulette']],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

KickSubcategoriesStreamParams = TypedDict('KickSubcategoriesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'category': NotRequired[Literal['games', 'irl', 'music', 'gambling', 'creative', 'alternative', 'chat-roulette']],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

KickSubcategoryDefaultParams = TypedDict('KickSubcategoryDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'slug': Required[str],
}, total=False)

KickSubcategoryTextResponseParams = TypedDict('KickSubcategoryTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'slug': Required[str],
}, total=False)

KickSubcategoryStreamParams = TypedDict('KickSubcategoryStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'slug': Required[str],
}, total=False)

KickTopChannelsDefaultParams = TypedDict('KickTopChannelsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

KickTopChannelsTextResponseParams = TypedDict('KickTopChannelsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

KickTopChannelsStreamParams = TypedDict('KickTopChannelsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

KickVideoDefaultParams = TypedDict('KickVideoDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

KickVideoTextResponseParams = TypedDict('KickVideoTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

KickVideoStreamParams = TypedDict('KickVideoStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)
