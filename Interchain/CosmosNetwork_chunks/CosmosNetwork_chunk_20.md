## CosmosNetwork - Chunk 20

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

Because anyone can connect a new zone to the Cosmos Hub, zones allow for future-compatibility with new blockchain innovations. With Cosmos interoperability between blockchains can be achieved. The potential of an internet of value, where assets are issued and controlled by different sets of validators, yet can be moved and exchanged seamlessly between blockchains without relying on trusted third parties can be realized. Tendermint
In this section we describe the Tendermint consensus protocol and the interface used to build applications with it. For more details, see the appendix. Validators
In classical Byzantine fault-tolerant (BFT) algorithms, each node has the same weight. In Tendermint, nodes have a non-negative amount of voting power, and nodes that have positive voting power are called validators. Validators participate in the consensus protocol by broadcasting cryptographic signatures, or votes, to agree upon the next block.

---

**LLM Contextual Output:**

This text chunk describes the Tendermint Core consensus algorithm and its Application Binary Interface (ABCI) interface.

**Technical Details:**

* Tendermint Core is responsible for consensus, validation, and block propagation.
* Components:
	+ Block Proposal: Proposes new blocks based on transaction data.
	+ Commit Vote: Collects votes from validators to finalize a block.
	+ Consensus Logic: Implements BFT (Byzantine Fault Tolerance) logic.
* ABCI Interface:
	+ Primary Messages:
		- AppendTx: Delivers transactions for validation and inclusion in blocks.
		- CheckTx: Validates transactions before they are included in a block (optional).
		- Commit: Computes cryptographic commitments of the current state.

**Context Connection:**

This chunk builds upon the surrounding context, which provides an overview of Tendermint Core's architecture and its Application Binary Interface (ABCI). It explains how the ABCI interface is used to interact with Tendermint Core, specifically for validating transactions and updating application state. The text also delves deeper into the technical details of the consensus algorithm and the role of validators in it.

**Requirements and Conditions:**

* None mentioned in this chunk. However, it's essential to note that the context assumes familiarity with blockchain concepts and the Tendermint Core architecture.
* Additional requirements include:
	+ A compatible blockchain or network where Tendermint Core is deployed.
	+ The presence of a validator set, which consists of validators with voting power.

**Analysis:**

This chunk provides a detailed explanation of Tendermint Core's consensus algorithm and its ABCI interface. It covers the technical details, components, and primary messages used for validation and block propagation. By understanding how Tendermint Core functions, developers can integrate their application logic with the system, ensuring consistency and reliability in blockchain operations.

In summary, this chunk explains the fundamental aspects of Tendermint Core's consensus protocol and its ABCI interface, providing a solid foundation for building applications that interact with Tendermint Core.
