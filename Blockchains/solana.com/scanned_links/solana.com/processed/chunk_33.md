# Documentation Analysis - Chunk chunk_33.txt

## Source Context
*From: https://solana.com/*

### Document Overview  
This content explains Solana's account model, detailing how data is stored in "accounts" and the structure of program accounts, system programs, and data accounts, including features like Program Derived Addresses (PDAs) and rent management.  

### Key Technical Concepts  
- **Program Account**: A type of account that stores program data, with a unique 32-byte address (e.g., `14grJpemFaf88c8tiVb77W7TYg2W3ir6pfkKz3YjhhZ5`).  
- **System Program**: A built-in program responsible for managing account operations, such as rent payment and program ownership.  
- **Rent**: A fee charged to users to maintain account space, calculated based on the account's balance and the current rent epoch.  
- **Program Owner**: The account that owns a program, which is a key component of a program account.  
- **Program Derived Addresses (PDAs)**: Deterministically generated addresses from a program ID and optional seeds, allowing flexible program deployment.  
- **Account Address**: A 32-byte identifier (base58 encoded) that uniquely identifies an account.  
- **Buffer Account**: A type of account used to store data (e.g., buffer data for programs).  
- **Data Account**: A generic account type that stores arbitrary data, often used for program state or metadata.  

### Implementation Details  
- **Account Size**: Each account has a maximum size of 10 MiB.  
- **Address Format**: Addresses are 32-byte values (e.g., `14grJpemFaf88c8tiVb77W7TYg2W3ir6pfkKz3YjhhZ5`) and encoded in base58.  
- **Program Ownership**: The "Program Owner" field in a program account specifies the account that owns the program.  
- **PDAs**: PDAs are derived using the formula:  
  ```
  PDA = program_id + seeds (optional) → deterministic address  
  ```  
- **Rent Management**: The system program handles rent payments, ensuring accounts remain within their allocated space.  

### Related Topics  
- **Anchor Documentation**: The content references built-in support for verifiable builds, which is relevant to program deployment.  
- **System Program**: The document connects to the System Program section, explaining its role in managing account operations.  
- **Data Account**: The "Data Account" section is referenced, highlighting the relationship between account types and data storage.  
- **Program Account Structure**: The document ties to the "Program Account" section, detailing fields like "Buffer" and "Data" accounts.

---

## Original Text
```
built-in support
for verifiable builds. Details can be found in theAnchor documentation.
- Deploy a new program or buffer
- Close a program or buffer
- Redeploy / upgrade an existing program
- Transfer the authority over a program
- Finalize a program

================================================================================
Document: Solana Account Model | Solana
Source: https://solana.com/docs/core/accounts#program-account
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

h3: Buffer Account

h3: Program Data Account

h2: Data Account

h3: Table of Contents

On Solana, all data is stored in what are called "accounts." You can think of
data on Solana as a public database with a single "Accounts" table, where each
entry in this table is an "account." Every Solana account shares the same baseAccount type.

Every account on Solana has a unique 32-byte address, often shown as a base58
encoded string (e.g.14grJpemFaf88c8tiVb77W7TYg2W3ir6pfkKz3YjhhZ5).

The relationship between the account and its address works like a key-value
pair, where the address is the key to locate the corresponding on-chain data of
the account. The account address acts as the "unique ID" for each entry in the
"Accounts" table.

Most Solana accounts use anEd25519public key as
their address.

While public keys are commonly used as account addresses, Solana also supports a
feature calledProgram Derived Addresses(PDAs). PDAs are
special addresses that you can deterministically derive from a program ID and
optional inputs (seeds).

Accounts have a max size of10MiBand every account on Solana shares the same baseAccounttype.

Every Account on Solana has the following fields:

```