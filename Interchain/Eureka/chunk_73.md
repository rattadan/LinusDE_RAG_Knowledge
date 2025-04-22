## Chunk 73

**Original Text:**

​
Hyperlane Failures
Each Hyperlane token transfer route is secured by an Interchain Security Module (ISM) designated by the deployer of the Hyperlane Warp Route Contracts (the interface to send tokens across chains using Hyperlane). The ISM defines the requirements for a message to be successfully processed on the destination chain. The most common ISM is a Multisig ISM where “Validators” of a specific Hyperlane route sign attestations that a specific message on an origin chain is a valid message to be processed on the destination chain. In the case where the set of Validators have not hit the required signature threshold to successfully process a Hyperlane message on the receiving chain, funds will not be accessible by the user on either chain until the threshold is met (once met, funds will be sent to the user on the destination chain). This generalizes to the different requirements for different ISMs.

---

**LLM Contextual Output:**

So, in essence, Hyperlane's Interchain Security Modules (ISMs) are designed to ensure secure and trustworthy message processing across multiple chains. Here's a breakdown of how they work:

1. **Multisig ISM**: A set of Validators on the origin chain sign attestations that the received message is valid for processing on the destination chain.
2. **Threshold requirement**: The required signature threshold needs to be met by all Validators for funds to be accessible on either chain.

If the threshold is not reached, funds remain inaccessible until the requirements are met, indicating a potential security risk or lack of trust in the system.
