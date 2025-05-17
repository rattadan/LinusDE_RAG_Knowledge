## CosmosNetwork - Chunk 70

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

General Scaling
Lightning Network
The Lightning Network is a proposed token transfer network operating at a layer above the Bitcoin blockchain (and other public blockchains), enabling improvement of many orders of magnitude in transaction throughput by moving the majority of transactions outside of the consensus ledger into so-called "payment channels". This is made possible by on-chain cryptocurrency scripts, which enable parties to enter into bilateral stateful contracts where the state can be updated by sharing digital signatures, and contracts can be closed by finally publishing evidence onto the blockchain, a mechanism first popularized by cross-chain atomic swaps. By opening payment channels with many parties, participants in the Lightning Network can become focal points for routing the payments of others, leading to a fully connected payment channel network, at the cost of capital being tied up on payment channels.

---

**LLM Contextual Output:**

This text chunk provides an overview of Tendermint Core's architecture and its Application Binary Interface (ABCI) components. Here's a focused analysis of what this specific section is explaining:

**Technical Details and Parameters:**

1. **Block Proposal**: Tendermint Core proposes new blocks based on transaction data.
2. **Commit Vote**: Collects votes from validators to finalize a block.
3. **Consensus Logic**: Implements Byzantine Fault Tolerance (BFT) logic, which enables the network to handle failures and partitions.
4. **AppendTx Message**: Delivers transactions for validation and inclusion in blocks via `AppendTx`.
5. **CheckTx Message**: Validates transactions before including them in a block via `CheckTx`.

**Context Connection:**

This chunk connects to the surrounding context by explaining Tendermint Core's role as a consensus mechanism, its components (Block Proposal, Commit Vote, Consensus Logic), and the purpose of ABCI messages (`AppendTx`, `CheckTx`) for interacting with Tendermint Core.

**Requirements and Conditions:**

None mentioned in this section. However, it's worth noting that Tendermint Core requires a secure and reliable consensus mechanism to function correctly. The network must be able to handle Byzantine faults, censorship attacks, and reorg-proposal coordination mechanisms to ensure the integrity of the blockchain.

In terms of constraints or conditions, there are several:

* The network must have sufficient voting power (≥ ⅓ for forks) to detect inconsistencies in the state root.
* The majority of validators (> ⅔) must sign off on reorg-proposal coordination mechanisms to make them robust.
* The Lightning Network requires a fully connected payment channel network, which may require significant amounts of capital tied up on payment channels.

Overall, this chunk provides an overview of Tendermint Core's architecture and its components, as well as the underlying technical concepts and constraints that enable it to function correctly.
