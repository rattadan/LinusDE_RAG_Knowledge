## Eureka - Chunk 31

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

Issuing a CW20 on the other hand, only requires deploying a new contract (just a transaction). ​
How do CW20 tokens compare to “tokenfactory” tokens? Tokenfactory tokens are created with the tokenfactory module. They’re designed to have the best of both worlds of CW20 and native tokens:

Like CW20s, they’re permissionless and users can create new ones just by submitting transactions — no need to modify the chain’s state machine
Like native tokens, they’re directly compatible with IBC out-of-the-box, and the bank module manages their balances + transferring functionality. This combination of traits leads many to see tokenfactory as a strict improvement on CW20 that devs should prefer in the vast majority of cases. We strongly agree with this conclusion. Unlike CW20s , tokenfactory tokens have no limitations in the cross-chain functionality Skip Go API can offer for them. ​
What limitations do CW20 tokens have within the Skip Go API?

---

**LLM Contextual Output:**

This text chunk appears to be discussing the technical details and parameters of various cross-chain asset transfer protocols, specifically focusing on the Inter-Blockchain Communication Protocol (IBC), Axelar GMP (Generalized Messaging Protocol), Circle Connect Transfer Protocol (CCTP), Hyperlane, and CW20 tokens.

**Technical Details:**

1. **IBC:** The protocol's potential for timeouts or slippage due to slow relaying from Axelar, as well as similar rules applicable after the swap.
2. **Axelar GMP:** Potential issues with slow relaying, similar to IBC, and post-swap failures.
3. **Circle Connect Transfer Protocol (CCTP):** Risks of funds becoming inaccessible due to Circle's service outage and user waiting for attestation service recovery.
4. **Hyperlane:** Secured by Interchain Security Modules (ISMs) with a multisig ISM that requires a specific number of validators to sign attestations, leading to potential fund inaccessibility if the threshold is not met.

**Context:**

The text chunk builds upon the surrounding context by connecting these technical details to the broader topic of cross-chain asset transfer protocols. The discussion highlights potential failure points and limitations of each protocol, as well as recommendations for developers and users to mitigate risks and improve cross-chain functionality.

**Requirements and Conditions:**

1. **User Education:** Informing users about potential failure points and what to expect if something goes wrong.
2. **Risk Management:** Encouraging users to monitor transactions and be prepared for potential delays or failures.
3. **Developer Best Practices:** Implementing robust error handling and fallback mechanisms in cross-chain applications.

**Additional Insights:**

1. Short-term solutions include adding packet tracking and live relayer/client status to the API, implementing priority multi-hop relaying in the API, and building better incentives for relayers to operate profitably.
2. Medium-term solutions could involve developing new protocols with improved functionality or features.
3. Long-term solutions might focus on integrating additional modules or improving existing ones to enhance overall cross-chain functionality.
