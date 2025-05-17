# Documentation Analysis - Chunk chunk_46.txt

## Source Context
*From: https://solana.com/*

### Document Overview  
This content explains how Solana transactions include instructions that execute programs, detailing the structure of transactions, account metadata, and the process of program ownership transfer.  

### Key Technical Concepts  
- **Instructions**: Operations defined by programs to perform actions (e.g., transferring lamports, initializing account data).  
- **AccountMeta**: Metadata about accounts, including fields like `rent_epoch` and `datafield` size.  
- **Program Ownership**: Transfer of control from the System Program to a custom program via a designated program owner.  
- **Transaction Size**: Metrics like message header, compact-array format, and array of instructions.  
- **Message Header**: A compact representation of transaction metadata (e.g., sender, receiver, fee).  
- **Compact-Array Format**: Efficient storage of arrays in transactions using a compact format.  
- **Array of Instructions**: A list of instructions to execute, critical for transaction validation.  

### Implementation Details  
- **System Program**: The only program allowed to create new accounts.  
- **Program Ownership Transfer**: Requires invoking the custom program to initialize account data.  
- **Compact-Array Format**: Used to reduce transaction size by storing arrays as pointers to memory.  
- **Account Meta Fields**: Includes `rent_epoch` (deprecated), `datafield` size, and `data` (actual storage).  
- **Transaction Structure**: Includes a message header, array of instructions, and recent blockhash for validation.  

### Related Topics  
- **Account Type**: The `Account` struct includes fields like `rent_epoch` and `datafield`.  
- **Program Ownership**: Connected to the "Transfer / Assign Program Ownership" section.  
- **Transaction Size**: Linked to "Transaction Size" and "Message Header" sections.  
- **Message Header**: Part of the "Transactions" section and required for transaction validation.

---

## Original Text
```
its lamports
balance.
- rent_epoch: A legacy field from when Solana had a mechanism that
periodically deducted lamports from accounts. While this field still exists in
the Account type, it is no longer used since rent collection was deprecated.
- Change the account'sdatafield
- Deduct lamports from the account's balance
- New Account Creation:
Only the System Program can create new accounts.
- Space Allocation:
Sets the byte capacity for the data field of each account.
- Transfer / Assign Program Ownership:
Once the System Program creates an account, it can reassign the designated
program owner to a different program account. That's how custom programs take
ownership of new accounts created by the System Program.
- Invoke the System Program to create an account, then transfer ownership to
the custom program
- Invoke the custom program, which now owns the account, to initialize the
account data as defined by the program's instruction

================================================================================
Document: Transactions and Instructions | Solana
Source: https://solana.com/docs/core/transactions#instruction
================================================================================

h1: Transactions and Instructions

h2: Key Points

h2: SOL Transfer Example

h2: Instructions

h3: AccountMeta

h3: Example Instruction Structure

h2: Transactions

h3: Transaction Size

h3: Message Header

h3: Compact-Array Format

h3: Array of Account Addresses

h3: Recent Blockhash

h3: Array of Instructions

h3: Example Transaction Structure

h3: Table of Contents

On Solana, users sendtransactionsto
interact with the network. Transactions contain one or moreinstructionsthat specify operations to
process. The execution logic for instructions are stored onprogramsdeployed to the Solana network, where each
program defines its own set of instructions.

Below are key details about Solana transaction processing:

```