# Documentation Analysis - Chunk chunk_10.txt

## Source Context
*From: https://solana.com/*

### Document Overview  
This content explains the structure of Solana RPC methods, focusing on transaction processing, inner instructions, token balances, and message components, including details about account keys, program IDs, and required signatures.  

### Key Technical Concepts  
- **Inner Instructions**: Grouped by transaction, processed in sequence, and executed atomically.  
- **Token Balances**: Represented as a list of objects tracking account balances for Solana's token system.  
- **Message Structure**: Includes account keys, program IDs, required signatures, and recent blockhashes to validate transactions.  
- **Account Keys**: Base-58 encoded public keys used for transaction signing and program execution.  
- **Program IDs**: Identifiers for deployed programs, referenced via index in the message.  
- **NumRequiredSignatures**: Specifies the number of signatures required for transaction validity.  
- **Recent Blockhash**: A hash of a recent block to prevent transaction duplication and ensure lifetime.  

### Implementation Details  
- **Inner Instructions**: A list of objects with `programIdIndex` (program account index) and `instructions` (list of execution steps).  
- **Token Balances**: A list of objects with `accountKeys` (public keys) and `balance` (lamports).  
- **Message Fields**:  
  - `accountKeys`: Array of base-58 encoded public keys (first `numRequiredSignatures` must sign).  
  - `header`: Includes `numRequiredSignatures` and `numReadonlySignedAccounts`/`numReadonlyUnsignedAccounts`.  
  - `recentBlockhash`: Base-58 encoded hash for transaction validation.  
- **Transaction Processing**: Instructions are executed in order, and all must succeed for atomicity.  

### Related Topics  
- **Solana RPC Methods**: This content is part of the broader Solana RPC documentation, which includes methods for querying transactions, accounts, and block data.  
- **Account Structure**: The message structure is aligned with Solana's account management system, which defines account keys, programs, and balances.  
- **Token Balance API**: Token balances are a key component of Solana's token system, often queried via RPC methods.

---

## Original Text
```
on-chain per transaction instruction. Invoked instructions
are grouped by the originating transaction instruction and are listed in order
of processing.

The JSON structure of inner instructions is defined as a list of objects in the
following structure:

The JSON structure of token balances is defined as a list of objects in the
following structure:

Is this page helpful?

Solana RPC Methods

- transactions
- inner instructions
- token balances
- message: <object>- Defines the content of the transaction.accountKeys: <array[string]>- List of base-58 encoded public keys used by
the transaction, including by the instructions and for signatures. The firstmessage.header.numRequiredSignaturespublic keys must sign the
transaction.header: <object>- Details the account types and signatures required by
the transaction.numRequiredSignatures: <number>- The total number of signatures
required to make the transaction valid. The signatures must match the
firstnumRequiredSignaturesofmessage.accountKeys.numReadonlySignedAccounts: <number>- The lastnumReadonlySignedAccountsof the signed keys are read-only accounts.
Programs may process multiple transactions that load read-only accounts
within a single PoH entry, but are not permitted to credit or debit
lamports or modify account data. Transactions targeting the same
read-write account are evaluated sequentially.numReadonlyUnsignedAccounts: <number>- The lastnumReadonlyUnsignedAccountsof the unsigned keys are read-only accounts.recentBlockhash: <string>- A base-58 encoded hash of a recent block in
the ledger used to prevent transaction duplication and to give transactions
lifetimes.instructions: <array[object]>- List of program instructions that will be
executed in sequence and committed in one atomic transaction if all succeed.programIdIndex: <number>- Index into themessage.accountKeysarray
indicating the program account that executes this instruction.accounts: <array[number]>- List of ordered indices into themessage.
```