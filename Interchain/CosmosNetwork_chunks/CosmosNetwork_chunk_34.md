## CosmosNetwork - Chunk 34

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

While double-spend attacks on these zones would result in the slashing of atoms with Tendermint's fork-accountability, a zone where >⅔ of the voting power are Byzantine can commit invalid state. The Cosmos Hub does not verify or execute transactions committed on other zones, so it is the responsibility of users to send tokens to zones that they trust. In the future, the Cosmos Hub's governance system may pass Hub improvement proposals that account for zone failures. For example, outbound token transfers from some (or all) zones may be throttled to allow for the emergency circuit-breaking of zones (a temporary halt of token transfers) when an attack is detected. Inter-blockchain Communication (IBC)
Now we look at how the Hub and zones communicate with each other. For example, if there are three blockchains, "Zone1", "Zone2", and "Hub", and we wish for "Zone1" to produce a packet destined for "Zone2" going through "Hub". To move a packet from one blockchain to another, a proof is posted on the receiving chain.

---

**LLM Contextual Output:**

This specific section of text is explaining the technical details and processes involved in Tendermint Core's Application Binary Interface (ABCI) and how it connects to or builds upon the surrounding context.

The key points being described are:

1. **AppendTx Message**: This message allows application logic to deliver transactions for validation and inclusion in blocks, while also validating these transactions against its internal state, protocol rules, and credentials.
2. **CheckTx Message**: This message validates transactions before they are included in a block by checking each transaction with Tendermint Core's mempool first, and then passing validated transactions to application via AppendTx if they pass.
3. **Commit Message**: After processing all transactions in a block, Tendermint Core computes the commit state, signs it based on validators' voting power, and includes it in the next block header.

This chunk also covers additional features such as:

* Validator Set Management: Messages sent to begin or end blocks, which allow application logic to update its state.
* Lightweight Client Support: Commit hashes and Merkle Proofs are used for verification by lightweight clients using block hashes and signed commit votes.

The specific requirements and conditions mentioned in this chunk include:

* Byzantine Fault Tolerance (BFT) with ≥ ⅓ voting power causing forks
* Detectable inconsistencies in the state root triggering social consensus mechanisms to heal the network
* Social consensus and legal measures for handling censorship attacks

Overall, this section provides a detailed explanation of how Tendermint Core's ABLI enables integration between application logic and its consensus mechanism, while also highlighting important technical considerations and requirements.
