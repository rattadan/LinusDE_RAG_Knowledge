## Chunk 25

**Original Text:**

Wait up to 24 hours and verify
Skip’s intelligent route detection should automatically detect new routes for all assets and chains that meet the above requirements in 4-8 hours. This will not happen immediately. Please ensure you wait the necessary amount of time. After you’ve let enough time pass, you can verify that Skip Go API supports the new routes you’ve configured using the /v2/fungible/recommend_assets endpoint. For each destination chain you’ve configured, call this endpoint with the following data:

source_denom: Your token
source_chain_id: The chain on which your token is issued
dest_chain_id: The chain to which you’ve warm-started an IBC route in the previous step
​
Common questions
​
I want a CW20 token added to Skip Go, what do I need to do to add it?

---

**LLM Contextual Output:**

I can help you with that.
To add a CW20 token to Skip Go, you'll need to follow these steps:

1. Wait for the necessary time: As mentioned in the message, wait at least 4-8 hours after setting up new routes using Skip's intelligent route detection.

2. Verify Skip Go API supports new routes: After waiting enough time, call the /v2/fungible/recommend_assets endpoint with the required data (source_denom, source_chain_id, and dest_chain_id) for each destination chain you've configured. For example:

    ```bash
curl -X POST \
  https://skip-go.com/v2/fungible/recommend_assets \
  -H 'Content-Type: application/json' \
  -d '{"source_denom": "your_token", "source_chain_id": "chain_name", "dest_chain_id": "destination_chain_id"}'
```

3. Verify the CW20 token is added: After verifying that the new routes are being detected and recommended, you can check if the CW20 token is added to Skip Go by checking the /v2/fungible/asset endpoint with the required data (asset_id, chain_id) for each asset.

For example:

    ```bash
curl -X GET \
  https://skip-go.com/v2/fungible/asset \
  -H 'Content-Type: application/json' \
  -d '{"asset_id": "cw20_token", "chain_id": "destination_chain_id"}'
```
