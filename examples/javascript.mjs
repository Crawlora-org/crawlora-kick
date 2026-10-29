import { KickClient } from "../javascript/src/index.js";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new KickClient({ apiKey });

  const categories = await client.categories({  });
  console.log("categories", categories);
  const livestreams = await client.livestreams({  });
  console.log("livestreams", livestreams);
