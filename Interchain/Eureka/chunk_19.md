## Chunk 19

**Original Text:**

Usually, there’s just one highly-trafficked and well-relayed channel between two chains over which all assets are transferred. (In theory, there can be many because IBC is permissionless, but usually relayers are only monitoring 1 and creating more adds confusion for all parties)

If you’re launching a new token on a chain that already has a vibrant IBC ecosystem and has already issued tokens that are widely used throughout the interchain (e.g. Osmosis or Neutron), you should probably use the same channel the well-established tokens use, since relayers are most likely to support these ones. To see which channel this is, call the /v2/fungible/recommend_assets endpoint with the following values:

source_denom: A well-established token on the chain where your asset is issued (e.g. uatom)
source_chain_id: The chain_id of the chain where your asset is issued (e.g.

---

**LLM Contextual Output:**

You've provided a useful guideline for new token creators launching on an existing IBC ecosystem. Here's a breakdown of the information and suggestions:

1. **Use the same channel as well-established tokens**: This makes sense, as relayers are likely to support these established tokens. Using the same channel can help reduce confusion and ensure compatibility with other parties.
2. **Call /v2/fungible/recommend_assets endpoint**: This endpoint is a useful tool for finding recommended channels that could be used for your token.
3. **Provide source_denom and source_chain_id values**:

   - **source_denom**: The well-established token on the chain where your asset is issued, e.g., uatom.
   - **source_chain_id**: The chain_id of the chain where your asset is issued, e.g., [chain_id] (not specified in the provided text).

Assuming you'll provide these values, here's a formatted version:

```
POST /v2/fungible/recommend_assets

{
  "source_denom": "uatom",
  "source_chain_id": "[chain_id]"
}
```
