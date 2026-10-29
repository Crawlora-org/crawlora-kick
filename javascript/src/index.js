import { groups } from "./operations.js";
import {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
} from "./client.js";

export class KickClient extends CrawloraClient {
  constructor(options = {}) {
    super({ ...options, userAgent: options.userAgent ?? "crawlora-kick-js/0.1.0" });
    this["categories"] = (...args) => this.request("kick-categories", ...args);
    this["categoryClips"] = (...args) => this.request("kick-category-clips", ...args);
    this["channel"] = (...args) => this.request("kick-channel", ...args);
    this["channelChatroom"] = (...args) => this.request("kick-channel-chatroom", ...args);
    this["channelClips"] = (...args) => this.request("kick-channel-clips", ...args);
    this["channelEmotes"] = (...args) => this.request("kick-channel-emotes", ...args);
    this["channelLinks"] = (...args) => this.request("kick-channel-links", ...args);
    this["channelStreams"] = (...args) => this.request("kick-channel-streams", ...args);
    this["channelVideos"] = (...args) => this.request("kick-channel-videos", ...args);
    this["clip"] = (...args) => this.request("kick-clip", ...args);
    this["clips"] = (...args) => this.request("kick-clips", ...args);
    this["drops"] = (...args) => this.request("kick-drops", ...args);
    this["gifts"] = (...args) => this.request("kick-gifts", ...args);
    this["languages"] = (...args) => this.request("kick-languages", ...args);
    this["livestreams"] = (...args) => this.request("kick-livestreams", ...args);
    this["searchCategories"] = (...args) => this.request("kick-search-categories", ...args);
    this["searchChannels"] = (...args) => this.request("kick-search-channels", ...args);
    this["subcategories"] = (...args) => this.request("kick-subcategories", ...args);
    this["subcategory"] = (...args) => this.request("kick-subcategory", ...args);
    this["topChannels"] = (...args) => this.request("kick-top-channels", ...args);
    this["video"] = (...args) => this.request("kick-video", ...args);
  }
}

export { KickClient as Client };
export {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
};
export { groups, operations, operationCount, OperationIds } from "./operations.js";
export const VERSION = "0.1.0";
export default KickClient;
