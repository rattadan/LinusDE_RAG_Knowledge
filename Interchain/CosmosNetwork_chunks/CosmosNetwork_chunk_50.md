## CosmosNetwork - Chunk 50

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

Atoms are a license for the holder to vote, validate, or delegate to other validators. Like Ethereum's ether, atoms can also be used to pay for transaction fees to mitigate spam. Additional inflationary atoms and block transaction fees are rewarded to validators and delegators who delegate to validators. The BurnAtomTx transaction can be used to recover any proportionate amount of tokens from the reserve pool. Fundraiser
The initial distribution of atom tokens and validators on Genesis will go to the donors of the Cosmos Fundraiser (75%), lead donors (5%), Cosmos Network Foundation (10%), and ALL IN BITS, Inc (10%). From genesis onward, 1/3 of the total amount of atoms will be rewarded to bonded validators and delegators every year. See the Cosmos Plan for additional details. Limitations on the Number of Validators
Unlike Bitcoin or other proof-of-work blockchains, a Tendermint blockchain gets slower with more validators due to the increased communication complexity.

---

**LLM Contextual Output:**

Analysis:

1. **Technical Details:**
   - The chunk describes the technical process and parameters involved in Tendermint Core's consensus logic.
   - It outlines how Tendermint Core processes transactions (AppendTx), validates them (CheckTx), and computes cryptographic commitments (Commit).
   - The focus on Byzantine Fault Tolerance (BFT) and social consensus mechanisms is noted, highlighting their role in ensuring the reliability of the network.

2. **Context Connection:**
   - This chunk connects to the surrounding context by providing an overview of Tendermint Core's architecture, Application Binary Interface (ABCI), and application logic.
   - It also establishes a foundation for understanding the key components involved in Tendermint Core's consensus mechanism and its interactions with application logic.

3. **Requirements and Conditions:**
   - The requirements mentioned include:
     - A blockchain network
     - A consensus algorithm to ensure agreement among nodes
     - A cryptographic mechanism to secure transactions
     - An ability to handle Byzantine faults through social consensus mechanisms

This chunk explains the technical process and parameters involved in Tendermint Core's consensus logic, including its role in ensuring the reliability of the network. It also establishes a foundation for understanding the key components and their interactions with application logic, providing context for the broader discussion on Tendermint Core's architecture and its Application Binary Interface (ABCI).
