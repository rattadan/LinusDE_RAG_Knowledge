## Chunk 42

**Original Text:**

At a high-level, basically any multi-chain action—in which the token is on the chain where it was issued for one stage of the action—requires multiple transactions. In particular, this means you cannot perform the following actions in 1 transaction:

IBC transfer after purchasing a cw20 asset
Chain 1 is the origin chain where the cw20 token can be swapped freely, but it cannot be transferred to another chain in the same transaction. Chain 1 is the origin chain where the cw20 token can be swapped freely, but it cannot be transferred to another chain in the same transaction. Call a contract on a remote chain after purchasing a cw20 asset (e.g. since this requires an IBC transfer under the hood)
Chain 1 is the origin chain, where the token can be used freely for post-route actions, but it cannot be used in post-route actions on other chains.

---

**LLM Contextual Output:**

You're highlighting a common limitation in multi-chain interactions involving tokens that are not native to those chains.

This issue arises because most blockchain protocols require a separate transaction for each chain interaction, such as IBC (Inter-Chain Bonding) transfers or contract calls. This is especially true when dealing with assets that can be swapped between chains, like CW20 tokens.

In your example:

1. Purchasing a CW20 asset on Chain 1
2. Performing an action call on the contract instance on another chain

These two steps require separate transactions, which can lead to inefficient use of resources and increased gas costs. This is because each transaction involves multiple interactions between different chains, including IBC transfers or similar.

To mitigate this issue, there are a few potential solutions being explored:

1. **Token bridges**: Some protocols, like Cosmos's Anchor or Polkadot's Nomic, offer token bridge services that allow for more efficient asset swaps between chains by using a single transaction.
2. **Interoperability standards**: Organizations like the Interoperability Working Group (IWG) are working on developing standards for interoperable blockchain interactions to enable seamless transactions across different chains.
3. **Chain-centric solutions**: Some projects, such as the CW20 bridge or Chainbridge, aim to provide a more streamlined experience by allowing users to perform asset swaps between chains using a single transaction.

It's essential to keep in mind that these solutions might not eliminate the need for multiple transactions entirely but can help reduce the complexity and costs associated with multi-chain interactions involving non-native tokens.
