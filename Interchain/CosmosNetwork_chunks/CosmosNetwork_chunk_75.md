## CosmosNetwork - Chunk 75

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

If the validator has already PreCommit a block at round R1, we say they are _locked on that block, and the Polka used to justify the new PreCommit at round R_2 must come in a round R_polka where R_1 < R_polka <= R_2. Second, validators must Propose and/or PreVote the block they are locked on. Together, these conditions ensure that a validator does not PreCommit without sufficient evidence as justification, and that validators which have already PreCommit cannot contribute to evidence to PreCommit something else. This ensures both safety and liveness of the consensus algorithm. The full details of the protocol are described here. Tendermint Light Clients
The need to sync all block headers is eliminated in Tendermint-PoS as the existence of an alternative chain (a fork) means ≥⅓ of bonded stake can be slashed. Of course, since slashing requires that someone share evidence of a fork, light clients should store any block-hash commits that it sees.

---

**LLM Contextual Output:**

This specific text chunk is explaining the technical details and parameters of Tendermint Core's consensus mechanism, specifically its handling of Byzantine Fault Tolerance (BFT) with regards to forks and censorship attacks.

Here are the exact technical details and parameters described in this chunk:

1. **Fork detection**: The chunk mentions that a fork can be detected through inconsistencies in the state root, which triggers social consensus mechanisms to heal the network.
2. **Censorship attack handling**: The chunk explains how censorship attacks can occur with ≥⅔ of Byzantine voting power, and discusses the role of social consensus mechanisms (such as Reorg-Proposal Coordination) in defending against these attacks.
3. **Locking on a block**: The chunk describes the conditions under which validators are considered "locked" on a particular block, including that they must Propose and/or PreVote the block they are locked on, and that they cannot PreCommit without sufficient evidence.

This chunk builds upon the surrounding context by providing specific details about Tendermint Core's consensus mechanism, its handling of Byzantine faults, and how it ensures safety and liveness.

The requirements, conditions, or constraints mentioned in this text chunk include:

* The need for validators to Propose and/or PreVote a block they are locked on
* The requirement that the validator's justification must be sufficient to justify their precommit action
* The possibility of forks occurring with ≥⅔ of Byzantine voting power
* The role of social consensus mechanisms (such as Reorg-Proposal Coordination) in defending against censorship attacks
* The necessity for light clients to store block-hash commits that they see during synchronization.
