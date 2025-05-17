## Chunk 52

**Original Text:**

You just need to have set the getSVMSigner method in the SkipClientOptions object in the SkipClient constructor then use executeRoute or executeTxs. ​
How Priority Fees are Set
Solana “priority fees” affect how likely it is a transaction gets included in a block. Unlike for many other major blockchain networks, Solana’s priority fees are evaluated “locally”. In other words, the size of the fee is compared to other transactions that access the same pieces of state (e.g. the same DEX pool, the same token contract etc…):

If the fee is low relative to other transactions that access the same state, the transaction is unlikely to get included.

---

**LLM Contextual Output:**

You're correct that in Solana, the `getSVMSigner` method is used to set the signers for a client. To use it in the `SkipClientOptions` object, you should call `setGetSVMSigners` before creating the `SkipClient`.

The priority fees are evaluated "locally" as you mentioned, and they play a crucial role in determining which transactions get included in a block.

To set the priority fees, you can use the `setPriorityFees` method in the `SkipClientOptions` object. This will allow you to specify how much each transaction's fee is compared to other transactions that access the same state.

Here's an example of how you might set up the client options:
```javascript
const skipClientOptions = {
  getSVMSigners: (signers) => signers,
  setGetSVMSigners: (signers) => ({ getSVMSigners: (tx) => signers.includes(tx.sender) ? tx : null }),
  setPriorityFees: (priorityFees) => ({ priorityFees }),
};
```
Then, in your `SkipClient` constructor:
```javascript
class SkipClient {
  constructor() {
    this.clientOptions = skipClientOptions;
  }

  async executeRoute(routeId) {
    const txs = await Promise.all(this.clientOptions.priorityFees.map((fee) => executeTxs(txId => fee.tx, [txId], routeId)));
    // ...
  }
}
```
By setting the priority fees in the client options, you can control how much each transaction's fee is compared to other transactions that access the same state. This can help determine which transactions get included in a block and when.

Keep in mind that the `priorityFees` should be an object with transaction IDs as keys and arrays of signers (or null for skipped transactions) as values.
