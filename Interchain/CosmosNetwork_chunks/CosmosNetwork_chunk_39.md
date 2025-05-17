## CosmosNetwork - Chunk 39

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

Given the state of cryptocurrency exchanges today, a great application for Cosmos is the distributed exchange (aka the Cosmos DEX). The transaction throughput capacity as well as commit latency can be comparable to those of centralized exchanges. Traders can submit limit orders that can be executed without both parties having to be online. And with Tendermint, the Cosmos hub, and IBC, traders can move funds in and out of the exchange to and from other zones with speed. Bridging to Other Cryptocurrencies
A privileged zone can act as the source of a bridged token of another cryptocurrency. A bridge is similar to the relationship between a Cosmos hub and zone; both must keep up with the latest blocks of the other in order to verify proofs that tokens have moved from one to the other. A "bridge-zone" on the Cosmos network keeps up with the Hub as well as the other cryptocurrency.

---

**LLM Contextual Output:**

This text chunk is explaining the technical details and parameters of Tendermint Core's Application Binary Interface (ABCI) and its connection to the surrounding context.

The key points discussed in this chunk are:

* Tendermint Core implements Byzantine Fault Tolerance (BFT) logic, which means it can handle consensus-related tasks like reorg-proposals even when a significant portion of validators are compromised.
* The ABCI interface provides primary messages that allow application logic to interact with Tendermint Core: AppendTx for transaction validation and inclusion in blocks, CheckTx for validation before block inclusion, and Commit for cryptographic commitment of the current state.
* The chunk also mentions Validator Set Management, which is a feature provided by Tendermint Core to manage validator sets and ensure fairness in consensus mechanisms.
* It concludes with an explanation of how Bridging works on the Cosmos network, where a privileged zone can act as a source of bridged tokens between two cryptocurrencies.

Technical Details:

* The text chunk mentions various technical concepts, such as Byzantine Fault Tolerance (BFT), consensus mechanisms like proof-of-stake (PoS) and Byzantine Fault Tolerance (BFT), and the use of cryptographic commitments.
* It also references specific Tendermint Core components, including Block Proposal, Commit Vote, Consensus Logic, AppendTx, CheckTx, and Commit.

Context:

* The text chunk is part of an overview that provides an excellent foundation for understanding Tendermint Core's architecture and its Application Binary Interface (ABCI).
* This context is likely provided by a technical document or presentation intended for developers, researchers, or users interested in exploring the capabilities of Tendermint Core.
* The surrounding context refers to the broader ecosystem of cryptocurrency exchanges and protocols, including decentralized exchanges (DEXs), bridges, and Cosmos hubs.
