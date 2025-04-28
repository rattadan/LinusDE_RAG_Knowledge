## Eureka - Chunk 23

**Document Summary:**

This document provides a comprehensive overview of potential failure points in various cross-chain asset transfer protocols. Here's a summary of the key points and some additional insights:

### 1. **Inter-Blockchain Communication Protocol (IBC)**
   - **Swap Failures:**
     - Potential for timeouts or slippage.
     - Tokens are expected to be sent back to the source chain if these issues arise.
   - **Post-Swap Failures:**
     - Similar rules apply as with IBC, but tokens may end up on the chain where the swap is supposed to take place.

### 2. **Axelar GMP (Generalized Messaging Protocol)**
   - **Swap Failures:**
     - Slow relaying from Axelar can cause timeouts.
     - Slippage issues are also possible.
   - **Post-Swap Failures:**
     - Same as IBC post-swap failures.

### 3. **Circle Connect Transfer Protocol (CCTP)**
   - Relies on Circle's attestation service.
   - Circles' service outage can lead to funds being inaccessible.
   - Users will need to wait until the Circle attestation service recovers before their funds are available.

### 4. **Hyperlane**
   - Secured by Interchain Security Modules (ISMs).
     - **Multisig ISM:**
       - Requires a specific number of validators to sign attestations for successful processing.
       - Fails if the required signature threshold is not met, leading to funds being inaccessible on both chains until the threshold is achieved.

### 5. **Go Fast**
   - Timeout mechanisms ensure that users do not lose funds.
     - Intent expiration and refund process in case no solver fills the intent before a timeout.
     - Each transaction in a multi-tx sequence can fail independently, leading to tokens potentially ending up on different chains.

### Additional Insights:
- **Short-term Solutions:**
  - Adding packet tracking and live relayer/client status to the API to identify stuck packets early.
  
- **Medium-term Solutions:**
  - Implementing priority multi-hop relaying in the API to improve transaction success rates.

- **Long-term Solutions:**
  - Building better incentives for relayers, so they can operate profitably rather than as charities.

### Recommendations:
1. **User Education:** 
   - Inform users about potential failure points and what to expect if something goes wrong.
2. **Risk Management:**
   - Encourage users to monitor transactions and be prepared for potential delays or failures.
3. **Developer Best Practices:**
   - Implement robust error handling and fallback mechanisms in cross-chain applications.

By understanding these failure points, developers and users can better prepare for and mitigate the risks associated with cross-chain asset transfers.

**Original Text:**

For each destination chain you’ve configured, call this endpoint with the following data:

source_denom: Your token
source_chain_id: The chain on which your token is issued
dest_chain_id: The chain to which you’ve warm-started an IBC route in the previous step
​
Common questions
​
I want a CW20 token added to Skip Go, what do I need to do to add it? To add a CW20 token, you should first make sure its usable (either has ibc20-cw20 converter contracts deployed to IBC transfer the token or source-chain swappable on a swap venue used by Skip Go). Once confirmed usable, you must add the CW20 token’s metadata to a registry we support indexing from. The easiest one is likely the Cosmos Chain Registry, you can check out an example of a CW20 token entry here in Archway’s assetlist.json. Once the PR is merged into a registry, our indexing will add it to the API on our next indexing run (hourly).

---

**LLM Contextual Output:**

This text chunk provides detailed technical specifications and parameters for cross-chain asset transfer protocols, specifically focusing on the IBC protocol.

**Exact Technical Details:**

1. The endpoint used to configure destination chains is `warm-start` or `IBC route`.
2. The data required to call this endpoint includes:
   - `source_denom`: Token denomination
   - `source_chain_id`: Chain on which the token is issued
   - `dest_chain_id`: Destination chain ID (in IBC terminology, it's called "swappable chain")
3. The process involves adding a CW20 token to a registry that supports indexing from (likely the Cosmos Chain Registry).
4. Once added, the registry will index the token for API access.

**Context and Connection:**

1. This text chunk is part of a comprehensive document providing an overview of potential failure points in cross-chain asset transfer protocols.
2. The chunk builds upon the surrounding context by describing specific technical details and parameters for the IBC protocol, including endpoint calls and registry indexing requirements.
3. The text assumes a familiar background with blockchain development and cross-chain assets, as it references specific terms (e.g., "IBC route," "swappable chain").

**Requirements, Conditions, or Constraints:**

1. Users need to ensure their CW20 token is usable before configuring destination chains.
2. The CW20 token must be added to a supported registry (Cosmos Chain Registry) and indexed for API access.
3. There are no specific time constraints mentioned in the text chunk.

By analyzing this technical detail-rich section, we can understand the intricacies of cross-chain asset transfer protocols, including IBC protocol specifics and their requirements.
