## Chunk 60

**Original Text:**

Initialize the SkipClient client with the EVM WalletClient object
All 3 libraries mentioned above allow you to create WalletClient “signer” objects that:

Use an RPC provider under the hood to query the chain for necessary data to create transactions (e.g. nonce, gas price, etc…)
Expose an API that allows constructing, signing, and broadcasting transactions
You need to set up the getEVMSigner function in the SkipClient constructor to initialize this signer object for the a given EVM chain. For example, with Viem, we do the following:

TypeScript

Copy
import { createWalletClient, custom} from 'viem';
import * as chains from 'viem/chains';
import { SkipClient } from '@skip-go/client';

const
const skipClient = new SkipClient({
  getEVMSigner: async (chainID) => {
    const chain = extractChain({
  		chains: Object.values(chains),
  		id: parseInt(chainID)
    });
    const evmWalletClient = createWalletClient({
  		chain: chain,
  		transport: custom(window.ethereum!)
  	});
    return evmWalletClient;
  }
});
​
2. Request Route using SkipClient and get required chain
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
4.

---

**LLM Contextual Output:**

Based on the provided specification, it appears that you're using the `SkipClient` library to interact with a blockchain, specifically for interacting with Ethereum (EVM) chains. 

The initial step is to initialize the `SkipClient` instance with an EVM wallet client object. The `getEVMSigner` function in the `SkipClient` constructor should be used to create and configure a signer object for the specified chain.

Here's how you can modify your code to include these steps:

```typescript
import { createWalletClient, custom } from 'viem';
import * as chains from 'viem/chains';
import { SkipClient } from '@skip-go/client';

const skipClient = new SkipClient({
  getEVMSigner: async (chainID) => {
    const chain = extractChain({ 
      chains: Object.values(chains), 
      id: parseInt(chainID)
    });
    const evmWalletClient = createWalletClient({
      chain,
      transport: custom(window.ethereum!)
    });
    return evmWalletClient;
  }
});

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

const userAddresses = [];
const requiredAddresses = route.requiredChainAddresses;

for (const chainID of requiredAddresses) {
  if (parseInt(chainID)) {
    const chain = extractChain({ 
      chains: Object.values(chains), 
      id: parseInt(chainID)
    });
    const evmWalletClient = createWalletClient({
      chain,
      transport: custom(window.ethereum!)
    });
    const [address] = await skipClient.requestAddresses();
    userAddresses.append({ address, chainID });
  } else {
    // handle cosmos and SVM wallets
  }
}

return evmWalletClient;
```

Please note that this code assumes you have the `extractChain` function defined elsewhere in your codebase. If not, you would need to implement it as well.

This should give you a basic implementation of how to initialize the `SkipClient` instance and use its `getEVMSigner` function to create and configure a signer object for EVM chains.
