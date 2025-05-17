# Documentation Analysis - Chunk chunk_47.txt

## Source Context
*From: https://solana.com/*

### Document Overview  
This content explains Solana's transaction structure, including how instructions are processed, the role of the System Program, and the steps involved in transferring SOL between accounts.  

### Key Technical Concepts  
- **Transactions**: Requests to execute one or more instructions on the Solana network.  
- **Instructions**: Operations (e.g., transferring SOL) defined by programs deployed to the network.  
- **Programs**: Self-contained logic that defines instructions for specific tasks.  
- **System Program**: Manages account balances and transaction processing (e.g., deducting lamports from sender accounts).  
- **Wallets**: Solana accounts owned by the System Program; only the program owner can modify their data.  
- **is_signer/is_writable**: Flags indicating whether an account can sign transactions or modify balances.  
- **Lamports**: Solana's native cryptocurrency unit (1 lamport = 1 SOL).  
- **Transaction Processing**: The System Program executes instructions, updates balances, and handles account permissions.  

### Implementation Details  
- **Instruction Building**: Client libraries abstract instruction creation; manual building requires knowledge of the instruction's implementation details.  
- **Transfer Process**: A transfer instruction (e.g., `transfer`) involves signing the transaction, invoking the System Program, and updating sender/recipient balances.  
- **Expanded Instruction Tab**: Functionally equivalent to the `Instruction` tab for visualizing instruction details.  
- **Manual Instruction Examples**: Demonstrated in the document, requiring understanding of program logic and lamport values.  

### Related Topics  
- **Program Execution**: Linked to the section on instructions and program logic.  
- **System Program**: Connected to the explanation of account balance management.  
- **Transaction Signing**: Related to the concept of `is_signer` and `is_writable` flags.  
- **Client Libraries**: Mentioned as tools for abstracting instruction-building complexity.

---

## Original Text
```
Transaction Structure

h3: Table of Contents

On Solana, users sendtransactionsto
interact with the network. Transactions contain one or moreinstructionsthat specify operations to
process. The execution logic for instructions are stored onprogramsdeployed to the Solana network, where each
program defines its own set of instructions.

Below are key details about Solana transaction processing:

A transaction is essentially a request to process one or more instructions.

Transaction Simplified

A transaction is like an envelope containing forms. Each form is an instruction
that tells the network what to do. Sending the transaction is like mailing the
envelope to get the forms processed.

The diagram below represents a transaction with a single instruction to transfer
SOL from a sender to a receiver.

On Solana, "wallets" are accounts owned by theSystem Program. Only the program owner can
change an account's data, so transferring SOL requires sending a transaction to
invoke the System Program.

The sender account must sign (is_signer) the transaction to let the System
Program deduct its lamport balance. The sender and recipient accounts must be
writable (is_writable) since their lamport balances change.

After sending the transaction, the System Program processes the transfer
instruction. The System Program then updates the lamport balances of both the
sender and recipient accounts.

SOL Transfer Process

The examples below show how to send a transaction that transfers SOL from one
account to another.

Client libraries often abstract the details for building program instructions.
If a library isn't available, you can manually build the instruction. This
requires you to know the implementation details of the instruction.

The examples below show how to manually build the transfer instruction. TheExpanded Instructiontab is functionally equivalent to theInstructiontab.

In the sections below, we'll walk through the details of transactions and
instructions.

```