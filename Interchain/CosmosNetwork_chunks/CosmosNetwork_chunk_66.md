## CosmosNetwork - Chunk 66

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

Like the Lightning Network, the purpose of ILP is to facilitate payments, but it specifically focuses on payments across disparate ledger types, and extends the atomic transaction mechanism to include not only hash-locks, but also a quorum of notaries (called the Atomic Transport Protocol). The latter mechanism for enforcing atomicity in inter-ledger transactions is similar to Tendermint's light-client SPV mechanism, so an illustration of the distinction between ILP and Cosmos/IBC is warranted, and provided below. The notaries of a connector in ILP do not support membership changes, and do not allow for flexible weighting between notaries. On the other hand, IBC is designed specifically for blockchains, where validators can have different weights, and where membership can change over the course of the blockchain. As in the Lightning Network, the receiver of payment in ILP must be online to send a confirmation back to the sender.

---

**LLM Contextual Output:**

Here's a focused analysis of the provided text chunk:

**Technical Details and Processes:**

1. **Block Proposal (BPT)**: The block proposal is responsible for proposing new blocks based on transaction data, which involves creating a block proposal message (`AppendTx`) that passes through Tendermint Core and updates its internal state.
2. **Commit Vote**: The commit vote collects votes from validators to finalize a block, which involves checking transactions against the current state using `CheckTx` messages.
3. **Consensus Logic (BFT)**: Tendermint Core implements Byzantine Fault Tolerance (BFT) logic, which enables the system to handle network partitions and detect anomalies in the state root.

**Context Connection and Building upon Surrounding Context:**

This chunk connects to the surrounding context by describing the key components and functionalities of Tendermint Core, including its role in consensus, validation, and block propagation. It also highlights the importance of atomic transactions and inter-ledger payments. The connection is further reinforced by the text discussing ILP's Atomic Transport Protocol (ATP) mechanism, which shares similarities with Tendermint's light-client SPV mechanism.

**Specific Requirements, Conditions, or Constraints:**

The chunk requires knowledge of:

1. Tendermint Core's architecture and Application Binary Interface (ABCI)
2. The Block Proposal, Commit Vote, and Consensus Logic
3. Atomic transactions and inter-ledger payments

These requirements are crucial for understanding the technical details and processes involved in Tendermint Core and ILP.

**Analysis:**

The chunk provides a detailed explanation of how Tendermint Core handles atomic transactions and inter-ledger payments, highlighting the importance of consensus mechanisms like BFT. The discussion also touches on the limitations and constraints of ILP's Atomic Transport Protocol, which can be seen as a variation of Tendermint's light-client SPV mechanism.

Overall, this chunk provides a comprehensive understanding of the technical details and processes involved in Tendermint Core and ILP, including their respective architectures, functionalities, and constraints.
