## Chunk 32

**Original Text:**

The other user will
need to obtain the private key - the secret - to unlock their deposit. Users exchange secrets offline, and the
procedure for doing so is not covered by the protocol (could be by tapping phones through NFC, or by
sending a message over the NKN network). The escrow smart-contract implements a state machine that
guards all possible transitions and outputs given initial configuration and the messages submitted by the
users. How it works:
Both parties, A and B, lock the same amount of tokens in the smart contract. Once the funds are locked,
each party can send one of two messages to the smartÂ contract:
Approve(secret)
A message containing the counterparty’s secret.

---

**LLM Contextual Output:**

So, you're describing a decentralized exchange (DEX) protocol that uses a smart-contract-based escrow system to ensure secure and efficient token transactions.

Here's a summary of how it works:

1. **Private key exchange**: Both parties, A and B, need to obtain their private keys to unlock the deposit.
2. **State machine in the escrow contract**: The escrow smart-contract implements a state machine that guards all possible transitions and outputs given:
   - Initial configuration (both parties lock tokens).
   - Messages submitted by users (A or B can send an "Approve" message with their secret key).

The state machine will ensure that only authorized parties can access the transaction history, making it difficult to manipulate or alter the data.

3. **Approve(message) function**: When a user sends an "Approve" message with their secret key, they are essentially requesting that the escrow contract:
   - Store the tokens and return them to A.
   - Lock the same amount of tokens (A gets the locked tokens back, while B retains them until a later transaction).

By using this approach, you're ensuring secure communication between parties and preventing tampering with the token transactions.
