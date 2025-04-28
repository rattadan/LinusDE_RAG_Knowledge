## CosmosNetwork - Chunk 77

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

However, since validator sets must be able to change, over a long range of time the original validators may all become unbonded, and hence would be free to create a new chain from the genesis block, incurring no cost as they no longer have deposits locked up. This attack came to be known as the Long Range Attack (LRA), in contrast to a Short Range Attack, where validators who are currently bonded cause a fork and are hence punishable (assuming a fork-accountable BFT algorithm like Tendermint consensus). Long Range Attacks are often thought to be a critical blow to proof-of-stake. Fortunately, the LRA can be mitigated as follows. First, for a validator to unbond (thereby recovering their collateral deposit and no longer earning fees to participate in the consensus), the deposit must be made untransferable for an amount of time known as the "unbonding period", which may be on the order of weeks or months.

---

**LLM Contextual Output:**

The current text chunk is providing a detailed explanation of Tendermint Core's architecture, Application Binary Interface (ABCI) functionality, and Byzantine Fault Tolerance (BFT) mechanisms in the context of blockchain consensus.

**Technical Details:**

1. **Block Proposal**: The process involves proposing new blocks based on transaction data, which are collected by `Commit Vote` messages.
2. **Commit Vote**: These votes are collected from validators to finalize a block, indicating their agreement with the proposed block.
3. **Consensus Logic**: Tendermint Core implements BFT logic, which ensures that transactions are included in the blockchain without interference from malicious actors.

**Context:**

1. The text is situated within an overview of Tendermint Core's architecture and its Application Binary Interface (ABCI), providing a foundation for understanding the underlying technologies.
2. The surrounding context includes three sections discussing specific technical details:
	* **AppendTx Message**: A transaction that delivers new blocks or state updates to Tendermint Core.
	* **CheckTx Message**: Validates transactions before they are included in a block, ensuring their correctness and compliance with protocol rules.
	* **Commit Message**: Computes cryptographic commitments of the current application state, which is signed by validators based on their voting power.
3. Additional sections discuss Validator Set Management and Lightweight Client Support, highlighting features that enable efficient interaction between Tendermint Core and application logic.

**Connections to Surrounding Context:**

1. The text connects its technical details to the surrounding context, discussing BFT mechanisms in the context of Byzantine Fault Tolerance (BFT) and network resilience.
2. It also mentions Validator Set Management and Lightweight Client Support, providing additional features that support Tendermint Core's consensus mechanism.

**Requirements and Conditions:**

1. The text does not mention any specific requirements or conditions for Tendermint Core to function correctly.
2. However, it implies the necessity of a secure and robust system, as demonstrated by the Long Range Attack (LRA) and its mitigation strategies.
3. The focus on BFT mechanisms suggests that Tendermint Core's architecture is designed to withstand malicious attacks and maintain network stability.

In summary, this text chunk provides an in-depth explanation of Tendermint Core's technical details, its Application Binary Interface (ABCI) functionality, and Byzantine Fault Tolerance (BFT) mechanisms within the context of blockchain consensus.
