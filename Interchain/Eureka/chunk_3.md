## Chunk 3

**Original Text:**

Permissioning will be removed in the near future. ​
Eureka
Integration Guide
A guide on how to integrate IBC Eureka for chain developers, asset issuers, and application developers

​
Types of Integrators
There are three types of integrators of Eureka:

Chain Developers - ensuring that your chain is compatible with Eureka and can facilitate the bridging of assets to and from other chains in the Eureka ecosystem. Asset Issuers - ensuring the assets you care about being bridged over Eureka are properly set up in the protocol and in the Skip Go API for application developers to support easily. Application Developers - ensuring your end users have access to Eureka assets and bridging capabilities via the Skip Go API. ​
Chain Developers
If you’re developing a Cosmos-based blockchain, the easiest way to unlock Eureka assets and bridging capabilities is by opening up an IBC connection to the Cosmos Hub:

Requires an IBC (classic) connection to the Cosmos Hub
No chain upgrade is needed if you’re already using IBC
Users benefit from reduced cost of asset transfers between Eureka-enabled domains through batching
Chains only need to maintain a single relayer to the Cosmos Hub to reach the entire Eureka and IBC network
If you are interested in a direct Eureka connection to Ethereum or L2s/Solana coming later this year, please reach out to Jeremy or Susannah directly as additional integration work is required.

---

**LLM Contextual Output:**

It appears that permissioning will be removed from the near future, which may impact your ability to use IBC (Inter-Blockchain Communication) with Cosmos-based blockchain networks like Eureka.

The guide provided outlines the types of integrators for Eureka and explains how Chain Developers can facilitate bridging between chains, Asset Issuers can set up assets on Eureka, and Application Developers need to provide access to Eureka assets via the Skip Go API. Additionally, there's information about integrating with Cosmos Hub for developing Cosmos-based blockchain applications.

Regarding permissioning, it seems that this process will be phased out in the near future. The guide does not provide further details on what exactly permissioning is or how it was implemented, but it implies that the removal of permissioning may require additional work from developers interested in using Eureka's IBC capabilities for Ethereum or L2s/Solana.

It's also worth noting that a direct Eureka connection to Ethereum or L2s/Solana is mentioned as something coming later this year, suggesting that this feature will be developed and implemented in the future.
