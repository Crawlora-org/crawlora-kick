# Crawlora Kick API client for Ruby (`crawlora-kick`)

This Ruby gem calls Crawlora's hosted Kick API at `https://api.crawlora.net/api/v1`. It exposes 21 endpoints covering channels, livestreams, clips, categories, search, and public mobile-app catalogues; it does not call or scrape Kick directly. Requests require your Crawlora API key and use your account's service plan.

## Install

```ruby
gem "crawlora-kick"
```

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=kick-ruby-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=kick-ruby-console) to get an API key, and set `CRAWLORA_API_KEY` before running the client:

```ruby
require "json"
require "crawlora/kick"

client = Crawlora::Kick::Client.new
result = client.request("kick-categories", JSON.parse("{}"))
puts result
client.close
```

Use an operation-specific method for normal calls. `request(operation_id, params = {}, response_type: :auto)` is available for every operation. `response_type: :text` returns raw response text. This gem includes 21 API operations.

```ruby
client = Crawlora::Kick::Client.new(api_key: ENV.fetch("CRAWLORA_API_KEY"), timeout: 30)
# client.<operation_method>(<endpoint parameters>)
client.close
```

Client options include `api_key`, `base_url`, and `timeout`. Ruby stdlib provides the HTTP and JSON support.

## Supported Kick API endpoints

Browse every route included in this gem. The [endpoint reference](https://github.com/Crawlora-org/crawlora-kick/blob/main/docs/usage.md) includes parameter and response details.

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

See [Crawlora](https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=kick-ruby-homepage), the [API documentation](https://crawlora.net/docs?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=kick-ruby-api-docs), and [the package repository](https://github.com/Crawlora-org/crawlora-kick) for account setup, the API operation reference, and release history.
