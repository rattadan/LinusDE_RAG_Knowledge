## Chunk 54

**Original Text:**

At this time, we are setting priority fees to match the 90% percentile of priority fees for the “wif” pool state on Jupiter, which we believe is highly congested state. This is a very conservative setting, but it even with these “high amounts”, fees are still fractions of a cent. EVM Transactions
This doc covers how to interact with the EvmTx type returned by the Skip Go API

​
Intro
When a user needs to transfer or swap from an EVM chain (e.g. Ethereum mainnet, Arbitrum, Optimism, etc…), the Skip Go API will return an EvmTx type for the developer to pass to the user for signing
Unlike CosmosSDK transactions, EVM transactions do not have a notion of messages, so this object doesn’t correspond 1-to-1 to a “message”, which might be a more familiar notion to Cosmos developers
This doc is intended for CosmosSDK developers who aren’t already familiar with the concepts of transaction construction in the EVM and need to use EvmTx to help their users move from/to EVM chains. ​
EvmTx Data Structure
The EvmTx has 4 fields that the developer needs to understand:

to: The address of the smart contract or externally owned account (EOA) with which this transaction interacts, as a hex-string prefixed with 0x (e.g.

---

**LLM Contextual Output:**

It looks like you're setting priority fees for a specific state on Jupiter, likely referring to the "wif" pool state. I'll do my best to summarize the information provided.

To recap, you're using the Skip Go API to interact with EVM transactions, and you want to know how to build an EVM transaction (EvmTx) in order to help users sign and send transactions on EVM chains like Ethereum mainnet, Arbitrum, Optimism, etc.

Here's a breakdown of the information provided:

1. **Intro**: The document introduces the Skip Go API and its return type for creating EVM transactions.
2. **EvmTx Data Structure**: The document explains the structure of an EvmTx, which consists of 4 fields:
	* `to`: The address of the smart contract or Externally Owned Account (EOA) that interacts with the transaction.
		+ Note: The format is a hex-string prefixed with "0x", e.g. `0x1234567890abcdef`.
3. **Purpose**: You mentioned that you're aiming for a conservative setting, but even with high amounts, fees are still only fractions of a cent.

It seems like the document is primarily aimed at providing guidance on how to build EvmTx data structures in order to work with users who need to transfer or swap assets on EVM chains. Is there anything specific you'd like me to help with?
