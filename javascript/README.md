# @crawlora-org/kick — Kick API client for JavaScript and TypeScript

JavaScript and TypeScript client for Crawlora's hosted Kick API.
It exposes 21 API endpoints for channels, livestreams, clips, categories, search, and public mobile-app catalogues through [Crawlora](https://crawlora.net/?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=kick-javascript-homepage). It does not run a browser or scrape Kick locally. A Crawlora account and `CRAWLORA_API_KEY` are required, and API use is billed under your Crawlora account. Crawlora is independent from and not endorsed by Kick or its owners.

## Install

```sh
npm install @crawlora-org/kick
```

## Get an API key

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=kick-javascript-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=kick-javascript-console) for API-key setup. Set your key in the shell before running the client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

## Use

Save this example as `example.mjs`, then run `node example.mjs` after installing the package and setting your API key.

```js
import process from "node:process";
import { KickClient } from "@crawlora-org/kick";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new KickClient({ apiKey });
const result1 = await client.categories({});
console.log(result1);
const result2 = await client.livestreams({});
console.log(result2);
```

The client also exports `Client` as an alias for `KickClient`. Operation
methods are available directly in camelCase and through the `kick`
group. See the full method and parameter list in the [online reference](https://github.com/Crawlora-org/crawlora-kick/blob/main/docs/usage.md).

Methods return promises and can be awaited. See the [runnable example](https://github.com/Crawlora-org/crawlora-kick/blob/main/examples/javascript.mjs) for a complete usage example.

## Supported Kick API endpoints

This package exposes each route below as a direct method and through the `kick` group. See the [endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-kick/blob/main/docs/usage.md) for complete input details.

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

## Configuration

Pass your key through `apiKey` or set `CRAWLORA_API_KEY` and read it from the
environment. Keep credentials out of source control and logs. Requests are
made to Crawlora's hosted API. Response data and availability depend on
Crawlora's current API behavior.
