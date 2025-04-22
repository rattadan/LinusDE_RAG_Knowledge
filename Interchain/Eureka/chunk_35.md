## Chunk 35

**Original Text:**

​
How do CW20 tokens interact with IBC? CW20-ICS20 converter contracts make a CW20 token compatible with the ICS20 token transfer standard, so they can be sent to other chains over normal ICS20 transfer channels. When they arrive on the destination chain, they’re indistinguishable from bank module and tokenfactory tokens. These converter contracts are the source of much difficulty when attempting to perform cross-chain actions with CW20s:

Different converter contracts implement different versions of the ICS20 standard (e.g. Some don’t support memos, which are required for post-transfer contract calls and multi-hop transfers)
On transfer failure, converter contracts just return assets to sender.

---

**LLM Contextual Output:**

According to your information, here's how CW20 tokens interact with IBC (Inter-Blockchain Communication) protocol:

1. **ICS20 token compatibility**: CW20-ICS20 converter contracts can make CW20 tokens compatible with the ICS20 token transfer standard, allowing them to be sent across chains using normal ICS20 transfer channels.
2. **Cross-chain transfer**: When a CW20 token is transferred from one chain (e.g., from Ethereum to Binance Smart Chain) and arrives on another chain, it's indistinguishable from a bank module and tokenfactory tokens.
3. **Converter contracts**: However, different converter contracts implement different versions of the ICS20 standard, which can lead to difficulties when performing cross-chain actions with CW20s.

To summarize, the main issues are:

* Converter contracts may have varying implementations of the ICS20 standard, making them incompatible with each other.
* On transfer failure, some converter contracts simply return assets to the sender without attempting to resolve or resolve conflicts.
