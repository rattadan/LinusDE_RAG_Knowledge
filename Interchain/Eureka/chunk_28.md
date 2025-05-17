## Chunk 28

**Original Text:**

Support Requirements
Swap Venue Requirements
This document covers what Skip Go API requires of DEXes to support them as potential swapping venues within the API’s cross-chain DEX aggregation functionality. At the end, the document provides instructions for helping the Skip team add your DEX to the API as a swapping venue

​
Background
DEXes often want Skip Go API to add support for their DEX as a swapping venue because the API powers cross-chain swaps + transfers in all the major cosmos wallets (Leap, Keplr, IBC Wallet, Metamask Snap) and cross-chain DEX aggregation to many popular defi aggregator and dapp frontends (e.g. Stargaze). As a result, being added to the Skip Go API instantly offers distribution across the interchain for your DEX
The Skip Go API’s swapping system is currently built in CosmWasm and can support swapping assets on Cosmos SDK modules (ex: Osmosis Poolmanager) and other CosmWasm contracts (ex: Astroport DEX) that can be queried and executed by Skip Go API’s CosmWasm contracts. You can use this form to submit information about your swapping venue to Skip and track your progress through the required steps
​
Chain Requirements
The chain must already be supported by the Skip Go API
Use the /info/chains endpoint to query a list of actively supported chains: /v2/info/chains
If your chain is not already supported, follow the instructions in Chain Support Requirements to request support
This is a pre-requisite
CosmWasm Support
IBC support
ibc-hooks Support (Check out our blog post about ibc-hooks)
​
Module / Contract Requirements
​
General
The module / contract must be able to be called by the Skip Go API’s CosmWasm contracts.

---

**LLM Contextual Output:**

To ensure compliance with the requirements outlined in this document, here are some key points to consider:

**Swap Venue Requirements**

* The DEX should be able to swap assets on Cosmos SDK modules (e.g. Osmosis Poolmanager) and other CosmWasm contracts.
* This means that the DEX's code should be compatible with these platforms.

**Chain Requirements**

* The chain must already be supported by the Skip Go API.
* If the chain is not already supported, follow the instructions in Chain Support Requirements to request support.

**CosmWasm Support**

* IBC (Inter-Blockchain Communication) support: This means that the DEX's code should be able to interact with CosmWasm contracts that use IBC for inter-chain communication.
* Ibc-hooks support: This is a specific type of IBC support, but it's mentioned as part of the Chain Support Requirements. However, it's not clear what this entails.

**Module and Contract Requirements**

* The module or contract must be able to be called by CosmWasm contracts.
* This means that the DEX should have a well-defined interface for interacting with other platforms (e.g. Osmosis Poolmanager) using CosmWasm.

To add your DEX as a swapping venue to the Skip Go API, follow these steps:

1. Check if your chain is already supported by the Skip Go API.
2. If not, request support from the Skip Go API team.
3. Once supported, ensure that your module or contract can be called by CosmWasm contracts.
4. Verify that your DEX meets all other requirements outlined in this document.

Additionally, you may want to:

* Review the documentation provided by the Skip Go API and CosmWasm community to understand their expectations for integrating with these platforms.
* Test your DEX's functionality on a small scale before submitting it as a swapping venue to ensure that everything works as expected.
