## CosmosNetwork - Chunk 31

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

Cosmos is a network of many blockchains powered by Tendermint. While existing proposals aim to create a "single blockchain" with total global transaction ordering, Cosmos permits many blockchains to run concurrently with one another while retaining interoperability. At the basis, the Cosmos Hub manages many independent blockchains called "zones" (sometimes referred to as "shards", in reference to the database scaling technique known as "sharding"). A constant stream of recent block commits from zones posted on the Hub allows the Hub to keep up with the state of each zone. Likewise, each zone keeps up with the state of the Hub (but zones do not keep up with each other except indirectly through the Hub). Packets of information are then communicated from one zone to another by posting Merkle-proofs as evidence that the information was sent and received. This mechanism is called inter-blockchain communication, or IBC for short.

---

**LLM Contextual Output:**

Here's a focused analysis of the current text chunk:

**Technical Details:**

* The text mentions the following technical details:
	+ Tendermint Core's role in consensus, validation, and block propagation.
	+ The Block Proposal (BP) message that proposes new blocks based on transaction data.
	+ The Commit Vote (CV) message that collects votes from validators to finalize a block.
	+ Byzantine Fault Tolerance (BFT) logic implemented by Tendermint Core.
* The text also mentions the following parameters or processes:
	+ Consensus Logic, which implements BFT (Byzantine Fault Tolerance) logic.
	+ Application Binary Interface (ABCI) messages that allow application logic to interact with Tendermint Core's consensus mechanism.

**Context:**

* This chunk is located in a larger document that provides an overview of Tendermint Core's architecture and its Application Binary Interface (ABCI).
* The surrounding context mentions other components, such as the Tendermint Core role, Block Proposal, Commit Vote, Consensus Logic, and Application Binary Interface (ABCI) messages.
* The text assumes some background knowledge of blockchain concepts, including blockchains, zones (or shards), and inter-blockchain communication.

**Connections to or building upon the surrounding context:**

* This chunk builds upon the information provided in the surrounding context about Tendermint Core's architecture and its Application Binary Interface (ABCI).
* It also connects to other components mentioned in the document, such as the Tendermint Core role, Block Proposal, Commit Vote, Consensus Logic, and Application Binary Interface (ABCI) messages.
* The text provides additional information about inter-blockchain communication (IBC), which is a key feature of the Cosmos network.

**Requirements, conditions, or constraints:**

* The text does not explicitly mention any requirements, conditions, or constraints for Tendermint Core to function properly.
* However, it implies that the system must be able to handle Byzantine faults through social consensus mechanisms, and that it requires sufficient resources (such as validators' voting power) to implement such mechanisms.
