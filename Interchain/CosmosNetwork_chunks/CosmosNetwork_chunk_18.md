## CosmosNetwork - Chunk 18

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

Merged mining, for instance, allows the work done to secure a parent chain to be reused on a child chain, but transactions must still be validated, in order, by each node, and a merge-mined blockchain is vulnerable to attack if a majority of the hashing power on the parent is not actively merge-mining the child. An academic review of alternative blockchain network architectures is provided for additional context, and we provide summaries of other proposals and their drawbacks in Related Work. Here we present Cosmos, a novel blockchain network architecture that addresses all of these problems. Cosmos is a network connecting many independent blockchains, called zones. The zones are powered by Tendermint Core [8], which provides a high-performance, consistent, secure PBFT-like consensus engine, where strict fork-accountability guarantees hold over the behaviour of malicious actors. Tendermint Core's BFT consensus algorithm is well suited for scaling public proof-of-stake blockchains.

---

**LLM Contextual Output:**

Here's a focused analysis of the current text chunk:

**Technical Details and Parameters:**

* The technical details described include:
	+ Merged mining, which allows the work done to secure a parent chain to be reused on a child chain.
	+ Node validation, where transactions must still be validated in order by each node.
	+ Merge-mined blockchain vulnerability to attack if majority hashing power is not actively merge-mining the child.
* The parameters mentioned include:
	+ Majority hashing power required for fork attacks
	+ Social consensus mechanisms to heal network partitions

**Connections and Context:**

* This chunk connects to or builds upon the surrounding context by discussing Tendermint Core's role in consensus, validation, and block propagation, as well as its Application Binary Interface (ABCI) interface that allows application logic to interact with Tendermint Core.
* The context is also provided through mentions of other blockchain networks architectures, such as Cosmos, which is discussed as a novel blockchain network architecture that addresses problems faced by existing systems.

**Requirements, Conditions, or Constraints:**

* None mentioned in this chunk.
