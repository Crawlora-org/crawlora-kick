# Kick clients for Crawlora

Official Crawlora client packages for the hosted Kick API. Access 21 API endpoints covering channels, livestreams, clips, categories, search, and public mobile-app catalogues from JavaScript/TypeScript, Python, Go, Ruby, Java, PHP, and Rust. These clients call Crawlora's hosted API; they do not scrape Kick locally. Requests use your Crawlora account and `CRAWLORA_API_KEY`; service usage follows your account billing plan. Crawlora is independent from and not affiliated with or endorsed by Kick or its owners.

## Language packages

- JavaScript / TypeScript: [`@crawlora-org/kick`](javascript/README.md)
- Python: [`crawlora-kick`](python/README.md)
- Go: [`github.com/Crawlora-org/crawlora-kick`](go.mod)
- Ruby: [`crawlora-kick`](ruby/README.md)
- Java: [`net.crawlora:crawlora-kick:0.1.0`](java/README.md)
- PHP: [`crawlora/kick`](php/README.md)
- Rust: [`crawlora-kick`](rust/README.md)

For installation and runnable examples, use the README for your language. See the [API endpoint and parameter reference](docs/usage.md) for shared operation details.

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=kick-repository-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=kick-repository-console) to get an API key, or read the [API documentation](https://crawlora.net/docs?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=kick-repository-api-docs). Keep `CRAWLORA_API_KEY` out of source control.

## API coverage and supported endpoints

The seven language clients provide access to all 21 selected public Kick API operations. Search or browse by endpoint path and operation ID below; the [complete API reference](docs/usage.md) adds parameters, enums, and response details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/kick/categories` | `kick-categories` | List Kick's top-level categories |
| `GET` | `/kick/category-clips` | `kick-category-clips` | List the newest clips in a Kick category |
| `GET` | `/kick/channel` | `kick-channel` | Get a Kick channel profile and live state |
| `GET` | `/kick/channel-chatroom` | `kick-channel-chatroom` | Get a Kick channel's chat settings and rules |
| `GET` | `/kick/channel-clips` | `kick-channel-clips` | List a Kick channel's clips |
| `GET` | `/kick/channel-emotes` | `kick-channel-emotes` | List the chat emotes a Kick channel offers |
| `GET` | `/kick/channel-links` | `kick-channel-links` | List a Kick channel's link panels |
| `GET` | `/kick/channel-streams` | `kick-channel-streams` | List a Kick channel's recent broadcast history |
| `GET` | `/kick/channel-videos` | `kick-channel-videos` | List a Kick channel's recent past broadcasts |
| `GET` | `/kick/clip` | `kick-clip` | Get one Kick clip |
| `GET` | `/kick/clips` | `kick-clips` | List Kick's site-wide clips |
| `GET` | `/kick/drops` | `kick-drops` | List Kick Drops campaigns |
| `GET` | `/kick/gifts` | `kick-gifts` | List the gifts viewers can send on Kick |
| `GET` | `/kick/languages` | `kick-languages` | List Kick stream languages |
| `GET` | `/kick/livestreams` | `kick-livestreams` | List live broadcasts on Kick |
| `GET` | `/kick/search-categories` | `kick-search-categories` | Search Kick categories |
| `GET` | `/kick/search-channels` | `kick-search-channels` | Search Kick channels |
| `GET` | `/kick/subcategories` | `kick-subcategories` | List Kick's game and activity categories |
| `GET` | `/kick/subcategory` | `kick-subcategory` | Get one Kick category |
| `GET` | `/kick/top-channels` | `kick-top-channels` | List Kick's top channels |
| `GET` | `/kick/video` | `kick-video` | Get a Kick video by its uuid |

## License

MIT. See [LICENSE](LICENSE).
