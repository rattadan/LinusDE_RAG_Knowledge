## CosmosNetwork - Chunk 73

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

When the legal system is unreliable or excessively expensive to invoke, validators can be forced to make security deposits in order to participate, and those deposits can be revoked, or slashed, when malicious behaviour is detected [10]. Note this is unlike Bitcoin, where forking is a regular occurrence due to network asynchrony and the probabilistic nature of finding partial hash collisions. Since in many cases a malicious fork is indistinguishable from a fork due to asynchrony, Bitcoin cannot reliably implement fork-accountability, other than the implicit opportunity cost paid by miners for mining an orphaned block. Tendermint Consensus
We call the voting stages PreVote and PreCommit. A vote can be for a particular block or for Nil. We call a collection of >⅔ PreVotes for a single block in the same round a Polka, and a collection of >⅔ PreCommits for a single block in the same round a Commit. If >⅔ PreCommit for Nil in the same round, they move to the next round.

---

**LLM Contextual Output:**

This text chunk provides technical details on Tendermint Core's consensus mechanism and the Application Binary Interface (ABCI) that it uses.

**Technical Details:**

1. **PreVote**: A phase of the voting process where validators gather to discuss and propose a block.
2. **PreCommit**: Another phase where validators vote on a block proposal.
3. **Polka**: A collection of >⅔ PreVotes for a single block in the same round, which can trigger a fork or reorg-proposal if not fulfilled by >⅔ PreCommits.
4. **Commit**: The final step where Tendermint Core computes and includes a block header into the blockchain.

**Context:**

The current text chunk is building upon the surrounding context of Tendermint Core's architecture and its Application Binary Interface (ABCI). It explains how Tendermint Core handles consensus-related tasks such as pre-voting, pre-committing, polka voting, fork/accountability, and reorg-proposal coordination. This technical information is essential for understanding how Tendermint Core's consensus mechanism works and how it interacts with the surrounding application logic.

**Requirements and Conditions:**

* Understanding of Tendermint Core's architecture and its Application Binary Interface (ABCI)
* Familiarity with blockchain concepts such as voting, consensus, and fork/accountability
* Knowledge of cryptography and digital signatures
