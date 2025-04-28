## CosmosNetwork - Chunk 60

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

If a network partition or offline nodes is the reason why block N hasn't committed, then N+i won't commit anyway. In addition, the batching of transactions into blocks allows for regular Merkle-hashing of the application state, rather than periodic digests as with PBFT's checkpointing scheme. This allows for faster provable transaction commits for light-clients and faster inter-blockchain communication. Tendermint Core also includes many optimizations and features that go above and beyond what is specified in PBFT. For example, the blocks proposed by validators are split into parts, Merkle-ized, and gossipped in such a way that improves broadcasting performance (see LibSwift [19] for inspiration). Also, Tendermint Core doesn't make any assumption about point-to-point connectivity, and functions for as long as the P2P network is weakly connected.

---

**LLM Contextual Output:**

This text chunk provides detailed technical specifications of Tendermint Core's architecture and its Application Binary Interface (ABCI) interface. Here's a focused analysis:

**Technical Details:**

1. **Block Proposal**: Tendermint Core proposes new blocks based on transaction data, which are then voted on by validators.
2. **Commit Vote**: Validators collect votes to finalize a block, ensuring consensus among all validators.
3. **Consensus Logic**: The consensus logic implements Byzantine Fault Tolerance (BFT) logic, which allows the network to withstand failures and partitions.

**Connection to surrounding context:**

This chunk builds upon the provided overview of Tendermint Core's architecture and its Application Binary Interface (ABCI). It explains how Tendermint Core handles block proposals, votes, and consensus in more detail. The text also discusses Byzantine Fault Tolerance, which is a critical aspect of Tendermint Core's architecture.

**Requirements and conditions:**

1. **Network Partition**: A network partition or offline nodes can cause blocks to skip committing.
2. **Offline Nodes**: Tendermint Core does not make assumptions about point-to-point connectivity between nodes.
3. **P2P Network**: The P2P network must be weakly connected for the system to function optimally.

**Additional features and constraints:**

1. **Validation Sets Management**: `BeginBlock` and `EndBlock` messages are passed to application at block start and end, enabling updates of state.
2. **Lightweight Client Support**: Commit hashes and Merkle proofs provide cryptographic proof of committed states for lightweight clients.
3. **Byzantine Fault Tolerance (BFT) Requirements**: ≥ ⅓ Byzantine voting power can cause forks; > ⅔ Byzantine voting power can commit arbitrary invalid states.

Overall, this chunk provides a detailed understanding of Tendermint Core's technical architecture and its ABCI interface, as well as the requirements and constraints for handling network partitions, offline nodes, and P2P networks.
