## CosmosNetwork - Chunk 22

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

Each round has a round-leader, or proposer, who proposes a block. The validators then vote, in stages, on whether to accept the proposed block or move on to the next round. The proposer for a round is chosen deterministically from the ordered list of validators, in proportion to their voting power. The full details of the protocol are described here. Tendermint’s security derives from its use of optimal Byzantine fault-tolerance via super-majority (>⅔) voting and a locking mechanism. Together, they ensure that:

≥⅓ voting power must be Byzantine to cause a violation of safety, where more than two values are committed. if any set of validators ever succeeds in violating safety, or even attempts to do so, they can be identified by the protocol. This includes both voting for conflicting blocks and broadcasting unjustified votes. Despite its strong guarantees, Tendermint provides exceptional performance.

---

**LLM Contextual Output:**

I'll provide a focused analysis of the current text chunk.

**Technical Details:**

1. **Block Proposal**: A block proposal is a message that proposes new blocks based on transaction data.
2. **Commit Vote**: A commit vote is a message that collects votes from validators to finalize a block.
3. **Consensus Logic**: Tendermint Core implements Byzantine Fault Tolerance (BFT) logic, which ensures the integrity of the blockchain.

**Context and Connection:**

1. This chunk provides an overview of Tendermint Core's architecture and its Application Binary Interface (ABCI).
2. The context is set with a detailed breakdown of Tendermint Core's components, including Block Proposal, Commit Vote, Consensus Logic, and ABCI messages.
3. The text also mentions the Validator Set Management features, which are specific to Tendermint Core.

**Requirements and Conditions:**

1. **Security**: The protocol ensures security through optimal Byzantine fault-tolerance via super-majority (>⅔) voting and a locking mechanism.
2. **Reliability**: The system provides exceptional performance despite its strong guarantees on safety.
3. **Scalability**: Tendermint Core's architecture is designed to handle large amounts of data, including multiple rounds and validators.

**Key Concepts:**

1. **Byzantine Fault Tolerance (BFT)**: A consensus mechanism that ensures the integrity of the blockchain by tolerating a certain number of faulty nodes or votes.
2. **Super-majority**: A voting threshold where more than two values are committed to ensure safety and prevent malicious behavior.
3. **Locking Mechanism**: A mechanism used to prevent attacks, such as censorship attacks, by ensuring that only validators with the necessary voting power can modify the blockchain.

Overall, this chunk provides a comprehensive understanding of Tendermint Core's architecture, security guarantees, and scalability features, which are essential for understanding its Application Binary Interface (ABCI).
