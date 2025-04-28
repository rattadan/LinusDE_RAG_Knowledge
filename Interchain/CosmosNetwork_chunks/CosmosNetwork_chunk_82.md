## CosmosNetwork - Chunk 82

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

For these types of attacks, a subset of the validators should coordinate through external means to sign a reorg-proposal that chooses a fork (and any evidence thereof) and the initial subset of validators with their signatures. Validators who sign such a reorg-proposal forego their collateral on all other forks. Clients should verify the signatures on the reorg-proposal, verify any evidence, and make a judgement or prompt the end-user for a decision. For example, a phone wallet app may prompt the user with a security warning, while a refrigerator may accept any reorg-proposal signed by +½ of the original validators by voting power. No non-synchronous Byzantine fault-tolerant algorithm can come to consensus when ≥⅓ of voting power are dishonest, yet a fork assumes that ≥⅓ of voting power have already been dishonest by double-signing or lock-changing without justification. So, signing the reorg-proposal is a coordination problem that cannot be solved by any non-synchronous protocol (i.e.

---

**LLM Contextual Output:**

This chunk provides detailed technical details and processes related to Tendermint Core's Architecture and Application Binary Interface (ABCI). It specifically breaks down the functionality of Tendermint Core components such as Block Proposal, Commit Vote, Consensus Logic, AppendTx messages, CheckTx messages, and Commit message.

**Technical Details:**

* The `Block Proposal` component proposes new blocks based on transaction data.
* The `Commit Vote` collects votes from validators to finalize a block.
* The `Consensus Logic` implements Byzantine Fault Tolerance (BFT) logic, which is crucial for the system's resilience in the presence of malicious actors.

**Connections and Building upon Surrounding Context:**

This chunk connects to or builds upon the surrounding context by providing detailed explanations of Tendermint Core's components and their functions. It also establishes the following relationships:

* Tendermint Core is a consensus mechanism responsible for validating transactions and block propagation.
* The ABCI interface allows application logic to interact with Tendermint Core, enabling communication between the two.
* Application logic is responsible for validating transactions, updating state, and responding to ABCI messages.

**Requirements, Conditions, or Constraints:**

This chunk does not explicitly mention specific requirements, conditions, or constraints related to Tendermint Core's architecture. However, it implicitly mentions the following:

* ≥ ⅓ Byzantine voting power can cause forks.
* Detectable through inconsistencies in the state root, triggering social consensus mechanisms to heal the network.
* ≥ ⅔ Byzantine voting power can commit arbitrary invalid states.

These conditions suggest that Tendermint Core requires robust security measures and coordination mechanisms to handle Byzantine faults. The implementation of these mechanisms is likely dependent on specific requirements such as network partitions, malicious actor behavior, and the level of decentralization desired by the application logic.

Overall, this chunk provides a comprehensive understanding of Tendermint Core's technical details, processes, and relationships with surrounding context. It serves as a foundation for further analysis and explanation of the system's architecture and its applications in various use cases.
