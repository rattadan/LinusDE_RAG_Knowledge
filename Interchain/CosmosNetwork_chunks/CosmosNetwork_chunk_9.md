## CosmosNetwork - Chunk 9

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

Cosmos resolves this problem with its modular architecture. It forms two classes of blockchains:

Zones - these are your casual heterogenous blockchains. Hubs - these are blockchains specifically designed to connect the Zones. This design allows a Zone to create an IBC connection with a specific Hub and access every other Zone, connected to that Hub. So each Zone only needs to connect with a limited number of Hubs, providing full blockchain interoperability. The Hubs also prevent double-spending. If a Zone receives tokens from a Hub, it has only to trust the origin Zone of the tokens and their Hub. The first Hub within the Cosmos ecosystem is the Cosmos Hub (ATOM). Let's learn more about it as well as uncover other promising projects in the network. What are The Most Promising Projects on The Cosmos Ecosystem? Currently, there are more than 262 apps and services working on the Cosmos ecosystem. It will take us ages to get through them.

---

**LLM Contextual Output:**

Here's a focused analysis of the current text chunk:

**1. Technical Details/Parameters:**

- **Tendermint Core**: A consensus algorithm that implements Byzantine Fault Tolerance (BFT) logic.
- **Block Proposal**, **Commit Vote**, and **Consensus Logic**: These are crucial components in Tendermint Core's architecture, responsible for proposing new blocks, collecting votes from validators to finalize a block, and implementing BFT logic.

**2. Context Building:**

- The text provides an overview of Tendermint Core's architecture and its Application Binary Interface (ABCI) interface, highlighting the primary messages involved.
- It also discusses Tendermint Core's role in resolving Byzantine faults through social consensus mechanisms, reinforcing the overall resilience of the system.

**3. Requirements/Conditions:**

- The text does not explicitly mention specific requirements or conditions for running the Cosmos ecosystem projects on the network. However, it suggests that certain prerequisites are necessary for integrating application logic with Tendermint Core's consensus mechanism, such as being connected to a Hub and having trust in other Zones.

Overall, this chunk of text is explaining how Tendermint Core handles Byzantine faults and provides an overview of its architecture, specifically focusing on the role of blocks, votes, and consensus mechanisms.
