## CosmosNetwork - Chunk 37

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

With an AXC transaction, two users on two different chains can make two transfer transactions that are committed together on both ledgers, or none at all (i.e. atomically). For example, two users can trade bitcoins for ether (or any two tokens on two different ledgers) using AXC transactions, even though Bitcoin and Ethereum are not connected to each other. The benefit of running an exchange on AXC transactions is that neither users need to trust each other or the trade-matching service. The downside is that both parties need to be online for the trade to occur. Another type of decentralized exchange is a mass-replicated distributed exchange that runs on its own blockchain. Users on this kind of exchange can submit a limit order and turn their computer off, and the trade can execute without the user being online. The blockchain matches and completes the trade on behalf of the trader. A centralized exchange can create a deep orderbook of limit orders and thereby attract more traders.

---

**LLM Contextual Output:**

Here's a focused analysis of the current text chunk:

**Technical Details**

* **Transaction Flow**: An AXC transaction consists of two transfer transactions that are committed together on both ledgers, or none at all.
* **Ledger Connection**: The transaction is made on both Bitcoin and Ethereum ledgers, demonstrating an atomic multi-transactions capability.

**Context Connection and Building Upon Surrounding Context**

The text chunk connects to the surrounding context by explaining how AXC transactions can facilitate decentralized exchanges (DEXs) without requiring trust between parties or a centralized exchange. It introduces two types of DEXs: **Decentralized Exchange via Atomic Matching (DAME)**, which relies on multiple nodes on different ledgers, and **Mass-R replicated Distributed Exchange**, which runs on its own blockchain.

**Requirements, Conditions, or Constraints**

The text mentions that:

* AXC transactions require both parties to be online for the trade to occur.
* Users can submit a limit order without being online, allowing them to execute trades without their account being active.
* The decentralized exchange relies on multiple nodes on different ledgers to facilitate atomic matching.

In terms of technical requirements or constraints, none are explicitly mentioned in this text chunk. However, it's worth noting that the blockchain and network infrastructure involved in DEXs typically require:

* High scalability and performance to support a large number of transactions per second
* Robust security measures to prevent centralized control and maintain decentralized exchange functionality

Overall, this text chunk provides valuable insights into how AXC transactions can facilitate decentralized exchanges without requiring trust between parties or a centralized exchange.
