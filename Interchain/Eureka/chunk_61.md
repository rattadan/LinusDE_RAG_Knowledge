## Chunk 61

**Original Text:**

Request Route using SkipClient and get required chain
Next, request your route as normal:

TypeScript

Copy
const route = await skipClient.route({
  amountIn: "1000",
  sourceAssetDenom: "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
  sourceAssetChainID: "1",
  destAssetDenom: "0xaf88d065e77c8cC2239327C5EDb3A432268e5831",
  destAssetChainID: "42161",
  smartRelay: true,
  smartSwapOptions: {
    splitRoutes: true
  }
};

​
3. Get User Addresses for all Required Chains
Use the route to determine the chains for which you need to supply a user address (the source, destination, and all intermediate chains that require a recovery address for receiving tokens in case of a failure)

TypeScript

Copy
let userAddresses = []
const requiredAddresses = route.requiredChainAddresses;
// iterate over chain IDs for chains that require addresses
for (const chainID of requiredAddresses) {
  	// Check that the chain is an EVM chain
    if (parseInt(chainID)) {
      // use signer library to get address from wallet
      const chain = extractChain({
        chains: Object.values(chains),
        id: parseInt(chainID)
      });
      const evmWalletClient = createWalletClient({
        chain: chain,
        transport: custom(window.ethereum!)
      });
      const [address] = await client.requestAddresses();
      // add to map
      userAddresses.append({address: address, chainID: chainID})
    } else {
      // handle cosmos and SVM wallets -- not shown
    }

});
return evmWalletClient;
}

​
4. Execute the Route using SkipClient
Finally, you can use SkipClient.executeRoute to prompt the user to sign the approval(s) and transaction, and submit the transaction on chain. TypeScript

Copy
await skipClient.executeRoute({
  route:route,
  userAddresses: userAddresses
});


Cross-chain Failure Cases
This page covers the different ways our cross-chain swaps + transfers might fail to help identify failures and manage user expectations

​
Failures during IBC Transfers and Swaps
There are two types of IBC failures that may occur when a user attempts to traverse a swap / transfer route produced by the Skip Go API. Pre-Swap / swap failures
What: These are failures in the sequence of ICS-20 transfers leading up to the swap or a failure in the swap itself (usually due to slippage).

---

**LLM Contextual Output:**

I can help you with all the steps, but I'll need to make some assumptions about the code and libraries you're using. Since you didn't provide the code for `extractChain` and `createWalletClient`, I'll assume that these functions are defined elsewhere in your project.

Here's the updated code:

**Step 1: Request Route**
```typescript
const route = await skipClient.route({
  amountIn: "1000",
  sourceAssetDenom: "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
  sourceAssetChainID: "1",
  destAssetDenom: "0xaf88d065e77c8cC2239327C5EDb3A432268e5831",
  destAssetChainID: "42161",
  smartRelay: true,
  smartSwapOptions: {
    splitRoutes: true
  }
});
```

**Step 2: Get Required Chain Addresses**
```typescript
let userAddresses = [];
const requiredAddresses = route.requiredChainAddresses;
// iterate over chain IDs for chains that require addresses
for (const chainID of requiredAddresses) {
  if (parseInt(chainID)) { // EVM chain
    const chain = extractChain({
      chains: Object.values(chains),
      id: parseInt(chainID)
    });
    const evmWalletClient = createWalletClient({
      chain: chain,
      transport: custom(window.ethereum!)
    });
    const [address] = await client.requestAddresses();
    userAddresses.push({ address, chainID });
  } else { // Cosmos and SVM wallets
    // handle non-EVM chains for now
  }
}
return evmWalletClient;
```

**Step 3: Execute Route**
```typescript
await skipClient.executeRoute({
  route,
  userAddresses
});
```

Some notes:

* The `extractChain` function is assumed to be defined elsewhere in your code.
* The `createWalletClient` function is also assumed to be defined elsewhere.
* The `custom` function from the `window.ethereum` API is used to get a custom Ethereum client instance. You'll need to set up this environment variable or use a different method to get the correct client instance.
* This code assumes that the user addresses will be stored in an array and added to the `userAddresses` map. If your data storage approach is different, you may need to adjust this part of the code accordingly.

Please let me know if these assumptions are incorrect or if you have any further questions!
