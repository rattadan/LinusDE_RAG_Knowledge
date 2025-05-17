# Documentation Analysis - Chunk chunk_49.txt

## Source Context
*From: https://solana.com/*

### Document Overview  
This content explains the transaction format on Solana, focusing on compact arrays for account addresses and instructions, blockhash expiration, and message structure details.  

### Key Technical Concepts  
- **Compact array format**: A compact encoding method for lengths of account addresses and instructions in transaction messages.  
- **Blockhash expiration**: A blockhash expires after 150 blocks (1 minute) to prevent invalid transactions.  
- **Transaction message structure**: Includes `header`, `accountKeys`, and `CompiledInstruction` for instructions.  
- **Privilege ordering**: Account addresses are ordered by their privileges as defined in the message header.  

### Implementation Details  
- **Compact-u16**: Used to encode the number of account addresses in a transaction.  
- **Blockhash expiration**: A blockhash is valid for 150 blocks (1 minute) based on 400ms block times.  
- **Transaction response fields**: Includes `header` (privileges and signer addresses) and `accountKeys` (list of instruction accounts).  
- **Instructions**: Converted to `CompiledInstruction` type, with each instruction containing serialized data.  
- **Example usage**: The `getLatestBlockhash` RPC method retrieves the current blockhash and its validity period.  

### Related Topics  
- **SDK examples**: Transaction message outputs vary by SDK but include the same structure.  
- **Transaction response**: Fetches `header` and `accountKeys` after a transaction is signed and broadcasted.  
- **Blockhash lifecycle**: Expiration time and retrieval via `getLatestBlockhash` are critical for transaction validation.

---

## Original Text
```

Transaction Format

Themessage headeruses three bytes to define account privileges.

A compact array in a transaction message is an array serialized in the following
format:

Compact array format

This format is used to encode the lengths of theAccount AddressesandInstructionsarrays in
transaction messages.

A transaction message contains an array ofaccount addressesrequired by its instructions. The array starts with acompact-u16number indicating
how many addresses it contains. The addresses are then ordered by their
privileges, as determined by the message header.

Compact array of account addresses

Every transaction requires arecent blockhashthat serves two purposes:

A blockhash expires after150blocks (about 1 minute assuming 400ms block times), after which the transaction
cannot be processed.

You can use thegetLatestBlockhashRPC
method to get the current blockhash and last block height at which the blockhash
will be valid. Here is an example onSolana Playground.

A transaction message contains an array ofinstructionsin theCompiledInstructiontype. Instructions are converted to this type when added to a transaction.

Like the account addresses array in the message, it starts with acompact-u16length followed by
the instruction data. Each instruction contains:

Compact array of Instructions

Run the examples below to see the structure of a transaction with a single SOL
transfer instruction.

The following examples show the transaction message output from the previous
code snippets. The exact format differs depending on the SDK, but includes the
same information.

When you fetch a transaction using its signature after sending it to the
network, you'll receive a response with the following structure.

Themessagefield contains the following fields:

header: Specifies read/write and signer privileges for addresses in theaccountKeysarray

accountKeys: Array of all account addresses used in the transaction's
instructions

```