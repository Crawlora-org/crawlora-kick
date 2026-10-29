import os

from crawlora_kick import KickClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with KickClient(api_key=api_key) as client:
    categories = client.categories()
    print('categories', categories)
    livestreams = client.livestreams()
    print('livestreams', livestreams)
