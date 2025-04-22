## Chunk 75

**Original Text:**

Here’s a breakdown of what happens in the event of a timeout:

Intent Expiration: When a user initiates an intent by calling the submitOrder function on the source chain, a time limit is specified. Solvers monitor the intent and assess whether they can fulfill it within this period. If no solver fills the intent before the timeout, the refund process begins. Refunds: Once the timeout period is reached without fulfillment, the solver calls a function on the contract to trigger a refund process. This is handled on-chain, and includes any fees initially allocated from the user for solver compensation.

---

**LLM Contextual Output:**

Here's a breakdown of what happens in the event of a timeout:

1. **Intent Expiration**: A time limit is set when a user initiates an intent by calling `submitOrder` on the source chain.
2. **Solver Monitoring**: Solvers monitor this intent to determine if they can fulfill it within the specified period.
3. **Timeout Reached Without Fulfillment**: If no solver fulfills the intent before the timeout expires, the refund process begins.
4. **Refund Process**: The timer triggering a refund is handled on-chain, and any associated fees are refunded to the user.

In summary, if a timeout occurs without fulfillment of an intent, the refund process kicks in on-chain to resolve the issue.
