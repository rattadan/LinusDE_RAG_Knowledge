## Chunk 53

**Original Text:**

In other words, the size of the fee is compared to other transactions that access the same pieces of state (e.g. the same DEX pool, the same token contract etc…):

If the fee is low relative to other transactions that access the same state, the transaction is unlikely to get included. If its high relative to these other transactions accessing similar state, its likely to be included
As a result, transactions that touch “congested” or “popular” state will be the most expensive. At this time, we are setting priority fees to match the 90% percentile of priority fees for the “wif” pool state on Jupiter, which we believe is highly congested state. This is a very conservative setting, but it even with these “high amounts”, fees are still fractions of a cent.

---

**LLM Contextual Output:**

You're explaining that in a state where multiple transactions compete to access the same resources or data, such as a decentralized exchange (DEX) pool or a token contract, the size of a transaction's fee relative to other transactions accessing the same state determines its likelihood of being included in the network. If fees are low compared to others in similar states, it may be difficult for a new transaction to get accepted. Conversely, if fees are high, it increases the chances of a new transaction being included.

In this context, setting priority fees to match 90% of the "WIF" (withheld from interest) pool state on Jupiter suggests that the team is prioritizing these congested or popular states and allocating more resources (in terms of fee) to ensure that only the most valuable transactions can access them. This approach aims to maintain a balance between incentivizing legitimate transactions while minimizing the cost of adding new activity to these high-value areas.
