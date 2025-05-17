# Documentation Analysis - Chunk chunk_45.txt

## Source Context
*From: https://solana.com/*

### Document Overview  
This content explains how Solana's System Program creates new accounts, emphasizing the two-step process for data accounts and the roles of program ownership, lamports, and sysvars.  

### Key Technical Concepts  
- **System Program**: The only program allowed to create new accounts.  
- **Data Accounts**: Created by programs to store non-executable state (e.g., arbitrary data).  
- **Program Accounts**: Store executable code (smart contracts) and are owned by their program owner.  
- **Ownership Transfer**: Ownership of an account can be transferred to another program.  
- **Lamports**: The account's balance, deducted by the program owner.  
- **Rent Epoch**: A legacy field for rent collection, no longer used.  

### Implementation Details  
- **Account Creation Process**:  
  1. **Create the account** (via System Program).  
  2. **Transfer ownership** to another program (e.g., via `transfer` instruction).  
- **Account Types**:  
  - **Data Accounts**: Use `data` field for non-executable state (e.g., user data).  
  - **Program Accounts**: Use `executable` flag to distinguish between code and state.  
  - **Sysvars**: Special accounts storing network state (e.g., `rent_epoch`).  
- **Program Owner**: Determined by the `owner` field, which must match the program's public key.  

### Related Topics  
- **Transactions and Instructions**: The content connects to the broader theme of account management and program interactions.  
- **System Program**: Links to other sections explaining its role in account creation and rent collection.  
- **Account Types**: References the distinction between data and program accounts, which are detailed in the "Accounts" section of Solana documentation.

---

## Original Text
```
new accounts. Once the System Program creates an account, it can then
transfer or assign ownership of the new account to another program.

In other words, creating a data account for a custom program takes two steps:

This account creation process is often abstracted as a single step, but it's
helpful to understand the underlying process.

Is this page helpful?

Transactions and Instructions

- Accounts can store up to10MiBof data, which contains either executable program code or program state.
- Accounts require arent depositin lamports (SOL) that's proportional to the amount of data stored, and you
can fully recover it when you close the account.
- Every account has a programowner.
Only the program that owns an account can change its data or deduct its
lamport balance. But anyone can increase the balance.
- Sysvar accountsare special accounts that store network cluster state.
- Program accountsstore the executable code of smart contracts.
- Data accountsare created by programs to store and manage program state.
- data: A byte array that stores arbitrary data for an account. For
non-executable accounts, this often stores state that's meant be read from.
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
```