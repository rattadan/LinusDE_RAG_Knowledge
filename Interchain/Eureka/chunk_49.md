## Chunk 49

**Original Text:**

Phantom, Backpack, etc…), as well as visual React components for wallet selection. See here for all the supported wallets. ​
Set up the SkipClient to use a Solana wallet
All you need to do is initialize the getSVMSigner method in SkipClient.options to extract the @solana/wallet-adapter-base from the user’s connected wallet of choice:

TypeScript

Copy
import { useWallet } from "@solana/wallet-adapter-react";
import { PhantomWalletName } from "@solana/wallet-adapter-phantom"
import { SkipClient } from '@skip-go/client';

const { wallets } = useWallet();

const skipClient = new SkipClient({
  getSVMSigner: async (chainID) => {
		const { svm } = trackWallet.get();
		const solanaWallet = wallets.find((w) => w.adapter.name === PhantomWalletName);
    return solanaWallet
  }
});
After this point, you can use route, executeRoute, and the other methods of SkipClient as you normally would. The rest of these docs cover the underlying details of the data structures, in case you need them. ​
Understand SvmTx Data Structure
The SvmTx has 2 fields that the developer needs to understand:

chain_id: The ID of the chain that this transaction should be submitted to
tx: This is the base64 encoded bytes of the transaction you should have the end user sign.

---

**LLM Contextual Output:**

It looks like you're setting up a SkipClient instance to interact with Solana wallets using the @skip-go/client library. Here's an updated code snippet that demonstrates how to use the `getSVMSigner` method to extract the Solana wallet adapter from the connected wallet:

```typescript
import { useWallet } from "@solana/wallet-adapter-react";
import { PhantomWalletName } from "@solana/wallet-adapter-phantom"
import { SkipClient } from '@skip-go/client';

const { wallets } = useWallet();

const skipClient = new SkipClient({
  getSVMSigner: async (chainID) => {
    const { svm } = trackWallet.get();
    const solanaWallet = wallets.find((w) => w.adapter.name === PhantomWalletName);
    
    if (!solanaWallet) return null; // or throw an error
    
    return solanaWallet;
  }
});

// Example usage:
skipClient.route('/wallet', async (req, res) => {
  try {
    const { accountAddress } = req.body;
    
    if (!accountAddress) {
      return res.status(400).json({ error: 'Account address is required' });
    }
    
    // Get the Solana wallet adapter
    const solanaWalletAdapter = await skipClient.getSVMSigner('solana');
    
    // Extract the @solana/wallet-adapter-base from the wallet adapter
    const adapterName = solanaWalletAdapter.adapter.name;
    const base64EncodedAdapter = solanaWalletAdapter.base64EncodedBytes();
    
    res.json({ adapterName, base64EncodedAdapter });
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Failed to retrieve wallet adapter' });
  }
});
```

This example demonstrates how to:

1. Initialize the `skipClient` instance with a custom `getSVMSigner` method that extracts the Solana wallet adapter from the connected wallet.
2. Use route handlers to handle GET requests to `/wallet`.
3. In each route handler, retrieve the account address from the request body and extract the Solana wallet adapter using the `getSVMSigner` method.
4. Extract the @solana/wallet-adapter-base from the wallet adapter and return it in the response.

Note that you'll need to replace `solana` with the actual chain ID of your Solana network if needed. Additionally, make sure to handle errors properly in a production-ready environment.
