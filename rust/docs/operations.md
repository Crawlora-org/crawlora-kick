# Crawlora Kick Rust SDK Operations

Generated from `openapi/public.json`. Deprecated, admin, and internal operations are excluded from this SDK contract.

Total operations: `21`

| Group | SDK method | Operation ID | HTTP | Params | Auth | Response | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| kick | `kick.categories` | `kick-categories` | `GET /kick/categories` | none | `ApiKeyAuth` | `KickCategoriesResponse` |  |
| kick | `kick.category_clips` | `kick-category-clips` | `GET /kick/category-clips` | `slug` (query String required)<br>`cursor` (query String) | `ApiKeyAuth` | `KickCategoryClipsResponse` |  |
| kick | `kick.channel` | `kick-channel` | `GET /kick/channel` | `slug` (query String required) | `ApiKeyAuth` | `KickChannelResponse` |  |
| kick | `kick.channel_chatroom` | `kick-channel-chatroom` | `GET /kick/channel-chatroom` | `slug` (query String required) | `ApiKeyAuth` | `KickChannelChatroomResponse` |  |
| kick | `kick.channel_clips` | `kick-channel-clips` | `GET /kick/channel-clips` | `slug` (query String required)<br>`cursor` (query String) | `ApiKeyAuth` | `KickChannelClipsResponse` |  |
| kick | `kick.channel_emotes` | `kick-channel-emotes` | `GET /kick/channel-emotes` | `slug` (query String required) | `ApiKeyAuth` | `KickChannelEmotesResponse` |  |
| kick | `kick.channel_links` | `kick-channel-links` | `GET /kick/channel-links` | `slug` (query String required) | `ApiKeyAuth` | `KickChannelLinksResponse` |  |
| kick | `kick.channel_streams` | `kick-channel-streams` | `GET /kick/channel-streams` | `slug` (query String required) | `ApiKeyAuth` | `KickChannelStreamsResponse` |  |
| kick | `kick.channel_videos` | `kick-channel-videos` | `GET /kick/channel-videos` | `slug` (query String required) | `ApiKeyAuth` | `KickChannelVideosResponse` |  |
| kick | `kick.clip` | `kick-clip` | `GET /kick/clip` | `id` (query String required) | `ApiKeyAuth` | `KickClipResponse` |  |
| kick | `kick.clips` | `kick-clips` | `GET /kick/clips` | `sort` (query String enum{date, views})<br>`time` (query String enum{day, week, month, all})<br>`cursor` (query String) | `ApiKeyAuth` | `KickClipsResponse` |  |
| kick | `kick.drops` | `kick-drops` | `GET /kick/drops` | `status` (query String enum{active, expired, all}) | `ApiKeyAuth` | `KickDropsResponse` |  |
| kick | `kick.gifts` | `kick-gifts` | `GET /kick/gifts` | none | `ApiKeyAuth` | `KickGiftsResponse` |  |
| kick | `kick.languages` | `kick-languages` | `GET /kick/languages` | none | `ApiKeyAuth` | `KickLanguagesResponse` |  |
| kick | `kick.livestreams` | `kick-livestreams` | `GET /kick/livestreams` | `sort` (query String enum{viewer_count_desc, featured})<br>`language` (query String)<br>`category_id` (query i64)<br>`limit` (query i64)<br>`after` (query String) | `ApiKeyAuth` | `KickLivestreamsResponse` |  |
| kick | `kick.search_categories` | `kick-search-categories` | `GET /kick/search-categories` | `query` (query String required)<br>`limit` (query i64) | `ApiKeyAuth` | `KickSearchCategoriesResponse` |  |
| kick | `kick.search_channels` | `kick-search-channels` | `GET /kick/search-channels` | `query` (query String required)<br>`live` (query bool)<br>`limit` (query i64) | `ApiKeyAuth` | `KickSearchChannelsResponse` |  |
| kick | `kick.subcategories` | `kick-subcategories` | `GET /kick/subcategories` | `category` (query String enum{games, irl, music, gambling, creative, alternative, chat-roulette})<br>`page` (query i64)<br>`limit` (query i64) | `ApiKeyAuth` | `KickSubcategoriesResponse` |  |
| kick | `kick.subcategory` | `kick-subcategory` | `GET /kick/subcategory` | `slug` (query String required) | `ApiKeyAuth` | `KickSubcategoryResponse` |  |
| kick | `kick.top_channels` | `kick-top-channels` | `GET /kick/top-channels` | none | `ApiKeyAuth` | `KickTopChannelsResponse` |  |
| kick | `kick.video` | `kick-video` | `GET /kick/video` | `id` (query String required) | `ApiKeyAuth` | `KickVideoResponse` |  |
