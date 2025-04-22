## Chunk 44

**Original Text:**

IBC transfer from a remote chain to the CW20’s origin chain then perform a swap or any other post-route action on that chain
Chain 2 is the origin chain. The token can be transferred back there, but it can't be used or swapped for anything in the same transaction. Chain 2 is the origin chain. The token can be transferred back there, but it can't be used or swapped for anything in the same transaction. In principle, you can use the Skip Go API to construct any of these action sequences across multiple transactions, but it will be more challenging for you and your end users.

---

**LLM Contextual Output:**

It seems like we're working with a transfer chain that involves two origin chains: Chain 2 (the origin chain) and Chain 20 (or CW20's origin chain). The goal is to perform an action sequence on the Chain 2 origin chain, which includes transferring IBC tokens between these two chains.

To clarify, you mentioned several actions:

1. Transfer from Chain 2 to Chain 20.
2. Perform a swap or any other post-route action on that chain.

Here's some guidance on how to approach this process using the Skip Go API:

**Note:** You'll need to handle token transfer and swap in separate transactions since they can't be part of the same transaction.

1. **Transfer from Chain 2 to Chain 20:**
   Use the `IBC` function with the desired `from`, `to`, and any relevant parameters (e.g., `transfer` flags, `tokenIds`) to transfer tokens between the two chains. The API call should look something like this:

   ```javascript
   const  ibc = require('ibc-sdk');
   const chain2Address = Chain2Address; // Replace with your Chain 2 address or token contract symbol
   const chain20Address = CW20Address; // Replace with your CW20 address or token contract symbol

   ics.chain2ToChain20({
     from: Chain2Address,
     to: chain20Address,
     tokens: [1, 2], // replace with actual token ids
     transferFlags: 'from',
     transferParams: { /* optional params */ },
   });
   ```

2. **Post-route action (swap):**
   To swap tokens between the two chains, you can use the `IBC` function again, but this time specify the `from`, `to`, and `tokens` parameters with a `swap` flag set to `'yes'`. The API call should look something like this:

   ```javascript
   const  ibc = require('ibc-sdk');
   const Chain2Address = Chain2Address; // Replace with your Chain 2 address or token contract symbol
   const chain20Address = CW20Address; // Replace with your CW20 address or token contract symbol

   ics.chain2ToChain20({
     from: Chain2Address,
     to: chain20Address,
     tokens: [1, 2], // replace with actual token ids
     transferFlags: 'from',
     transferParams: { /* optional params */ },
     swap: true,
   });
   ```

3. **Token Transfer back to Origin Chain (Chain 2):**

   To transfer tokens from the post-route chain back to Chain 2, you can use a similar API call but with the `to` parameter set to your original Chain 2 address:

   ```javascript
   const  ibc = require('ibc-sdk');
   const Chain2Address = Chain2Address; // Replace with your Chain 2 address or token contract symbol

   ics.chain20ToChain2({
     from: CW20Address,
     to: Chain2Address,
     tokens: [1, 2], // replace with actual token ids
     transferFlags: 'from',
     transferParams: { /* optional params */ },
   });
   ```

**Important Considerations:**

- Make sure to handle token balances and transfers correctly to avoid any errors or unexpected behavior.
- You should also test these API calls in a controlled environment before deploying them on your network.

By following these steps, you can successfully perform an action sequence involving IBC transfers between the Chain 2 origin chain and CW20's origin chain.
