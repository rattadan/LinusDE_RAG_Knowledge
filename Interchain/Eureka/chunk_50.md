## Chunk 50

**Original Text:**

The rest of these docs cover the underlying details of the data structures, in case you need them. ​
Understand SvmTx Data Structure
The SvmTx has 2 fields that the developer needs to understand:

chain_id: The ID of the chain that this transaction should be submitted to
tx: This is the base64 encoded bytes of the transaction you should have the end user sign. ​
Info on SvmTx.tx
This is a fully constructed transaction. You don’t need to change it or add anything to it to prepare it for signing. You just need to sign it and have the user submit it on chain within about 1 minute (or the nonce will expire).

---

**LLM Contextual Output:**

So, the SvmTx data structure consists of two main fields:

1. `chain_id`: This is the ID of the chain that this transaction should be submitted to.
2. `tx`: This is the base64 encoded bytes of the transaction that needs to be signed by the user.

Additionally, there's an "Info on SvmTx.tx" field which indicates what you need the user to do with the transaction (in this case, just sign and submit it within a certain time frame).
