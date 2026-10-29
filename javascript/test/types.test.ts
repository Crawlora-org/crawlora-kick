import { KickClient } from "../src/index.js";

const client = new KickClient({ apiKey: "test-key" });
void client.categoryClips({"slug": "sample"});
void client.request("kick-category-clips", {"slug": "sample"});
const streamResponse: Promise<Response> = client.request("kick-category-clips", {"slug": "sample"}, { responseType: "stream" });
const operationStream: Promise<Response> = client.operation("kick-category-clips", {"slug": "sample"}, { responseType: "stream" });
const directStream: Promise<Response> = client.categoryClips({"slug": "sample"}, { responseType: "stream" });
void streamResponse; void operationStream; void directStream;
void client.request("kick-category-clips", {"slug": "sample", "cursor": "sample"}, { responseType: "text" });
const rawText: Promise<string> = client.request("kick-category-clips", {"slug": "sample"}, { responseType: "text" });
void rawText;


void client.categories();
void client.request("kick-categories");
// @ts-expect-error The selected operation requires its documented params.
void client.categoryClips();
