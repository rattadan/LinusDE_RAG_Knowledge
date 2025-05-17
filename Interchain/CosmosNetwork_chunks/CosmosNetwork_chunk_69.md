## CosmosNetwork - Chunk 69

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

That said, the core mechanism of the two-way peg is in principle the same as that employed by the Cosmos network. Ethereum Scalability Efforts
Ethereum is currently researching a number of different strategies to shard the state of the Ethereum blockchain to address scalability needs. These efforts have the goal of maintaining the abstraction layer offered by the current Ethereum Virtual Machine across the shared state space. Multiple research efforts are underway at this time. [18][22]

Cosmos vs Ethereum 2.0 Mauve
Cosmos and Ethereum 2.0 Mauve [22] have different design goals. Cosmos is specifically about tokens. Mauve is about scaling general computation. Cosmos is not bound to the EVM, so even different VMs can interoperate. Cosmos lets the zone creator determine who validates the zone. Anyone can start a new zone in Cosmos (unless governance decides otherwise). The hub isolates zone failures so global token invariants are preserved.

---

**LLM Contextual Output:**

Here's a focused analysis of the specific section:

**Technical Details/Parameters:**

* Tendermint Core is responsible for consensus, validation, and block propagation.
* Components include:
	+ Block Proposal (BP): Proposes new blocks based on transaction data.
	+ Commit Vote: Collects votes from validators to finalize a block.
	+ Consensus Logic: Implements Byzantine Fault Tolerance (BFT) logic.
* ABCI Interface provides primary messages for the application logic:
	+ AppendTx: Delivers transactions for validation and inclusion in blocks.
	+ CheckTx: Validates transactions before they are included in a block (optional).
	+ Commit: Computes cryptographic commitments of the current state.

**Contextual Connection/Building Upon:**

* This chunk is connected to or builds upon the surrounding context by explaining Tendermint Core's architecture, its components, and how it interacts with the Application Binary Interface (ABCI) interface.
* The text also provides an overview of Tendermint Core's role in consensus, validation, and block propagation, as well as its key features and design goals.

**Specific Requirements/Conditions/Constraints:**

* None mentioned. The text does not impose any specific requirements or conditions on the reader to understand the concept being explained.
* The context assumes a basic understanding of blockchain technology, consensus algorithms, and programming concepts, but it does not provide additional constraints or information that would limit its applicability.

By providing technical details, explaining the surrounding context, and outlining the connection between this chunk and the larger topic, this section effectively communicates complex ideas in a clear and concise manner.
