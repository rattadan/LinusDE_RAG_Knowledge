# Documentation Analysis - Chunk chunk_35.txt

## Source Context
*From: https://solana.com/*

### Document Overview  
This content explains Solana's program account structure, loader versions, and how executable code is stored and managed in the network.  

### Key Technical Concepts  
- **Program Account**: A Solana account that stores the executable code of a deployed program.  
- **Loader Version**: Different versions of the loader (e.g., loader-v3, loader-v4) handle code storage differently, with loader-v3 using a separate "program data account" for code.  
- **Program Data Account**: A special account that stores the actual executable code, while the program account only holds its address.  
- **System Program**: The only account capable of creating new accounts on Solana.  
- **Instructions**: Programs define instructions to create separate accounts for state storage.  

### Implementation Details  
- **Code Storage**:  
  - Loader-v3 stores executable code in a separate "program data account," with the program account pointing to it.  
  - Loader-v4 uses normal program accounts for buffers, but they are still treated as program accounts.  
- **Loader Versioning**:  
  - The Solana CLI defaults to the latest loader version (e.g., loader-v4) when deploying new programs.  
- **Program Account Behavior**:  
  - Program accounts are owned by a loader program (e.g., the System Program for loader-v3).  
  - Programs invoke instructions by specifying the program account's address (Program ID).  

### Related Topics  
- **Data Accounts**: The distinction between program data accounts and data accounts (e.g., the note about not confusing them).  
- **System Program**: The role of the System Program in creating new accounts.  
- **Instructions**: How programs define and invoke instructions to manage state.

---

## Original Text
```
to cluster state data. These accounts update dynamically with data about the
network cluster. You can find the full list of Sysvar Accountshere.

Deploying a Solana program creates an executable program account. The program
account stores the executable code of the program.

Program accounts are owned by aLoader Program.

For simplicity, you can treat the program account as the program itself. When
you invoke a program's instructions, you specify the program account's address
(commonly called the "Program ID").

When you deploy a Solana program, it's stored in a program account. Program
accounts are owned by aLoader Program.
There are several versions of the loader, but all except loader-v3 store the
executable code directly in the program account. Loader-v3 stores the executable
code in a separate "program data account" and the program account just points to
it. When you deploy a new program, the Solana CLI uses the latest loader version
by default.

Loader-v3 has a special account type for temporarily staging the upload of a
program during deployment or redeployment/upgrades. In loader-v4, there are
still buffers, but they're just normal program accounts.

Loader-v3 works differently from all other BPF Loader programs. The program
account only contains the address of a program data account, which stores the
actual executable code:Program Data Account

Don't confuse these program data accounts with the data accounts of programs
(see below).

On Solana, the executable code of a program is stored in a different account
than the program's state. This is like how operating systems typically have
separate files for programs and their data.

To maintain state, programs define instructions to create separate accounts that
they own. Each of these accounts has its own unique address and can store any
arbitrary data defined by the program.

Note that only theSystem Programcan
create new accounts.
```