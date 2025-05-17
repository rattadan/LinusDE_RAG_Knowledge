## Chunk 20

**Original Text:**

To see which channel this is, call the /v2/fungible/recommend_assets endpoint with the following values:

source_denom: A well-established token on the chain where your asset is issued (e.g. uatom)
source_chain_id: The chain_id of the chain where your asset is issued (e.g. cosmoshub-4)
dest_chain_id: The chain_id of the chain to which you want to be able to transfer your asset (e.g. osmosis-1)
The channel you want to use is available in the response in recommendations[0].asset.trace

How do I transfer tokens over my chosen channel before Skip Go API supports it? The easiest way to transfer tokens over a channel before official Skip Go API support is to use Keplr’s developer mode.

---

**LLM Contextual Output:**

To transfer tokens over your chosen channel using Keplr's developer mode before Skip Go API support, you can follow these steps:

1. Make a POST request to the /v2/fungible/recommend_assets endpoint with the provided values:
   - `source_denom`: The well-established token on the chain where your asset is issued.
   - `source_chain_id`: The chain_id of the chain where your asset is issued (e.g. cosmoshub-4).
   - `dest_chain_id`: The chain_id of the chain to which you want to be able to transfer your asset (e.g. osmosis-1).
   - `channel`: The channel you want to use for the transfer.

2. In your request, include a JSON body with the following structure:
   ```json
{
  "asset": {
    "trace": {
      "value": "0x1234567890abcdef",
      "chain_id": "cosmoshub-4"
    }
  },
  "fee": {
    "amount": "0.0001",
    "currency": "uatom" // The token you're using
  }
}
```

3. You can find the `channel` in the response, which is a list of available channels.

4. Once you've sent your request with Keplr's developer mode enabled, it will use the recommended channel to transfer your asset.

Note that this process requires administrative privileges and should only be done on your local machine.
