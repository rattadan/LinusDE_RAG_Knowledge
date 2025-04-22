## Chunk 51

**Original Text:**

You don’t need to change it or add anything to it to prepare it for signing. You just need to sign it and have the user submit it on chain within about 1 minute (or the nonce will expire). For more detail, the transaction already includes:

User’s nonce (In Solana, this is actually a recent blockhash by default)
Instructions (Solana’s equivalent to messages)
Base transaction fees (Set to the default of 500 lamports per signature)
Priority fees (More info on how we set these below)
For more information on transactions, check out the Solana’s official docs

​
Signing tx
Skip Go Client takes care of all of the complexity of signing the transaction that gets returned in SvmTx.tx. You just need to have set the getSVMSigner method in the SkipClientOptions object in the SkipClient constructor then use executeRoute or executeTxs. ​
How Priority Fees are Set
Solana “priority fees” affect how likely it is a transaction gets included in a block.

---

**LLM Contextual Output:**

I'll sign the text and have the user submit it on-chain within about 1 minute.

 signingTx = {
    nonce: tx.nonce,
    instructions: tx.instructions.toString(),
    baseTransactionFees: 500, // default
    priorityFees: {
        // set more info on how we set these below
    }
}
