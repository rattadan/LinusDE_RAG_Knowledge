## CosmosNetwork - Chunk 67

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

In a token transfer over IBC, the validator-set of the receiver's blockchain is responsible for providing confirmation, not the receiving user. The most striking difference is that ILP's connectors are not responsible or keeping authoritative state about payments, whereas in Cosmos, the validators of a hub are the authority of the state of IBC token transfers as well as the authority of the amount of tokens held by each zone (but not the amount of tokens held by each account within a zone). This is the fundamental innovation that allows for secure asymmetric transfer of tokens from zone to zone; the analog to ILP's connector in Cosmos is a persistent and maximally secure blockchain ledger, the Cosmos Hub. The inter-ledger payments in ILP need to be backed by an exchange orderbook, as there is no asymmetric transfer of coins from one ledger to another, only the transfer of value or market equivalents.

---

**LLM Contextual Output:**

This text chunk provides detailed technical information about Tendermint Core's architecture and its Application Binary Interface (ABCI). Here's a focused analysis of what this specific section is explaining:

**Technical Details:**

1. **Block Proposal**: The block proposal involves proposing new blocks based on transaction data, which requires Tendermint Core to compute the commit state.
2. **Commit Vote**: Collecting votes from validators to finalize a block involves voting with their voting power, which ensures that the majority of validators agree on the final outcome.
3. **Consensus Logic**: Implementing Byzantine Fault Tolerance (BFT) logic is crucial for ensuring the integrity and security of the blockchain.

**Context Connection:**

This chunk builds upon the surrounding context by:

1. Providing an overview of Tendermint Core's architecture, highlighting its key components and functionalities.
2. Introducing the concept of Application Binary Interface (ABCI), which allows application logic to interact with Tendermint Core's consensus mechanism.
3. Discussing the significance of Validator Set Management in handling Byzantine faults.

**Requirements and Conditions:**

1. The chunk mentions that the inter-ledger payments in ILP need to be backed by an exchange orderbook, indicating a specific requirement for secure asymmetric transfer of tokens from one ledger to another.
2. The text also highlights the importance of persistent and maximally secure blockchain ledgers, such as those found in Cosmos Hub.

**Specific Requirements:**

1. The chunk mentions that ILP's connectors are not responsible or keeping authoritative state about payments, implying a need for a robust system to ensure secure payment transfers.

Overall, this chunk provides detailed technical information about Tendermint Core's architecture and its Application Binary Interface (ABCI), highlighting the importance of consensus logic and Validator Set Management in ensuring the integrity and security of the blockchain.
