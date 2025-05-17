# Documentation Analysis - Chunk chunk_44.txt

## Source Context
*From: https://solana.com/*

### Document Overview  
This content explains how Solana manages program accounts, loader versions, and the storage of executable code in program data accounts, emphasizing the distinction between program state and executable code.  

### Key Technical Concepts  
- **Program Account**: A Solana account that stores a program's metadata and ownership, with the address used as the "Program ID."  
- **Loader Versions**:  
  - *Loader-v3*: Stores executable code in a separate "program data account," with the program account pointing to it.  
  - *Loader-v4*: Uses normal program accounts for buffers, but still supports temporary staging for deployment.  
- **Program Data Account**: A separate account that holds the actual executable code, distinct from the program's state.  
- **State vs. Executable Code**: Solana separates program state (data stored in accounts) from executable code (stored in program data accounts).  
- **System Program**: The only program allowed to create new accounts, which can later transfer ownership to other programs.  
- **Data Accounts**: Separate accounts for program state, distinct from program data accounts.  

### Implementation Details  
- **Loader-v3 vs. Loader-v4**:  
  - Loader-v3: Stores code in a program data account, with the program account pointing to it.  
  - Loader-v4: Uses normal program accounts for buffers, but still allows temporary staging for deployment.  
- **Account Creation**:  
  - To create a data account for a custom program, two steps are required:  
    1. Create the program data account.  
    2. Transfer ownership of the data account to the program.  
- **Transactions and Instructions**: The content connects to the "Transactions and Instructions" section, discussing how programs invoke instructions to manage accounts and state.  

### Related Topics  
- **Transactions and Instructions**: The document references this section to explain how programs interact with the Solana network.  
- **Program Accounts and Data Accounts**: The distinction between program data accounts and data accounts is clarified, linking to Solana's broader account management system.

---

## Original Text
```
account as the program itself. When
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
create new accounts. Once the System Program creates an account, it can then
transfer or assign ownership of the new account to another program.

In other words, creating a data account for a custom program takes two steps:

This account creation process is often abstracted as a single step, but it's
helpful to understand the underlying process.

Is this page helpful?

Transactions and Instructions

```