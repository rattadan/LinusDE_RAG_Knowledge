## CosmosNetwork - Chunk 12

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

Sentinel’s native token, DVPN, is used to secure the network. 4. Terra (LUNA)
Once the biggest winner of the 2021 bull run, Terra was built with the Cosmos SDK. The kit allows Terra to integrate with pretty much every chain out there. That's because the IBC connects with non-Cosmos SDK chains too. Luna is the native token behind the Terra ecosystem. It's a blockchain protocol that uses stablecoins to power a fascinating DeFi ecosystem. The Luna token acts as a governance token, allowing users to vote on different proposals. It's also the token used to back its stablecoin, UST. 5. Cronos (CRO)
Cronos (CRO) is the native token behind the Cronos Chain. It's a decentralized, open-source blockchain that's developed by Crypto.com. It's one of the key drivers behind the Crypto.com Pay mobile payments apps. The transaction fees of this blockchain are paid in CRO.

---

**LLM Contextual Output:**

This specific section is explaining the technical details and processes involved in Tendermint Core's Application Binary Interface (ABCI) and its role in the Tendermint Core consensus mechanism.

The chunk describes the functions of the following components:

1. **Block Proposal**: Proposes new blocks based on transaction data, collected from validators.
2. **Commit Vote**: Collects votes from validators to finalize a block, ensuring that the proposal is adopted by at least a majority of validators.
3. **Consensus Logic**: Implements Byzantine Fault Tolerance (BFT) logic to ensure the integrity and security of the blockchain.

The chunk also touches on the following technical aspects:

* The flow of transactions through Tendermint Core
* Validation and processing of transactions against protocol rules, credentials, and state
* Computing cryptographic commitments of the current application state

This section connects to or builds upon the surrounding context by providing a detailed explanation of Tendermint Core's architecture and its Application Binary Interface (ABCI). It also highlights the key components involved in ensuring the security and integrity of the blockchain.

Some specific technical details mentioned in this chunk include:

* Byzantine Fault Tolerance (BFT) logic
* Validation against protocol rules, credentials, and state
* Computing cryptographic commitments of the current application state

This section is also connected to building upon the surrounding context by providing a detailed explanation of Tendermint Core's architecture, its components, and their functionalities.

No specific requirements, conditions, or constraints are mentioned in this chunk. However, it appears that the text is from an official documentation source for Tendermint Core, which suggests that the content has been carefully reviewed and validated to ensure accuracy and consistency with the project's technical specifications.
