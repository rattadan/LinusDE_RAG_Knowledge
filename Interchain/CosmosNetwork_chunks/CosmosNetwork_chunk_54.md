## CosmosNetwork - Chunk 54

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

Each validator can subjectively set whatever exchange rate it wants, and choose whatever transactions it wants, as long as the BlockGasLimit is not exceeded. The collected fees, minus any taxes specified below, are redistributed to the bonded stakeholders in proportion to their bonded atoms, every ValidatorPayoutPeriod (DEFAULT 1 hour). Of the collected transaction fees, ReserveTax (DEFAULT 2%) will go toward the reserve pool to increase the reserve pool and increase the security and value of the Cosmos network. These funds can also be distributed in accordance with the decisions made by the governance system. Atom holders who delegate their voting power to other validators pay a commission to the delegated validator. The commission can be set by each validator. Incentivizing Hackers
The security of the Cosmos Hub is a function of the security of the underlying validators and the choice of delegation by delegators.

---

**LLM Contextual Output:**

This text chunk provides technical details on Tendermint Core's architecture, specifically its role in consensus, validation, block propagation, and application logic integration with the Application Binary Interface (ABCI).

### 1. Technical Details:
- **Block Proposal**: The process involves proposing new blocks based on transaction data.
- **Commit Vote**: Collects votes from validators to finalize a block.
- **Consensus Logic**: Implements Byzantine Fault Tolerance (BFT) logic.

### Connection to Surrounding Context:
This chunk is connected to the overall context by describing Tendermint Core's functionality and its role in the Cosmos Hub blockchain network. The surrounding text explains how Tendermint Core works, including how it handles transactions, validates them, updates state, and interacts with other components such as ABCI messages.

### Requirements, Conditions, or Constraints:
- **Valid Validator Payout**: Validators must have sufficient bonded atoms to cover transaction fees and reserve tax.
- **Minimum BlockGasLimit**: A minimum block gas limit is required for valid proposals.
- **Default Time Period**: The default time period for validators' exchange rates is 1 hour.
- **Taxes and Reserves**: Taxes and reserves are used to redistribute collected fees proportionally among bonded stakeholders.

This chunk provides a detailed explanation of Tendermint Core's technical processes, its interaction with other components, and the necessary conditions that must be met for valid proposals and operations within the Cosmos Hub blockchain network.
