# Documentation Analysis - Chunk chunk_36.txt

## Source Context
*From: https://solana.com/*

### Document Overview  
This content explains how Solana manages account states, including program accounts, data accounts, and sysvars, emphasizing the separation of program code and data and the role of the System Program in account creation.  

### Key Technical Concepts  
- **Accounts**: Segmented storage units for program state or data, with distinct ownership and balances.  
- **Program Accounts**: Store executable code (smart contracts), tied to a program owner.  
- **Data Accounts**: Created by programs to store arbitrary state data, requiring the System Program to initialize.  
- **System Program**: The sole entity allowed to create new accounts, transferring ownership to other programs.  
- **Lamports**: The smallest unit of SOL, with balances recoverable upon account closure.  
- **Sysvars**: Special accounts storing network cluster state (e.g., `clock`, `fees`).  
- **Owner**: A program ID (public key) that owns an account, controlling its data and balance.  

### Implementation Details  
- **Data Account Creation**: Requires the System Program to initialize a data account, which can later be transferred or owned by another program.  
- **Data Storage**: For non-executable accounts, the `data` field stores read-only state; for program accounts, it holds executable code.  
- **Balance Proportionality**: Lamports are proportional to the data size stored, with full recovery possible upon account closure.  
- **Account Types**:  
  - **Program Accounts**: Executable code (flag `executable` set to `true`).  
  - **Data Accounts**: Non-executable, storing arbitrary data (flag `executable` set to `false`).  
  - **Sysvars**: Special accounts (e.g., `clock`, `fees`) managed by the System Program.  

### Related Topics  
- **Transactions and Instructions**: Discusses how accounts interact via transactions, including ownership transfers and balance adjustments.  
- **Sysvars**: Linked to the explanation of sysvar accounts.  
- **Program Accounts**: Connected to the broader context of smart contract execution and ownership.

---

## Original Text
```
in a different account
than the program's state. This is like how operating systems typically have
separate files for programs and their data.

To maintain state, programs define instructions to create separate accounts that
they own. Each of these accounts has its own unique address and can store any
arbitrary data defined by the program.

Note that only theSystem Programcan
create new accounts. Once the System Program creates an account, it can then
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
```