## CosmosNetwork - Chunk 80

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

However, for light clients that are not expected to have frequent access to the internet or the blockchain network, yet another solution can be used to overcome the LRA. Non-validator token holders can post their tokens as collateral with a very long unbonding period (e.g. much longer than the unbonding period for validators) and serve light clients with a secondary method of attesting to the validity of current and past block-hashes. While these tokens do not count toward the security of the blockchain's consensus, they nevertheless can provide strong guarantees for light clients. If historical block-hash querying were supported in Ethereum, anyone could bond their tokens in a specially designed smart contract and provide attestation services for pay, effectively creating a market for light-client LRA security. Overcoming Forks and Censorship Attacks
Due to the definition of a block commit, any ≥⅓ coalition of voting power can halt the blockchain by going offline or not broadcasting their votes.

---

**LLM Contextual Output:**

Here's a focused analysis of this specific section:

**Exact Technical Details, Parameters, or Processes:**

The text chunk discusses various technical details related to Tendermint Core and its Application Binary Interface (ABCI). Specific technical concepts include:

1. **Block Proposal**: A process where new blocks are proposed based on transaction data.
2. **Commit Vote**: A voting mechanism collected from validators to finalize a block.
3. **Consensus Logic**: BFT (Byzantine Fault Tolerance) logic implemented in Tendermint Core.

**Connection to or Building upon the Surrounding Context:**

This chunk connects to the surrounding context by:

1. Introducing Tendermint Core and its role in consensus, validation, and block propagation.
2. Explaining the purpose of ABCI Interface and primary messages (AppendTx, CheckTx, Commit).
3. Discussing the responsibilities of application logic and responding to ABCI messages.

**Specific Requirements, Conditions, or Constraints:**

The text chunk doesn't explicitly mention specific requirements, conditions, or constraints for Tendermint Core. However, it mentions that:

1. The application needs to validate transactions against its state, protocol rules, and credentials.
2. If validation fails, the application updates its internal state (e.g., UTXO database).
3. Tendermint Core schedules transactions for inclusion in a block using `AppendTx`.
4. Applications use `CheckTx` to validate transactions before they are included in a block.

Overall, this chunk provides technical details and explanations about Tendermint Core's architecture and its interaction with ABCI Interface. It builds upon the surrounding context by discussing application logic, validation processes, and social consensus mechanisms for handling Byzantine faults and ensuring blockchain consistency.
