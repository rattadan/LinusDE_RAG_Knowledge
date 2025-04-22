## Chunk 55

**Original Text:**

Ethereum mainnet, Arbitrum, Optimism, etc…), the Skip Go API will return an EvmTx type for the developer to pass to the user for signing
Unlike CosmosSDK transactions, EVM transactions do not have a notion of messages, so this object doesn’t correspond 1-to-1 to a “message”, which might be a more familiar notion to Cosmos developers
This doc is intended for CosmosSDK developers who aren’t already familiar with the concepts of transaction construction in the EVM and need to use EvmTx to help their users move from/to EVM chains. ​
EvmTx Data Structure
The EvmTx has 4 fields that the developer needs to understand:

to: The address of the smart contract or externally owned account (EOA) with which this transaction interacts, as a hex-string prefixed with 0x (e.g. 0xfc05aD74C6FE2e7046E091D6Ad4F660D2A159762)
value: The amount of wei this transaction sends to the contract its interacting with (1 ETH = 1^18 WEI)
data: The calldata this transaction uses to call the smart contract it interacts with, as a hex string. The data bytes will be interpreted according to the application-binary-interface (ABI) of the contract that’s being interacted with. If this field is empty, it means the transaction is sending funds to an address, rather than calling a contract.

---

**LLM Contextual Output:**

This documentation explains the structure and fields of the EVMTransaction object in Ethereum development, specifically for developers using the CosmosSDK. Here's a breakdown of the key points:

* The EvmTx object has four main fields:
 1. `to`: This is the address of the smart contract or externally owned account (EOA) with which this transaction interacts. It should be represented as a hexadecimal string prefixed with `0x`, e.g., `0xfc05aD74C6FE2e7046E091D6Ad4F660D2A159762`.
 2. `value`: This is the amount of wei sent to the contract in this transaction. One ETH (1^18 Wei) equals 1^18 WEI, so it's essential to understand the conversion factor.
 3. `data`: This is the calldata used to call the smart contract being interacted with. It should be represented as a hexadecimal string. The data bytes will be interpreted according to the application-binary-interface (ABI) of the contract being called.

If the `data` field is empty, it means the transaction is sending funds to an address rather than calling a contract.
