## CosmosNetwork - Chunk 45

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

This allows many existing cryptocurrency frameworks, such as those of Ethereum, Zerocash, Bitcoin, CryptoNote and so on, to be used with Tendermint Core, which is a higher performance consensus engine, on a common network, opening tremendous opportunity for interoperability across platforms. Furthermore, as a multi-asset blockchain, a single transaction may contain multiple inputs and outputs, where each input can be any token type, enabling Cosmos to serve directly as a platform for decentralized exchange, though orders are assumed to be matched via other platforms. Alternatively, a zone can serve as a distributed fault-tolerant exchange (with orderbooks), which can be a strict improvement over existing centralized cryptocurrency exchanges which tend to get hacked over time.

---

**LLM Contextual Output:**

This specific section of the text chunk is explaining the technical details and parameters related to Tendermint Core's Application Binary Interface (ABCI) and its role in connecting it with application logic.

**Technical Details:**

1. **AppendTx Message**: This message allows applications to send transactions for validation and inclusion in blocks, which are then processed by Tendermint Core.
2. **CheckTx Message**: This message validates transactions before they are included in a block, ensuring that the blockchain remains secure and reliable.
3. **Commit Hashes**: These signed hashes of the current application state provide cryptographic proof of committed states, allowing lightweight clients to verify the integrity of the blockchain.

**Contextual Connection:**

This section builds upon the surrounding context by:

1. Providing an overview of Tendermint Core's architecture and its Application Binary Interface (ABCI).
2. Introducing the concept of a consensus mechanism in blockchain systems.
3. Explaining the role of Tendermint Core in handling transactions, validation, and block propagation.

**Requirements and Conditions:**

The requirements mentioned include:

1. **Validation**: The ability to validate transactions before they are included in blocks.
2. **Commitment**: The requirement for cryptographic commitments to be computed during transaction processing.
3. **Consensus Mechanism**: Tendermint Core's role in handling transactions, validation, and block propagation.

Overall, this section provides a technical framework for understanding how Tendermint Core interacts with application logic through its Application Binary Interface (ABCI).
