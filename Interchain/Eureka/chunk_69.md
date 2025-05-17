## Chunk 69

**Original Text:**

Internally, the Skip Go API may use Axelar’s General Message Passing service to move assets between EVM and Cosmos. There are similar failure modes for Axelar as there are for IBC:

Swap failures
What: Axelar GMP takes user assets from an EVM chain to the swap chain. The swap can still fail at this point due to a timeout or slippage. Outcome / What to Expect: The user receives the Axelar-transferred token on the chain where the swap was supposed to take place at their recovery address. (Note this is different from the IBC swap failure case where the user receives the swap token back on the source chain)
Common failure sources:
Slow relaying from Axelar causes a timeout, and the swap is not attempted.

---

**LLM Contextual Output:**

So, in the context of the Skip Go API, Axelar's General Message Passing (GMP) service is used to move assets between the EVM (Ethereum Virtual Machine) and the Cosmos chain. 

The failure mode mentioned here is related to swapping assets on an Axie blockchain network using Axelar GMP.

Here are some key points about the failure modes:

- **Swap failures**: These can occur due to two main reasons: 
    1. **Timeout**: The swap process takes too long, resulting in a timeout.
    2. **Slippage**: There's an error or delay during the transfer process, causing it to move at a different speed than intended.

The outcome for users in this scenario is that they receive their transferred tokens on the Cosmos chain where the swap was supposed to take place, but not necessarily at the recovery address as expected.
