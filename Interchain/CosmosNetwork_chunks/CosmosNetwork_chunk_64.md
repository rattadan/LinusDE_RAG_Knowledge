## CosmosNetwork - Chunk 64

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

BitcoinNG
BitcoinNG is a proposed improvement to Bitcoin that would allow for forms of vertical scalability, such as increasing the block size, without the negative economic consequences typically associated with such a change, such as the disproportionately large impact on small miners. This improvement is achieved by separating leader election from transaction broadcast: leaders are first elected by proof-of-work in "key-blocks", and then able to broadcast transactions to be committed until a new key-block is found. This reduces the bandwidth requirements necessary to win the PoW race, allowing small miners to more fairly compete, and allowing transactions to be committed more regularly by the last miner to find a key-block. Casper
Casper [16] is a proposed proof-of-stake consensus algorithm for Ethereum. Its prime mode of operation is "consensus-by-bet".

---

**LLM Contextual Output:**

This text chunk is providing detailed technical information about two different blockchain projects: Tendermint Core and Casper.

**1. Technical Details, Parameters, or Processes Described in this Chunk:**

- Block Proposal: The process of proposing new blocks based on transaction data.
- Commit Vote: Collecting votes from validators to finalize a block.
- Consensus Logic: Implementing Byzantine Fault Tolerance (BFT) logic for Tendermint Core.

**2. How this Chunk Connects to or Builds Upon the Surrounding Context:**

This chunk is directly related to the surrounding context of Tendermint Core's architecture and Application Binary Interface (ABCI). It provides detailed information about the technical aspects of Tendermint Core, specifically its consensus mechanism and leader election process, which are essential components of its overall design.

**3. Specific Requirements, Conditions, or Constraints Mentioned:**

- A Byzantine Fault Tolerance (BFT) requirement in Tendermint Core.
- The need for small miners to be able to compete fairly with larger ones.
- The importance of reducing bandwidth requirements necessary to win the proof-of-work race.
- The goal of allowing transactions to be committed regularly by the last miner to find a key-block.

This chunk is explaining how Tendermint Core's consensus mechanism and leader election process work, which are critical components of its design. It sets the stage for understanding the surrounding context, Tendermint Core's architecture, and Application Binary Interface (ABCI), providing specific details about the technical aspects of these projects.
