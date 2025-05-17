## CosmosNetwork - Chunk 33

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

While each zone may be a Tendermint blockchain that is secured by as few as 4 (or even less if BFT consensus is not needed), the Hub must be secured by a globally decentralized set of validators that can withstand the most severe attack scenarios, such as a continental network partition or a nation-state sponsored attack. The Zones
A Cosmos zone is an independent blockchain that exchanges IBC messages with the Hub. From the Hub's perspective, a zone is a multi-asset dynamic-membership multi-signature account that can send and receive tokens using IBC packets. Like a cryptocurrency account, a zone cannot transfer more tokens than it has, but can receive tokens from others who have them. A zone may be designated as an "source" of one or more token types, granting it the power to inflate that token supply. Atoms of the Cosmos Hub may be staked by validators of a zone connected to the Hub.

---

**LLM Contextual Output:**

Here's a focused analysis of the current text chunk and its context:

**Technical Details/Parameters:**

- The block proposal and commit vote processes involve sending transactions via AppendTx messages.
- CheckTx involves validating transactions before inclusion in blocks, which are relayed to other peers for further validation.
- Tendermint Core computes a cryptographic commitment of the current application state using Commit Message.

**Context Connection/Building Upon:**

- This text chunk provides an overview of Tendermint Core's architecture and its Application Binary Interface (ABCI).
- It breaks down the key components and their functionalities, providing details on how they interact with each other.
- The context is built upon the surrounding explanation of Tendermint Core's role in consensus, validation, and block propagation.

**Specific Requirements/Conditions:**

- The Hub must be secured by a globally decentralized set of validators to withstand severe attack scenarios.
- Zones are independent blockchains that exchange IBC messages with the Hub and can send and receive tokens using IBC packets.
- Zones may be designated as source tokens for inflation or have their atoms staked by validators connected to the Hub.

This text chunk is providing a detailed explanation of Tendermint Core's architecture, focusing on its components, processes, and interactions. It provides context for understanding the broader framework in which Tendermint Core operates, including how it handles block propagation, validation, and consensus mechanisms.
