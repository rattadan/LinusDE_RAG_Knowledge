## CosmosNetwork - Chunk 86

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

The Commit message is used to compute a cryptographic commitment to the current application state, to be placed into the next block header. This has some handy properties. Inconsistencies in updating that state will now appear as blockchain forks which catches a whole class of programming errors. This also simplifies the development of secure lightweight clients, as Merkle-hash proofs can be verified by checking against the block-hash, and the block-hash is signed by a quorum of validators (by voting power). Additional ABCI messages allow the application to keep track of and change the validator set, and for the application to receive the block information, such as the height and the commit votes.

---

**LLM Contextual Output:**

This specific section provides detailed technical details about the Commit message in Tendermint Core's Application Binary Interface (ABCI), its purpose, flow, and properties.

**Technical Details:**

* The Commit message is used to compute a cryptographic commitment of the current application state.
* This commitment is then included in the next block header.
* Inconsistencies in updating the state will now appear as blockchain forks, which can be detected through inconsistencies in the state root.

**Parameters and Processes:**

* The Commit message takes two parameters:
  - The current application state
  - The commit votes (signed by validators)

**Processes:**

1. Validation of transactions against their state, protocol rules, and credentials.
2. Updates of internal application state based on transaction outcomes.
3. Response to ABCI messages with appropriate responses.

**Connecting to or Building Upon the Surrounding Context:**

This section builds upon the understanding of Tendermint Core's architecture and its Application Binary Interface (ABCI). It provides a detailed explanation of how the Commit message operates, including its properties, such as detecting inconsistencies in state updates. This information is essential for developers working with Tendermint Core to integrate application logic with the consensus mechanism.

**Specific Requirements, Conditions, or Constraints:**

* The Commit message requires a current application state and commit votes (signed by validators).
* Inconsistencies in updating the state will now appear as blockchain forks.
* This process simplifies the development of secure lightweight clients, as Merkle-hash proofs can be verified by checking against the block-hash.

The section also mentions that Validator Set Management is handled through messages `BeginBlock` and `EndBlock`, which provide cryptographic proof of committed states. However, it does not explicitly mention any specific constraints or conditions on these messages.
