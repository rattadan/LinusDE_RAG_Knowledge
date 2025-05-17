## CosmosNetwork - Chunk 7

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

Cosmos SDK 
So Tendermint BFT reduces the time needed for the development of a blockchain. But it's still hard to build an ABCI-app from the ground up. This is where the Cosmos software development kit (SDK) comes in. Cosmos SDK is a modular framework for building secure blockchain applications. Developers could use ready-built modules, or create their own for their specific use case, and they can do that without having to code every functionality from scratch. As more developers start building in the Cosmos ecosystem, the number of SDK modules will expand, making it even easier in the future to build complex blockchain applications. That's good news for us degens. Another great thing about Cosmos SDK is that it's not Tendermint BFT exclusive. As long as the consensus engine is ABCI-compatible, you could use the SDK to build your own blockchain. Over time, many kits will emerge, allowing developers to create blockchains on different consensus engines.

---

**LLM Contextual Output:**

This text chunk provides a detailed explanation of Tendermint Core's architecture and its Application Binary Interface (ABCI). It breaks down the key components, their functionalities, and how they interact with each other.

Here's a focused analysis of what this specific section is explaining:

**Technical Details:**

* Tendermint Core uses Byzantine Fault Tolerance (BFT) logic for consensus.
* BFT ensures that the network remains robust even in the presence of faulty nodes or malicious actors.

**Contextual Connection:**

This chunk connects to and builds upon the surrounding context by:

* Providing an overview of Tendermint Core's architecture and its components (Block Proposal, Commit Vote, Consensus Logic).
* Explaining the purpose and functionality of each component.
* Discussing the role of Tendermint Core in the overall system.

**Requirements and Conditions:**

The text does not explicitly mention any specific requirements or conditions for building an ABCI-app using Tendermint Core. However, it implies that:

* The developer should have a basic understanding of blockchain concepts and Tendermint Core's architecture.
* The developer should be familiar with the Cosmos SDK framework and its modules.

Overall, this chunk provides a comprehensive explanation of Tendermint Core's architecture and its Application Binary Interface, setting the stage for building complex blockchain applications.
