## CosmosNetwork - Chunk 3

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

Developers could use the existing tools or create new ones. Its vision is to build the "Internet of Blockchains"; this would be a network of blockchains that can all talk to each other in a decentralized way. Let's take a look at the team that founded Cosmos and created this ambitious vision. Who’s the team behind Cosmos
Jae Know and Ethan Buchman are the two developers that created the Cosmos network, but it wasn't a very straightforward process. First, they built the Tendermint consensus algorithm in 2014. This is the consensus mechanism that powers the Cosmos ecosystem. The two developers then created Tendermint Inc - the oldest company in the ecosystem. It has raised more than $9 million in a Series A funding round to continue developing Cosmos. In 2017, during the initial coin offering (ICO) craze, Cosmos launched via an ICO conducted by the Interchain Foundation. Interchain is a Swiss non-profit that invests in the Cosmos ecosystem via grants. They raised more than $17 million during the ICO.

---

**LLM Contextual Output:**

This specific text chunk appears to be providing a detailed technical overview of Tendermint Core's architecture and its Application Binary Interface (ABCI). Here's a focused analysis of what this section is explaining:

1. **Technical details:**
	* The block proposal, commit vote, and consensus logic are the core components responsible for validating transactions and updating the state.
	* The `AppendTx` message delivers transactions to Tendermint Core, which validates them before including them in blocks using the `CheckTx` message.
	* The `Commit` message computes a cryptographic commitment of the current application state, signed by validators based on their voting power.
2. **Context connection and building upon surrounding context:**
	* This chunk is connected to Tendermint Core's architecture and its role in the Cosmos ecosystem.
	* It builds upon the understanding of how Tendermint Core interacts with applications via the ABCI interface.
3. **Requirements, conditions, or constraints:**
	* The text does not explicitly mention any specific requirements or conditions for implementing this technology stack.

In terms of explaining complex technical concepts to a general audience, this chunk is effectively using clear and concise language to describe the inner workings of Tendermint Core's architecture and its ABCI interface. It assumes some basic knowledge of blockchain technology and consensus mechanisms, making it accessible to readers without extensive technical expertise.
