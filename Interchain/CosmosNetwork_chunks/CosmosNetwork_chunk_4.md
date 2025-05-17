## CosmosNetwork - Chunk 4

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

These funds allowed the two developers to focus on building. They co-wrote the Cosmos whitepaper and released the software in 2019. Fast forward to today, and the core contributor, Jae Know has stepped down as CEO of Tendermint in 2020 and now focuses on other initiatives. The company's entire board of directors is different at this point, but the goal remains - to create an interoperable ecosystem of application-specific blockchains. Now let's take a look at the tools that could make this vision a reality. The Tools that Power the Cosmos Ecosystem


© Cesar Carlevarino Aragon | Unsplash

In the past few years, blockchain technology has improved tremendously. We have thousands if not more blockchain networks in existence. But there's one big issue - they can't speak to each other. Why is this a problem? Because it's hard to send data and assets from one blockchain to another. If you have a Solana NFT, good luck trying to send it to Ethereum. Cosmos aims to solve that problem.

---

**LLM Contextual Output:**

This text chunk provides an excellent overview of Tendermint Core, its architecture, and the Application Binary Interface (ABCI) interface within it. Here's a focused analysis of what this specific section is explaining:

**Technical Details:**

* Tendermint Core consists of three main components:
  + Block Proposal: proposes new blocks based on transaction data.
  + Commit Vote: collects votes from validators to finalize a block.
  + Consensus Logic: implements Byzantine Fault Tolerance (BFT) logic.
* The ABCI interface allows the application logic to interact with Tendermint Core's consensus mechanism.

**Contextual Connection and Building Upon Surrounding Context:**

This chunk connects to the surrounding context by providing an in-depth look at Tendermint Core's architecture, highlighting its components, functions, and interactions. It builds upon the existing overview, providing additional technical details that are essential for understanding the inner workings of Tendermint Core.

**Requirements, Conditions, or Constraints:**

* The chunk requires a basic understanding of blockchain technology, specifically Consensus Mechanisms like BFT.
* It also assumes familiarity with the Cosmos ecosystem and its vision for creating an interoperable ecosystem of application-specific blockchains.
