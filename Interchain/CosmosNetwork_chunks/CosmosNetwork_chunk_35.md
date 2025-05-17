## CosmosNetwork - Chunk 35

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

The proof states that the sending chain published a packet for the alleged destination. For the receiving chain to check this proof, it must be able keep up with the sender's block headers. This mechanism is similar to that used by sidechains, which requires two interacting chains to be aware of one another via a bidirectional stream of proof-of-existence datagrams (transactions). The IBC protocol can naturally be defined using two types of transactions: an IBCBlockCommitTx transaction, which allows a blockchain to prove to any observer of its most recent block-hash, and an IBCPacketTx transaction, which allows a blockchain to prove to any observer that the given packet was indeed published by the sender's application, via a Merkle-proof to the recent block-hash. By splitting the IBC mechanics into two separate transactions, we allow the native fee market-mechanism of the receiving chain to determine which packets get committed (i.e.

---

**LLM Contextual Output:**

This chunk of text is providing detailed information about Tendermint Core's Application Binary Interface (ABCI) and its role in facilitating interactions between application logic and the consensus mechanism.

**Technical Details:**

* The ABPI interface includes three primary messages:
  + AppendTx: Delivers transactions for validation and inclusion in blocks.
  + CheckTx: Validates transactions before they are included in a block (optional).
  + Commit: Computes cryptographic commitments of the current state.
* Tendermint Core uses Byzantine Fault Tolerance (BFT) logic to implement consensus, which is achieved through its commitment logic.

**Context Connection and Building Upon Surrounding Context:**

This chunk connects to the surrounding context by:

* Providing a detailed overview of Tendermint Core's architecture and its Application Binary Interface (ABCI).
* Breaking down key components and their functionalities.
* Explaining how different messages within ABPI are used for validation, state updates, and consensus-related tasks.

**Requirements, Conditions, or Constraints:**

There are no specific requirements, conditions, or constraints mentioned in this text chunk. However, it is essential to note that the provided technical details may require knowledge of Tendermint Core's architecture, Byzantine Fault Tolerance (BFT) mechanisms, and application-specific protocols like IBC. Additionally, the context suggests that this material is part of a larger system or documentation, which implies that there might be specific requirements for deployment, testing, or troubleshooting.
