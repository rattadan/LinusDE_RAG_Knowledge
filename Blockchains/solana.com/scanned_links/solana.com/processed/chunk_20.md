# Documentation Analysis - Chunk chunk_20.txt

## Source Context
*From: https://solana.com/*

### Document Overview  
This content covers technical terms and concepts related to Solana's blockchain infrastructure, including accounts, transactions, programs, consensus mechanisms, and related features like PoH (Proof of History), CPI (Cross-Program Invocation), and slot management.

---

### Key Technical Concepts  
1. **Account**: A ledger record that holds data or executable programs (like a Solana account).  
2. **Lamport**: Solana's native token unit, used to represent value in accounts.  
3. **Instruction**: A unit of execution in Solana programs, requiring a fee (e.g., `rent` or `prioritization fee`).  
4. **Program**: A self-contained executable code unit that can be deployed on the Solana network.  
5. **PoH (Proof of History)**: A consensus mechanism that ensures sequential transaction order using a time-based hash.  
6. **CPI (Cross-Program Invocation)**: A mechanism allowing programs to call functions in other programs.  
7. **Slot**: A unit of time in the Solana consensus process, used for transaction ordering.  
8. **Transaction**: A message sent to the Solana network, validated and processed by validators.  
9. **Validator**: A node in the Solana network responsible for validating transactions and maintaining consensus.  
10. **Rent**: A fee paid to reserve system resources (e.g., memory) for program execution.  

---

### Implementation Details  
- **Account Structure**: Solana accounts are stored in a trie (hash tree) and managed via public keys.  
- **PoH Implementation**: Uses a time-based hash (e.g., `hash(λ)`), where `λ` is a counter incremented by 1 per slot.  
- **CPI Mechanism**: Programs can call external functions via `CPI`, requiring a `system_program` instruction to encode the call.  
- **Slot Management**: Transactions are grouped into slots, and validators use PoH to ensure sequential order.  
- **Fee Accounts**: Programs use `fee_account` to pay for transaction costs (e.g., `rent` or `prioritization fee`).  

---

### Related Topics  
- **PoH** is linked to the **slot** and **finality** sections.  
- **CPI** is part of the **programmatic interface** and connects to **entry** and **transaction** sections.  
- **Accounts** and **instructions** are foundational to the **program** and **transaction** sections.  
- The **Table of Contents** references these terms, emphasizing their role in Solana’s consensus and execution layers.

---

## Original Text
```
compute budget

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

h2: keypair

h2: lamport

h2: leader

h2: leader schedule

h2: ledger

h2: ledger vote

h2: light client

h2: loader

h2: lockout

h2: message

h2: Nakamoto coefficient

h2: native token

h2: node

h2: node count

h2: onchain program

h2: PoH

h2: point

h2: private key

h2: program

h2: program derived account (PDA)

h2: program id

h2: proof of history (PoH)

h2: prioritization fee

h2: public key (pubkey)

h2: rent

h2: rent exempt

h2: root

h2: runtime

h2: Sealevel

h2: shred

h2: signature

h2: skip rate

h2: skipped slot

h2: slot

h2: smart contract

h2: SOL

h2: Solana Program Library (SPL)

h2: stake

h2: stake-weighted quality of service (SWQoS)

h2: supermajority

h2: sysvar

h2: thin client

h2: tick

h2: tick height

h2: token

h2: Token Extensions Program

h2: token mint

h2: Token Program

h2: tps

h2: tpu

h2: transaction

h2: transaction id

h2: transaction confirmations

h2: transactions entry

h2: tvu

h2: validator

h2: VDF

h2: verifiable delay function (VDF)

h2: vote

h2: vote credit

h2: wallet

h2: warmup period

h3: Table of Contents

The following terms are used throughout the Solana documentation and development
ecosystem.

A record in the Solana ledger that either holds data or is an executable
program.

Like an account at a traditional bank, a Solana account may hold funds calledlamports. Like a file in Linux, it is addressable by a key, often
referred to as apublic keyor pubkey.

The key may be one of:

The address of the program that owns the account. Only the owning program is
capable of modifying the account.

See alsoauthority.

```