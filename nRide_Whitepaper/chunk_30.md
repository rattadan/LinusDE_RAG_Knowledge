## Chunk 30

**Original Text:**

Functioning
The escrow smart-contract allows multiple users to create independent escrows. Each escrow involves two
users and has a unique id (for future calls to reference it) as well as other parameters that guard the state
transitions that are involved in the lifecycle of the escrow. Each escrow is composed of two accounts, each guarded by what we call a secret. Once an escrow is
funded by both parties, a user must obtain the other user’s secret to unlock all of their deposit, otherwise
they will lose a portion of it. In effect, the secret is simply the private component of a cryptographic key
pair created for the purpose of the escrow.

---

**LLM Contextual Output:**

So, you're describing an escrow smart-contract that allows multiple users to create independent escrows, each with its own unique ID and parameters. Here's a summary:

* Each escrow is composed of two accounts, guarded by a secret (also known as a cryptographic key pair).
* The secret serves as the private component, allowing only one account to access the funds held within the escrow.
* When an escrow is funded, both parties agree on the terms and conditions, but before releasing the funds, one party must obtain the other's secret in order to unlock their deposit.

This model implies that there are two types of users involved in an escrow:

1. Funders: The parties who initially fund the escrow, requiring the receiving user's secret to access their deposit.
2. Recipients: The users whose secrets can be used to unlock their deposits once they've obtained theirs from the other party.

This setup ensures that each party has a vested interest in keeping their funds secure and only releasing them when they're fully paid or unlocked by another party.
