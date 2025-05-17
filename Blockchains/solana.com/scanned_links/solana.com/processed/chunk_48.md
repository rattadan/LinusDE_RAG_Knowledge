# Documentation Analysis - Chunk chunk_48.txt

## Source Context
*From: https://solana.com/*

### Document Overview  
The content explains the structure of Solana transactions, the building of instructions, and the use of compact arrays to optimize transaction sizes.  

### Key Technical Concepts  
- **Transaction Message**: A structured format containing message headers, account addresses, and compact arrays.  
- **Compact Array Format**: A method to encode account addresses and instructions efficiently by storing lengths in the array.  
- **Instruction**: A public function in a Solana program, requiring account addresses and privileges for execution.  
- **Transaction Size Limit**: 1232 bytes (MTU 1280 bytes minus 48 bytes for network headers).  
- **Account Privileges**: Defined by the message header to specify which accounts can access resources.  

### Implementation Details  
- **Instruction Building**: Requires specifying accounts (via `AccountMeta`) and their roles (read/write).  
- **Compact Array Format**: Uses a compact array (e.g., `u8[3]` for account privileges) to store lengths of account addresses and instruction arrays.  
- **Transaction Structure**: Includes a message header (3 bytes for privileges) and a compact array (e.g., `u8[3]` for account addresses).  
- **Size Limit**: Transactions must stay under 1232 bytes, including signatures and message data.  

### Related Topics  
- **Transaction Message**: Details the structure of Solana transactions.  
- **Instructiontab**: Functionally equivalent to the "Expanded Instructiontab" for instruction definitions.  
- **Account Metas**: Required for specifying which accounts an instruction reads/write.

---

## Original Text
```
instructions.
If a library isn't available, you can manually build the instruction. This
requires you to know the implementation details of the instruction.

The examples below show how to manually build the transfer instruction. TheExpanded Instructiontab is functionally equivalent to theInstructiontab.

In the sections below, we'll walk through the details of transactions and
instructions.

Aninstructionon a Solanaprogramcan be thought of as
a public function that can be called by anyone using the Solana network.

Invoking a program's instruction requires three key pieces of information:

Transaction Instruction

Each account required by an instruction must be provided as anAccountMetathat contains:

By specifying up front which accounts an instruction reads or writes,
transactions that don't modify the same accounts can execute in parallel.

Run the examples below to see the structure of a SOL transfer instruction.

The following examples show the output from the previous code snippets. The
exact format differs depending on the SDK, but every Solana instruction requires
the following information:

A Solanatransactionconsists of:

Transaction Format

The structure of a transaction message consists of:

Transaction Message

Solana transactions have a size limit of1232bytes. This limit comes from the IPv6 Maximum Transmission Unit (MTU) size of
1280 bytes, minus 48 bytes for network headers (40 bytes IPv6 + 8 bytes fragment
header).

A transaction's total size (signatures and message) must stay under this limit
and includes:

Transaction Format

Themessage headeruses three bytes to define account privileges.

A compact array in a transaction message is an array serialized in the following
format:

Compact array format

This format is used to encode the lengths of theAccount AddressesandInstructionsarrays in
transaction messages.

A transaction message contains an array ofaccount addressesrequired by its instructions.
```