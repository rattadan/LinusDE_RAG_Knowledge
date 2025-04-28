## CosmosNetwork - Chunk 56

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

Governance Specification
The Cosmos Hub is operated by a distributed organization that requires a well-defined governance mechanism in order to coordinate various changes to the blockchain, such as the variable parameters of the system, as well as software upgrades and constitutional amendments. All validators are responsible for voting on all proposals. Failing to vote on a proposal in a timely manner will result in the validator being deactivated automatically for a period of time called the AbsenteeismPenaltyPeriod (DEFAULT 1 week). Delegators automatically inherit the vote of the delegated validator. This vote may be overridden manually. Unbonded atoms get no vote. Each proposal requires a deposit of MinimumProposalDeposit tokens, which may be a combination of one or more tokens including atoms. For each proposal, the voters may vote to take the deposit. If more than half of the voters choose to take the deposit (e.g.

---

**LLM Contextual Output:**

Analysis of the current text chunk:

1. **Technical details and parameters**: The chunk provides detailed information about the Governance Specification's components, such as validators, proposals, voting mechanisms, token deposits, and constitutional amendments.

2. **Connection to or building upon surrounding context**: This chunk builds upon the overall architecture and Application Binary Interface (ABCI) overview provided earlier. It expands on the details of Tendermint Core, including its role in consensus, validation, and block propagation, as well as the ABCI interface for application logic interactions.

3. **Specific requirements, conditions, or constraints**: The Governance Specification outlines key aspects that validators must comply with, such as voting on proposals within a timely manner, depositing minimum token amounts, and overriding manual overrides. It also specifies the structure of proposals, including voters' roles, deposit mechanics, and bonding mechanisms to ensure decentralization.

Specific technical details mentioned in this chunk include:

- Validator management: The specification explains how validators are managed, including their voting power, role in proposing new blocks, and participation in the consensus mechanism.
- Proposal structure: Details on proposal formats, components (e.g., minimum token deposits), and voters' roles (including delegators) are provided.

The Governance Specification is essential for ensuring the decentralized and resilient functioning of the Cosmos Hub network. It provides a framework for validators to operate within, addressing concerns related to Byzantine faults, censorship attacks, and social consensus mechanisms.
