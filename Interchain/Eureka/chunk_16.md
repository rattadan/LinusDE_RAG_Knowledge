## Chunk 16

**Original Text:**

and we will help guide you through it to the extent we can. These other interop protocols are less standardized and/or less permissionless than IBC, so the process of adding support for transferring new tokens over them is more bespoke and varies by protocol. We’re happy to help where we can, providing guidance, implementation, and introductions where necessary. ​
1. Satisfy the following basic requirements
The chain where the token is issued must already be supported by the Skip Go API
Use the /info/chains endpoint to query a list of actively supported chains: /v2/info/chains
If the chain is not already supported, follow the instructions in Chain Support Requirements to request support
This is a pre-requisite
The Skip Go API must also support the remote chains to which you wish users to be able to transfer the asset
Use the /info/chains endpoint to query a list of actively supported chains: /v2/info/chains
If the chain is not already supported, follow the instructions in Chain Support Requirements to request support
This is a pre-requisite
Token metadata is available in a commonly used chain registry (e.g.

---

**LLM Contextual Output:**

It seems like you're trying to understand the requirements for adding token support over other interop protocols, specifically Skip Go API and its supported chains, as well as the requirement for supporting remote chains.

To summarize, you need to:

1. Ensure that the chain where your token is issued already has Skip Go API support.
2. Use the `/v2/info/chains` endpoint to query a list of actively supported chains in the currently supported chain's registry.
3. If the chain isn't already supported, follow the instructions in Chain Support Requirements to request support from the Skip Go API.
4. Similarly, use the `/v2/info/chains` endpoint to query a list of actively supported chains for remote chains, and if necessary, follow the instructions in Chain Support Requirements to request support.

The key takeaways are:

* The chain's token support must already be established with Skip Go API.
* The Skip Go API must also support the requested remote chains.
* Token metadata is available in commonly used chain registries (e.g., Etherscan, etc.).

It seems like you're working towards adding support for transferring new tokens over other interop protocols. Am I correct?
