## CosmosNetwork - Chunk 30

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

Validators and delegators on the Cosmos Hub can vote on proposals that can change preset parameters of the system automatically (such as the block gas limit), coordinate upgrades, as well as vote on amendments to the human-readable constitution that govern the policies of the Cosmos Hub. The constitution allows for cohesion among the stakeholders on issues such as theft and bugs (such as TheDAO incident), allowing for quicker and cleaner resolution. Each zone can also have their own constitution and governance mechanism as well. For example, the Cosmos Hub could have a constitution that enforces immutability at the Hub (no roll-backs, save for bugs of the Cosmos Hub node implementation), while each zone can set their own policies regarding roll-backs. By enabling interoperability among differing policy zones, the Cosmos network gives its users ultimate freedom and potential for permissionless experimentation. The Hub and Zones
Here we describe a novel model of decentralization and scalability.

---

**LLM Contextual Output:**

**Technical Details/Parameters:**

* **Tendermint Core Components:**
	+ Block Proposal: proposes new blocks based on transaction data.
	+ Commit Vote: collects votes from validators to finalize a block.
	+ Consensus Logic: implements Byzantine Fault Tolerance (BFT) logic.
* **ABCI Interface Messages:**
	+ AppendTx: delivers transactions for validation and inclusion in blocks.
	+ CheckTx: validates transactions before they are included in a block (optional).
	+ Commit: computes cryptographic commitments of the current state.

**Context Connection/Building Upon Surrounding Context:**

This chunk explains the technical details and processes involved in Tendermint Core's consensus mechanism, specifically its role in validating and propagating blocks. It also discusses how this system interacts with external applications via the Application Binary Interface (ABCI) interface.

The context provided includes:

* An overview of Tendermint Core's architecture, highlighting its components and functionalities.
* A detailed breakdown of specific messages exchanged between Tendermint Core and the application logic, including AppendTx, CheckTx, Commit, and others.
* The inclusion of various technical terms and concepts, such as Byzantine Fault Tolerance (BFT) logic, social consensus mechanisms, and lightweight client support.

The chunk builds upon this context by providing a deeper understanding of how Tendermint Core handles Byzantine faults, the importance of validation and propagation in maintaining network integrity, and the role of external applications within the system's architecture.

**Requirements/Conditions/Cstraints:**

* None specified in the given text chunk.
