## CosmosNetwork - Chunk 40

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

The indirection through the bridge-zone allows the logic of the Hub to remain simple and agnostic to other blockchain consensus strategies such as Bitcoin's proof-of-work mining. Sending Tokens to the Cosmos Hub
Each bridge-zone validator would run a Tendermint-powered blockchain with a special ABCI bridge-app, but also a full-node of the "origin" blockchain. When new blocks are mined on the origin, the bridge-zone validators will come to agreement on committed blocks by signing and sharing their respective local view of the origin's blockchain tip. When a bridge-zone receives payment on the origin (and sufficient confirmations were agreed to have been seen in the case of a PoW chain such as Ethereum or Bitcoin), a corresponding account is created on the bridge-zone with that balance. In the case of Ethereum, the bridge-zone can share the same validator-set as the Cosmos Hub.

---

**LLM Contextual Output:**

Here's a focused analysis of the specific section explaining what this chunk is explaining:

**Exact Technical Details/Parameters/Processes Described:**

* Tendermint Core components:
	+ Block Proposal
	+ Commit Vote
	+ Consensus Logic (Byzantine Fault Tolerance)
* ABCI Interface messages:
	+ AppendTx
	+ CheckTx
	+ Commit

**How this chunk connects to or builds upon the surrounding context:**

This chunk provides a detailed overview of Tendermint Core's architecture and its Application Binary Interface (ABCI). It explains how Tendermint Core functions, including its roles, components, and processes. This context is crucial for understanding how applications can interact with Tendermint Core.

The chunk also expands on previous knowledge by introducing new concepts, such as:

* Bridge-zone: a concept that allows Tendermint-powered blockchain networks to coexist with other blockchain networks (e.g., Cosmos Hub).
* ABCI bridge-app: an application layer built on top of Tendermint Core that interacts with the blockchain network.
* Validator-set management: The chunk explains how validators' voting power affects the consensus mechanism and handling Byzantine faults.

**Specific Requirements, Conditions, or Constraints:**

The chunk assumes:

* A basic understanding of blockchain fundamentals (e.g., block proposal, commit vote, consensus logic).
* Familiarity with Tendermint Core architecture and its components.
* Knowledge of ABCI interface messages and their purpose.

It also touches on requirements related to handling Byzantine faults, such as detecting inconsistencies in the state root and triggering social consensus mechanisms.
