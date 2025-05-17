# Documentation Analysis - Chunk chunk_32.txt

## Source Context
*From: https://solana.com/*

### Document Overview  
This document explains Solana's program model, including how programs are structured, managed, and verified, with focus on their role in the network and tools for deployment and verification.  

### Key Technical Concepts  
- **Program Accounts**: Stateless accounts containing executable code, organized into functions (instructions).  
- **Upgrade Authority**: A mechanism to update programs, which becomes immutable once removed.  
- **Verifiable Builds**: A feature allowing users to verify program code against its on-chain representation using tools like the Verifiable Build CLI.  
- **Anchor Framework**: A Rust-based framework for writing Solana programs, offering reduced boilerplate code and faster development.  
- **Native Rust**: Alternative approach for writing programs without frameworks, offering flexibility but requiring more complexity.  
- **Program Management Commands**: Actions like deploy, close, redeploy, and transfer authority for programs.  

### Implementation Details  
- **Program Structure**: Programs are stateless but can create/modify other accounts (e.g., storing data).  
- **Upgrade Authority**: Users can transfer control (e.g., `transfer_authority`) to update programs.  
- **Verifiable Builds**: Uses the Solana Verifiable Build CLI (via Ellipsis Labs) to verify program code against its on-chain representation.  
- **Anchor Framework**: Includes built-in support for verifiable builds, with examples of Rust macros for simplifying code.  
- **Deployment Commands**:  
  - `deploy` to create a new program.  
  - `close` to terminate a program.  
  - `redeploy/upgrade` to replace existing programs.  
  - `transfer_authority` to change control.  

### Related Topics  
- **Solana Account Model**: Described in the document, linking to the broader account system.  
- **Verifiable Build CLI**: Connected to the document’s focus on program verification.  
- **Anchor Documentation**: Mentioned as a key resource for program development.  
- **Solana Explorer**: Referred to as a tool for searching verified programs (e.g., example link provided).

---

## Original Text
```
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
- Users can verify an on-chain program account's data matches its public source
code through verifiable builds.
- Anchor: A framework designed for Solana
program development. It provides a faster and simpler way to write programs,
using Rust macros to reduce boilerplate code. For beginners, it is recommended
to start with the Anchor framework.
- Native Rust: This approach involves writing Solana
programs in Rust without leveraging any frameworks. It offers more flexibility
but comes with increased complexity.
- Searching for Verified Programs: To quickly check for verified programs,
users can search for a program address onSolana Explorer. View an example of a verified
programhere.
- Verification Tools: TheSolana Verifiable Build CLIby Ellipsis Labs enables users to independently verify on-chain programs
against published source code.
- Support for Verifiable Builds in Anchor: Anchor provides built-in support
for verifiable builds. Details can be found in theAnchor documentation.
- Deploy a new program or buffer
- Close a program or buffer
- Redeploy / upgrade an existing program
- Transfer the authority over a program
- Finalize a program

================================================================================
Document: Solana Account Model | Solana
Source: https://solana.
```