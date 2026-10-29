# Crawlora Kick API client for PHP (`crawlora/kick`)

This PHP package calls Crawlora's hosted Kick API at `https://api.crawlora.net/api/v1`. It exposes 21 endpoints covering channels, livestreams, clips, categories, search, and public mobile-app catalogues. It does not call or scrape Kick directly. Requests require a Crawlora API key and use your Crawlora account's service plan.

## Install

```sh
composer require crawlora/kick
```

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=kick-php-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=kick-php-console) to get an API key, then set `CRAWLORA_API_KEY` in your environment.

```php
<?php
require __DIR__ . '/vendor/autoload.php';

$client = new Crawlora\Kick\Client(apiKey: getenv('CRAWLORA_API_KEY'));
$result = $client->request("kick-categories", []);
print_r($result);
$client->close();
```

The client uses PHP cURL and JSON. Constructor options are `apiKey`, `baseUrl`, and `timeout`. Call the operation-specific method for direct access to each supported operation, or `request($operationId, $params, $responseType)` to dispatch by operation ID. Set `$responseType` to `text` for raw text output such as transcript formats. The package includes 21 API operations.

## Supported Kick API endpoints

Browse every route included in this Composer package. The [endpoint reference](https://github.com/Crawlora-org/crawlora-kick/blob/main/docs/usage.md) includes parameter and response details.

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

See [Crawlora](https://crawlora.net/?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=kick-php-homepage), the [API documentation](https://crawlora.net/docs?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=kick-php-api-docs), and the [PHP client source](https://github.com/Crawlora-org/crawlora-kick). The complete operation and parameter reference is in the [platform repository](https://github.com/Crawlora-org/crawlora-kick/blob/main/docs/usage.md).
