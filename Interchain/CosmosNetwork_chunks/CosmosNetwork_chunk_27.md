## CosmosNetwork - Chunk 27

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

We are designing a protocol for an open network of distributed ledgers that can serve as a new foundation for future financial systems, based on principles of cryptography, sound economics, consensus theory, transparency, and accountability. Tendermint-BFT
The Cosmos Hub is the first public blockchain in the Cosmos Network, powered by Tendermint's BFT consensus algorithm. The Tendermint open-source project was born in 2014 to address the speed, scalability, and environmental issues of Bitcoin's proof-of-work consensus algorithm. By using and improving upon proven BFT algorithms developed at MIT in 1988 [20], the Tendermint team was the first to conceptually demonstrate a proof-of-stake cryptocurrency that addresses the nothing-at-stake problem suffered by first-generation proof-of-stake cryptocurrencies such as NXT and BitShares1.0. Today, practically all Bitcoin mobile wallets use trusted servers to provide them with transaction verification.

---

**LLM Contextual Output:**

This text chunk is explaining the technical details of Tendermint Core's architecture and Application Binary Interface (ABCI) in the context of a distributed ledger system.

**Context:**
The surrounding text provides an overview of Tendermint Core's architecture and its relationship to the underlying technology, which includes Tendermint's BFT (Byzantine Fault Tolerance) consensus algorithm. The text also mentions the Cosmos Hub, another public blockchain powered by Tendermint's BFT consensus algorithm.

**1. Technical details:**

* **Tendermint Core:** Responsible for consensus, validation, and block propagation.
* **Block Proposal:** Proposes new blocks based on transaction data, collected through a committee vote (Commit Vote) with validators' signatures.
* **Consensus Logic:** Implements Byzantine Fault Tolerance logic to ensure the integrity of the network.

**2. Connection to surrounding context:**
The text chunk builds upon the understanding of Tendermint Core's architecture and its connection to the underlying technology, including the Cosmos Hub. The discussion about Byzantine faults and social consensus mechanisms highlights the importance of maintaining the integrity of the network.

**3. Requirements, conditions, or constraints:**

* **Byzantine Fault Tolerance:** Ensures the integrity of the network through Consensus Logic.
* **Consensus Algorithm:** Tendermint's BFT algorithm is a key component of Tendermint Core and Cosmos Hub.
* **Network Resilience:** The ability to handle Byzantine faults and social consensus mechanisms is crucial for maintaining the overall system's stability.

This text chunk provides detailed information about the technical architecture of Tendermint Core, its role in a distributed ledger system, and how it connects to other technologies like the Cosmos Hub.
