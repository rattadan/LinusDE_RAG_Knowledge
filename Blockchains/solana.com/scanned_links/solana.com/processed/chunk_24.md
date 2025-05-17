# Documentation Analysis - Chunk chunk_24.txt

## Source Context
*From: https://solana.com/*

### Document Overview  
This content discusses Solana's blockchain technology, focusing on validators, transaction structures, decentralization metrics (e.g., Nakamoto Coefficient), and technical concepts like lockout periods, proof of history, and onchain programs.  

### Key Technical Concepts  
- **Validator**: A node in a cluster responsible for validating transactions and voting on forks, with a lockout period to prevent conflicting votes.  
- **Transaction Message**: Structured data containing headers, account addresses, block hashes, and instructions, essential for ledger verification.  
- **Lockout Period**: A time window during which validators cannot vote on forks, ensuring consensus stability.  
- **Nakamoto Coefficient**: A metric for decentralization, measuring the minimum number of nodes needed to disrupt a blockchain.  
- **Onchain Program**: A self-executing smart contract on Solana, governed by a public key and executed via instructions.  
- **Proof of History (PoH)**: A consensus mechanism that ensures sequential transaction ordering, verified in less time than production.  
- **Cluster**: A group of validators working together to maintain blockchain integrity.  
- **Reward Credit**: Weighted points in a rewards system, calculated as votes × lamports staked.  

### Implementation Details  
- **Lockout Period**: Validators are temporarily blocked from voting on forks for a specified duration (e.g., 30 minutes).  
- **Transaction Structure**: Includes a header, array of account addresses, recent block hash, and instructions, with instructions stored as binary data.  
- **Nakamoto Coefficient**: Calculated as the smallest number of nodes required to disrupt a blockchain, derived from validator participation and network topology.  
- **Onchain Programs**: Executable code (e.g., `wasm`) that modifies accounts via instructions, stored in the cluster’s memory.  
- **Proof of History**: A stack of proofs (e.g., timestamps, data sequences) verified in O(1) time, ensuring transaction order.  

### Related Topics  
- **Proof of History**: Mentioned in the context of transaction verification and consensus.  
- **Onchain Programs**: Linked to the description of validators and transaction structures.  
- **Decentralization Metrics**: The Nakamoto Coefficient is discussed alongside validator cluster dynamics.

---

## Original Text
```
not to vote for a conflictingblock(i.e.fork)
for a specific amount of time, thelockoutperiod.

A type ofclientthat can verify it's pointing to a validcluster. It performs more ledger verification than athin clientand less than avalidator.

Aprogramwith the ability to interpret the binary encoding of other
onchain programs.

The duration of time for which avalidatoris unable tovoteon anotherfork.

The structured contents of atransaction. Generally containing a
header, array of account addresses, recentblockhash, and an array
ofinstructions.

Learn more about themessage formatting inside of transactionshere.

A measure of decentralization, the Nakamoto Coefficient is the smallest number
of independent entities that can act collectively to shut down a blockchain. The
term was coined by Balaji S. Srinivasan and Leland Lee inQuantifying Decentralization.

Thetokenused to track work done bynodesin a cluster.

A computer participating in acluster.

The number ofvalidatorsparticipating in acluster.

The executable code on Solana blockchain that interprets theinstructionssent inside of eachtransactionto
read and modify accounts over which it has control. These programs are often
referred to as "smart contracts" on other
blockchains.

SeeProof of History.

A weightedcreditin a rewards regime. In thevalidatorrewards regime,
the number of points owed to astakeduring redemption is the product
of thevote creditsearned and the number of lamports staked.

The private key of akeypair.

Seeonchain program.

An account whose signing authority is a program and thus is not controlled by a
private key like other accounts.

The public key of theaccountcontaining aprogram.

A stack of proofs, each of which proves that some data existed before the proof
was created and that a precise duration of time passed before the previous
proof. Like aVDF, a Proof of History can be
verified in less time than it took to produce.

```