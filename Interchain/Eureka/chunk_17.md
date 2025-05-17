## Chunk 17

**Original Text:**

​
1. Satisfy the following basic requirements
The chain where the token is issued must already be supported by the Skip Go API
Use the /info/chains endpoint to query a list of actively supported chains: /v2/info/chains
If the chain is not already supported, follow the instructions in Chain Support Requirements to request support
This is a pre-requisite
The Skip Go API must also support the remote chains to which you wish users to be able to transfer the asset
Use the /info/chains endpoint to query a list of actively supported chains: /v2/info/chains
If the chain is not already supported, follow the instructions in Chain Support Requirements to request support
This is a pre-requisite
Token metadata is available in a commonly used chain registry (e.g. Cosmos Chain Registry) . Metadata should include at least:
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
How do I pick a channel for a destination chain?

---

**LLM Contextual Output:**

To help you with picking a channel for a destination chain, here are some general guidelines:

1. **Choose channels that offer sufficient liquidity**: Select channels with a good balance of buying and selling liquidity to minimize the risk of receiving tokens at unfavorable exchange rates.
2. **Consider the trade volume**: Opt for channels with high trade volumes, as this will increase the likelihood of successfully transferring tokens.
3. **Think about network congestion**: Avoid choosing channels that are heavily congested, especially if you're planning to transfer a large amount of tokens.
4. **Look for channels with reliable support**: Select channels that have a good reputation for receiving and relaying packets, as well as those that offer robust error handling and monitoring.
5. **Check the channel's technical specifications**: Make sure the chosen channel meets your requirements, including the minimum balance, transaction fees, and any specific regulatory or compliance needs.

When selecting a channel, you can use various tools to help with this process, such as:

1. **Chain ID**: Use the Chain ID of the destination chain to find suitable channels.
2. **Token pair charts**: Look at token pair charts (e.g., Chart.js) to identify channels with high liquidity and minimal price fluctuations.
3. **Exchange data**: Check exchange data (e.g., CoinGecko, Binance, or Kraken) for information on channel balances, trading volumes, and fees.

Some popular tools that can help you pick a channel include:

1. **Chain ID Explorer**: A free tool that allows you to explore token pairs and select suitable channels.
2. **Token pair charts by CryptoCompare**: A charting platform that provides detailed information on token pairs and channels.
3. **Exchange data APIs**: Utilize APIs like CoinGecko or Binance API to fetch exchange data, including channel balances, trading volumes, and fees.

By considering these factors and using available tools, you can make an informed decision when picking a channel for transferring your asset to the destination chain.
