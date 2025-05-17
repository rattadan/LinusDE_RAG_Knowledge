## CosmosNetwork - Chunk 21

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

Validators' voting powers are determined at genesis, or are changed deterministically by the blockchain, depending on the application. For example, in a proof-of-stake application such as the Cosmos Hub, the voting power may be determined by the amount of staking tokens bonded as collateral. NOTE: Fractions like ⅔ and ⅓ refer to fractions of the total voting power, never the total number of validators, unless all the validators have equal weight. >⅔ means "more than ⅔", ≥⅓ means "at least ⅓". Consensus
Tendermint is a partially synchronous BFT consensus protocol derived from the DLS consensus algorithm [20]. Tendermint is notable for its simplicity, performance, and fork-accountability. The protocol requires a fixed known set of validators, where each validator is identified by their public key. Validators attempt to come to consensus on one block at a time, where a block is a list of transactions. Voting for consensus on a block proceeds in rounds.

---

**LLM Contextual Output:**

This text chunk provides detailed technical details about the Tendermint Core's architecture and its Application Binary Interface (ABCI). Here's a focused analysis of what this specific section is explaining:

**Exact Technical Details:**

1. **Validators' voting powers:** The text mentions that validators' voting powers are determined at genesis or can be changed deterministically by the blockchain.
2. **Fractional voting power:** It explains that fractions like ⅔ and ⅓ refer to fractions of the total voting power, not the total number of validators.

**Context Connection:**

This chunk builds upon the surrounding context about Tendermint Core's architecture and its Application Binary Interface (ABCI). The text is providing a detailed explanation of how Tendermint Core handles consensus and validates transactions, which is essential for understanding the application logic.

**Specific Requirements, Conditions, or Constraints:**

None mentioned in this text chunk. However, it's worth noting that the chunk assumes some basic knowledge about blockchain concepts, such as voting power, Byzantine Fault Tolerance (BFT), and proof-of-stake consensus algorithms like Tendermint Core.

Overall, this text chunk is providing a technical overview of Tendermint Core's architecture and its Application Binary Interface (ABCI) for understanding how it handles consensus and validates transactions.
