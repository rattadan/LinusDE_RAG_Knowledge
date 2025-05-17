# Documentation Analysis - Chunk chunk_9.txt

## Source Context
*From: https://solana.com/*

### Document Overview  
This content explains the common JSON data structures returned by Solana RPC methods, including transactions, inner instructions, and token balances, with details on their structure and usage.  

### Key Technical Concepts  
- **Transactions**: Structured JSON objects with fields like `dataSize` and account instructions.  
- **Inner Instructions**: Lists of objects representing cross-program instructions executed during transactions.  
- **Token Balances**: Arrays of objects tracking token balances for accounts.  
- **Data Size Comparison**: `dataSize` field in transactions compares the actual data length of an account with the provided size.  
- **Base64 Support**: Availability restricted to solana-core v1.14.0 or newer.  

### Implementation Details  
- **Transaction Structure**:  
  - `dataSize`: `u64` field comparing account data length to provided size.  
  - Example: `{"dataSize": 123}`.  
- **Inner Instructions**:  
  - Defined as a list of objects with fields like `programId`, `data`, and `accounts`.  
- **Token Balances**:  
  - Each object includes `accountAddress`, `tokenAccount`, and `balance`.  
- **Base64 Support**:  
  - Only available in solana-core v1.14.0 or newer; omitted in older versions.  

### Related Topics  
- **Anatomy of a Transaction**: Explains transaction structure in detail.  
- **Solana RPC Methods**: Overview of all RPC methods and their JSON structures.  
- **Solana Core Versioning**: Notes on compatibility with solana-core versions.

---

## Original Text
```
and base64 support generally, is only available in
solana-core v1.14.0 or newer. Please omit when querying nodes on earlier
versions
- dataSize: u64- compares the program account data length with the provided
data size

================================================================================
Document: Common JSON Data Structures for Solana RPC Methods | Solana
Source: https://solana.com/docs/rpc/json-structures
================================================================================

h1: Common JSON Data Structures for Solana RPC Methods

h2: Transactions

h3: JSON

h3: Reference

h3: JSON Parsed

h3: Reference

h2: Transaction Status Metadata

h3: Reference

h2: Inner Instructions

h3: Reference

h2: Token Balances

h3: Reference

h3: Table of Contents

Various Solana RPC methods will return more complex responses as structured JSON
objects, filled with specific keyed values.

The most common of these JSON data structures include:

Transactions are quite different from those on other blockchains. Be sure to
reviewAnatomy of a Transactionto learn about
transactions on Solana.

The JSON structure of a transaction is defined as follows:

The JSON parsed structure of a transaction follows a similar structure to the
regular JSON format, with additional parsing of account and instruction
information:

The Solana runtime records the cross-program instructions that are invoked
during transaction processing and makes these available for greater transparency
of what was executed on-chain per transaction instruction. Invoked instructions
are grouped by the originating transaction instruction and are listed in order
of processing.

The JSON structure of inner instructions is defined as a list of objects in the
following structure:

The JSON structure of token balances is defined as a list of objects in the
following structure:

Is this page helpful?

Solana RPC Methods

```