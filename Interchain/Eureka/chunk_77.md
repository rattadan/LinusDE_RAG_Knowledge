## Chunk 77

**Original Text:**

This means it’s technically inaccurate to say that tokens will always end up on the initial chain or the chain where the swap takes place. More accurately, tokens may end up on each chain where a transaction is initiated or the chain where the swap takes place. For instance, if a pre-swap failure takes place on the second transaction in a sequence, the tokens will end up on the chain that transaction targeted. In our example above, if the transfer from Cosmos Hub to Osmosis required a separate user transaction and the Neutron to Hub leg of the route succeeded in the first transaction, the ATOM tokens would end up in the user’s account on the Hub if the swap exceeds maximum slippage. We’re working to make these failures even less common

In the short term, we’re working to add packet tracking + live relayer + client status to the API to help identify when packets get stuck and prevent folks from using channels where they’re likely to get stuck in the first place
In the medium term, we are working to add priority multi-hop relaying into the API.

---

**LLM Contextual Output:**

It seems you're discussing a decentralized exchange (DEX) like Osmosis and Cosmos Hub, specifically how token transfers work and potential issues that can arise during the process.

To summarize, your main points are:

1. Tokens might end up on multiple chains depending on where transactions are initiated or swapped.
2. Pre-swap failures can result in tokens being stuck on the chain involved in the failure.
3. To mitigate this, you're working to improve packet tracking, live relayer, and client status in the API.

You also mention potential medium-term enhancements, such as:

1. Priority multi-hop relaying into the API, which would help prevent packets from getting stuck.

It's clear that your team is focused on improving the functionality and reliability of DEXs like Osmosis and Cosmos Hub to reduce the likelihood of token misplacement or failure.
