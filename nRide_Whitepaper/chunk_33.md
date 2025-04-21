## Chunk 33

**Original Text:**

How it works:
Both parties, A and B, lock the same amount of tokens in the smart contract. Once the funds are locked,
each party can send one of two messages to the smartÂ contract:
Approve(secret)
A message containing the counterparty’s secret. Cancel

A message signifying the user’s desire to redeem a proportion of their deposit prior to
completion, or because they failed to obtain the other user’s secret. Additionally, the escrow smart-contract is configured with two timeouts:
T1

After the first deposit is paid into the escrow account, party B has T1 time to send their deposit,
after which party A will get their deposit back. T1 is left to the discretion of the first party to
create and instantiate the contract.

---

**LLM Contextual Output:**

Here's a breakdown of how it works:

**Initial State:**

* Both parties (A and B) lock an equal amount of tokens in the smart contract.
* The smart contract holds these funds until the deposit is redeemed or canceled.

**Message Types:**

* **Approve**: A message sent by party A to the smart contract, containing their secret. This message confirms that they want to proceed with redeeming a proportion of their deposit.
* **Cancel**: A message sent by party B to the smart contract, indicating that they don't want to redeem their portion.

**Redemption Mechanism:**

1. Upon receiving an Approve message from party A, party B gets their deposit back after a specified timeout (T1).
2. If no redemption is requested, T1 remains unset for both parties.
3. The smart contract holds the funds until one of the parties requests redeeming them.

Key points to note:

* The escrow contract has two timeouts: T1 and an unspecified second timeout (T2). These timeouts are managed by the first party to create and instantiate the contract.
* If no redemption is requested before T1 expires, both parties will retain their locked funds.
