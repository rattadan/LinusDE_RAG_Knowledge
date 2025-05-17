## CosmosNetwork - Chunk 55

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

In order to encourage the discovery and early reporting of found vulnerabilities, the Cosmos Hub encourages hackers to publish successful exploits via a ReportHackTx transaction that says, "This validator got hacked. Please send bounty to this address". Upon such an exploit, the validator and delegators will become inactive, HackPunishmentRatio (default 5%) of everyone's atoms will get slashed, and HackRewardRatio (default 5%) of everyone's atoms will get rewarded to the hacker's bounty address. The validator must recover the remaining atoms by using their backup key. In order to prevent this feature from being abused to transfer unvested atoms, the portion of vested vs unvested atoms of validators and delegators before and after the ReportHackTx will remain the same, and the hacker bounty will include some unvested atoms, if any.

---

**LLM Contextual Output:**

This text chunk is explaining the technical details and parameters related to Tendermint Core's Application Binary Interface (ABCI) for consensus.

**Context**: This context assumes that the reader has a basic understanding of blockchain and cryptocurrency concepts, specifically focusing on the Tendermint Core implementation.

**Analysis 1: Technical Details**

- **Block Proposal**: Proposes new blocks based on transaction data.
- **Commit Vote**: Collects votes from validators to finalize a block.
- **Consensus Logic**: Implements Byzantine Fault Tolerance (BFT) logic for handling network partitions and censorship attacks.

**Analysis 2: Connection to surrounding context**

This chunk builds upon the understanding of Tendermint Core's architecture and its components, specifically highlighting the role of consensus in blockchain operations. It also provides a detailed explanation of how the ABCI interface facilitates communication between application logic and Tendermint Core, enabling validation, state updates, and coordination with validators.

**Analysis 3: Requirements and Conditions**

- **Vulnerability reporting**: The text assumes the existence of vulnerable transactions or states that can be exploited to gain unauthorized control (e.g., by hackers) through a ReportHackTx transaction.
- **Validator status**: The chunk mentions the need for a validator to become inactive if an exploit is reported, which implies a specific condition (i.e., recovery of remaining atoms after a failed report).
- **Atomic balance management**: The text ensures that the portion of vested vs unvested atoms among validators and delegators remains unchanged before and after a ReportHackTx transaction.

This chunk provides detailed technical explanations for Tendermint Core's ABCI, highlighting its role in facilitating consensus operations within the blockchain ecosystem.
