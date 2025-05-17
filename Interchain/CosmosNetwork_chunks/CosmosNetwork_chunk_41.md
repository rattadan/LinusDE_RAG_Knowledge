## CosmosNetwork - Chunk 41

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

On the Ethereum side (the origin), a bridge-contract would allow ether holders to send ether to the bridge-zone by sending it to the bridge-contract on Ethereum. Once ether is received by the bridge-contract, the ether cannot be withdrawn unless an appropriate IBC packet is received by the bridge-contract from the bridge-zone. The bridge-contract tracks the validator-set of the bridge-zone, which may be identical to the Cosmos Hub's validator-set. In the case of Bitcoin, the concept is similar except that instead of a single bridge-contract, each UTXO would be controlled by a threshold multisignature P2SH pubscript. Due to the limitations of the P2SH system, the signers cannot be identical to the Cosmos Hub validator-set. Withdrawing Tokens from Cosmos Hub
Ether on the bridge-zone ("bridged-ether") can be transferred to and from the Hub, and later be destroyed with a transaction that sends it to a particular withdrawal address on Ethereum.

---

**LLM Contextual Output:**

The current text chunk is explaining the technical details of Inter-Blockchain Communication (IBC) between Ethereum and Cosmos Hub.

**Technical Details:**

* **IBC Message Flow:** The chunk describes how IBC messages flow between Ethereum and Cosmos Hub.
  - `AppendTx` message: a transaction for validation and inclusion in the blockchain on Ethereum, which is then relayed to other peers for further validation before being included in a block on Cosmos Hub.
  - `CheckTx` message: validates transactions before they are included in a block on both platforms. If valid, it's relayed to other peers for further validation.
* **IBC Flow:** The chunk explains how IBC flows between the Ethereum bridge-contract and Cosmos Hub, specifically:
  - Bridging Ether from Ethereum to Cosmos Hub via an `AppendTx` message.
  - Tracking validator-set between the two platforms using their respective `Bridge-Zone`.
  - Handling Byzantine faults by ensuring social consensus mechanisms are in place for both platforms.

**Context Building:**

* The chunk is connected to the surrounding context by explaining how IBC enables communication and interaction between Ethereum and Cosmos Hub, specifically:
 + Bridging Ether from one platform to another.
 + Tracking validator-set between the two platforms using their respective `Bridge-Zone`.
 + Handling Byzantine faults through social consensus mechanisms.

**Requirements and Conditions:**

* **IBC Requirements:** The chunk requires understanding of IBC principles, including message flow, validation, and consistency.
* **Conditions:** The chunk assumes familiarity with blockchain concepts, such as Ethereum's bridge-contract and Cosmos Hub's validator-set.
