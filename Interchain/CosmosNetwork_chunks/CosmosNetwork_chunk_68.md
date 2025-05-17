## CosmosNetwork - Chunk 68

**Document Summary:**

This overview provides an excellent foundation for understanding Tendermint Core's architecture and its Application Binary Interface (ABCI). Let's break down the key components and their functionalities:

### 1. **Tendermint Core**
   - **Role**: Responsible for consensus, validation, and block propagation.
   - **Components**:
     - **Block Proposal**: Proposes new blocks based on transaction data.
     - **Commit Vote**: Collects votes from validators to finalize a block.
     - **Consensus Logic**: Implements BFT (Byzantine Fault Tolerance) logic.

### 2. **ABCI Interface**
   - **Purpose**: Allows the application logic to interact with Tendermint Core.
   - **Primary Messages**:
     - **AppendTx**: Delivers transactions for validation and inclusion in blocks.
     - **CheckTx**: Validates transactions before they are included in a block (optional).
     - **Commit**: Computes cryptographic commitments of the current state.

### 3. **Application Logic**
   - **Responsibilities**:
     - Validate and process transactions.
     - Update application state based on transaction outcomes.
     - Respond to ABCI messages with appropriate responses.
     - Handle consensus-related tasks like reorg-proposals (if necessary).

### Detailed Breakdown

#### **AppendTx Message**
- **Purpose**: Delivers a transaction for validation and inclusion in the blockchain.
- **Flow**:
  1. Tendermint Core receives a new transaction via the network.
  2. The transaction is passed to the application via `AppendTx`.
  3. Application validates the transaction against its state, protocol rules, and credentials.
  4. If valid, the application updates its internal state (e.g., UTXO database).
  5. Tendermint Core schedules the transaction for inclusion in a block.

#### **CheckTx Message**
- **Purpose**: Validates transactions before they are included in a block.
- **Flow**:
  1. Tendermint Core's mempool first checks each transaction with `CheckTx`.
  2. If the transaction passes, it is relayed to other peers for further validation.
  3. Validated transactions are then passed to application via `AppendTx` for state updates.

#### **Commit Message**
- **Purpose**: Computes a cryptographic commitment of the current application state.
- **Flow**:
  1. After processing all transactions in a block, Tendermint Core computes the commit state.
  2. This commit is signed by validators based on their voting power.
  3. The commit is then included in the next block header.

### Additional Features

#### **Validator Set Management**
- **Messages**: `BeginBlock` and `EndBlock`.
- **Purpose**:
  - `BeginBlock`: Passed to application at the start of each block, allowing it to update its state.
  - `EndBlock`: Passed after transactions have been processed, enabling finalization actions like reorg-proposal signing.

#### **Lightweight Client Support**
- **Commit Hashes**: Signed by validators, providing cryptographic proof of committed states.
- **Merkle Proofs**: Simplify verification for lightweight clients using block hashes and signed commit votes.

### Handling Byzantine Faults

1. **Forks**:
   - ≥ ⅓ Byzantine voting power can cause forks.
   - Detectable through inconsistencies in the state root, triggering social consensus mechanisms to heal the network.

2. **Censorship Attacks**:
   - > ⅔ Byzantine voting power can commit arbitrary invalid states.
   - Social consensus and legal measures are necessary for handling such failures.

3. **Reorg-Proposal Coordination**:
   - Signed by +½ of original validators, ensuring that external coordination is robust to network partitions.

### Conclusion
ABCI provides a flexible interface for integrating application logic with Tendermint Core’s consensus mechanism. By carefully validating transactions and updating state, applications can ensure consistency and reliability in blockchain operations. The ability to handle Byzantine faults through social consensus mechanisms further strengthens the overall system's resilience.

**Original Text:**

Sidechains
Sidechains [15] are a proposed mechanism for scaling the Bitcoin network via alternative blockchains that are "two-way pegged" to the Bitcoin blockchain. (Two-way pegging is equivalent to bridging. In Cosmos we say "bridging" to distinguish from market-pegging). Sidechains allow bitcoins to effectively move from the Bitcoin blockchain to the sidechain and back, and allow for experimentation in new features on the sidechain. As in the Cosmos Hub, the sidechain and Bitcoin serve as light-clients of each other, using SPV proofs to determine when coins should be transferred to the sidechain and back. Of course, since Bitcoin uses proof-of-work, sidechains centered around Bitcoin suffer from the many problems and risks of proof-of-work as a consensus mechanism. Furthermore, this is a Bitcoin-maximalist solution that doesn't natively support a variety of tokens and inter-zone network topology as Cosmos does.

---

**LLM Contextual Output:**

Based on the provided text chunk, here's a focused analysis of what this specific section is explaining:

**Exact Technical Details:**

1. **Two-way pegging:** A concept in which two blockchains are "two-way pegged" to each other, allowing bitcoins to move freely between them.
2. **SPV proofs:** Short Proof of Stake proofs, used to determine when coins should be transferred from the Bitcoin blockchain to a sidechain or vice versa.

**Contextual Connection:**

This chunk builds upon the surrounding context by explaining how Tendermint Core handles Byzantine faults and social consensus mechanisms. It provides an overview of the system's architecture, including its components (Block Proposal, Commit Vote, Consensus Logic), primary messages (AppendTx, CheckTx, Commit), responsibilities of Application Logic, and how it interacts with Tendermint Core.

**Requirements and Conditions:**

1. **Two-way pegging:** The sidechain must be "two-way pegged" to the Bitcoin blockchain for this mechanism to work.
2. **Proof-of-stake (PoS) consensus mechanism:** The system uses a PoS consensus mechanism, which is not suitable for scaling the Bitcoin network with token support.

**Additional Insights:**

1. **Token support:** This approach does not natively support a variety of tokens and inter-zone network topology as Cosmos does.
2. **Inter-chain networking:** Sidechains are designed to communicate with each other using SPV proofs, but this may require additional infrastructure and architecture beyond the current system.

Overall, this chunk provides an explanation of how Tendermint Core handles Byzantine faults and social consensus mechanisms in a Bitcoin-maximalist context, which is not suitable for scaling the network with token support.
