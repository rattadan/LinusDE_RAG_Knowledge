## CosmosNetwork - Chunk 42

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

An IBC packet proving that the transaction occurred on the bridge-zone can be posted to the Ethereum bridge-contract to allow the ether to be withdrawn. In the case of Bitcoin, the restricted scripting system makes it difficult to mirror the IBC coin-transfer mechanism. Each UTXO has its own independent pubscript, so every UTXO must be migrated to a new UTXO when there is a change in the set of Bitcoin escrow signers. One solution is to compress and decompress the UTXO-set as necessary to keep the total number of UTXOs down. Total Accountability of Bridge Zones
The risk of such a bridgeging contract is a rogue validator set. ≥⅓ Byzantine voting power could cause a fork, withdrawing ether from the bridge-contract on Ethereum while keeping the bridged-ether on the bridge-zone. Worse, >⅔ Byzantine voting power can steal ether outright from those who sent it to the bridge-contract by deviating from the original bridgeging logic of the bridge-zone.

---

**LLM Contextual Output:**

This text chunk provides a detailed analysis of Tendermint Core's architecture and Application Binary Interface (ABCI), specifically focusing on the technical details, parameters, processes, connections, and requirements.

The key points in this chunk are:

1. **Tendermint Core's components**: The text describes the Block Proposal, Commit Vote, and Consensus Logic of Tendermint Core, highlighting their roles and functionalities.
2. **ABCI Interface**: It explains the purpose of ABCI and its primary messages (AppendTx, CheckTx, Commit), detailing how they interact with Tendermint Core and other components.
3. **Application Logic**: The text outlines the responsibilities of the application logic, including validation, transaction processing, state updates, and responses to ABCI messages.

The chunk connects this context to the surrounding overview of Tendermint Core's architecture by explaining its role in consensus, validation, and block propagation.

To identify specific technical details, parameters, or processes described in this chunk:

* Block Proposal: `Proposes new blocks based on transaction data`
* Commit Vote: Collects votes from validators to finalize a block
* Consensus Logic: Implements Byzantine Fault Tolerance (BFT) logic

For connections to or building upon the surrounding context:

* Tendermint Core's role in consensus, validation, and block propagation
* ABCI Interface's purpose and messages (AppendTx, CheckTx, Commit)
* Application Logic's responsibilities and interactions with Tendermint Core and other components

To identify specific requirements, conditions, or constraints mentioned:

* ≥⅓ Byzantine voting power can cause forks
* >⅔ Byzantine voting power can steal ether
* Validator set management: messages (BeginBlock, EndBlock), commit hashes, Merkle proofs
* Handling Byzantine faults through social consensus mechanisms and reorg-proposal coordination

Overall, this chunk provides a detailed understanding of Tendermint Core's architecture and ABCI interface, highlighting their roles, functionalities, and interactions with other components.
