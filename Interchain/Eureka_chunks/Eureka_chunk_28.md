## Eureka - Chunk 28

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

The form will help us scope how much work is required on our side to add support, guide our implementation, and inform our decision for how quickly to prioritize it in our roadmap (e.g. based on swapping volume + liquidity, and clarity of the technical information)

CW20 Tokens & Their Limitations
Information about performing CW20 swaps

This page covers the basics of CW20s and the limitations around performing cross-chain actions with CW20 tokens — compared to tokenfactory and “native” Cosmos assets (aka Bank Module assets). ​
CW20 Token Denom Formatting In API Requests
To use CW20 tokens in the Skip Go API, specify the denom as “cw20:” + the token contract address. Example denom for Astro on Terra2: cw20:terra1nsuqsk6kh58ulczatwev87ttq2z6r3pusulg9r24mfj2fvtzd4uq3exn26

​
Background
​
What is a CW20 token? CW20 is the fungible token spec for the CosmWasm (i.e. CW) VM. CosmWasm is the most popular smart contract VM among CosmosSDK blockchains today.

---

**LLM Contextual Output:**

This text chunk provides detailed technical information and context about cross-chain asset transfer protocols, specifically focusing on:

1. Technical details:
   - Inter-Blockchain Communication Protocol (IBC) timeouts and slippage.
   - Axelar GMP swap failures, including slow relaying and timeout issues.
   - Circle Connect Transfer Protocol (CCTP) service outage and funds accessibility limitations.
   - Hyperlane security features, such as multisig ISMs and timeout mechanisms.
   - Go Fast's intent expiration and refund process for transaction timeouts.

2. Connection to the surrounding context:
   - The text is part of a comprehensive overview of potential failure points in cross-chain asset transfer protocols, discussing various technical aspects, including protocol specifications (IBC, Axelar GMP) and security features.
   - The page also references specific assets and their limitations, such as CW20 tokens and CosmWasm.

3. Specific requirements, conditions, or constraints mentioned:
   - Users need to specify the denom of a CW20 token in API requests when using the Skip Go API (e.g., "cw20:terra1nsuqsk6kh58ulczatwev87ttq2z6r3pusulg9r24mfj2fvtzd4uq3exn26").
   - The text also mentions specific requirements for services such as Circle Connect and Hyperlane, emphasizing the importance of their uptime and functionality.

The current text chunk is explaining how to implement support for cross-chain asset transfers using CW20 tokens and other CosmosSDK blockchains. It's providing technical details about potential failure points in various protocols, highlighting security features and user-specific requirements for a successful implementation.
