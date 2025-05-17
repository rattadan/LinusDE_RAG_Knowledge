## CosmosNetwork - Chunk 13

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

You can also earn CRO if you use one of Crypto.com's debit cards (that's how I do it.) Here's a full guide to the different debit cards that provide crypto rewards. Cosmos - the Network of Blockchains


© Alina Grubnyak | Unsplash

Cosmos takes a different approach to create interoperable blockchains. It's a decentralized network that aims to disrupt the blockchain industry by creating the "Internet of Blockchains."

Thanks to its design, Cosmos allows for better performance and more customization on the application layer. Whether or not it succeeds, it's fascinating to see how it tackles one of the biggest problems when it comes to crypto blockchains - the lack of interoperability. One thing is for sure - blockchain developers benefit the most. With Cosmos's toolkit, they could easily create application-specific blockchains. And if developers win, we, the users, also win.

---

**LLM Contextual Output:**

This text chunk provides an overview of Tendermint Core and its Application Binary Interface (ABCI). Here's a focused analysis:

**Technical Details:**

* The text mentions that Tendermint Core is responsible for consensus, validation, and block propagation.
* It lists three key components:
  + Block Proposal: Proposes new blocks based on transaction data.
  + Commit Vote: Collects votes from validators to finalize a block.
  + Consensus Logic: Implements Byzantine Fault Tolerance (BFT) logic.
* The text also mentions that Tendermint Core uses BFT, which is a consensus algorithm that allows the network to reach a consensus in the presence of faulty nodes.

**Context Connection and Building Upon:**

* The chunk connects to the surrounding context by mentioning the importance of Tendermint Core's role in maintaining the integrity of the blockchain.
* It builds upon this context by providing details about Tendermint Core's components, BFT logic, and how it interacts with transactions and validators.

**Requirements, Conditions, or Constraints:**

* None mentioned explicitly. However, the text assumes that a user is familiar with blockchain concepts and terminology, such as validation, consensus, and Byzantine Fault Tolerance.

The chunk provides valuable information about Tendermint Core's architecture and its Application Binary Interface (ABCI). It helps users understand how Tendermint Core works, including its components, consensus mechanisms, and how it interacts with transactions and validators. The text also touches on the importance of BFT logic in maintaining the integrity of the blockchain, which is a crucial aspect of blockchain development.
