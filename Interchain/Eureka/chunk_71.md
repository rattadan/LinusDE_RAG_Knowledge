## Chunk 71

**Original Text:**

their slippage exceeds their tolerance)
Post-swap failures
Once the swap is executed, Axelar is no longer involved, and the same rules that apply to IBC post-swap failures apply here, so the Post-swap failures section above applies. ​
CCTP Failures
Routes that use CCTP transfers rely on Circle to produce attestations. The Circle attestation service waits for a specified number of on-chain block confirmations before producing an attestation. The number of block confirmations required is specified by Circle in their documentation here. If Circle’s attestation service experiences an outage, malfunction, or otherwise becomes unresponsive, CCTP transfers will continue to burn assets on the source chain, but will not be able to mint assets on the destination chain.

---

**LLM Contextual Output:**

This text appears to be discussing the security and reliability of a specific cryptocurrency or blockchain project, likely Circle's attestations service for Cross-Chain Transactions (CCTPs). Here's a breakdown of what it says:

* The first sentence states that the slippage between the source and destination chains exceeds their tolerance, which is an important concept in trading and liquidity provision.
* The Post-swap failures section explains that once the swap is executed, Axelar is no longer involved, and the same rules apply to IBC (Inter-Blockchain Communication) post-swap failures. This suggests that the text is discussing a specific protocol or service for inter-chain communication.
 
The second paragraph talks about Circle's CCTP transfer mechanism. If the attestation service fails, it will continue to process transfers but won't be able to mint assets on the destination chain.
