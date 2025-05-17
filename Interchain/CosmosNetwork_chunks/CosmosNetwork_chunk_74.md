## CosmosNetwork - Chunk 74

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

Note that strict determinism in the protocol incurs a weak synchrony assumption as faulty leaders must be detected and skipped. Thus, validators wait some amount of time, TimeoutPropose, before they Prevote Nil, and the value of TimeoutPropose increases with each round. Progression through the rest of a round is fully asynchronous, in that progress is only made once a validator hears from >⅔ of the network. In practice, it would take an extremely strong adversary to indefinitely thwart the weak synchrony assumption (causing the consensus to fail to ever commit a block), and doing so can be made even more difficult by using randomized values of TimeoutPropose on each validator. An additional set of constraints, or Locking Rules, ensure that the network will eventually commit just one block at each height. Any malicious attempt to cause more than one block to be committed at a given height can be identified. First, a PreCommit for a block must come with justification, in the form of a Polka for that block.

---

**LLM Contextual Output:**

I'll provide a focused analysis of the current text chunk and its context.

**Technical Details and Processes:**

The current text chunk describes several technical details and processes related to Tendermint Core's architecture and Application Binary Interface (ABCI). These include:

* The role, components, and primary messages associated with Tendermint Core (Block Proposal, Commit Vote, Consensus Logic)
* Detailed breakdowns of the AppendTx message flow, CheckTx message validation process, and Commit message computation
* Additional features such as validator set management, lightweight client support, fork detection, censorship attacks mitigation, reorg-proposal coordination, and strong synchrony assumptions

**Context:**

The current text chunk is part of an overview that provides a foundation for understanding Tendermint Core's architecture and Application Binary Interface (ABCI). The surrounding context mentions Tendermint Core as the consensus algorithm responsible for block propagation, validation, and block creation.

This chunk builds upon the surrounding context by providing specific details about how Tendermint Core functions, its components, and their interactions. It also introduces additional concepts such as Byzantine faults, social consensus mechanisms, and synchronization assumptions that are critical to understanding Tendermint Core's architecture.

**Requirements, Conditions, or Constraints:**

The current text chunk does not explicitly mention any requirements, conditions, or constraints related to the technical details described in the chunk. However, based on the context and surrounding information, it can be inferred that:

* The system must be designed to handle Byzantine faults and social consensus mechanisms
* Strong synchrony assumptions are required to ensure the protocol's reliability
* Limited determinism is acceptable due to the weak synchrony assumption inherent in the protocol
* Randomized values of TimeoutPropose may be used to mitigate these issues

Overall, the current text chunk provides a detailed understanding of Tendermint Core's architecture and its components, highlighting their interactions and functions.
