## CosmosNetwork - Chunk 36

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

acknowledged), while allowing for complete freedom on the sending chain as to how many outbound packets are allowed. Figure of Zone1, Zone2, and Hub IBC without
acknowledgement

In the example above, in order to update the block-hash of "Zone1" on "Hub" (or of "Hub" on "Zone2"), an `IBCBlockCommitTx` transaction must be posted on "Hub" with the block-hash of "Zone1" (or on "Zone2" with the block-hash of "Hub"). See IBCBlockCommitTx and IBCPacketTx for for more information on the two IBC transaction types. Use Cases
Distributed Exchange
In the same way that Bitcoin is more secure by being a distributed, mass-replicated ledger, we can make exchanges less vulnerable to external and internal hacks by running it on the blockchain. We call this a distributed exchange. What the cryptocurrency community calls a decentralized exchange today are based on something called "atomic cross-chain" (AXC) transactions.

---

**LLM Contextual Output:**

I'll analyze the given text chunk focusing on the exact technical details, parameters, or processes described in this chunk.

**Technical Details:**

1. **IBCBlockCommitTx**: A transaction type used for committing a block to the blockchain. It is an `IBC` (Inter-Blockchain Communication) transaction type, which allows applications to send data between different blockchains.
2. **IBCPacketTx**: An IBC packet transmission protocol that enables sending data between two blockchains over the internet.
3. **Zone1**, **Zone2**, and **Hub IBC without acknowledgement**: This refers to a specific architecture or configuration for inter-blockchain communication (IBC) transactions, where packets are transmitted without explicitly acknowledging receipt.

**Context Connection:**

The context is Tendermint Core's Application Binary Interface (ABCI), which provides an interface for the application logic to interact with the consensus mechanism. The IBCBlockCommitTx and IBCPacketTx transaction types are part of this interaction, allowing applications to send data between blockchains in a secure and controlled manner.

**Requirements and Conditions:**

1. **Inter-blockchain communication (IBC)**: To enable this technology, the application must be able to communicate with other blockchains over an internet connection.
2. **Distributed exchange**: The ability to facilitate decentralized transactions between different blockchains is required for distributed exchanges to function.
3. **Atomic cross-chain transactions (AXC)**: This refers to the use of IBC to enable secure and controlled communication between blockchains, which is a specific requirement for atomic cross-chain transactions.

**Additional Insights:**

1. The text mentions that Zone1, Zone2, and Hub IBC without acknowledgement are part of an architecture or configuration, suggesting that this technology may require additional setup or configuration beyond the standard Tendermint Core environment.
2. The mention of distributed exchanges and atomic cross-chain transactions implies a level of complexity and sophistication in implementing this technology, which may require specialized expertise or infrastructure.
