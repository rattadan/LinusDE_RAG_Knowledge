## Eureka - Chunk 37

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

You just need to have set the getSVMSigner method in the SkipClientOptions object in the SkipClient constructor then use executeRoute or executeTxs. ​
How Priority Fees are Set
Solana “priority fees” affect how likely it is a transaction gets included in a block. Unlike for many other major blockchain networks, Solana’s priority fees are evaluated “locally”. In other words, the size of the fee is compared to other transactions that access the same pieces of state (e.g. the same DEX pool, the same token contract etc…):

If the fee is low relative to other transactions that access the same state, the transaction is unlikely to get included. If its high relative to these other transactions accessing similar state, its likely to be included
As a result, transactions that touch “congested” or “popular” state will be the most expensive. At this time, we are setting priority fees to match the 90% percentile of priority fees for the “wif” pool state on Jupiter, which we believe is highly congested state.

---

**LLM Contextual Output:**

This text chunk provides technical details and parameters related to cross-chain asset transfer protocols in the context of Solana.

**Exact Technical Details and Processes:**

1. **Priority Fees:** The importance of setting priority fees in Solana's local evaluation system, where the size of a fee is compared to other transactions accessing similar state.
2. **Priority Fee Percentiles:** Calculating the 90% percentile for priority fees in "wif" pool state on Jupiter, indicating how congested or popular this state is.

**Connection to Surrounding Context:**

This chunk builds upon previous information about potential failure points in cross-chain asset transfer protocols (IBC, Axelar GMP, Circle Connect Transfer Protocol, and Hyperlane) and provides additional insights into user education, risk management, and developer best practices for mitigating risks associated with these protocols.

**Requirements, Conditions, or Constraints:**

1. **Local Evaluation System:** The Solana network's local evaluation system for priority fees, which considers the size of a fee relative to other transactions accessing similar state.
2. **Congested State:** The "wif" pool state on Jupiter as an example of congested or popular state in Solana, indicating that priority fees will be evaluated differently.

By analyzing this text chunk, we can understand how priority fees are set locally in the Solana network and their implications for cross-chain asset transfer protocols.
