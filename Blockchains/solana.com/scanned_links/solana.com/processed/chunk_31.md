# Documentation Analysis - Chunk chunk_31.txt

## Source Context
*From: https://solana.com/*

### Document Overview  
This content discusses Solana's program loaders, security mechanisms for signature verification, transaction fees, and the role of special programs in the network.  

### Key Technical Concepts  
- **Program Loaders**: Essential for managing and modifying programs, with loader-v3 and loader-v4 supporting dynamic updates.  
- **Signature Verification**: Uses ed25519 and secp256k1 programs to validate transactions, with low S values to prevent malleability.  
- **Transaction Fees**: Calculated based on the number of signatures verified, multiplied by a predefined cost factor.  
- **Program Derivation**: Accounts containing executable code, organized into instructions for execution.  

### Implementation Details  
- **Signature Verification**:  
  - ed25519: Validates instructions with a count of signatures, padding, and serialized structs.  
  - secp256k1: Similar structure but uses a different elliptic curve.  
  - **Cost Factor**: Transaction fees = (number of signatures) × (signature cost multiplier).  
- **Loader-Specific Features**:  
  - loader-v3/v4 allow program modifications post-deployment, governed by account ownership.  
  - **Low S Values**: Enforced to prevent accidental signature malleability.  
- **Transaction Fees**: Directly tied to the number of signatures verified, not the number of instructions.  

### Related Topics  
- **Solana Cluster Genesis**: Lists special programs (e.g., native programs) for core network functionalities.  
- **Program Derivation**: Explains how programs are organized into instructions for execution.  
- **Transaction Fees**: Connected to the cost calculation mechanism described in the text.

---

## Original Text
```
program itself is owned by another program, which is its loader.
Currently, five loaders programs exist:

These loaders are necessary to create and manage custom programs:

Loader-v3 and loader-v4 support modifications to programs after their initial
deployment. Permission to do so is regulated by the authority of a program
because the account ownership of each program resides with the loader.

The ed25519 program processes an instruction. The firstu8is a count of the
number of signatures to check, which is followed by a single byte padding. After
that, the following struct is serialized, one for each signature to check.

The pseudo code of the signature verification:

The secp256k1 program processes an instruction which takes in as the first byte
a count of the following struct serialized in the instruction data:

The pseudo code of the recovery verification:

This allows the user to specify any instruction data in the transaction for
signature and message data. By specifying a special instructions sysvar, one can
also receive data from the transaction itself.

Cost of the transaction will count the number of signatures to verify multiplied
by the signature cost verify multiplier.

The secp256r1 program processes an instruction. The firstu8is a count of the
number of signatures to check, followed by a single byte padding. After that,
the following struct is serialized, one for each signature to check:

The pseudo code of the signature verification:

Note: Low S values are enforced for all signatures to avoid accidental signature
malleability.

The Solana cluster genesis includes a list of special programs that provide core
functionalities for the network. Historically these were referred to as "native"
programs and they used to be distributed together with the validator code.

Is this page helpful?

Transaction Fees

Program Derived Address

- Programs are accounts containingexecutable code, organized into functions
calledinstructions.
```