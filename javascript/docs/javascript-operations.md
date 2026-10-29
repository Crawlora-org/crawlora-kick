# Crawlora Kick JavaScript Client Operations

Generated from `openapi/public.json`. Deprecated, admin, and internal operations are excluded from this SDK contract.

Total operations: `21`

| Group | SDK method | Operation ID | HTTP | Params | Auth | Response | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| kick | `kick.categories` | `kick-categories` | `GET /kick/categories` | none | `ApiKeyAuth` | `KickCategoriesResponse` |  |
| kick | `kick.categoryClips` | `kick-category-clips` | `GET /kick/category-clips` | `slug` (query string required)<br>`cursor` (query string) | `ApiKeyAuth` | `KickCategoryClipsResponse` |  |
| kick | `kick.channel` | `kick-channel` | `GET /kick/channel` | `slug` (query string required) | `ApiKeyAuth` | `KickChannelResponse` |  |
| kick | `kick.channelChatroom` | `kick-channel-chatroom` | `GET /kick/channel-chatroom` | `slug` (query string required) | `ApiKeyAuth` | `KickChannelChatroomResponse` |  |
| kick | `kick.channelClips` | `kick-channel-clips` | `GET /kick/channel-clips` | `slug` (query string required)<br>`cursor` (query string) | `ApiKeyAuth` | `KickChannelClipsResponse` |  |
| kick | `kick.channelEmotes` | `kick-channel-emotes` | `GET /kick/channel-emotes` | `slug` (query string required) | `ApiKeyAuth` | `KickChannelEmotesResponse` |  |
| kick | `kick.channelLinks` | `kick-channel-links` | `GET /kick/channel-links` | `slug` (query string required) | `ApiKeyAuth` | `KickChannelLinksResponse` |  |
| kick | `kick.channelStreams` | `kick-channel-streams` | `GET /kick/channel-streams` | `slug` (query string required) | `ApiKeyAuth` | `KickChannelStreamsResponse` |  |
| kick | `kick.channelVideos` | `kick-channel-videos` | `GET /kick/channel-videos` | `slug` (query string required) | `ApiKeyAuth` | `KickChannelVideosResponse` |  |
| kick | `kick.clip` | `kick-clip` | `GET /kick/clip` | `id` (query string required) | `ApiKeyAuth` | `KickClipResponse` |  |
| kick | `kick.clips` | `kick-clips` | `GET /kick/clips` | `sort` (query "date" \| "views")<br>`time` (query "day" \| "week" \| "month" \| "all")<br>`cursor` (query string) | `ApiKeyAuth` | `KickClipsResponse` |  |
| kick | `kick.drops` | `kick-drops` | `GET /kick/drops` | `status` (query "active" \| "expired" \| "all") | `ApiKeyAuth` | `KickDropsResponse` |  |
| kick | `kick.gifts` | `kick-gifts` | `GET /kick/gifts` | none | `ApiKeyAuth` | `KickGiftsResponse` |  |
| kick | `kick.languages` | `kick-languages` | `GET /kick/languages` | none | `ApiKeyAuth` | `KickLanguagesResponse` |  |
| kick | `kick.livestreams` | `kick-livestreams` | `GET /kick/livestreams` | `sort` (query "viewer_count_desc" \| "featured")<br>`language` (query string)<br>`category_id` (query number)<br>`limit` (query number)<br>`after` (query string) | `ApiKeyAuth` | `KickLivestreamsResponse` |  |
| kick | `kick.searchCategories` | `kick-search-categories` | `GET /kick/search-categories` | `query` (query string required)<br>`limit` (query number) | `ApiKeyAuth` | `KickSearchCategoriesResponse` |  |
| kick | `kick.searchChannels` | `kick-search-channels` | `GET /kick/search-channels` | `query` (query string required)<br>`live` (query boolean)<br>`limit` (query number) | `ApiKeyAuth` | `KickSearchChannelsResponse` |  |
| kick | `kick.subcategories` | `kick-subcategories` | `GET /kick/subcategories` | `category` (query "games" \| "irl" \| "music" \| "gambling" \| "creative" \| "alternative" \| "chat-roulette")<br>`page` (query number)<br>`limit` (query number) | `ApiKeyAuth` | `KickSubcategoriesResponse` |  |
| kick | `kick.subcategory` | `kick-subcategory` | `GET /kick/subcategory` | `slug` (query string required) | `ApiKeyAuth` | `KickSubcategoryResponse` |  |
| kick | `kick.topChannels` | `kick-top-channels` | `GET /kick/top-channels` | none | `ApiKeyAuth` | `KickTopChannelsResponse` |  |
| kick | `kick.video` | `kick-video` | `GET /kick/video` | `id` (query string required) | `ApiKeyAuth` | `KickVideoResponse` |  |
