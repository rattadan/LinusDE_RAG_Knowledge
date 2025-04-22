## Chunk 29

**Original Text:**

As a result, being added to the Skip Go API instantly offers distribution across the interchain for your DEX
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
The module / contract must be able to be called by the Skip Go API’s CosmWasm contracts. For Cosmos SDK modules, this will require the module queries described below to be whitelisted and queryable by CosmWasm contracts (see Osmosis for an example). ​
Execution Messages
Supports a “Swap Exact In” method where a user specifies an input asset and path to swap, and the module / contract swaps the given user asset to the user’s desired output asset and sends it to the user (see Osmosis for a module example, or Astroport for a contract example). Inputs into the swap:
An asset (Native cosmos coin or CW20 token, incl.

---

**LLM Contextual Output:**

It appears that you're looking for information on how to integrate with the Skip Go API through CosmWasm contracts and specifically the swapping functionality for DEXs (Decentralized Exchanges).

To summarize, here are the key points:

1. **Chain Requirements**: The chain must be supported by the Skip Go API, and if not already supported, you'll need to follow specific instructions to request support.
2. **CosmWasm Support**: Your module or contract must be able to be called by CosmWasm contracts, including those for Cosmos SDK modules that can be queried and executed by the Skip Go API's CosmWasm contracts.
3. **Module/Contract Requirements**:
   - General: The module/contract must be able to handle input/output operations using the Swap Exact In method, which involves specifying an input asset and swapping it with the desired output asset.
   - Execution Messages: Your contract should have a function that swaps the specified assets according to the Swap Exact In method.

Some specific details you may want to consider:

- The Skip Go API's CosmWasm contracts can support various modules and chains, but IBC (Inter-Blockchain Communication) support is mentioned as required.
- For Cosmos SDK modules, whitelisting and queryability for these functions will require additional setup, which is outlined in the "Module / Contract Requirements" section.
- The Swap Exact In method allows for a user to specify an input asset and swap it with another asset. This can be done by sending execution messages through the Skip Go API's CosmWasm contracts.

To get started, I recommend checking out the official documentation on the Skip Go API and CosmWasm for more detailed information on implementing these features in your specific use case.
