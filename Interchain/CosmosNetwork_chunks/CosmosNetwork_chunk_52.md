## CosmosNetwork - Chunk 52

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

In that case, the transaction is only valid if the amount of atoms is greater than the amount of effective atoms held by the smallest validator, where effective atoms include delegated atoms. When a new validator replaces an existing validator in such a way, the existing validator becomes inactive and all the atoms and delegated atoms enter the unbonding state. Penalties for Validators
There must be some penalty imposed on the validators for any intentional or unintentional deviation from the sanctioned protocol. Some evidence is immediately admissible, such as a double-sign at the same height and round, or a violation of "prevote-the-lock" (a rule of the Tendermint consensus protocol). Such evidence will result in the validator losing its good standing and its bonded atoms as well its proportionate share of tokens in the reserve pool -- collectively called its "stake" -- will get slashed. Sometimes, validators will not be available, either due to regional network disruptions, power failure, or other reasons.

---

**LLM Contextual Output:**

Here's a focused analysis of the current text chunk:

**Technical Details and Processes:**

1. The transaction is only valid if the amount of atoms is greater than the amount of effective atoms held by the smallest validator.
2. When a new validator replaces an existing validator in such a way, the existing validator becomes inactive and all the atoms and delegated atoms enter the unbonding state.

**Context Connection and Building upon Surrounding Context:**

This chunk connects to the surrounding context on Tendermint Core's consensus mechanism, specifically on Byzantine Fault Tolerance (BFT) logic. It builds upon this understanding by introducing the concept of "effective atoms" and how validators interact with each other during validator swaps.

The chunk also highlights key concepts such as penalties for validators, sanctions against intentional or unintentional deviations from the protocol, and the role of evidence in determining a validator's good standing. These ideas are essential to understanding Tendermint Core's architecture and its Application Binary Interface (ABCI).

**Requirements, Conditions, or Constraints:**

1. The amount of atoms must be greater than the amount of effective atoms held by the smallest validator.
2. When a new validator replaces an existing one, the existing validator becomes inactive and all atoms and delegated atoms enter the unbonding state.

In essence, this chunk requires a basic understanding of Tendermint Core's consensus mechanism and its implications for validator behavior during network changes or intentional deviation from protocol rules.
