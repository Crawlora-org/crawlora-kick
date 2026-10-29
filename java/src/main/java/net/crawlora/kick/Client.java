package net.crawlora.kick;

import net.crawlora.Json;

import java.io.IOException;
import java.net.URI;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.time.Duration;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Set;
import java.util.TreeSet;

/** Client for the Kick endpoints hosted by Crawlora. */
public final class Client implements AutoCloseable {
    public static final String DEFAULT_BASE_URL = "https://api.crawlora.net/api/v1";
    public static final int OPERATION_COUNT = 21;
    public static final List<String> OPERATION_IDS = List.of(
            "kick-categories",
            "kick-category-clips",
            "kick-channel",
            "kick-channel-chatroom",
            "kick-channel-clips",
            "kick-channel-emotes",
            "kick-channel-links",
            "kick-channel-streams",
            "kick-channel-videos",
            "kick-clip",
            "kick-clips",
            "kick-drops",
            "kick-gifts",
            "kick-languages",
            "kick-livestreams",
            "kick-search-categories",
            "kick-search-channels",
            "kick-subcategories",
            "kick-subcategory",
            "kick-top-channels",
            "kick-video"
    );

    private static final Map<String, Operation> OPERATIONS;
    static {
        Map<String, Operation> operations = new LinkedHashMap<>();
        operations.put("kick-categories", new Operation("kick-categories", "GET", "/kick/categories", Map.of(), List.of("application/json")));
        operations.put("kick-category-clips", new Operation("kick-category-clips", "GET", "/kick/category-clips", Map.ofEntries(Map.entry("slug", new Param("slug", "query", true, "string", List.of(), "csv")), Map.entry("cursor", new Param("cursor", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("kick-channel", new Operation("kick-channel", "GET", "/kick/channel", Map.ofEntries(Map.entry("slug", new Param("slug", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("kick-channel-chatroom", new Operation("kick-channel-chatroom", "GET", "/kick/channel-chatroom", Map.ofEntries(Map.entry("slug", new Param("slug", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("kick-channel-clips", new Operation("kick-channel-clips", "GET", "/kick/channel-clips", Map.ofEntries(Map.entry("slug", new Param("slug", "query", true, "string", List.of(), "csv")), Map.entry("cursor", new Param("cursor", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("kick-channel-emotes", new Operation("kick-channel-emotes", "GET", "/kick/channel-emotes", Map.ofEntries(Map.entry("slug", new Param("slug", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("kick-channel-links", new Operation("kick-channel-links", "GET", "/kick/channel-links", Map.ofEntries(Map.entry("slug", new Param("slug", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("kick-channel-streams", new Operation("kick-channel-streams", "GET", "/kick/channel-streams", Map.ofEntries(Map.entry("slug", new Param("slug", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("kick-channel-videos", new Operation("kick-channel-videos", "GET", "/kick/channel-videos", Map.ofEntries(Map.entry("slug", new Param("slug", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("kick-clip", new Operation("kick-clip", "GET", "/kick/clip", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("kick-clips", new Operation("kick-clips", "GET", "/kick/clips", Map.ofEntries(Map.entry("sort", new Param("sort", "query", false, "string", List.of("date", "views"), "csv")), Map.entry("time", new Param("time", "query", false, "string", List.of("day", "week", "month", "all"), "csv")), Map.entry("cursor", new Param("cursor", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("kick-drops", new Operation("kick-drops", "GET", "/kick/drops", Map.ofEntries(Map.entry("status", new Param("status", "query", false, "string", List.of("active", "expired", "all"), "csv"))), List.of("application/json")));
        operations.put("kick-gifts", new Operation("kick-gifts", "GET", "/kick/gifts", Map.of(), List.of("application/json")));
        operations.put("kick-languages", new Operation("kick-languages", "GET", "/kick/languages", Map.of(), List.of("application/json")));
        operations.put("kick-livestreams", new Operation("kick-livestreams", "GET", "/kick/livestreams", Map.ofEntries(Map.entry("sort", new Param("sort", "query", false, "string", List.of("viewer_count_desc", "featured"), "csv")), Map.entry("language", new Param("language", "query", false, "string", List.of(), "csv")), Map.entry("category_id", new Param("category_id", "query", false, "integer", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("after", new Param("after", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("kick-search-categories", new Operation("kick-search-categories", "GET", "/kick/search-categories", Map.ofEntries(Map.entry("query", new Param("query", "query", true, "string", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("kick-search-channels", new Operation("kick-search-channels", "GET", "/kick/search-channels", Map.ofEntries(Map.entry("query", new Param("query", "query", true, "string", List.of(), "csv")), Map.entry("live", new Param("live", "query", false, "boolean", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("kick-subcategories", new Operation("kick-subcategories", "GET", "/kick/subcategories", Map.ofEntries(Map.entry("category", new Param("category", "query", false, "string", List.of("games", "irl", "music", "gambling", "creative", "alternative", "chat-roulette"), "csv")), Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("kick-subcategory", new Operation("kick-subcategory", "GET", "/kick/subcategory", Map.ofEntries(Map.entry("slug", new Param("slug", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("kick-top-channels", new Operation("kick-top-channels", "GET", "/kick/top-channels", Map.of(), List.of("application/json")));
        operations.put("kick-video", new Operation("kick-video", "GET", "/kick/video", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        OPERATIONS = Collections.unmodifiableMap(operations);
    }

    private final String apiKey;
    private final String baseUrl;
    private final Duration timeout;
    private final HttpClient http;
    private volatile boolean closed;

    /** Create a client using Crawlora's hosted API and the default 30 second timeout. */
    public Client(String apiKey) {
        this(apiKey, DEFAULT_BASE_URL, Duration.ofSeconds(30));
    }

    /** Create a client with an explicit hosted API base URL and request timeout. */
    public Client(String apiKey, String baseUrl, Duration timeout) {
        if (apiKey == null || apiKey.isBlank()) throw new IllegalArgumentException("apiKey is required");
        if (baseUrl == null || baseUrl.isBlank()) throw new IllegalArgumentException("baseUrl is required");
        this.apiKey = apiKey;
        this.baseUrl = baseUrl.replaceAll("/+$", "");
        this.timeout = Objects.requireNonNull(timeout, "timeout");
        if (timeout.isZero() || timeout.isNegative()) throw new IllegalArgumentException("timeout must be positive");
        this.http = HttpClient.newBuilder().connectTimeout(timeout).build();
    }

    public String getBaseUrl() { return baseUrl; }
    public Duration getTimeout() { return timeout; }
    public int getOperationCount() { return OPERATION_COUNT; }
    public List<String> getOperationIds() { return OPERATION_IDS; }
    public static Map<String, Operation> operations() { return OPERATIONS; }

    /** Dispatch a selected operation by id. Parameters use the exact OpenAPI names. */
    public Object request(String operationId, Map<String, ?> params) {
        if (closed) throw new IllegalStateException("client is closed");
        Operation operation = OPERATIONS.get(operationId);
        if (operation == null) throw new IllegalArgumentException("unknown Kick operation: " + operationId);
        Map<String, ?> values = params == null ? Map.of() : params;
        boolean post = operation.method().equals("POST");
        Set<String> unknown = new TreeSet<>(values.keySet());
        unknown.removeAll(operation.params().keySet());
        // POST operations take their JSON body under the body parameter name or "body".
        if (post) {
            unknown.remove("body");
            unknown.remove(operation.bodyParam());
        }
        if (!unknown.isEmpty()) throw new IllegalArgumentException("unknown parameters for " + operationId + ": " + unknown);

        String path = operation.path();
        List<Map.Entry<String, String>> query = new ArrayList<>();
        for (Param param : operation.params().values()) {
            Object value = values.get(param.name());
            if (value == null) {
                if (param.required()) throw new IllegalArgumentException("missing required parameter: " + param.name());
                continue;
            }
            validateEnum(param, value);
            if (param.location().equals("path")) {
                path = path.replace("{" + param.name() + "}", pathEncode(value.toString()));
            } else {
                addQuery(query, param, value);
            }
        }
        if (path.matches(".*\\{[^}]+}.*")) throw new IllegalArgumentException("missing path parameter for " + operationId);
        StringBuilder url = new StringBuilder(baseUrl).append(path);
        for (int i = 0; i < query.size(); i++) {
            url.append(i == 0 ? '?' : '&').append(queryEncode(query.get(i).getKey()))
                    .append('=').append(queryEncode(query.get(i).getValue()));
        }
        HttpRequest.Builder builder = HttpRequest.newBuilder(URI.create(url.toString()))
                .timeout(timeout)
                .header("x-api-key", apiKey)
                .header("Accept", acceptHeader(operation));
        if (post) {
            Object body = values.get(operation.bodyParam());
            if (body == null) body = values.get("body");
            if (body == null) throw new IllegalArgumentException("missing request body for " + operationId);
            String payload = body instanceof String text ? text : Json.write(body);
            builder.header("Content-Type", "application/json")
                    .POST(HttpRequest.BodyPublishers.ofString(payload, StandardCharsets.UTF_8));
        } else {
            builder.GET();
        }
        HttpRequest request = builder.build();
        try {
            HttpResponse<String> response = http.send(request, HttpResponse.BodyHandlers.ofString(StandardCharsets.UTF_8));
            String body = response.body();
            String contentType = response.headers().firstValue("content-type").orElse("").toLowerCase();
            Object parsed = body;
            if (contentType.contains("application/json") && !body.isEmpty()) {
                try { parsed = Json.parse(body); }
                catch (RuntimeException error) { throw new CrawloraException("Crawlora returned invalid JSON", error); }
            }
            if (response.statusCode() < 200 || response.statusCode() >= 300) {
                String message = "Crawlora request failed with HTTP " + response.statusCode();
                if (parsed instanceof Map<?, ?> map && map.get("msg") != null) message = map.get("msg").toString();
                throw new CrawloraException(message, response.statusCode(), parsed);
            }
            return parsed;
        } catch (InterruptedException error) {
            Thread.currentThread().interrupt();
            throw new CrawloraException("Crawlora request interrupted", error);
        } catch (IOException error) {
            throw new CrawloraException("Crawlora network request failed", error);
        }
    }

    public Object categories(Map<String, ?> params) { return request("kick-categories", params); }
    public Object categoryClips(Map<String, ?> params) { return request("kick-category-clips", params); }
    public Object channel(Map<String, ?> params) { return request("kick-channel", params); }
    public Object channelChatroom(Map<String, ?> params) { return request("kick-channel-chatroom", params); }
    public Object channelClips(Map<String, ?> params) { return request("kick-channel-clips", params); }
    public Object channelEmotes(Map<String, ?> params) { return request("kick-channel-emotes", params); }
    public Object channelLinks(Map<String, ?> params) { return request("kick-channel-links", params); }
    public Object channelStreams(Map<String, ?> params) { return request("kick-channel-streams", params); }
    public Object channelVideos(Map<String, ?> params) { return request("kick-channel-videos", params); }
    public Object clip(Map<String, ?> params) { return request("kick-clip", params); }
    public Object clips(Map<String, ?> params) { return request("kick-clips", params); }
    public Object drops(Map<String, ?> params) { return request("kick-drops", params); }
    public Object gifts(Map<String, ?> params) { return request("kick-gifts", params); }
    public Object languages(Map<String, ?> params) { return request("kick-languages", params); }
    public Object livestreams(Map<String, ?> params) { return request("kick-livestreams", params); }
    public Object searchCategories(Map<String, ?> params) { return request("kick-search-categories", params); }
    public Object searchChannels(Map<String, ?> params) { return request("kick-search-channels", params); }
    public Object subcategories(Map<String, ?> params) { return request("kick-subcategories", params); }
    public Object subcategory(Map<String, ?> params) { return request("kick-subcategory", params); }
    public Object topChannels(Map<String, ?> params) { return request("kick-top-channels", params); }
    public Object video(Map<String, ?> params) { return request("kick-video", params); }

    private static String acceptHeader(Operation operation) {
        return operation.produces().isEmpty() ? "application/json" : String.join(", ", operation.produces());
    }

    private static void validateEnum(Param param, Object value) {
        if (param.enumValues().isEmpty()) return;
        for (Object item : items(value)) {
            if (!param.enumValues().contains(String.valueOf(item))) {
                throw new IllegalArgumentException("invalid " + param.name() + ": expected one of " + param.enumValues());
            }
        }
    }

    private static void addQuery(List<Map.Entry<String, String>> query, Param param, Object value) {
        List<?> values = items(value);
        String delimiter = switch (param.collectionFormat()) {
            case "ssv" -> " ";
            case "tsv" -> "\t";
            case "pipes" -> "|";
            default -> ",";
        };
        if (value instanceof Iterable<?> || value.getClass().isArray()) {
            String joined = String.join(delimiter, values.stream().map(String::valueOf).toList());
            query.add(Map.entry(param.name(), joined));
        } else {
            query.add(Map.entry(param.name(), String.valueOf(value)));
        }
    }

    private static List<?> items(Object value) {
        if (value instanceof Iterable<?> iterable) {
            List<Object> result = new ArrayList<>();
            iterable.forEach(result::add);
            return result;
        }
        if (value != null && value.getClass().isArray()) {
            int length = java.lang.reflect.Array.getLength(value);
            List<Object> result = new ArrayList<>(length);
            for (int i = 0; i < length; i++) result.add(java.lang.reflect.Array.get(value, i));
            return result;
        }
        return List.of(value);
    }

    private static String pathEncode(String value) {
        return URLEncoder.encode(value, StandardCharsets.UTF_8).replace("+", "%20");
    }

    private static String queryEncode(String value) {
        return URLEncoder.encode(value, StandardCharsets.UTF_8);
    }

    @Override public void close() { closed = true; }
}
