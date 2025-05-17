# Documentation Analysis - Chunk chunk_21.txt

## Source Context
*From: https://solana.com/*

### Document Overview  
This content explains the structure of Solana's ledger, including accounts, programs, validators, block mechanics, and related technical concepts.  

### Key Technical Concepts  
- **Account**: A Solana account holds lamports (the smallest unit of Solana) and can own programs.  
- **Public Key**: A unique identifier for an account, used to address programs or users.  
- **Program**: A self-contained executable on the ledger, owned by an account and capable of interacting with the runtime.  
- **Block**: A unit of data in the ledger, containing transactions, validators, and block hashes.  
- **Block Hash**: A cryptographic hash of the block’s data, computed from the last entry in the block.  
- **Compute Units**: The maximum computational resources a transaction can consume.  
- **Epoch**: A period during which validators are deactivated and gradually reactivated.  
- **Gossip Network**: A decentralized communication system connecting nodes in a Solana cluster.  

### Implementation Details  
- **Block Hash Calculation**: Solana computes block hashes from the last entry ID of the block.  
- **Account Structure**: Accounts hold lamports and programs, with programs using BPF (Berkeley Packet Filter) for runtime interaction.  
- **Compute Units**: Transactions are limited to a maximum of 256 compute units per transaction.  
- **Epoch Management**: Validators are deactivated for a specified number of epochs and reactivated gradually.  
- **Gossip Network**: Nodes communicate via a gossip protocol to propagate block updates.  

### Related Topics  
- **Solana Programming Model**: Details about programs, BPF, and the runtime.  
- **Consensus Mechanism**: Overview of validators, block validation, and the Proof of Stake (PoS) system.  
- **Network Architecture**: Description of the Solana cluster, gossip, and node interactions.

---

## Original Text
```
ledger that either holds data or is an executable
program.

Like an account at a traditional bank, a Solana account may hold funds calledlamports. Like a file in Linux, it is addressable by a key, often
referred to as apublic keyor pubkey.

The key may be one of:

The address of the program that owns the account. Only the owning program is
capable of modifying the account.

See alsoauthority.

A front-end application that interacts with a Solana cluster.

The address of a user that has some kind of permission over an account.

The result of interpreting all programs on the ledger at a giventick height. It includes at least the set of allaccountsholding nonzeronative tokens.

A contiguous set ofentrieson the ledger covered by avote. Aleaderproduces at most one block perslot.

A unique value (hash) that identifies a record (block). Solana computes
a blockhash from the lastentry idof the block.

The number ofblocksbeneath the current block. The first block after
thegenesis blockhas height one.

Thevalidatorthat produces the genesis (first)blockof
a block chain.

The Solana program that owns and loadsBPFonchain programs, allowing the program to interface with the
runtime.

A computer program that accesses the Solana server networkcluster.

A measure of the network confirmation for theblock.

A set ofvalidatorsmaintaining a singleledger.

The maximum number ofcompute unitsconsumed per transaction.

The smallest unit of measure for consumption of computational resources of the
blockchain.

The wallclock duration between aleadercreating atick entryand creating aconfirmed block.

Ablockthat has received asuper majorityofledger votes.

A gossip network connecting allnodesof acluster.

Some number ofepochsafterstakehas been deactivated while
it progressively becomes available for withdrawal. During this period, the stake
is considered to be "deactivating". More info about:warmup and cooldown

A call from oneonchain programto another.
```