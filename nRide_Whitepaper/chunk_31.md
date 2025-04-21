## Chunk 31

**Original Text:**

Once an escrow is
funded by both parties, a user must obtain the other user’s secret to unlock all of their deposit, otherwise
they will lose a portion of it. In effect, the secret is simply the private component of a cryptographic key
pair created for the purpose of the escrow. When a user funds their account in the escrow, they create a new
key pair locally, and set the new public key as the ’lock’ of their account in the escrow. The other user will
need to obtain the private key - the secret - to unlock their deposit. Users exchange secrets offline, and the
procedure for doing so is not covered by the protocol (could be by tapping phones through NFC, or by
sending a message over the NKN network).

---

**LLM Contextual Output:**

In blockchain-based escrow systems like NKN, once an escrow is funded, users must obtain each other's secret keys to unlock their deposits. The secret key serves as the private component of a cryptographic key pair created for the purpose of the escrow.

When a user funds their account in the escrow, they create a new key pair locally and set the public key as the "lock" of their account in the escrow. However, to unlock their deposit, they need access to the private key - also known as the secret key.

To facilitate this exchange without being directly connected to each other, users typically use one of two methods: 

1. Offline exchanges using Near Field Communication (NFC) or Bluetooth.
2. Messaging over the NKN network.
