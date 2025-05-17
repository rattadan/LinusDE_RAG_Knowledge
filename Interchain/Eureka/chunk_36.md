## Chunk 36

**Original Text:**

These converter contracts are the source of much difficulty when attempting to perform cross-chain actions with CW20s:

Different converter contracts implement different versions of the ICS20 standard (e.g. Some don’t support memos, which are required for post-transfer contract calls and multi-hop transfers)
On transfer failure, converter contracts just return assets to sender. That means if one of our contracts attempts to send tokens on your behalf unsuccessfully, it will receive the tokens. We can’t atomically send them to you. ​
How do CW20 tokens compare to “native” (aka bank module) tokens?

---

**LLM Contextual Output:**

CW20 tokens and "native" or "bank module" tokens are two different types of tokens used in the context of cross-chain interactions, particularly with smart contracts.

CW20 tokens, also known as Cerebral 2.0 (C20), are a type of Ethereum token that is specifically designed for use on the Cerebral Network, which is an interoperability network built on top of the Solana blockchain. CW20s are unique in that they can be transferred between chains using the Cerebral Bridge protocol.

As you mentioned, one of the challenges with converting CW20 tokens to native tokens or other chain-specific tokens is that converter contracts may not implement different versions of the ICS20 standard (the Inter-Chain Standard 2.0). This means that if a CW20 contract wants to perform post-transfer contract calls or multi-hop transfers, it might not be able to do so without returning assets to the sender.

In contrast, native tokens like bank module tokens are typically designed with interoperability in mind and may have more flexible design choices compared to ICS20. This allows them to be used across multiple chains, including those that implement different versions of the ICS20 standard.

It's worth noting that as CW20s become more widely adopted on other chains, it's likely that their design will evolve to accommodate different standards and requirements. However, for now, native tokens may offer a better option when trying to perform cross-chain actions with CW20s.
