## Eureka - Chunk 29

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

At a high-level, CW20 is very similar to ERC20 (the popular EVM fungible token standard). Contracts that comply with the standard implement the following functionalities:

Transferring tokens from one account to another
Sending tokens to a contract along with a message (similar to callContractWithToken)
Tracking balances
Delegating balance spending to other accounts and contracts
ASTRO (Astroport’s governance token) is one CW20 token issued on Terra2. ​
How do CW20 tokens interact with IBC? CW20-ICS20 converter contracts make a CW20 token compatible with the ICS20 token transfer standard, so they can be sent to other chains over normal ICS20 transfer channels. When they arrive on the destination chain, they’re indistinguishable from bank module and tokenfactory tokens. These converter contracts are the source of much difficulty when attempting to perform cross-chain actions with CW20s:

Different converter contracts implement different versions of the ICS20 standard (e.g.

---

**LLM Contextual Output:**

This text chunk is explaining specific technical details related to the functionality of CW20 tokens in a cross-chain asset transfer protocol, specifically their interaction with Inter-Blockchain Communication Protocol (IBC).

**Technical Details:**

1. **IBC Swap Failures:** The chunk discusses potential issues that can arise during an IBC swap, including timeouts and slippage.
2. **Post-Swap Failures:** It also mentions similar rules for what happens after a successful swap on another chain.
3. **Axelar GMP (Generalized Messaging Protocol) Post-Swap Failures:** The chunk talks about potential issues that can occur when relaying data from Axelar, including slow relaying and slippage.

**Connection to the Surrounding Context:**

The text builds upon the surrounding context of discussing potential failure points in various cross-chain asset transfer protocols. It provides specific technical details on how CW20 tokens interact with IBC and other protocols, such as Axelar GMP and Circle Connect Transfer Protocol (CCTP).

**Requirements, Conditions, or Constraints:**

The chunk does not mention any specific requirements, conditions, or constraints that are relevant to the context. However, it provides some general information about potential issues that can arise during cross-chain asset transfers.

In terms of technical specifications, the text mentions:

* The CW20-ICS20 converter contracts, which are used to make CW20 tokens compatible with the ICS20 token transfer standard.
* The different versions of the ICS20 standard implemented by various converter contracts.
* The Interchain Security Modules (ISMs) that secure the Hyperlane protocol.

Overall, this chunk provides technical details and explanations related to the functionality of CW20 tokens in a cross-chain asset transfer protocol.
