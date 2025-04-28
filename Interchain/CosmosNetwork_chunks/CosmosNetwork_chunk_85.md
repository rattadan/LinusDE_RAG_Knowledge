## CosmosNetwork - Chunk 85

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

ABCI Specification
ABCI consists of 3 primary message types that get delivered from the core to the application. The application replies with corresponding response messages. The AppendTx message is the work horse of the application. Each transaction in the blockchain is delivered with this message. The application needs to validate each transactions received with the AppendTx message against the current state, application protocol, and the cryptographic credentials of the transaction. A validated transaction then needs to update the application state — by binding a value into a key values store, or by updating the UTXO database. The CheckTx message is similar to AppendTx, but it’s only for validating transactions. Tendermint Core’s mempool first checks the validity of a transaction with CheckTx, and only relays valid transactions to its peers. Applications may check an incrementing nonce in the transaction and return an error upon CheckTx if the nonce is old.

---

**LLM Contextual Output:**

This section provides detailed technical details on the **AppendTx** message, which is one of the primary messages delivered from Tendermint Core's consensus mechanism to the application logic.

### Technical Details:

* The **AppendTx** message contains a transaction that needs to be validated by the application.
* Upon receipt of an `AppendTx` message, Tendermint Core schedules it for inclusion in a block (optionally using a commit vote).
* Applications must validate the transactions received through this message against their internal state, protocol rules, and cryptographic credentials.
* If valid, applications update their internal state by binding values into key-value stores or updating the UTXO database.

### Parameters:

* **Transaction data**: The transaction to be validated is delivered in the `AppendTx` message.
* **Application-specific parameters**: These may include nonce (incrementing value), transaction type, and other application-specific details.

### Connection to surrounding context:

This chunk connects to the overall Tendermint Core architecture by explaining how the `AppendTx` message is used within it. It also highlights the importance of validation and state updates in ensuring consistency and reliability in blockchain operations.

### Requirements, conditions, or constraints:

* **Application requirements**: The application must have a way to validate transactions against its internal state, protocol rules, and cryptographic credentials.
* **Tendermint Core requirements**: Tendermint Core needs to be able to schedule `AppendTx` messages for inclusion in blocks and handle them through commit votes.

Overall, this section provides technical details on the `AppendTx` message's role in Tendermint Core's consensus mechanism, emphasizing its importance in validating transactions and updating application state.
