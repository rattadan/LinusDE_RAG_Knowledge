## Chunk 47

**Original Text:**

​
Intro
When a user needs to transfer or swap from an SVM chain (e.g. Solana), the Skip Go API will return an SvmTx type for the developer to pass to the user for signing
This doc is intended for CosmosSDK and EVM developers who aren’t already familiar with the concepts of transaction construction in the SVM and need to use SvmTx to help their users move from/to Solana and other SVM chains. Due to the difficult nature of including Solana transactions on chain during times of high network congestion, we HIGHLY recommend using the /submit endpoint to avoid dealing with complex retry logic and/or multiple RPC providers for submission reliability. Skip Go API’s /submit endpoint implements best practices for Solana transactions submission for you! ​
Interact with Solana Wallets
We recommend using @solana/wallet-adapter to interact with Solana wallets and build transactions.

---

**LLM Contextual Output:**

Here's a more detailed explanation of the provided text:

**Context**: The Skip Go API is used by developers, particularly those working with the CosmosSDK and EVM (Ethereum Virtual Machine) for building and deploying blockchain applications.

**Purpose**: The documentation aims to educate developers who are unfamiliar with constructing transactions on the SVM (Solana Virtual Machine) using the SvmTx type. This is crucial because creating complex transactions can be challenging when dealing with high network congestion, making it essential to utilize a simpler alternative.

**Recommendation**: To avoid complications and improve reliability, developers should use the /submit endpoint offered by Skip Go API for submitting Solana transactions. This approach provides best practices for Solana transaction submission, reducing the need for complex retry logic and multiple RPC providers.

**Recommended Practice**: The text also recommends using `@solana/wallet-adapter` to interact with Solana wallets.
