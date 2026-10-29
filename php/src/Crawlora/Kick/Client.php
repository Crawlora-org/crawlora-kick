<?php

declare(strict_types=1);

namespace Crawlora\Kick;

class CrawloraException extends \RuntimeException
{
    public function __construct(string $message, public readonly ?int $status = null, public readonly ?string $operationId = null, public readonly ?string $responseBody = null, ?\Throwable $previous = null)
    {
        parent::__construct($message, 0, $previous);
    }
}

class ClientException extends CrawloraException {}
class ServerException extends CrawloraException {}
class NetworkException extends CrawloraException {}

final class Client
{
    private static array $operations;
    private bool $closed = false;
    private string $apiKey;
    private string $baseUrl;
    private float $timeout;
    private ?\Closure $transport;

    public const PLATFORM = 'kick';
    public const VERSION = '0.1.0';
    public const OPERATION_COUNT = 21;
    public const OPERATION_IDS = ["kick-categories", "kick-category-clips", "kick-channel", "kick-channel-chatroom", "kick-channel-clips", "kick-channel-emotes", "kick-channel-links", "kick-channel-streams", "kick-channel-videos", "kick-clip", "kick-clips", "kick-drops", "kick-gifts", "kick-languages", "kick-livestreams", "kick-search-categories", "kick-search-channels", "kick-subcategories", "kick-subcategory", "kick-top-channels", "kick-video"];

    public function __construct(?string $apiKey = null, string $baseUrl = 'https://api.crawlora.net/api/v1', float $timeout = 30.0, ?callable $transport = null)
    {
        $this->apiKey = $apiKey ?? (getenv('CRAWLORA_API_KEY') ?: '');
        $this->baseUrl = rtrim($baseUrl, '/');
        $this->timeout = $timeout;
        $this->transport = $transport === null ? null : \Closure::fromCallable($transport);
        self::$operations ??= json_decode(<<<'JSON'
{"kick-categories": {"bodyParam": null, "bodyRequired": false, "id": "kick-categories", "method": "GET", "params": [], "path": "/kick/categories", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "kick-category-clips": {"bodyParam": null, "bodyRequired": false, "id": "kick-category-clips", "method": "GET", "params": [{"description": "Category slug from kick-subcategories or kick-search-categories, lowercase; a kick.com/category URL is also accepted", "in": "query", "name": "slug", "required": true, "type": "string", "x-example": "just-chatting"}, {"description": "Previous response's next_cursor; omit for the newest page", "in": "query", "name": "cursor", "type": "string", "x-example": "clip_01M5TR7FRZPCDA6BS1NP7HKV4T"}], "path": "/kick/category-clips", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "slug", "required": true, "type": "string"}, {"in": "query", "name": "cursor", "type": "string"}], "security": ["ApiKeyAuth"]}, "kick-channel": {"bodyParam": null, "bodyRequired": false, "id": "kick-channel", "method": "GET", "params": [{"description": "Channel slug from kick.com/{slug}, case-insensitive; a kick.com URL is also accepted", "in": "query", "name": "slug", "required": true, "type": "string", "x-example": "xqc"}], "path": "/kick/channel", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "slug", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "kick-channel-chatroom": {"bodyParam": null, "bodyRequired": false, "id": "kick-channel-chatroom", "method": "GET", "params": [{"description": "Channel slug from kick.com/{slug}, case-insensitive; a kick.com URL is also accepted", "in": "query", "name": "slug", "required": true, "type": "string", "x-example": "xqc"}], "path": "/kick/channel-chatroom", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "slug", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "kick-channel-clips": {"bodyParam": null, "bodyRequired": false, "id": "kick-channel-clips", "method": "GET", "params": [{"description": "Channel slug from kick.com/{slug}, case-insensitive; a kick.com URL is also accepted", "in": "query", "name": "slug", "required": true, "type": "string", "x-example": "xqc"}, {"description": "Previous response's next_cursor; omit for the newest page", "in": "query", "name": "cursor", "type": "string", "x-example": "abc"}], "path": "/kick/channel-clips", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "slug", "required": true, "type": "string"}, {"in": "query", "name": "cursor", "type": "string"}], "security": ["ApiKeyAuth"]}, "kick-channel-emotes": {"bodyParam": null, "bodyRequired": false, "id": "kick-channel-emotes", "method": "GET", "params": [{"description": "Channel slug from kick.com/{slug}, case-insensitive; a kick.com URL is also accepted", "in": "query", "name": "slug", "required": true, "type": "string", "x-example": "xqc"}], "path": "/kick/channel-emotes", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "slug", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "kick-channel-links": {"bodyParam": null, "bodyRequired": false, "id": "kick-channel-links", "method": "GET", "params": [{"description": "Channel slug from kick.com/{slug}, case-insensitive; a kick.com URL is also accepted", "in": "query", "name": "slug", "required": true, "type": "string", "x-example": "xqc"}], "path": "/kick/channel-links", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "slug", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "kick-channel-streams": {"bodyParam": null, "bodyRequired": false, "id": "kick-channel-streams", "method": "GET", "params": [{"description": "Channel slug from kick.com/{slug}, case-insensitive; a kick.com URL is also accepted", "in": "query", "name": "slug", "required": true, "type": "string", "x-example": "xqc"}], "path": "/kick/channel-streams", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "slug", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "kick-channel-videos": {"bodyParam": null, "bodyRequired": false, "id": "kick-channel-videos", "method": "GET", "params": [{"description": "Channel slug from kick.com/{slug}, case-insensitive; a kick.com URL is also accepted", "in": "query", "name": "slug", "required": true, "type": "string", "x-example": "xqc"}], "path": "/kick/channel-videos", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "slug", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "kick-clip": {"bodyParam": null, "bodyRequired": false, "id": "kick-clip", "method": "GET", "params": [{"description": "Clip id from kick-clips' or kick-channel-clips' own clips[].id field", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "clip_01M5SKVA6GGAAAT5YPJ7J43WE4"}], "path": "/kick/clip", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "kick-clips": {"bodyParam": null, "bodyRequired": false, "id": "kick-clips", "method": "GET", "params": [{"description": "Ordering: date is newest first (default), views ranks by views inside the time window", "enum": ["date", "views"], "in": "query", "name": "sort", "type": "string", "x-example": "views"}, {"description": "Window that views ranks within; omit for Kick's default window", "enum": ["day", "week", "month", "all"], "in": "query", "name": "time", "type": "string", "x-example": "week"}, {"description": "Previous response's next_cursor; omit for the first page", "in": "query", "name": "cursor", "type": "string", "x-example": "abc"}], "path": "/kick/clips", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["date", "views"], "in": "query", "name": "sort", "type": "string"}, {"enum": ["day", "week", "month", "all"], "in": "query", "name": "time", "type": "string"}, {"in": "query", "name": "cursor", "type": "string"}], "security": ["ApiKeyAuth"]}, "kick-drops": {"bodyParam": null, "bodyRequired": false, "id": "kick-drops", "method": "GET", "params": [{"description": "Which campaigns to return: active (default), expired or all", "enum": ["active", "expired", "all"], "in": "query", "name": "status", "type": "string", "x-example": "active"}], "path": "/kick/drops", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["active", "expired", "all"], "in": "query", "name": "status", "type": "string"}], "security": ["ApiKeyAuth"]}, "kick-gifts": {"bodyParam": null, "bodyRequired": false, "id": "kick-gifts", "method": "GET", "params": [], "path": "/kick/gifts", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "kick-languages": {"bodyParam": null, "bodyRequired": false, "id": "kick-languages", "method": "GET", "params": [], "path": "/kick/languages", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "kick-livestreams": {"bodyParam": null, "bodyRequired": false, "id": "kick-livestreams", "method": "GET", "params": [{"description": "Ordering: viewer_count_desc is most viewers first (default), featured is Kick's featured order", "enum": ["viewer_count_desc", "featured"], "in": "query", "name": "sort", "type": "string", "x-example": "viewer_count_desc"}, {"description": "Stream language code such as en, ja, es, pt-BR, optionally with a region (2 to 3 letters, then an optional 2 to 4 letter region); see kick-languages for the codes Kick lists", "in": "query", "name": "language", "type": "string", "x-example": "ja"}, {"description": "Category id from kick-subcategories' or kick-search-categories' own id field", "in": "query", "name": "category_id", "type": "integer", "x-example": 15}, {"description": "Page size, 1 to 100; defaults to 24", "in": "query", "name": "limit", "type": "integer", "x-example": 24}, {"description": "Previous response's next_cursor; omit for the first page", "in": "query", "name": "after", "type": "string", "x-example": "eyJvIjoxfQ"}], "path": "/kick/livestreams", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["viewer_count_desc", "featured"], "in": "query", "name": "sort", "type": "string"}, {"in": "query", "name": "language", "type": "string"}, {"in": "query", "name": "category_id", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "after", "type": "string"}], "security": ["ApiKeyAuth"]}, "kick-search-categories": {"bodyParam": null, "bodyRequired": false, "id": "kick-search-categories", "method": "GET", "params": [{"description": "Category name to search for, up to 100 characters", "in": "query", "name": "query", "required": true, "type": "string", "x-example": "chat"}, {"description": "Maximum results, 1 to 100; defaults to 10", "in": "query", "name": "limit", "type": "integer", "x-example": 10}], "path": "/kick/search-categories", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "query", "required": true, "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "kick-search-channels": {"bodyParam": null, "bodyRequired": false, "id": "kick-search-channels", "method": "GET", "params": [{"description": "Channel name to search for, up to 100 characters", "in": "query", "name": "query", "required": true, "type": "string", "x-example": "xqc"}, {"description": "Only channels live now", "in": "query", "name": "live", "type": "boolean", "x-example": true}, {"description": "Maximum results, 1 to 100; defaults to 10", "in": "query", "name": "limit", "type": "integer", "x-example": 10}], "path": "/kick/search-channels", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "query", "required": true, "type": "string"}, {"in": "query", "name": "live", "type": "boolean"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "kick-subcategories": {"bodyParam": null, "bodyRequired": false, "id": "kick-subcategories", "method": "GET", "params": [{"description": "Top-level category slug from kick-categories; a parent Kick adds later is also accepted once it appears there", "enum": ["games", "irl", "music", "gambling", "creative", "alternative", "chat-roulette"], "in": "query", "name": "category", "type": "string", "x-example": "irl"}, {"description": "Page number, 1 to 20; defaults to 1", "in": "query", "name": "page", "type": "integer", "x-example": 1}, {"description": "Page size, 1 to 32; defaults to 24", "in": "query", "name": "limit", "type": "integer", "x-example": 10}], "path": "/kick/subcategories", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["games", "irl", "music", "gambling", "creative", "alternative", "chat-roulette"], "in": "query", "name": "category", "type": "string"}, {"in": "query", "name": "page", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "kick-subcategory": {"bodyParam": null, "bodyRequired": false, "id": "kick-subcategory", "method": "GET", "params": [{"description": "Category slug from kick-subcategories' or kick-search-categories' own slug field", "in": "query", "name": "slug", "required": true, "type": "string", "x-example": "just-chatting"}], "path": "/kick/subcategory", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "slug", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "kick-top-channels": {"bodyParam": null, "bodyRequired": false, "id": "kick-top-channels", "method": "GET", "params": [], "path": "/kick/top-channels", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "kick-video": {"bodyParam": null, "bodyRequired": false, "id": "kick-video", "method": "GET", "params": [{"description": "Video uuid (36 characters) from kick-channel-videos or kick-channel-streams, or a kick.com video URL", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "eb707c31-208b-4737-8bcf-a5c9fd187e82"}], "path": "/kick/video", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}}
JSON, true, 512, JSON_THROW_ON_ERROR);
    }

    public function request(string $operationId, array $params = [], string $responseType = 'auto'): mixed
    {
        if ($this->closed) {
            throw new ClientException('Client is closed', null, $operationId);
        }
        $operation = self::$operations[$operationId] ?? null;
        if ($operation === null) {
            throw new ClientException('Unknown operation: ' . $operationId, null, $operationId);
        }
        if ($this->apiKey === '') {
            throw new ClientException('Crawlora API key is required', null, $operationId);
        }
        $payload = $this->requestBody($operation, $params);
        $url = $this->buildUrl($operation, $params);
        $headers = [
            'x-api-key: ' . $this->apiKey,
            'User-Agent: crawlora-kick-php/0.1.0',
            'Accept: ' . (in_array('text/plain', $operation['produces'], true) ? 'application/json, text/plain' : 'application/json'),
        ];
        if ($payload !== null) {
            $headers[] = 'Content-Type: application/json';
        }
        try {
            [$status, $contentType, $body] = $this->send($url, $headers, $operationId, $operation['method'], $payload);
        } catch (CrawloraException $exception) {
            throw $exception;
        } catch (\Throwable $exception) {
            throw new NetworkException('Crawlora request failed: ' . $exception->getMessage(), null, $operationId, null, $exception);
        }
        if ($status < 200 || $status >= 300) {
            $class = $status >= 500 ? ServerException::class : ClientException::class;
            throw new $class('Crawlora returned HTTP ' . $status, $status, $operationId, $body);
        }
        return $this->parseResponse($body, $contentType, $operation, $params, $responseType);
    }

    public function close(): void
    {
        $this->closed = true;
    }

    public function isClosed(): bool
    {
        return $this->closed;
    }

    public function operationCount(): int
    {
        return self::OPERATION_COUNT;
    }

    public function operationIds(): array
    {
        return self::OPERATION_IDS;
    }

    public function operations(): array
    {
        return self::$operations;
    }

    public function categories(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("kick-categories", $params, $responseType);
    }
    public function category_clips(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("kick-category-clips", $params, $responseType);
    }
    public function channel(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("kick-channel", $params, $responseType);
    }
    public function channel_chatroom(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("kick-channel-chatroom", $params, $responseType);
    }
    public function channel_clips(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("kick-channel-clips", $params, $responseType);
    }
    public function channel_emotes(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("kick-channel-emotes", $params, $responseType);
    }
    public function channel_links(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("kick-channel-links", $params, $responseType);
    }
    public function channel_streams(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("kick-channel-streams", $params, $responseType);
    }
    public function channel_videos(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("kick-channel-videos", $params, $responseType);
    }
    public function clip(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("kick-clip", $params, $responseType);
    }
    public function clips(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("kick-clips", $params, $responseType);
    }
    public function drops(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("kick-drops", $params, $responseType);
    }
    public function gifts(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("kick-gifts", $params, $responseType);
    }
    public function languages(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("kick-languages", $params, $responseType);
    }
    public function livestreams(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("kick-livestreams", $params, $responseType);
    }
    public function search_categories(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("kick-search-categories", $params, $responseType);
    }
    public function search_channels(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("kick-search-channels", $params, $responseType);
    }
    public function subcategories(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("kick-subcategories", $params, $responseType);
    }
    public function subcategory(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("kick-subcategory", $params, $responseType);
    }
    public function top_channels(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("kick-top-channels", $params, $responseType);
    }
    public function video(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("kick-video", $params, $responseType);
    }

    /** POST operations take their JSON body under the body parameter name or "body". */
    private function requestBody(array $operation, array $params): ?string
    {
        $name = $operation['bodyParam'] ?? null;
        if ($name === null) {
            return null;
        }
        $value = $params[$name] ?? ($params['body'] ?? null);
        if ($value === null) {
            if ($operation['bodyRequired'] ?? false) {
                throw new ClientException('Missing request body: ' . $name, null, $operation['id']);
            }
            return null;
        }
        return is_string($value) ? $value : json_encode($value, JSON_THROW_ON_ERROR);
    }

    private function buildUrl(array $operation, array $params): string
    {
        $known = array_column($operation['params'], 'name');
        if (($operation['bodyParam'] ?? null) !== null) {
            $known[] = 'body';
        }
        $unknown = array_diff(array_keys($params), $known, ['response_type', '_response_type']);
        if ($unknown !== []) {
            throw new ClientException('Unknown parameters: ' . implode(', ', $unknown), null, $operation['id']);
        }
        $path = $operation['path'];
        foreach ($operation['params'] as $param) {
            if ($param['in'] !== 'path') {
                continue;
            }
            $name = $param['name'];
            if (!array_key_exists($name, $params) || $params[$name] === null) {
                throw new ClientException('Missing path parameter: ' . $name, null, $operation['id']);
            }
            $path = str_replace('{' . $name . '}', rawurlencode((string) $params[$name]), $path);
        }
        $pairs = [];
        foreach ($operation['queryParams'] as $param) {
            $name = $param['name'];
            $value = $params[$name] ?? ($param['default'] ?? null);
            if ($value === null) {
                if ($param['required'] ?? false) {
                    throw new ClientException('Missing query parameter: ' . $name, null, $operation['id']);
                }
                continue;
            }
            $enumValues = $param['enum'] ?? ($param['items']['enum'] ?? null);
            $values = is_array($value) ? $value : [$value];
            $invalidEnum = false;
            foreach ($values as $item) {
                if ($enumValues !== null && !in_array((string) $item, array_map('strval', $enumValues), true)) {
                    $invalidEnum = true;
                    break;
                }
            }
            if ($invalidEnum) {
                throw new ClientException('Invalid value for ' . $name, null, $operation['id']);
            }
            if (is_array($value)) {
                $format = $param['collectionFormat'] ?? 'csv';
                if ($format === 'multi') {
                    foreach ($value as $item) {
                        $pairs[] = [rawurlencode($name), rawurlencode($this->stringify($item))];
                    }
                } else {
                    $separator = ['csv' => ',', 'ssv' => ' ', 'tsv' => "\t", 'pipes' => '|'][$format] ?? ',';
                    $pairs[] = [rawurlencode($name), rawurlencode(implode($separator, array_map([$this, 'stringify'], $value)))];
                }
            } else {
                $pairs[] = [rawurlencode($name), rawurlencode($this->stringify($value))];
            }
        }
        $query = implode('&', array_map(static fn(array $pair): string => $pair[0] . '=' . $pair[1], $pairs));
        return $this->baseUrl . $path . ($query === '' ? '' : '?' . $query);
    }

    private function stringify(mixed $value): string
    {
        if (is_bool($value)) {
            return $value ? 'true' : 'false';
        }
        if (is_array($value)) {
            return json_encode($value, JSON_THROW_ON_ERROR);
        }
        return (string) $value;
    }

    private function send(string $url, array $headers, string $operationId, string $method = 'GET', ?string $payload = null): array
    {
        if ($this->transport !== null) {
            $result = $method === 'POST'
                ? ($this->transport)($url, $headers, $this->timeout, $method, $payload)
                : ($this->transport)($url, $headers, $this->timeout);
            return [(int) $result['status'], (string) ($result['content_type'] ?? ''), (string) ($result['body'] ?? '')];
        }
        $handle = curl_init($url);
        if ($handle === false) {
            throw new NetworkException('Could not initialize cURL', null, $operationId);
        }
        curl_setopt_array($handle, $method === 'POST' ? [
            CURLOPT_POST => true,
            CURLOPT_POSTFIELDS => $payload ?? '',
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_TIMEOUT_MS => (int) ($this->timeout * 1000),
            CURLOPT_CONNECTTIMEOUT_MS => (int) ($this->timeout * 1000),
        ] : [
            CURLOPT_HTTPGET => true,
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_TIMEOUT_MS => (int) ($this->timeout * 1000),
            CURLOPT_CONNECTTIMEOUT_MS => (int) ($this->timeout * 1000),
        ]);
        $body = curl_exec($handle);
        if ($body === false) {
            $message = curl_error($handle);
            curl_close($handle);
            throw new NetworkException('Crawlora request failed: ' . $message, null, $operationId);
        }
        $status = (int) curl_getinfo($handle, CURLINFO_RESPONSE_CODE);
        $contentType = (string) curl_getinfo($handle, CURLINFO_CONTENT_TYPE);
        curl_close($handle);
        return [$status, $contentType, (string) $body];
    }

    private function parseResponse(string $body, string $contentType, array $operation, array $params, string $responseType): mixed
    {
        if (!in_array($responseType, ['auto', 'json', 'text'], true)) {
            throw new ClientException('responseType must be auto, json, or text', null, $operation['id']);
        }
        $format = null;
        foreach ($operation['params'] as $param) {
            if ($param['name'] === 'format') {
                $format = $param;
                break;
            }
        }
        $textFormats = array_values(array_filter($format['enum'] ?? [], static fn($value): bool => !in_array(strtolower((string) $value), ['json', 'application/json'], true)));
        $rawFormat = isset($params['format']) && in_array((string) $params['format'], array_map('strval', $textFormats), true);
        $jsonFormat = isset($params['format']) && in_array(strtolower((string) $params['format']), ['json', 'application/json'], true);
        $isJson = $jsonFormat || stripos($contentType, 'json') !== false || $operation['produces'] === ['application/json'];
        if ($responseType === 'text' || $rawFormat || ($responseType === 'auto' && !$isJson)) {
            return $body;
        }
        try {
            return json_decode($body, true, 512, JSON_THROW_ON_ERROR);
        } catch (\JsonException $exception) {
            throw new CrawloraException('Invalid JSON response from Crawlora: ' . $exception->getMessage(), null, $operation['id'], $body, $exception);
        }
    }
}
