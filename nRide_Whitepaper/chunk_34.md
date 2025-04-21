## Chunk 34

**Original Text:**

Additionally, the escrow smart-contract is configured with two timeouts:
T1

After the first deposit is paid into the escrow account, party B has T1 time to send their deposit,
after which party A will get their deposit back. T1 is left to the discretion of the first party to
create and instantiate the contract. However, T1 is intended to be relatively short, only a few
minutes after the agreement is initially formed and the first party engages with the contract (i.e. sending tokens to the contract). -7T2

T2 is a longer timeout that triggers a default action in case either of the parties fails to submit a
message to the smart contract after both deposits have been paid.

---

**LLM Contextual Output:**

The escrow smart-contract has two timeouts: T1 and T2.

- T1 (Timeout 1) is intended to be relatively short, lasting only a few minutes after the agreement is initially formed and the first party engages with the contract. This allows for quick communication between parties.
 
- T2 (Timeout 2), on the other hand, triggers a default action in case either of the parties fails to submit a message to the smart contract after both deposits have been paid.
