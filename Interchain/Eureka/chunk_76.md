## Chunk 76

**Original Text:**

Refunds: Once the timeout period is reached without fulfillment, the solver calls a function on the contract to trigger a refund process. This is handled on-chain, and includes any fees initially allocated from the user for solver compensation. Failures might occur for each transaction in a multi-tx sequence

In the event of a multi-tx route, each transaction may suffer from the kinds of failures noted above. This means it’s technically inaccurate to say that tokens will always end up on the initial chain or the chain where the swap takes place. More accurately, tokens may end up on each chain where a transaction is initiated or the chain where the swap takes place.

---

**LLM Contextual Output:**

You're discussing the implementation and limitations of refunds in Ethereum-based contracts, specifically when using multi-tx (multi-token) sequences.

To summarize:

1. When the timeout period is reached without fulfillment, the solver calls a function to trigger a refund process on-chain, which includes any fees initially allocated from the user for solver compensation.
2. This process is handled on-chain, meaning it doesn't involve any external or decentralized services.
3. Failures can occur for each transaction in a multi-tx sequence, potentially affecting multiple chains.

Your point about token distribution across different chains is well-taken. It's not accurate to assume that tokens will always end up on the same chain as the timeout event or the swap itself. Instead, they might be distributed across multiple chains where transactions are initiated or swaps take place.

This highlights the complexity and nuance of implementing refunds in multi-tx sequences, which requires careful consideration of token distribution and processing.
