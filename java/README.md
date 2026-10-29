# Crawlora Kick API client for Java

The official Java client for Crawlora's hosted Kick API. It exposes 21 endpoints covering channels, livestreams, clips, categories, search, and public mobile-app catalogues. Requests use your `x-api-key`; the client does not connect to the upstream site directly.

## Install

```xml
<dependency>
  <groupId>net.crawlora</groupId>
  <artifactId>crawlora-kick</artifactId>
  <version>0.1.0</version>
</dependency>
```

## Use

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=kick-java-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=kick-java-console) to get an API key.

```java
import net.crawlora.kick.Client;
import java.time.Duration;
import java.util.Map;

try (Client client = new Client(System.getenv("CRAWLORA_API_KEY"))) {
    Object result = client.categories(Map.of());
    System.out.println(result);
}
```

Each operation has a direct method that accepts the parameters documented for that endpoint. Use `client.request(operationId, params)` for generic dispatch. `Client.OPERATION_IDS`, `Client.OPERATION_COUNT`, `client.getOperationIds()`, and `client.getOperationCount()` describe this platform's operations only.

For custom hosted API routing and timeouts, use `new Client(apiKey, baseUrl, Duration.ofSeconds(20))`. Text responses are returned as `String`; JSON responses are parsed into Java maps, lists, and scalar values.

## Supported Kick API endpoints

Browse every route included in this Java package. The [endpoint reference](https://github.com/Crawlora-org/crawlora-kick/blob/main/docs/usage.md) also lists parameters and response details.

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

## Links

- [Crawlora](https://crawlora.net/?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=kick-java-homepage)
- [Crawlora platform clients](https://github.com/Crawlora-org/crawlora-kick)
- [API documentation](https://crawlora.net/docs?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=kick-java-api-docs)
