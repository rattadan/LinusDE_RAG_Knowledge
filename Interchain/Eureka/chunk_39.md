## Chunk 39

**Original Text:**

As a result, issuing a new native token requires a chain upgrade. Issuing a CW20 on the other hand, only requires deploying a new contract (just a transaction). ​
How do CW20 tokens compare to “tokenfactory” tokens? Tokenfactory tokens are created with the tokenfactory module. They’re designed to have the best of both worlds of CW20 and native tokens:

Like CW20s, they’re permissionless and users can create new ones just by submitting transactions — no need to modify the chain’s state machine
Like native tokens, they’re directly compatible with IBC out-of-the-box, and the bank module manages their balances + transferring functionality.

---

**LLM Contextual Output:**

So, you're comparing CW20 tokens (which are permissionless and can be created using a transaction) to Tokenfactory tokens.

Tokenfactory tokens seem to offer a unique combination of benefits:

1. **Permissionlessness**: Similar to CW20s, they allow users to create new tokens without modifying the chain's state machine.
2. **IBC compatibility**: They're directly compatible with Inter-Blockchain Communication (IBC), which enables seamless transfer of assets between blockchains.

Compared to CW20 tokens, Tokenfactory tokens have several advantages:

1. **Scalability**: Since they can be created in a transaction, they don't require a chain upgrade or additional gas fees.
2. **Flexibility**: Tokenfactory tokens can be deployed on multiple blockchain networks without modifications.
3. **No need for bank integration**: As mentioned earlier, banks manage balances and transferring functionality directly through the tokenfactory module.

However, there are some potential drawbacks to consider:

1. **Liquidity risks**: Creating new tokens using a transaction may not always lead to liquidity in the market, especially if there's limited demand.
2. **Regulatory uncertainty**: The regulatory environment for Tokenfactory tokens is still evolving, and it's unclear how they'll be treated by law enforcement or regulatory bodies.

In summary, Tokenfactory tokens offer a convenient and scalable way to create new tokens without requiring a chain upgrade or additional gas fees. However, users should be aware of the potential liquidity risks and regulatory uncertainty before deploying their tokens.
