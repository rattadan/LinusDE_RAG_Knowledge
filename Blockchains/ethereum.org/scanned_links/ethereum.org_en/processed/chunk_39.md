# Documentation Analysis - Chunk chunk_39.txt

## Source Context
*From: https://ethereum.org/en/*

### Document Overview  
This content provides technical details about Ethereum's blockchain, including metrics like transaction volumes, network throughput, price dynamics, supply, and epoch-related data, essential for understanding the protocol's operation and performance.  

### Key Technical Concepts  
- **Block Rewards**: New ETH is created with each block via block rewards, incentivizing validators.  
- **Transactions per Second (TPS)**: The number of transactions processed per second by the network.  
- **ETH Price**: The value of 1 ETH in fiat currency (e.g., USD).  
- **Total ETH Supply**: The total amount of ETH in circulation, including new tokens generated via block rewards.  
- **Market Cap**: Calculated as price × supply, reflecting the total value of ETH in the market.  
- **Epochs**: Periods in the Ethereum consensus mechanism (PoS), with each epoch containing slots, attestations, and validator activities.  
- **Slots**: Units of time in an epoch, each containing one valid block.  
- **Validators**: Active validators staking ETH to propose blocks and attest to their validity.  
- **Attestations**: Votes for blocks in slots, requiring stake to be validated.  
- **Deposits**: ETH staked by validators to become validators, tied to their slot participation.  
- **Slashings**: Penalties imposed on proposers or attestors for malicious behavior.  

### Implementation Details  
- **Market Cap Calculation**: Price × supply (current ETH price × total circulating supply).  
- **Epoch Metrics**:  
  - **Epoch Number**: Unique identifier for each epoch.  
  - **Finalized Status**: Tracks whether an epoch is finalized (Yes/No).  
  - **Slots**: Each slot includes one valid block with a specific timestamp and proposer.  
  - **Attestations**: Count of votes for blocks in slots, linked to validator staked ETH.  
  - **Deposits**: Number of ETH staked by validators during the epoch.  
  - **Slashings**: Number of penalties imposed for malicious behavior (e.g., block or attestation fraud).  
- **Technical Parameters**:  
  - **Block Roots**: Hash-tree-roots of BeaconBlocks (e.g., `BlockRoot`, `ParentRoot`, `StateRoot`).  
  - **Randao Reveal**: Secret used to determine slot proposers.  
  - **Graffiti**: Optional 32-byte message included in block proposals.  
  - **Execution Data**: Hashes of blocks, deposits, and deposit roots.  

### Related Topics  
- **Ethereum Consensus Mechanism**: Linked to the PoS (Proof of Stake) system, where validators stake ETH to validate blocks.  
- **Validator Roles**: Connected to the concepts of deposits, slashes, and attestations.  
- **Epoch Data**: Integrated with the Ethereum blockchain's architecture, affecting network throughput and security.  
- **Protocol Specifications**: Tied to the technical details of Ethereum's blockchain, such as hash-tree proofs and state transitions.

---

## Original Text
```
- The number of transactions since Ethereum was created
- Transactions per second - The number of transactions processable within a second
- ETH price - The current valuations of 1 ETH
- Total ETH supply - Number of ETH in circulationremember new ETH is created with the creation of every block in the form of block rewards
- Market cap - Calculation of price*supply
- Epoch number
- Finalized status- Whether the epoch has been finalized (Yes/No)
- Time - The time the epoch ended
- Attestations - The number of attestations in the epoch (votes for blocks within slots)
- Deposits - The number of ETH deposits included in the epoch (validators must stake ETH to become validators)
- Slashings - Number of penalties given to proposers of blocks or attestors
- Voting participation - The amount of staked ETH used to attest blocks
- Validators - Number of validators active for the epoch
- Average Validator balance - Average balance for active validators
- Slots - Number of slots included in the epoch (slots include one valid block)
- Epoch - The epoch in which the slot is valid
- Slot number
- Status - The status of the slot (Proposed/Missed)
- Time - The slot timestamp
- Proposer - The validator that proposed the block for the slot
- Block root - The hash-tree-root of the BeaconBlock
- Parent root - The hash of the block that came before
- State root - The hash-tree-root of the BeaconState
- Randao reveal
- Graffiti - A block proposer can include 32 byte long message to its block proposal
- Execution DataBlock hashDeposit countDeposit root
- Deposit count
- Deposit root
- Attestations - Number of attestations for the block in this slot
- Deposits - The number of deposits during this slot
- Voluntary exits - The number of validators that left during the slot
- Slashings - Number of penalties given to proposers of blocks or attestors
- Votes - The validators that voted for the block in this slot
- Proposer - The validator that was algorithmically chosen to propose the new block
-
```