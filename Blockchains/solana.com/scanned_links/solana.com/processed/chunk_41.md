# Documentation Analysis - Chunk chunk_41.txt

## Source Context
*From: https://solana.com/*

### Document Overview  
This content discusses the Solana Account Model, focusing on program accounts, system programs, rent, and the process of deploying/upgrading programs. It also covers transaction fees, program derivation, and verification tools.  

### Key Technical Concepts  
- **Program Derived Address**: Programs are stateless but can create/modify other accounts to store data.  
- **Rent**: A fee charged for using an account, managed by the system program.  
- **Program Owner**: The authority that can update or redeploy a program.  
- **System Program**: A built-in program responsible for managing account states, rent, and other system-level functions.  
- **Sysvar Accounts**: Accounts that manage system-wide variables (e.g., rent, clock).  
- **Program Account**: An account that stores executable code (programs) and their associated data.  
- **Verifiable Builds**: Tools to verify program code against on-chain data, enabling trust in deployed programs.  

### Implementation Details  
- **Program Structure**: Programs are written in Rust, with instructions (functions) stored in the program account.  
- **Rent Management**: The system program calculates and charges rent based on the account’s usage.  
- **Authority Management**: Programs can be upgraded by transferring ownership to a new authority.  
- **Verification Tools**: The Solana Verifiable Build CLI allows users to audit programs against published source code.  
- **Deployment Process**: Users can deploy new programs, close buffers, or redeploy/upgrade existing ones via the Solana Explorer or CLI.  

### Related Topics  
- **Solana Explorer**: Used to search for verified programs and view program addresses.  
- **Anchor Framework**: A Rust-based tool for simplifying program development with macros.  
- **Verifiable Builds**: Key to ensuring program integrity and trust in on-chain data.  
- **System Program**: Central to managing account states and rent, linked to the Solana Account Model.

---

## Original Text
```
validator code.

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
Source: https://solana.com/docs/core/accounts#system-program
================================================================================

h1: Solana Account Model

h2: Key Points

h2: Account

h3: Account Type

h3: Rent

h3: Program Owner

h2: System Program

h2: Sysvar Accounts

h2: Program Account

```