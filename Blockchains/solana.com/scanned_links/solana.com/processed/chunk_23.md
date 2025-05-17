# Documentation Analysis - Chunk chunk_23.txt

## Source Context
*From: https://solana.com/*

### Document Overview  
This content discusses Solana's blockchain technology, focusing on transaction processing, validator roles, compute budget management, and technical concepts like instruction handlers, cross-program invocations, and ledger verification.  

### Key Technical Concepts  
- **Cross-program invocation**: A mechanism for invoking functions in other programs (e.g., smart contracts) within a transaction.  
- **Instruction handlers**: Functions in programs that process transactions, specifying which accounts to read/write and additional data.  
- **Compute budget**: A limit on the amount of computation (micro-lamports) used to calculate prioritization fees for transactions.  
- **Validator state hash**: A cryptographic hash of a validator's state at a specific block height, ensuring immutability and preventing forks.  
- **Fractional native token**: A token with a value of 0.000000001 SOL (Solana's native token).  
- **Ledger verification**: The process of validating transactions and blocks, with clients, thin clients, and validators performing different levels of verification.  

### Implementation Details  
- **Micro-lamports**: Units of computation used to calculate transaction prioritization fees within the compute budget.  
- **Cross-program invocations**: Instructions that call external functions (e.g., in other programs) to process transactions, requiring at least one instruction per transaction.  
- **Compute budget**: A system where transactions consume a portion of the validator's compute budget, affecting fee prioritization.  
- **Validator state hash**: A hash of the validator's state (e.g., public key, balance, active slots) at a specific block height, used to enforce lockout periods against conflicting blocks.  

### Related Topics  
- **Validator roles**: The content connects to the broader topic of validators managing block production, ledger verification, and fork prevention.  
- **Transaction processing**: The discussion ties into Solana's transaction structure, including instruction execution and cross-program interactions.  
- **Compute budget management**: The concepts align with Solana's economic model, where compute resources are allocated to prioritize transactions.

---

## Original Text
```
fingerprint of a sequence of bytes.

An increase in token supply over time used to fund rewards for validation and to
fund continued development of Solana.

Seecross-program invocation.

A call to invoke a specificinstruction handlerin aprogram. An instruction also specifies which accounts it wants to
read or modify, and additional data that serves as auxiliary input to theinstruction handler. Aclientmust include at
least one instruction in atransaction, and all instructions
must complete for the transaction to be considered successful.

Instruction handlers areprogramfunctions that processinstructionsfromtransactions. An instruction
handler may contain one or morecross-program invocations.

Apublic keyand correspondingprivate keyfor accessing an account.

A fractionalnative tokenwith the value of 0.000000001sol.

Within the compute budget, a quantity ofmicro-lamportsis used in the calculation ofprioritization fees.

The role of avalidatorwhen it is appendingentriesto
theledger.

A sequence ofvalidatorpublic keysmapped
toslots. The cluster uses the leader schedule to determine which
validator is theleaderat any moment in time.

A list ofentriescontainingtransactionssigned byclients. Conceptually, this can be traced back to thegenesis block, but an actualvalidator's ledger
may have only newerblocksto reduce storage, as older ones are not
needed for validation of future blocks by design.

Ahashof thevalidator's stateat a giventick height. It comprises avalidator'saffirmation that ablockit has received has been verified, as well as
a promise not to vote for a conflictingblock(i.e.fork)
for a specific amount of time, thelockoutperiod.

A type ofclientthat can verify it's pointing to a validcluster. It performs more ledger verification than athin clientand less than avalidator.

Aprogramwith the ability to interpret the binary encoding of other
onchain programs.

The duration of time for which avalidatoris unable tovoteon anotherfork.

```