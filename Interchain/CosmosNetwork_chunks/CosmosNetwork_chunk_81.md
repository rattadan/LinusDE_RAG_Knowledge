## CosmosNetwork - Chunk 81

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

Such a coalition can also censor particular transactions by rejecting blocks that include these transactions, though this would result in a significant proportion of block proposals to be rejected, which would slow down the rate of block commits of the blockchain, reducing its utility and value. The malicious coalition might also broadcast votes in a trickle so as to grind blockchain block commits to a near halt, or engage in any combination of these attacks. Finally, it can cause the blockchain to fork, by double-signing or violating the locking rules. If a globally active adversary were also involved, it could partition the network in such a way that it may appear that the wrong subset of validators were responsible for the slowdown. This is not just a limitation of Tendermint, but rather a limitation of all consensus protocols whose network is potentially controlled by an active adversary.

---

**LLM Contextual Output:**

Based on this detailed breakdown of the text chunk, here's a focused analysis:

**Technical Details:**

* The section discusses **Byzantine Fault Tolerance (BFT) logic**, which is implemented in Tendermint Core to prevent malicious actors from manipulating the blockchain.
* BFT uses consensus protocols like Byzantine Fault Tolerance (BFT), which ensure that all nodes on the network agree on a valid state without resorting to complex voting mechanisms.

**Contextual Connection:**

* The section provides an overview of Tendermint Core's architecture and its Application Binary Interface (ABCI) interface, which allows application logic to interact with the core consensus mechanism.
* This context is crucial in understanding how BFT works within Tendermint Core, including the roles of individual components like block proposal, commit vote, and consensus logic.

**Requirements and Constraints:**

* The section mentions that Byzantine Fault Tolerance (BFT) can be achieved through social consensus mechanisms, which implies that there are constraints on the number of validators required to prevent attacks.
* The requirement for a coalition of at least ⅓ Byzantine voting power to cause forks is mentioned, indicating that this specific scenario would lead to significant disruption in the blockchain.

**Additional Insights:**

* The section discusses various attack vectors, including censorship, fork propagation, and reorg-proposal coordination, which highlight the importance of robustness and security measures within Tendermint Core.
* It also touches on the limitations of consensus protocols when operated by an active adversary, emphasizing that BFT is not a guarantee against such attacks.

Overall, this chunk provides detailed technical information about Byzantine Fault Tolerance (BFT) and its implementation in Tendermint Core's architecture.
