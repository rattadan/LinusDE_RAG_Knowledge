## CosmosNetwork - Chunk 25

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

Bitcoin is a cryptocurrency blockchain where each node maintains a fully audited Unspent Transaction Output (UTXO) database. If one wanted to create a Bitcoin-like system on top of ABCI, Tendermint Core would be responsible for

Sharing blocks and transactions between nodes
Establishing a canonical/immutable order of transactions (the blockchain)
Meanwhile, the ABCI application would be responsible for

Maintaining the UTXO database
Validating cryptographic signatures of transactions
Preventing transactions from spending non-existent funds
Allowing clients to query the UTXO database
Tendermint is able to decompose the blockchain design by offering a very simple API between the application process and consensus process. Cosmos Overview
Cosmos is a network of independent parallel blockchains that are each powered by classical BFT consensus algorithms like Tendermint 1. The first blockchain in this network will be the Cosmos Hub.

---

**LLM Contextual Output:**

Here's a focused analysis of the current text chunk:

**Technical Details, Parameters, or Processes:**

* Tendermint Core is responsible for consensus, validation, and block propagation.
* It uses Byzantine Fault Tolerance (BFT) logic to implement consensus.
* The ABCI Interface allows application logic to interact with Tendermint Core's consensus mechanism.

**Context Connection and Building Upon the Surrounding Context:**

* The text provides a high-level overview of Tendermint Core and its role in a blockchain system.
* It also discusses the requirements for handling Byzantine faults, such as forks and censorship attacks, which are crucial for ensuring the resilience of a distributed network.

**Requirements, Conditions, or Constraints:**

* The text mentions several key components, including Tendermint Core, ABCI Interface, Validator Set Management, Lightweight Client Support, Fork Handling, Censorship Attacks, Reorg-Proposal Coordination, and Consensus Mechanisms.
* It also highlights the importance of maintaining a fully audited UTXO database in a Bitcoin-like system.

Breakdown:

The current text chunk is explaining the technical details of Tendermint Core's architecture and its role in handling Byzantine faults. It provides an overview of the ABCI Interface, which allows application logic to interact with Tendermint Core's consensus mechanism. The text also discusses several key components, including Validator Set Management, Lightweight Client Support, Fork Handling, Censorship Attacks, Reorg-Proposal Coordination, and Consensus Mechanisms.

The text is building upon a broader context that explains the requirements for handling Byzantine faults in a distributed network. It mentions several technical details, such as BFT consensus algorithms and the importance of maintaining a fully audited UTXO database.

Overall, this chunk provides a high-level overview of Tendermint Core's architecture and its role in ensuring the resilience of a blockchain system.
