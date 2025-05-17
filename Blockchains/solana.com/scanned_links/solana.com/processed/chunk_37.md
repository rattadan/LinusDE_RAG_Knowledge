# Documentation Analysis - Chunk chunk_37.txt

## Source Context
*From: https://solana.com/*

### Document Overview  
This content explains Solana's program accounts, their structure, and how they manage data, ownership, and balance, focusing on loader programs, account data, and the System Program's role in creating and transferring ownership of accounts.  

### Key Technical Concepts  
- **Program Accounts**: Accounts containing executable code (loader programs) and data (account data).  
- **Lamports**: The smallest unit of SOL, used to represent account balances.  
- **Owner Program**: The program ID that owns an account, controlling data modifications and lamport deductions.  
- **Rent Epoch**: A legacy field for rent collection, now deprecated.  
- **Account Data**: The program's data (e.g., program state, metadata) stored in the account.  
- **Space Allocation**: The byte capacity allocated to the data field of an account.  
- **Ownership Transfer**: The System Program can reassign ownership of new accounts to custom programs.  
- **BPF (Berkeley Packet Filter)**: A security feature for restricting access to account data.  

### Implementation Details  
- **System Program**: The only program allowed to create new accounts.  
- **Account Data Structure**: Includes `executable` (bool), `lamports` (uint), `owner` (public key), and `rent_epoch` (legacy).  
- **Data Field Management**: The owner program can modify `account data` via the `invoke` instruction.  
- **Space Allocation**: Defined in the `space` field of the account, specifying the maximum size for `data`.  
- **Ownership Transfer Process**:  
  1. System Program creates an account (e.g., via `invoke` with `CREATE` instruction).  
  2. Owner program (via `transfer` instruction) assigns new ownership to another program account.  
- **BPF Security**: Restricts access to account data via BPF filters.  

### Related Topics  
- **BPF**: Mentioned in the document as a security mechanism for account data access.  
- **Built-in Programs**: Covered in the "Built-in Programs" section of the document.  
- **Table of Contents**: The document references the "Table of Contents" for further navigation.

---

## Original Text
```
that's meant be read from.
For program accounts (smart contracts), this contains the executable program
code. The data field is commonly called "account data."
- executable: This flag shows if an account is a program.
- lamports: The account's balance in lamports, the smallest unit of SOL (1 SOL
= 1 billion lamports).
- owner: The program ID (public key) of the program that owns this account.
Only the owner program can change the account's data or deduct its lamports
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
Document: Programs | Solana
Source: https://solana.com/docs/core/programs#loader-programs
================================================================================

h1: Programs

h2: Key Points

h2: Writing Solana Programs

h2: Updating Solana Programs

h2: Verifiable Programs

h2: Berkeley Packet Filter (BPF)

h2: Built-in Programs

h3: Loader Programs

h3: Precompiled Programs

h4: Ed25519 Program

h4: Secp256k1 Program

h4: Secp256r1 Program

h3: Core Programs

h3: Table of Contents

```