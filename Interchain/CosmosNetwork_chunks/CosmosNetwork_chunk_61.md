## CosmosNetwork - Chunk 61

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

BitShares delegated stake
While not the first to deploy proof-of-stake (PoS), BitShares1.0 [12] contributed considerably to research and adoption of PoS blockchains, particularly those known as "delegated" PoS. In BitShares, stake holders elect "witnesses", responsible for ordering and committing transactions, and "delegates", responsible for coordinating software updates and parameter changes. BitShares2.0 aims to achieve high performance (100k tx/s, 1s latency) in ideal conditions, with each block signed by a single signer, and transaction finality taking quite a bit longer than the block interval. A canonical specification is still in development. Stakeholders can remove or replace misbehaving witnesses on a daily basis, but there is no significant collateral of witnesses or delegators in the likeness of Tendermint PoS that get slashed in the case of a successful double-spend attack.

---

**LLM Contextual Output:**

This text chunk provides technical details and parameters related to Tendermint Core's architecture and Application Binary Interface (ABCI).

**1. Technical Details:**

- **Tendermint Core**: A consensus algorithm responsible for managing blocks, validating transactions, and propagating them across the network.
- **Components**: Block Proposal (bProp), Commit Vote (cVote), and Consensus Logic (cLogic).
- **Block Proposals**: bProp proposes new blocks based on transaction data, while cProp collects votes from validators to finalize a block. cLogic implements Byzantine Fault Tolerance (BFT) logic.

**2. Connection to surrounding context:**

This chunk builds upon the overview of Tendermint Core and its Application Binary Interface (ABCI). The text explains how Tendermint Core functions as a consensus algorithm, handles blocks and transactions, and interacts with application logic. This connection is essential for understanding how Tendermint Core supports decentralized applications (dApps) built on top of it.

**3. Requirements and conditions:**

- **Tendermint Core**: A necessary component for any blockchain implementation that requires consensus and validation.
- **Application Logic**: The core functionality of dApps, which must interact with Tendermint Core to validate transactions and update application state.
- **Byzantine Fault Tolerance (BFT)**: A critical aspect of Tendermint Core's design, ensuring the integrity of blocks and transactions in a decentralized network.

This chunk provides detailed information on how Tendermint Core works, its architecture, and its interaction with dApps. It is essential for anyone interested in building or deploying blockchain applications that require consensus and validation mechanisms.
