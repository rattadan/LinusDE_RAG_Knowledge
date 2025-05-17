## CosmosNetwork - Chunk 2

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

But this approach leads to congestion, and results in high network fees for end-users (that's us!). Cosmos flips this dynamic on its head. It doesn't focus on its blockchain at all. Rather, Cosmos is building an ecosystem of "application-specific blockchains". "Sounds fancy, what is that all about?" Application-specific blockchains are blockchains that run a single application. So instead of having one big blockchain that handles all the apps and their transactions, each blockchain handles its own. This approach makes it easy for developers to optimize application-specific blockchains for their own use cases, thereby being able to provide (at least in theory) better sovereignty, security, and performance. Think of Cosmos as Apple's iOS. It provides the platform and tools for developers to create apps tailored to the users' needs. The goal of the Cosmos ecosystem is to make it easy to create new blockchains. It's an ecosystem built around different modular and adaptable tools.

---

**LLM Contextual Output:**

This text chunk is explaining how Tendermint Core, a consensus algorithm used in Tendermint, handles transactions, specifically through its Application Binary Interface (ABCI) interface.

1. **Technical Details and Parameters:**

- The `AppendTx` message is responsible for delivering transactions to the blockchain.
- Validation of transactions occurs before they are included in blocks using the `CheckTx` message.
- The `Commit` message computes a cryptographic commitment of the current application state, which is then signed by validators.

2. **Context and Connection to Surrounding Context:**

- This chunk connects to the surrounding context of Tendermint Core's architecture and its Application Binary Interface (ABCI).
- It explains how Tendermint Core handles transactions in blocks.
- The connection highlights the importance of ensuring the integrity and security of blockchain operations, particularly in the context of high network fees.

3. **Requirements, Conditions, or Constraints:**

- High network fees are a result of congestion, which can be mitigated by optimizing application-specific blockchains.
- Developers can optimize their own application-specific blockchains using Cosmos' modular tools and adaptable infrastructure.
