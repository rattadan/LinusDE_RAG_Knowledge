## CosmosNetwork - Chunk 6

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

It allows developers to solely focus on the application layer, saving them a lot of time. Tendermint engine employs a byzantine fault-tolerant (BFT) consensus algorithm. It connects to the application layer via the Application Blockchain Interface (ABCI). It's a protocol that allows developers to use any programming language they want. That way, they could use the language that best fits their needs. Tendermint BFT allows developers to build public AND private blockchains on top of it. That's because it handles the networking and the consensus layers. The developers have the complete freedom to define the application layer. Now that's open-mindedness. Tendermint BFT can have a block time on the order of 1 second, and can handle thousands of transactions per second. And it only needs a third of the validator nodes to be honest, to function without any forks. This means that we, the users, can get instant finality on our transactions. Now, on to the next tool in the Cosmos' tech stack.

---

**LLM Contextual Output:**

This text chunk is providing technical details and parameters for Tendermint Core's Architecture and its Application Binary Interface (ABCI). It focuses specifically on:

1. **Technical Details**: The BFT consensus algorithm implemented by Tendermint Core, which allows it to achieve Byzantine Fault Tolerance and can handle a significant portion of the validator nodes with a small number of honest validators.
2. **Connection to surrounding context**: This chunk builds upon the understanding of Tendermint's architecture, Application Binary Interface (ABCI), and its role in facilitating communication between Tendermint Core and application logic.
3. **Specific requirements, conditions, or constraints**: The technical parameters and algorithms used by Tendermint Core are essential for understanding how it ensures consistency, reliability, and fault tolerance in blockchain operations.

The chunk is structured as a detailed breakdown of the `AppendTx` message flow, which allows developers to understand how Tendermint Core validates and includes transactions in the blockchain. This information is crucial for building public and private blockchains on top of Tendermint BFT.

Some key points from this text chunk include:

- The ability to handle Byzantine faults through social consensus mechanisms.
- A block time on the order of 1 second, allowing thousands of transactions per second.
- Only requiring a third of the validator nodes to be honest for instant finality on transactions.
- The open-minded approach to defining the application layer, giving developers flexibility in choosing programming languages and technologies.

Overall, this text chunk provides critical information about Tendermint Core's architecture and its Application Binary Interface (ABCI), which is essential for building robust blockchain systems.
