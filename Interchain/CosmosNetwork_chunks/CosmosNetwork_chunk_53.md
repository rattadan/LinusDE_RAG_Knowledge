## CosmosNetwork - Chunk 53

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

If, at any point in the past ValidatorTimeoutWindow blocks, a validator's commit vote is not included in the blockchain more than ValidatorTimeoutMaxAbsent times, that validator will become inactive, and lose ValidatorTimeoutPenalty (DEFAULT 1%) of its stake. Some "malicious" behavior does not produce obviously discernible evidence on the blockchain. In these cases, the validators can coordinate out of band to force the timeout of these malicious validators, if there is a supermajority consensus. In situations where the Cosmos Hub halts due to a ≥⅓ coalition of voting power going offline, or in situations where a ≥⅓ coalition of voting power censor evidence of malicious behavior from entering the blockchain, the hub must recover with a hard-fork reorg-proposal. (Link to "Forks and Censorship Attacks"). Transaction Fees
Cosmos Hub validators can accept any token type or combination of types as fees for processing a transaction.

---

**LLM Contextual Output:**

This text chunk provides detailed technical details about Tendermint Core's architecture, specifically its components, processes, and interactions with the Application Binary Interface (ABCI).

**Technical Details:**

1. The text describes the following components:
	* Block Proposal (BP): A proposal to add new blocks based on transaction data.
	* Commit Vote (CV): A vote by validators to finalize a block.
	* Consensus Logic: Tendermint Core's Byzantine Fault Tolerance (BFT) logic implementation.
2. The text also describes the ABCI Interface, which allows application logic to interact with Tendermint Core:
	* AppendTx: Delivers transactions for validation and inclusion in blocks.
	* CheckTx: Validates transactions before they are included in a block (optional).
	* Commit: Computes cryptographic commitments of the current state.
3. The text provides detailed information about the flow of transactions through Tendermint Core, including:
	* Validation of transactions against state, protocol rules, and credentials.
	* Update of internal application state.

**Connections to Surrounding Context:**

This chunk builds upon the surrounding context by providing a comprehensive overview of Tendermint Core's architecture, its components, processes, and interactions with the ABCI Interface. It also explains how Tendermint Core handles Byzantine faults, censorship attacks, and reorg-proposal coordination, which are critical aspects of blockchain security.

**Requirements, Conditions, or Constraints:**

None mentioned in this text chunk.
