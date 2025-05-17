# Documentation Analysis - Chunk chunk_42.txt

## Source Context
*From: https://solana.com/*

### Document Overview  
This content explains Solana's account model, detailing how data is stored in accounts with unique addresses, rent management, and the relationship between account addresses and on-chain data.  

### Key Technical Concepts  
- **Account Address**: A 32-byte unique identifier (base58 encoded) for each account.  
- **Rent**: A lamport (SOL) balance proportional to stored data, acting as a deposit to prevent arbitrary data growth.  
- **Program Derived Addresses (PDAs)**: Deterministically generated addresses from program IDs and optional seeds.  
- **BaseAccount Type**: Shared by all accounts, with a max size of 10MiB.  
- **Ed25519 Public Key**: Common address format for most accounts.  
- **System Program**: Manages account creation and data storage.  
- **Sysvar Accounts**: Manage system variables like rent, lamports, and program ownership.  

### Implementation Details  
- **Address Format**: 32-byte base58 encoded strings (e.g., `14grJpemFaf88c8tiVb77W7TYg2W3ir6pfkKz3YjhhZ5`).  
- **Rent Calculation**: Uses constants like `RENT_LAMPORTS_PER_BYTE` to determine lamport balance.  
- **PDAs**: Derived from program IDs and seeds, enabling deterministic account creation.  
- **Data Storage**: Accounts store data via buffers, program data, and sysvars, with rent managing growth.  
- **Max Account Size**: 10MiB (10,000,000 lamports).  

### Related Topics  
- **System Program**: Discusses account creation and data storage.  
- **Sysvar Accounts**: Explains system variables like rent and lamports.  
- **Rent Calculation**: Mentioned in the document context, linking to the "rent" section.

---

## Original Text
```
=====================================================
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

To store data on-chain, accounts must also keep a lamport (SOL) balance that's
proportional to the amount of data stored on the account (in bytes). This
balance is called "rent," but it works more like a deposit because you can
recover the full amount when you close an account. You can find the calculationhereusing theseconstants.

```