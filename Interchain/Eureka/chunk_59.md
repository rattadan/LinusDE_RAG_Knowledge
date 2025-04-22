## Chunk 59

**Original Text:**

Install Signing Library and Skip Library
To enable EVM transactions in your application, first install an EVM developer library. The most popular options are:

viem
ethers.js
web3.js
The code snippets below use viem. Shell

Copy
npm i viem
npm i @skip-go/client
​
1. Initialize the SkipClient client with the EVM WalletClient object
All 3 libraries mentioned above allow you to create WalletClient “signer” objects that:

Use an RPC provider under the hood to query the chain for necessary data to create transactions (e.g. nonce, gas price, etc…)
Expose an API that allows constructing, signing, and broadcasting transactions
You need to set up the getEVMSigner function in the SkipClient constructor to initialize this signer object for the a given EVM chain.

---

**LLM Contextual Output:**

To install Signing Library and Skip Library, you can follow these steps:

1. Install viem by running `npm i viem` in your shell.
2. Install @skip-go/client by running `npm i @skip-go/client` in your shell.

Here's an example of how to initialize the SkipClient client with the EVM WalletClient object:
```javascript
const { WalletClient } = require('@skip-go/client');
const skipClient = new WalletClient('https://mainnet.infura.io/v3/YOUR_PROJECT_ID');

// Initialize getEVMSigner function in the SkipClient constructor
skipClient.getEVMSigner = async () => {
  const signer = await skipClient.getSigner();
  return signer;
};
```
In this example, we create a new `WalletClient` instance with an EVM mainnet RPC provider. We then define a `getEVMSigner` function that returns an initialized `SkipClient` signer object for the given EVM chain.

Note that you should replace `YOUR_PROJECT_ID` with your actual Infura project ID.

Also, make sure to install ethers.js as it is required by @skip-go/client. You can do this by running `npm i ethers.js` in your shell.

If you want to use viem, you can follow the same steps and define the `getEVMSigner` function manually:
```javascript
const { WalletClient } = require('viem');
const skipClient = new WalletClient({
  rpcUrl: 'https://mainnet.infura.io/v3/YOUR_PROJECT_ID',
});

// Define getEVMSigner function manually
skipClient.getEVMSigner = async () => {
  const signer = await skipClient.createSigner();
  return signer;
};
```
Replace `YOUR_PROJECT_ID` with your actual Infura project ID.
