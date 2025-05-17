## CosmosNetwork - Chunk 29

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

Non-validators can delegate their staking tokens (called "atoms") to any validator to earn a portion of block fees and atom rewards, but they incur the risk of getting punished (slashed) if the delegate validator gets hacked or violates the protocol. The proven safety guarantees of Tendermint BFT consensus, and the collateral deposit of stakeholders--validators and delegators--provide provable, quantifiable security for nodes and light clients. Governance
Distributed public ledgers should have a constitution and a governance system. Bitcoin relies on the Bitcoin Foundation and mining to coordinate upgrades, but this is a slow process. Ethereum split into ETH and ETC after hard-forking to address TheDAO hack, largely because there was no prior social contract nor mechanism for making such decisions.

---

**LLM Contextual Output:**

Here's a focused analysis of the specific section:

**Technical Details/Parameters:**

* Block Proposal: A new block is proposed by Tendermint Core based on transaction data.
* Commit Vote: Validators vote to finalize a block, with the outcome determining its inclusion in the blockchain.
* Consensus Logic: Tendermint Core implements Byzantine Fault Tolerance (BFT) logic, which allows for decentralized and fault-tolerant consensus.
* AppendTx Message: A new transaction is delivered to Tendermint Core via this message, which is then passed to the application via AppendTx or CheckTx.
* CheckTx Message: Transactions are validated before being included in a block by passing them through CheckTx.

**Context Connection/Building Upon:**

This chunk provides context on how Tendermint Core's consensus mechanism works, specifically focusing on its BFT logic and the role of validators. It also discusses the importance of social consensus mechanisms for handling Byzantine faults, such as forks or censorship attacks. Additionally, it touches on the concept of governance and distributed public ledgers, highlighting the need for a constitution and governance system to ensure security and reliability.

**Requirements/Conditions:**

* Validation and state updates: The application logic needs to validate transactions and update its internal state accordingly.
* Consistency and reliability: The blockchain must be consistent and reliable, with proper handling of Byzantine faults and censorship attacks.
* Security guarantees: Tendermint Core provides provable security guarantees through its consensus mechanism and collateral deposit of stakeholders.
* Governance: A constitution and governance system are necessary for managing distributed public ledgers.

Overall, this chunk explains the technical details and parameters of Tendermint Core's consensus mechanism, focusing on its BFT logic and social consensus mechanisms. It also discusses the requirements and conditions necessary to ensure consistency, reliability, security, and governance in a distributed public ledger.
