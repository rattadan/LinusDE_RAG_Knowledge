## CosmosNetwork - Chunk 58

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

Text Proposal
All other proposals, such as a proposal to upgrade the protocol, will be coordinated via the generic TextProposal. Roadmap
See the Plan. Related Work
There have been many innovations in blockchain consensus and scalability in the past couple of years. This section provides a brief survey of a select number of important ones. Consensus Systems
Classic Byzantine Fault Tolerance
Consensus in the presence of malicious participants is a problem dating back to the early 1980s, when Leslie Lamport coined the phrase "Byzantine fault" to refer to arbitrary process behavior that deviates from the intended behavior, in contrast to a "crash fault", wherein a process simply crashes. Early solutions were discovered for synchronous networks where there is an upper bound on message latency, though practical use was limited to highly controlled environments such as airplane controllers and datacenters synchronized via atomic clocks.

---

**LLM Contextual Output:**

This specific text chunk appears to be explaining the technical details of Tendermint Core's consensus mechanism, specifically its Byzantine Fault Tolerance (BFT) implementation.

Here are some key points that can be extracted from this chunk:

1. **Consensus Logic**: The BFT logic implemented by Tendermint Core is a Byzantine Fault Tolerant (BFT) consensus algorithm, which means it is designed to handle malicious participants in the network.
2. **Components**: The text mentions several components of Tendermint Core's BFT implementation, including:
	* Block Proposal: A proposal for new blocks based on transaction data.
	* Commit Vote: Collects votes from validators to finalize a block.
	* Consensus Logic: Implements the BFT logic to ensure agreement among validators.
3. **BFT Algorithm**: The text provides a high-level overview of the BFT algorithm used by Tendermint Core, including:
	* Proof-of-Work (PoW): A consensus mechanism that requires miners to solve complex mathematical problems to validate transactions.
	* Byzantine Fault Tolerance: Ensures that no single participant can manipulate the network to achieve their goals.
4. **Key Parameters**: The text mentions several key parameters of Tendermint Core's BFT implementation, including:
	* Threshold (≥ ⅓): The minimum number of validators required for a block to be considered valid.
	* Voting Power: The number of validators that can make decisions in the network.

The context of this chunk is part of an overview of Tendermint Core's architecture and Application Binary Interface (ABCI). It provides a detailed explanation of the BFT implementation used by Tendermint Core, which is essential for understanding how the system works and how it integrates with application logic.

To build upon this surrounding context:

* The text assumes that the reader has a basic understanding of blockchain consensus and scalability concepts.
* It provides specific technical details about Tendermint Core's BFT implementation, including its components, algorithm, parameters, and key parameters.
* To connect to or build upon this context, one would need to have a solid grasp of these technical details and be familiar with the broader topic of Byzantine Fault Tolerance in consensus algorithms.

Specific requirements and conditions:

* The text requires an understanding of blockchain consensus and scalability concepts.
* It assumes that the reader is familiar with the basic architecture of Tendermint Core and its components (Block Proposal, Commit Vote, Consensus Logic).
* To build upon this context, one would need to have a solid grasp of these technical details and be able to apply them to specific scenarios or use cases.
