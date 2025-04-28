## CosmosNetwork - Chunk 28

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

This is because proof-of-work requires waiting for many confirmations before a transaction can be considered irreversibly committed. Double-spend attacks have already been demonstrated on services like CoinBase. Unlike other blockchain consensus systems, Tendermint offers instant and provably secure mobile-client payment verification. Since the Tendermint is designed to never fork at all, mobile wallets can receive instant transaction confirmation, which makes trustless and practical payments a reality on smartphones. This has significant ramifications for Internet of Things applications as well. Validators in Cosmos have a similar role to Bitcoin miners, but instead use cryptographic signatures to vote. Validators are secure, dedicated machines that are responsible for committing blocks.

---

**LLM Contextual Output:**

This current text chunk provides detailed technical specifications and explanations about Tendermint Core's architecture and Application Binary Interface (ABCI) interface.

1. **Technical Details and Parameters:**
   - Tendermint Core is a consensus mechanism responsible for validating and propagating transactions.
   - It has three primary components:
     - Block Proposal: Proposes new blocks based on transaction data.
     - Commit Vote: Collects votes from validators to finalize a block.
     - Consensus Logic: Implements Byzantine Fault Tolerance (BFT) logic.
   - ABCI Interface: Allows application logic to interact with Tendermint Core, including sending and receiving messages.

2. **Context Connection and Building Upon Surrounding Context:**
   - The text provides an overview of Tendermint Core's architecture and its Application Binary Interface (ABCI), highlighting key components and functionalities.
   - It assumes a basic understanding of blockchain consensus mechanisms and their applications in the context of cryptocurrency and distributed systems.
   - The text connects to and builds upon the surrounding context by providing additional details about Tendermint Core's role, components, and ABCI interface.

3. **Requirements, Conditions, or Constraints:**
   - The text does not explicitly mention specific requirements or conditions for using Tendermint Core or its ABCI interface. However, it implies that mobile wallets and validators are necessary to implement the system.
   - As mentioned earlier, Tendermint Core is designed to never fork at all, which has significant implications for Internet of Things applications.

In summary, this text chunk provides a detailed explanation of Tendermint Core's technical specifications and ABCI interface, as well as its role in consensus mechanisms and blockchain systems. It assumes a basic understanding of blockchain concepts and their applications, providing a foundation for further exploration or implementation.
