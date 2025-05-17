## Chunk 72

**Original Text:**

The number of block confirmations required is specified by Circle in their documentation here. If Circle’s attestation service experiences an outage, malfunction, or otherwise becomes unresponsive, CCTP transfers will continue to burn assets on the source chain, but will not be able to mint assets on the destination chain. In this case, funds that have been burned to initiate a CCTP transfer will be inaccessible until the Circle attestation service recovers. ​
Hyperlane Failures
Each Hyperlane token transfer route is secured by an Interchain Security Module (ISM) designated by the deployer of the Hyperlane Warp Route Contracts (the interface to send tokens across chains using Hyperlane). The ISM defines the requirements for a message to be successfully processed on the destination chain.

---

**LLM Contextual Output:**

It appears that when Circle's attestation service becomes unavailable, block confirmations required for CCTP transfers will continue to burn assets on the source chain, but not mint new assets on the destination chain. This means that any funds burned during an unsuccessful attempt at initiating a transfer would be inaccessible until the attestation service is restored.
