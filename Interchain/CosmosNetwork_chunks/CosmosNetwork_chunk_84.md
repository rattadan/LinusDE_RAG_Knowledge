## CosmosNetwork - Chunk 84

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

Unlike double-signing, which creates forks with easily verifiable evidence, detecting commitment of an invalid state requires non-validating peers to verify whole blocks, which implies that they keep a local copy of the state and execute each transaction, computing the state root independently for themselves. Once detected, the only way to handle such a failure is via social consensus. For instance, in situations where Bitcoin has failed, whether forking due to software bugs (as in March 2013), or committing invalid state due to Byzantine behavior of miners (as in July 2015), the well connected community of businesses, developers, miners, and other organizations established a social consensus as to what manual actions were required by participants to heal the network. Furthermore, since validators of a Tendermint blockchain may be expected to be identifiable, commitment of an invalid state may even be punishable by law or some external jurisprudence, if desired.

---

**LLM Contextual Output:**

This chunk provides detailed technical details and parameters related to Tendermint Core's consensus mechanism and its Application Binary Interface (ABCI) with the surrounding context.

Here are specific analyses of what this section is explaining:

1. **Technical Details**: The chunk describes the technical components and processes involved in Tendermint Core's consensus, including Block Proposal, Commit Vote, Consensus Logic, and the ABCI interface.
2. **Connection to Surrounding Context**: This chunk builds upon the key components and functionalities described in the surrounding context (Point 1). It provides a deeper understanding of how these components interact with each other and what their primary functions are.
3. **Requirements and Constraints**: The text mentions various requirements and constraints, such as detecting commitment of an invalid state, handling Byzantine faults via social consensus mechanisms, and punishing validators for committing invalid states. This information helps the reader understand the trade-offs involved in implementing these systems.

Some specific technical details mentioned in this chunk include:

* Block Proposal: a message that proposes new blocks based on transaction data.
* Commit Vote: collects votes from validators to finalize a block.
* Consensus Logic: implements Byzantine Fault Tolerance (BFT) logic, which is the core of Tendermint Core's consensus mechanism.
* AppendTx and CheckTx messages: used for validation and verification of transactions.
* Merkle Proofs: used for lightweight clients to verify transaction history.

The chunk also highlights the social consensus mechanisms in place to handle Byzantine faults, such as forks, censorship attacks, and reorg-proposal coordination. These mechanisms involve a community of stakeholders working together to resolve issues and maintain network stability.
