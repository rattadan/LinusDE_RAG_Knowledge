# Documentation Analysis - Chunk chunk_19.txt

## Source Context
*From: https://solana.com/*

### Document Overview  
This document lists technical terminology related to Solana's blockchain, including concepts like accounts, authorities, transactions, and data structures, providing definitions and context for their use in the Solana network.

### Key Technical Concepts  
- **Account**: A data structure in Solana that contains information about a user or program.  
- **Owner**: The public key of the account's owner, determining permissions.  
- **Program**: A self-contained executable code unit in Solana.  
- **Authority**: A permission level (e.g., owner, signer) required to execute instructions.  
- **Transaction**: A message sent from an account to another, including data, signatures, and fees.  
- **Instruction**: A unit of work in a program, executed by a runtime.  
- **Data Plane**: The part of a transaction that contains the actual data (e.g., token balances).  
- **Compute Budget**: Resources allocated for executing instructions.  

### Implementation Details  
The document outlines technical terms and their definitions, such as:  
- **accountIndex**: An index into the `message.accountKeys` array specifying which account to use.  
- **mint**: A public key of a token's mint, defining its supply and decimals.  
- **owner**: The public key of the token's owner, determining token balances.  
- **programId**: The public key of the token program, responsible for managing tokens.  
- **uiAmount**: A float representing token amounts, accounting for decimals, with deprecated string alternatives.  

### Related Topics  
The terminology here connects to Solana’s broader documentation, such as:  
- **Transaction ID** (linked to the "Transaction ID" section in the Solana docs).  
- **Block** and **compute budget** concepts.  
- **Instruction** and **inner instruction** in the same document.

---

## Original Text
```
<array[number]>- List of ordered indices into themessage.accountKeysarray indicating which accounts to pass to the
program.
- data: <string>- The program input data encoded in a base-58 string.
- accountIndex: <number>- Index of the account in which the token balance is
provided for.
- mint: <string>- Pubkey of the token's mint.
- owner: <string|undefined>- Pubkey of token balance's owner.
- programId: <string|undefined>- Pubkey of the Token program that owns the
account.
- uiTokenAmount: <object>-amount: <string>- Raw amount of tokens as a string, ignoring decimals.decimals: <number>- Number of decimals configured for token's mint.uiAmount: <number|null>- Token amount as a float, accounting for
decimals.DEPRECATEDuiAmountString: <string>- Token amount as a string, accounting for
decimals.
- amount: <string>- Raw amount of tokens as a string, ignoring decimals.
- decimals: <number>- Number of decimals configured for token's mint.
- uiAmount: <number|null>- Token amount as a float, accounting for
decimals.DEPRECATED
- uiAmountString: <string>- Token amount as a string, accounting for
decimals.

================================================================================
Document: Terminology | Solana
Source: https://solana.com/docs/references/terminology#transaction-id
================================================================================

h1: Terminology

h2: account

h2: account owner

h2: app

h2: authority

h2: bank state

h2: block

h2: blockhash

h2: block height

h2: bootstrap validator

h2: BPF loader

h2: client

h2: commitment

h2: cluster

h2: compute budget

h2: compute units

h2: confirmation time

h2: confirmed block

h2: control plane

h2: cooldown period

h2: credit

h2: cross-program invocation (CPI)

h2: data plane

h2: drone

h2: entry

h2: entry id

h2: epoch

h2: fee account

h2: finality

h2: fork

h2: genesis block

h2: genesis config

h2: hash

h2: inflation

h2: inner instruction

h2: instruction

h2: instruction handler

```