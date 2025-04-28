## Eureka - Chunk 25

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

You can use this form to submit information about your swapping venue to Skip and track your progress through the required steps
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
The module / contract must be able to be called by the Skip Go API’s CosmWasm contracts. For Cosmos SDK modules, this will require the module queries described below to be whitelisted and queryable by CosmWasm contracts (see Osmosis for an example).

---

**LLM Contextual Output:**

This specific text chunk is explaining the technical details of potential failure points in various cross-chain asset transfer protocols, specifically focusing on Inter-Blockchain Communication Protocol (IBC), Axelar GMP, Circle Connect Transfer Protocol (CCTP), Hyperlane, and Go Fast.

### Technical Details:

1. **Timeouts or Slippage**: IBC, Axelar can cause timeouts if tokens are sent back to the source chain due to slippage issues.
2. **Post-Swap Failures**: Similar rules apply as with IBC, but tokens may end up on the chain where the swap is supposed to take place.
3. **Slow Relaying from Axelar**: Slow relaying from Axelar can cause timeouts.
4. **Slippage Issues**: Slippage issues are also possible in slow relay scenarios.

### Connection to or Building upon Surrounding Context:

This chunk connects directly to the surrounding context by providing an overview of potential failure points in various cross-chain asset transfer protocols. It builds upon this context by detailing specific technical details and processes related to each protocol, allowing users to better understand the risks associated with these protocols.

### Requirements, Conditions, or Constraints:

1. **Chain Support**: The text mentions that not all chains are supported by the Skip Go API.
2. **CosmWasm Contracts**: It requires CosmWasm contracts to be able to call the module and contract functions described in the section.
3. **Whitelisted Modules**: For Cosmos SDK modules, this will require the module queries to be whitelisted and queryable by CosmWasm contracts.

In summary, this chunk provides detailed technical information about potential failure points in various cross-chain asset transfer protocols, which is crucial for understanding and mitigating risks associated with these protocols.
