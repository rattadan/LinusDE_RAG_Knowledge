## Chunk 18

**Original Text:**

Metadata should include at least:
Denom (programmatic string identifier)
Symbol (aka “ticker”)
Asset name (human readable denom)
Display name (aka pretty name)
Decimals / exponent
Images
coingecko_id (if applicable)
Description
Ensure IBC relayers are actively monitoring and relaying packets on all channels over which you want users to transfer your token (See Chain Support Requirements for more info on relayers.)
​
2. “Warm Start” your Asset Routes
For each destination chain:

Pick a channel that you would like to be the canonical channel for transferring the asset to this destination chain
Transfer a non-zero amount of the token over the channel
Confirm that the token successfully gets transferred to the destination chain
Leave the transferred tokens on the destination chain
How do I pick a channel for a destination chain? If you’re launching a new chain, you should just pick whatever channel your team has set up. Usually, there’s just one highly-trafficked and well-relayed channel between two chains over which all assets are transferred. (In theory, there can be many because IBC is permissionless, but usually relayers are only monitoring 1 and creating more adds confusion for all parties)

If you’re launching a new token on a chain that already has a vibrant IBC ecosystem and has already issued tokens that are widely used throughout the interchain (e.g.

---

**LLM Contextual Output:**

Here's an expanded version of your request with additional details:

Metadata should include at least the following information:

1. Denom (programmatic string identifier): A unique string that identifies the asset or token.
2. Symbol (aka "ticker"): The symbol or ticker name for the token, which is often used to identify it in various contexts.
3. Asset name (human readable denom): A descriptive name for the asset, such as a brand or product name.
4. Display name (aka pretty name): A friendly and human-readable name for the asset, which can be useful for marketing and user interactions.
5. Decimals / exponent: Information about the token's decimal value or exponentiation factor.
6. Images: Additional image data that may be associated with the asset or token.

In addition to these technical details:

1. Coingecko_id (if applicable): If the token is listed on Coingecko, a popular cryptocurrency exchange and data source, include its ID as an additional metadata field.

2. Description: Provide a brief description of the token or asset, which can be useful for users and other stakeholders.

By including these additional details in your metadata, you'll make it easier to identify and understand your assets or tokens, both technically and non-technically.
