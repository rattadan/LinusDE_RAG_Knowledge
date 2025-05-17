# Documentation Analysis - Chunk chunk_14.txt

## Source Context
*From: https://solana.com/*

### Document Overview  
This content explains the structure of a Solana transaction message, detailing components like account keys, transaction ID, program instructions, and metadata required for validation and execution.  

### Key Technical Concepts  
- **Transaction Message**: A structured data object containing metadata and instructions for a Solana transaction.  
- **Account Keys**: An array of public keys representing accounts involved in the transaction. The first key is the transaction ID.  
- **Signer/Required Signer**: A boolean indicating whether an account is required to sign the transaction.  
- **Writable Account**: A boolean indicating if an account can be modified by the transaction.  
- **Program Instructions**: A list of parsed instructions executed by a program, including parameters like `programId`, `type`, and `info`.  
- **Stack Height**: A number representing the state of the stack during instruction execution.  
- **Base-58 Encoding**: Used to encode public keys and transaction IDs for readability and storage.  

### Implementation Details  
- **Message Structure**: The `message` object includes `header`, `accountKeys`, `pubkey`, `signer`, `writable`, `source`, `recentBlockhash`, `instructions`, and `program`.  
- **Account Keys**: Each key in `accountKeys` corresponds to an account, with the first key being the transaction ID.  
- **Program Execution**: Instructions are parsed into `type` (e.g., "transfer") and `info` specific to the program.  
- **Signer Requirements**: The `signer` field determines if an account must be signed to validate the transaction.  
- **Base-58 Encoding**: Public keys and transaction IDs are encoded using base-58 for compatibility with Solana's blockchain.  

### Related Topics  
- **Solana Transaction Documentation**: This content is part of the broader Solana documentation on transaction formats and validation.  
- **Account Information**: Details about `accountKeys`, `pubkey`, and `source` are connected to the broader topic of account management in Solana.  
- **Program Execution**: The `program` and `programId` fields are explained in the context of Solana's programmatic instructions and execution model.

---

## Original Text
```
of lengthmessage.header.numRequiredSignaturesand not empty. The signature at indexicorresponds to the public key at indexiinmessage.accountKeys. The
first one is used as thetransaction id.
- message: <object>- Defines the content of the transaction.accountKeys: <array[object]>- List of account information used by the
transaction.pubkey: <string>- The base-58 encoded public key of the account.signer: <boolean>- Indicates if the account is a required transaction
signer.writable: <boolean>- Indicates if the account is writable.source: <string>- Source of the account (transaction or lookup table).recentBlockhash: <string>- A base-58 encoded hash of a recent block in
the ledger used to prevent transaction duplication and to give transactions
lifetimes.instructions: <array[object]>- List of parsed program instructions.program: <string>- The name of the program being called.programId: <string>- The base-58 encoded public key of the program.stackHeight: <number|null>- The stack height of the instruction.parsed: <object>- Program-specific parsed data.type: <string>- The type of instruction (e.g., "transfer").info: <object>- Parsed instruction information specific to the
program and instruction type.
- accountKeys: <array[object]>- List of account information used by the
transaction.pubkey: <string>- The base-58 encoded public key of the account.signer: <boolean>- Indicates if the account is a required transaction
signer.writable: <boolean>- Indicates if the account is writable.source: <string>- Source of the account (transaction or lookup table).
- pubkey: <string>- The base-58 encoded public key of the account.
- signer: <boolean>- Indicates if the account is a required transaction
signer.
- writable: <boolean>- Indicates if the account is writable.
- source: <string>- Source of the account (transaction or lookup table).
```