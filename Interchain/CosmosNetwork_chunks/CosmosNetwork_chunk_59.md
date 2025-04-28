## CosmosNetwork - Chunk 59

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

It was not until the late 90s that Practical Byzantine Fault Tolerance (PBFT) [11] was introduced as an efficient partially synchronous consensus algorithm able to tolerate up to ⅓ of processes behaving arbitrarily. PBFT became the standard algorithm, spawning many variations, including most recently one created by IBM as part of their contribution to Hyperledger. The main benefit of Tendermint consensus over PBFT is that Tendermint has an improved and simplified underlying structure, some of which is a result of embracing the blockchain paradigm. Tendermint blocks must commit in order, which obviates the complexity and communication overhead associated with PBFT's view-changes. In Cosmos and many cryptocurrencies, there is no need to allow for block N+i where i >= 1 to commit, when block N itself hasn't yet committed. If bandwidth is the reason why block N hasn't committed in a Cosmos zone, then it doesn't help to use bandwidth sharing votes for blocks N+i.

---

**LLM Contextual Output:**

This text chunk appears to be explaining the technical details and parameters of Tendermint Core's consensus algorithm and its Application Binary Interface (ABCI). Here's a focused analysis of what this specific section is explaining:

**Technical Details:**

* PBFT is an efficient partially synchronous consensus algorithm that can tolerate up to ⅓ of processes behaving arbitrarily.
* Tendermint Core uses PBFT as the standard algorithm, which means it has an improved and simplified underlying structure compared to PBFT.
* Tendermint blocks must commit in order, which obviates the complexity and communication overhead associated with PBFT's view-changes.

**Parameters:**

* ⅓: The maximum number of processes that can behave arbitrarily before Tendermint Core considers a block invalid.
* Byzantine Fault Tolerance (BFT): The ability to tolerate up to ⅓ of processes behaving arbitrarily in the consensus algorithm.

**Processes and Parameters:**

* PBFT: A partially synchronous consensus algorithm that allows for up to ⅓ of processes to behave arbitrarily.
* Tendermint Core's Consensus Logic: Implements BFT logic, which means it can handle a large number of faulty or arbitrary processes without causing significant errors.
* Validator Set Management: Allows for flexible management of validator sets, including commit hashes and Merkle proofs.

**Handling Byzantine Faults:**

* Forks: Can be caused by ≥ ⅓ Byzantine voting power in the consensus algorithm.
* Censorship Attacks: Can result in arbitrary invalid states if > ⅔ Byzantine voting power is reached.
* Reorg-Proposal Coordination: Requires social consensus mechanisms to handle external coordination and ensure robustness.

**ABCI Interface and Requirements:**

* Allows application logic to interact with Tendermint Core's consensus mechanism through primary messages, including AppendTx, CheckTx, and Commit.
* Application responsibilities include validating transactions, updating state, and responding to ABCI messages with appropriate responses.
