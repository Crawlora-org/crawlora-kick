# Kick API endpoint reference and client usage

This reference lists all 21 public Kick API endpoints exposed by the JavaScript/TypeScript, Python, Go, Ruby, Java, PHP, and Rust clients, including the `@crawlora-org/kick`, `crawlora-kick`, and `crawlora-kick` packages. The clients call Crawlora's hosted API. Set `CRAWLORA_API_KEY` to a key for your Crawlora account before making requests. Service usage is billed under that account. These clients do not run a browser or scrape Kick locally; Crawlora is independent from and not endorsed by Kick or its owners.

The package tracks the public API contract revision `sha256:21aa0d1aad656980f5ea6effcebad59951eac7af94ef33ab23888a3707f0ba5a` bundled with release `0.1.0`. Maintainers can preview daily contract updates with the repository's `Sync live API contract` workflow; unchanged contracts do not produce package releases.

All language packages expose the selected public API operations in the bundled contract. JavaScript uses camelCase methods, Python and Rust use snake_case methods. JavaScript, Python, and Rust methods are grouped under `kick`; Rust uses typed parameter structs and returns the complete HTTP response.

## Examples

The checked-in examples discover current entities or feeds before making the related requests, using parameter names and values supported by the API contract:

- [JavaScript](../examples/javascript.mjs)
- [Python](../examples/python.py)
- [Rust](../rust/examples/quick_start.rs)



## Complete operation reference

Required and optional parameter names below come from this package's generated OpenAPI contract. Path parameters are passed alongside query and body values in the same method argument object/keywords.

| JavaScript | Python | Rust | Endpoint | Parameters | Description |
| --- | --- | --- | --- | --- | --- |
| `categories` | `categories` | `kick.categories` | `GET /kick/categories` | — | List Kick's top-level categories |
| `categoryClips` | `category_clips` | `kick.category_clips` | `GET /kick/category-clips` | `slug` (query, required), `cursor` (query, optional) | List the newest clips in a Kick category |
| `channel` | `channel` | `kick.channel` | `GET /kick/channel` | `slug` (query, required) | Get a Kick channel profile and live state |
| `channelChatroom` | `channel_chatroom` | `kick.channel_chatroom` | `GET /kick/channel-chatroom` | `slug` (query, required) | Get a Kick channel's chat settings and rules |
| `channelClips` | `channel_clips` | `kick.channel_clips` | `GET /kick/channel-clips` | `slug` (query, required), `cursor` (query, optional) | List a Kick channel's clips |
| `channelEmotes` | `channel_emotes` | `kick.channel_emotes` | `GET /kick/channel-emotes` | `slug` (query, required) | List the chat emotes a Kick channel offers |
| `channelLinks` | `channel_links` | `kick.channel_links` | `GET /kick/channel-links` | `slug` (query, required) | List a Kick channel's link panels |
| `channelStreams` | `channel_streams` | `kick.channel_streams` | `GET /kick/channel-streams` | `slug` (query, required) | List a Kick channel's recent broadcast history |
| `channelVideos` | `channel_videos` | `kick.channel_videos` | `GET /kick/channel-videos` | `slug` (query, required) | List a Kick channel's recent past broadcasts |
| `clip` | `clip` | `kick.clip` | `GET /kick/clip` | `id` (query, required) | Get one Kick clip |
| `clips` | `clips` | `kick.clips` | `GET /kick/clips` | `sort` (query, optional; values: `date`, `views`), `time` (query, optional; values: `day`, `week`, `month`, `all`), `cursor` (query, optional) | List Kick's site-wide clips |
| `drops` | `drops` | `kick.drops` | `GET /kick/drops` | `status` (query, optional; values: `active`, `expired`, `all`) | List Kick Drops campaigns |
| `gifts` | `gifts` | `kick.gifts` | `GET /kick/gifts` | — | List the gifts viewers can send on Kick |
| `languages` | `languages` | `kick.languages` | `GET /kick/languages` | — | List Kick stream languages |
| `livestreams` | `livestreams` | `kick.livestreams` | `GET /kick/livestreams` | `sort` (query, optional; values: `viewer_count_desc`, `featured`), `language` (query, optional), `category_id` (query, optional), `limit` (query, optional), `after` (query, optional) | List live broadcasts on Kick |
| `searchCategories` | `search_categories` | `kick.search_categories` | `GET /kick/search-categories` | `query` (query, required), `limit` (query, optional) | Search Kick categories |
| `searchChannels` | `search_channels` | `kick.search_channels` | `GET /kick/search-channels` | `query` (query, required), `live` (query, optional), `limit` (query, optional) | Search Kick channels |
| `subcategories` | `subcategories` | `kick.subcategories` | `GET /kick/subcategories` | `category` (query, optional; values: `games`, `irl`, `music`, `gambling`, `creative`, `alternative`, `chat-roulette`), `page` (query, optional), `limit` (query, optional) | List Kick's game and activity categories |
| `subcategory` | `subcategory` | `kick.subcategory` | `GET /kick/subcategory` | `slug` (query, required) | Get one Kick category |
| `topChannels` | `top_channels` | `kick.top_channels` | `GET /kick/top-channels` | — | List Kick's top channels |
| `video` | `video` | `kick.video` | `GET /kick/video` | `id` (query, required) | Get a Kick video by its uuid |

## Client forms

- JavaScript: import `KickClient` (also exported as `Client`) from `@crawlora-org/kick`; use `new KickClient({ apiKey })` and `await client.method({ ... })`.
- Python: import `KickClient` (also exported as `Client`) from `crawlora_kick`; use `with KickClient(api_key=...) as client` and `client.method(...)`.
- Python async class: `AsyncKickClient`, used with `async with` and `await`.
- Rust: add `crawlora-kick` with Cargo; import `Client` and the generated operation parameter struct, then call `client.kick.<snake_case_method>(params).await`. See the [Rust example](https://github.com/Crawlora-org/crawlora-kick/blob/main/rust/examples/quick_start.rs).

See the package READMEs for installation details. Keep API keys in environment variables or a secret store; do not commit them.
