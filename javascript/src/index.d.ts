import type {
  CrawloraGeneratedGroups,
  OperationId,
  OperationParamsMap,
  OperationRequestArgs,
  OperationResponseMap
} from "./types.js";

export type CrawloraParams = Record<string, unknown>;
export type CrawloraLogEvent = { event: string; [key: string]: unknown };
export interface CrawloraRequestContext { operationId: string; method: string; url: string; headers: Record<string, string> }
export type CrawloraBeforeRequest = (ctx: CrawloraRequestContext) => void | Promise<void>;
export type CrawloraAfterResponse = (operationId: string, status: number, headers: Record<string, string>, body: unknown) => unknown;

export interface CrawloraClientOptions {
  apiKey?: string;
  jwtToken?: string;
  baseUrl?: string;
  timeout?: number;
  retries?: number;
  retryDelay?: number;
  maxRetryDelay?: number;
  retryStatuses?: Iterable<number>;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
  onRetry?: (attempt: number, error: CrawloraError, delay: number) => void;
  requestId?: boolean;
  idempotencyKeys?: boolean;
  rateLimit?: number;
  maxConcurrency?: number;
  logger?: (event: CrawloraLogEvent) => void;
  beforeRequest?: CrawloraBeforeRequest | Iterable<CrawloraBeforeRequest>;
  afterResponse?: CrawloraAfterResponse | Iterable<CrawloraAfterResponse>;
  headers?: Record<string, string>;
  userAgent?: string | false;
  fetch?: typeof globalThis.fetch;
}

export interface CrawloraRequestOptions {
  headers?: Record<string, string>;
  responseType?: "auto" | "json" | "text" | "stream";
  timeout?: number;
  signal?: AbortSignal;
  retries?: number;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
}

export interface OperationDefinition {
  id: string; method: string; path: string; pathParams: string[];
  queryParams: Array<{ name: string; in?: "query"; collectionFormat?: string; type?: string; required?: boolean; enum?: string[] }>;
  formParams: Array<{ name: string; in?: "formData"; type?: string; required?: boolean; enum?: string[] }>;
  bodyParam?: string; bodyRequired?: boolean; consumes: string[]; produces: string[]; security: string[];
  paginatable?: boolean; cursorParams?: string[];
}

export class CrawloraError extends Error {
  status: number; code?: number; body: unknown; headers: Record<string, string>;
  response?: Response; cause?: unknown; retryable?: boolean; requestId?: string;
}
export class CrawloraClientError extends CrawloraError {}
export class CrawloraServerError extends CrawloraError {}
export class CrawloraNetworkError extends CrawloraError {}

export interface CrawloraPaginateOptions extends CrawloraRequestOptions {
  pageParam?: string; cursorParam?: string; nextCursor?: (page: unknown) => unknown;
  start?: unknown; step?: number; maxPages?: number;
}
export interface CrawloraPaginateItemsOptions extends CrawloraPaginateOptions {
  items?: (page: unknown) => Iterable<unknown>;
}

export class CrawloraClient {
  constructor(options?: CrawloraClientOptions);
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  paginate<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateOptions): AsyncGenerator<OperationResponseMap[I], void, unknown>;
  paginateItems<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateItemsOptions): AsyncGenerator<unknown, void, unknown>;
  [group: string]: unknown;
}
export interface CrawloraClient extends CrawloraGeneratedGroups {}

export class KickClient extends CrawloraClient {
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  categories(params?: OperationParamsMap["kick-categories"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  categoryClips(params: OperationParamsMap["kick-category-clips"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  channel(params: OperationParamsMap["kick-channel"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  channelChatroom(params: OperationParamsMap["kick-channel-chatroom"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  channelClips(params: OperationParamsMap["kick-channel-clips"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  channelEmotes(params: OperationParamsMap["kick-channel-emotes"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  channelLinks(params: OperationParamsMap["kick-channel-links"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  channelStreams(params: OperationParamsMap["kick-channel-streams"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  channelVideos(params: OperationParamsMap["kick-channel-videos"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  clip(params: OperationParamsMap["kick-clip"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  clips(params?: OperationParamsMap["kick-clips"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  drops(params?: OperationParamsMap["kick-drops"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  gifts(params?: OperationParamsMap["kick-gifts"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  languages(params?: OperationParamsMap["kick-languages"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  livestreams(params?: OperationParamsMap["kick-livestreams"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  searchCategories(params: OperationParamsMap["kick-search-categories"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  searchChannels(params: OperationParamsMap["kick-search-channels"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  subcategories(params?: OperationParamsMap["kick-subcategories"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  subcategory(params: OperationParamsMap["kick-subcategory"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  topChannels(params?: OperationParamsMap["kick-top-channels"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  video(params: OperationParamsMap["kick-video"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  categories(params?: OperationParamsMap["kick-categories"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  categoryClips(params: OperationParamsMap["kick-category-clips"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  channel(params: OperationParamsMap["kick-channel"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  channelChatroom(params: OperationParamsMap["kick-channel-chatroom"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  channelClips(params: OperationParamsMap["kick-channel-clips"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  channelEmotes(params: OperationParamsMap["kick-channel-emotes"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  channelLinks(params: OperationParamsMap["kick-channel-links"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  channelStreams(params: OperationParamsMap["kick-channel-streams"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  channelVideos(params: OperationParamsMap["kick-channel-videos"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  clip(params: OperationParamsMap["kick-clip"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  clips(params?: OperationParamsMap["kick-clips"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  drops(params?: OperationParamsMap["kick-drops"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  gifts(params?: OperationParamsMap["kick-gifts"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  languages(params?: OperationParamsMap["kick-languages"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  livestreams(params?: OperationParamsMap["kick-livestreams"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  searchCategories(params: OperationParamsMap["kick-search-categories"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  searchChannels(params: OperationParamsMap["kick-search-channels"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  subcategories(params?: OperationParamsMap["kick-subcategories"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  subcategory(params: OperationParamsMap["kick-subcategory"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  topChannels(params?: OperationParamsMap["kick-top-channels"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  video(params: OperationParamsMap["kick-video"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;

  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  categories(...args: OperationRequestArgs<"kick-categories">): Promise<OperationResponseMap["kick-categories"]>;
  categoryClips(...args: OperationRequestArgs<"kick-category-clips">): Promise<OperationResponseMap["kick-category-clips"]>;
  channel(...args: OperationRequestArgs<"kick-channel">): Promise<OperationResponseMap["kick-channel"]>;
  channelChatroom(...args: OperationRequestArgs<"kick-channel-chatroom">): Promise<OperationResponseMap["kick-channel-chatroom"]>;
  channelClips(...args: OperationRequestArgs<"kick-channel-clips">): Promise<OperationResponseMap["kick-channel-clips"]>;
  channelEmotes(...args: OperationRequestArgs<"kick-channel-emotes">): Promise<OperationResponseMap["kick-channel-emotes"]>;
  channelLinks(...args: OperationRequestArgs<"kick-channel-links">): Promise<OperationResponseMap["kick-channel-links"]>;
  channelStreams(...args: OperationRequestArgs<"kick-channel-streams">): Promise<OperationResponseMap["kick-channel-streams"]>;
  channelVideos(...args: OperationRequestArgs<"kick-channel-videos">): Promise<OperationResponseMap["kick-channel-videos"]>;
  clip(...args: OperationRequestArgs<"kick-clip">): Promise<OperationResponseMap["kick-clip"]>;
  clips(...args: OperationRequestArgs<"kick-clips">): Promise<OperationResponseMap["kick-clips"]>;
  drops(...args: OperationRequestArgs<"kick-drops">): Promise<OperationResponseMap["kick-drops"]>;
  gifts(...args: OperationRequestArgs<"kick-gifts">): Promise<OperationResponseMap["kick-gifts"]>;
  languages(...args: OperationRequestArgs<"kick-languages">): Promise<OperationResponseMap["kick-languages"]>;
  livestreams(...args: OperationRequestArgs<"kick-livestreams">): Promise<OperationResponseMap["kick-livestreams"]>;
  searchCategories(...args: OperationRequestArgs<"kick-search-categories">): Promise<OperationResponseMap["kick-search-categories"]>;
  searchChannels(...args: OperationRequestArgs<"kick-search-channels">): Promise<OperationResponseMap["kick-search-channels"]>;
  subcategories(...args: OperationRequestArgs<"kick-subcategories">): Promise<OperationResponseMap["kick-subcategories"]>;
  subcategory(...args: OperationRequestArgs<"kick-subcategory">): Promise<OperationResponseMap["kick-subcategory"]>;
  topChannels(...args: OperationRequestArgs<"kick-top-channels">): Promise<OperationResponseMap["kick-top-channels"]>;
  video(...args: OperationRequestArgs<"kick-video">): Promise<OperationResponseMap["kick-video"]>;
}
export { KickClient as Client };
export const operations: Record<string, OperationDefinition>;
export const groups: Record<string, Record<string, string>>;
export const operationCount: number;
export const OperationIds: Readonly<Record<string, OperationId>>;
export const VERSION: string;
export * from "./types.js";
export default KickClient;
