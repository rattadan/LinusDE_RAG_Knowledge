# Documentation Analysis - Chunk chunk_40.txt

## Source Context
*From: https://solana.com/*

### Document Overview  
This content discusses Solana's program architecture, instruction processing, signature verification mechanisms, and transaction fee calculations, focusing on cryptographic programs like ed25519, secp256k1, and secp256r1.  

### Key Technical Concepts  
- **Programs**: Accounts containing executable code, organized into instructions (e.g., signatures, data storage).  
- **Instructions**: Atomic units of work executed by programs, including signature verification and data manipulation.  
- **Signature Verification**: Processes to validate transaction signatures using cryptographic algorithms (e.g., secp256k1, secp256r1).  
- **Transaction Fees**: Calculated based on the number of signatures verified, with costs tied to the multiplier.  
- **Upgrade Authority**: A role to update program code, which becomes immutable once removed.  
- **Low S Values**: Enforced to prevent signature malleability, ensuring security.  

### Implementation Details  
- **Instruction Structure**: Each instruction begins with a byte count of signatures followed by a padding byte. Subsequent bytes serialize signature data.  
- **Signature Verification**:  
  - **ed25519**: Verifies signatures using a count of signatures and padding.  
  - **secp256k1/secp256r1**: Use cryptographic algorithms to validate signatures, with low S values enforced to prevent malleability.  
- **Transaction Fees**: Cost = (number of signatures verified) × (signature cost multiplier).  
- **Programs**:  
  - **Native Programs**: Historically distributed with validators, now managed via a list of core functionalities.  

### Related Topics  
- **Program Derived Address**: Discusses how programs are organized into accounts and their addresses.  
- **Transaction Fees**: Connected to the fee calculation mechanism described here.  
- **Upgrade Authority**: Linked to program immutability and authority management.

---

## Original Text
```
so is regulated by the authority of a program
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
- While programs arestateless, they can include instructions that create
and update other accounts to store data.
- Anupgrade authoritycan update programs. Once this authority is removed,
the program becomes immutable.
```