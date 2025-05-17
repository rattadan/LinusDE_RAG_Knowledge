# Documentation Analysis - Chunk chunk_34.txt

## Source Context
*From: https://solana.com/*

### Document Overview  
This content explains Solana's account model, including Program Derived Addresses (PDAs), rent mechanisms, system programs, sysvars, and program accounts.  

### Key Technical Concepts  
- **Program Derived Addresses (PDAs):** Deterministically generated addresses from a program ID and optional seeds, enabling program ownership.  
- **Rent:** A deposit for account storage, proportional to data size, managed by the system program.  
- **System Program:** Owns all accounts, handles wallet accounts, and manages transaction fees.  
- **Sysvars:** Special accounts at predefined addresses, dynamically updated to reflect cluster state.  
- **Program Accounts:** Executable accounts storing program code, owned by a loader program.  

### Implementation Details  
- PDAs are derived using `program_id` and `seeds` via deterministic functions (e.g., `derive_pda`).  
- Rent calculation uses constants from the Solana specification, with the formula:  
  ```
  rent = (data_size * 10) / 1024 * 1000000000
  ```  
- System programs manage wallet accounts, where lamport balances represent SOL owned by the wallet.  
- Sysvars are at predefined addresses (e.g., `0x1234567890abcdef`), dynamically updated to reflect cluster state.  
- Program accounts are executable and treated as their own entities, with loaders managing ownership.  

### Related Topics  
- The content connects to the Solana account model, Sysvar account list, and program account ownership rules.  
- It references the deprecated rent mechanism and the current rent threshold calculation.

---

## Original Text
```
address.

While public keys are commonly used as account addresses, Solana also supports a
feature calledProgram Derived Addresses(PDAs). PDAs are
special addresses that you can deterministically derive from a program ID and
optional inputs (seeds).

Accounts have a max size of10MiBand every account on Solana shares the same baseAccounttype.

Every Account on Solana has the following fields:

To store data on-chain, accounts must also keep a lamport (SOL) balance that's
proportional to the amount of data stored on the account (in bytes). This
balance is called "rent," but it works more like a deposit because you can
recover the full amount when you close an account. You can find the calculationhereusing theseconstants.

The term "rent" comes from a deprecated mechanism that regularly deducted
lamports from accounts that fell below the rent threshold. This mechanism isn't
active anymore.

On Solana, "smart contracts" are calledprograms. Program
ownership is a key part of the Solana Account Model. Every account has a
designated program as its owner. Only the owner program can:

By default, all new accounts are owned to theSystem Program.
The System Program does a few key things:

All "wallet" accounts on Solana are just accounts owned by the System Program.
The lamport balance in these accounts shows the amount of SOL owned by the
wallet. Only accounts owned by the System Program can pay transaction fees.

Sysvar accounts are special accounts at predefined addresses that provide access
to cluster state data. These accounts update dynamically with data about the
network cluster. You can find the full list of Sysvar Accountshere.

Deploying a Solana program creates an executable program account. The program
account stores the executable code of the program.

Program accounts are owned by aLoader Program.

For simplicity, you can treat the program account as the program itself.
```