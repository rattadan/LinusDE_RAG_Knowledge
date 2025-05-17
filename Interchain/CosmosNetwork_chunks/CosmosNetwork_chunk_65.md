## CosmosNetwork - Chunk 65

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

By letting validators iteratively bet on which block they believe will become committed into the blockchain based on the other bets that they have seen so far, finality can be achieved eventually. link. This is an active area of research by the Casper team. The challenge is in constructing a betting mechanism that can be proven to be an evolutionarily stable strategy. The main benefit of Casper as compared to Tendermint may be in offering "availability over consistency" -- consensus does not require a >⅔ quorum of voting power -- perhaps at the cost of commit speed or implementation complexity. Horizontal Scaling
Interledger Protocol
The Interledger Protocol [14] is not strictly a scalability solution. It provides an ad hoc interoperation between different ledger systems through a loosely coupled bilateral relationship network.

---

**LLM Contextual Output:**

This text chunk describes the technical details and processes involved in Tendermint Core's Application Binary Interface (ABCI), specifically how it handles consensus, validation, block propagation, and communication with application logic.

**1. The exact technical details:**

- Tendermint Core uses a Byzantine Fault Tolerance (BFT) algorithm to validate transactions and update the blockchain state.
- Block Proposal is proposed by the user, then validated using commit vote from validators.
- Consensus Logic implements the BFT algorithm to ensure the validity of new blocks.

**2. How this chunk connects to or builds upon the surrounding context:**

This text chunk explains the technical components and processes of Tendermint Core's ABIC, providing a deeper understanding of how it works. The surrounding context discusses the application of these components in a broader blockchain ecosystem, highlighting the importance of ensuring consistency and reliability in transaction validation and block propagation.

**3. Any specific requirements, conditions, or constraints mentioned:**

- Consistency vs. Availability: The text mentions that achieving finality may require sacrificing commit speed or implementing complexity.
- Horizontal Scaling: This is discussed as an alternative approach to Tendermint's scalability solution.

With this analysis in mind, the current text chunk appears to be providing a detailed technical explanation of Tendermint Core's ABIC, covering its core components and processes. It also touches on broader topics such as scalability, reliability, and Byzantine Fault Tolerance in the context of blockchain applications.
