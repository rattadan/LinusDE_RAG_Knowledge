## CosmosNetwork - Chunk 79

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

In PoW, it is assumed that a light client can sync to the current height from the trusted genesis block at any time simply by processing the proof-of-work in every block header. To overcome the LRA, however, we require that a light client come online with some regularity to track changes in the validator set, and that the first time they come online they must be particularly careful to authenticate what they hear from the network against trusted sources. Of course, this latter requirement is similar to that of Bitcoin, where the protocol and software must also be obtained from a trusted source. The above method for preventing LRA is well suited for validators and full nodes of a Tendermint-powered blockchain because these nodes are meant to remain connected to the network. The method is also suitable for light clients that can be expected to sync with the network frequently.

---

**LLM Contextual Output:**

The provided text chunk focuses on Tendermint Core's architecture, specifically its components (Block Proposal, Commit Vote, Consensus Logic), ABCI interface, and application logic.

**Technical Details:**

- **Tendermint Core**: The central component of the Tendermint ecosystem responsible for consensus, validation, and block propagation.
- **Block Proposal**: Proposes new blocks based on transaction data.
- **Commit Vote**: Collects votes from validators to finalize a block.
- **Consensus Logic**: Implements Byzantine Fault Tolerance (BFT) logic.

**Context Connection:**

This chunk builds upon the surrounding context by explaining the core components and functionalities of Tendermint Core. It highlights how these components interact with each other, providing insights into Tendermint's consensus mechanism and its ability to handle faults such as forks and censorship attacks.

**Requirements, Conditions, or Constraints:**

- The text mentions that light clients must be able to sync to the current height from the trusted genesis block at any time.
- It also notes that validators and full nodes of a Tendermint-powered blockchain are intended to remain connected to the network.

Overall, this chunk is essential for understanding how Tendermint Core operates within the Tendermint ecosystem and its ability to handle faults in consensus.
