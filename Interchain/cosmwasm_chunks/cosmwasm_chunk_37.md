## cosmwasm - Chunk 37

**Document Summary:**

### Introduction to Storage in CosmWasm Smart Contracts

#### Why Persistent Data?
Persisting data across contract calls is essential for implementing complex functionalities such as token balances, voting systems, or games. Without storage, a smart contract would be limited in its ability to maintain state between transactions.

#### On-Chain Storage Limits
On-chain storage can be costly due to the nature of blockchain technology. It's generally advisable to keep stored data minimal and consider off-chain solutions for larger datasets (e.g., IPFS).

#### What Does cw-storage-plus Build Upon?
The CosmWasm framework itself provides a simple, raw API for binary key-value storage. However, this can be cumbersome to use directly. `cw-storage-plus` is a library that builds on top of this base API by providing:

1. **Type-Safe Interface**: Simplifying the process of storing and retrieving data.
2. **Key Management**: Ensuring unique keys and managing namespace conflicts.
3. **Persistent Data Structures**: Implementing feature-rich collections like maps, deques, etc.

### Basics of Storage Containers

#### Containers
- **Item**: A simple container for a single value.
- **Map**: A collection capable of storing multiple values with methods to interact with them.
- **Deque**: A double-ended queue that can store and manage elements efficiently.

#### Keys and Prefixes
Keys are crucial in managing the namespace. When you create a storage container, you must provide a key as a string literal or constant. For `Item`, this is the exact key under which the value will be saved. For collections like `Map` and `Deque`, the provided string acts as a prefix, used to generate keys for individual values.

### Key Management
It's essential to ensure that your keys are unique and do not conflict with other parts of the contract. Long keys can impact storage performance, so consider using single-character ASCII prefixes (e.g., "a", "b", "c").

#### Value Serialization
Values in `cw-storage-plus` are stored using JSON serialization via serde-json-wasm. This requires your data types to implement `serde::Serialize` and `serde::Deserialize`.

### Example Usage

#### Using Item
```rust
use cw_storage_plus::Item;

pub static BALANCE: Item<u128> = Item::new("balance");

fn main() {
    let mut storage = Storage::new();
    
    // Save a balance value
    BALANCE.save(&mut storage, &100).unwrap();

    // Load the balance value
    let balance: u128 = BALANCE.load(&storage);
}
```

#### Using Map
```rust
use cw_storage_plus::{Map, Item};

pub static BALANCES: Map<String, u128> = Map::new("balances");

fn main() {
    let mut storage = Storage::new();
    
    // Save balances for multiple users
    BALANCES.save(&mut storage, "alice", &50).unwrap();
    BALANCES.save(&mut storage, "bob", &75).unwrap();

    // Load a balance value
    let alice_balance: u128 = BALANCES.load(&storage, "alice");
}
```

#### Using Deque
```rust
use cw_storage_plus::{Deque, Item};

pub static HISTORY: Deque<u32> = Deque::new("history");

fn main() {
    let mut storage = Storage::new();
    
    // Push elements into the deque
    HISTORY.push_back(&mut storage, &1).unwrap();
    HISTORY.push_back(&mut storage, &2).unwrap();

    // Pop an element from the deque
    let last_value: u32 = HISTORY.pop_back(&mut storage);
}
```

### Key Considerations

- **Key Conflicts**: While `cw-storage-plus` tries to manage key collisions through unique prefixes, it's still important to ensure that your keys are unique and do not conflict with other parts of the contract.
- **Performance**: Long keys can impact storage performance. Use single-character ASCII prefixes for better performance.

### Conclusion
Using `cw-storage-plus` simplifies the process of storing and managing data in CosmWasm smart contracts, making it easier to implement complex stateful functionalities while maintaining type safety and performance optimization.

**Original Text:**

Execution: If the proposal passes, it is executed according to the details specified in the proposal, such as implementing a parameter change or initiating a software upgrade. In this section, we’ll dive into how to submit CosmWasm proposals. The submission process is a bit different from the Cosmos SDK, but the rest, including the deposit period, voting, tallying, and execution, follows the usual Cosmos SDK governance process. For more details on the gov module, check out the Cosmos SDK Governance Documentation and the Cosmos SDK Proposal Tutorial. Submit a CosmWasm proposal
You can submit a CosmWasm proposal using the wasmd tx wasm submit-proposal command. To see a full list of available proposal types, simply add the --help flag. Many of these commands, like wasm-store, instantiate-contract, execute-contract, migrate-contract, are similar to the standard tx commands and won’t be covered in detail here.

---

**LLM Contextual Output:**

This text chunk is providing technical details on how to use a library called `cw-storage-plus` within a CosmWasm smart contract.

**Technical Details:**

- The chunk explains that `cw-storage-plus` provides a type-safe interface for storing and retrieving data.
- It mentions the key management system, which ensures unique keys and manages namespace conflicts using single-character ASCII prefixes for collections like maps and deques.
- Key serialization uses JSON serialization via serde-json-wasm.

**Connecting to Surrounding Context:**

This chunk connects to the surrounding context by:

- Providing examples of how to use `cw-storage-plus` in a CosmWasm smart contract, demonstrating its usage with items, maps, and deques.
- Explaining key management best practices, such as using single-character ASCII prefixes for long keys.

**Requirements, Conditions, or Constraints:**

This chunk does not explicitly mention any specific requirements, conditions, or constraints. However:

- It provides examples of how to submit a CosmWasm proposal using the `wasm-store` command.
- The document also mentions that the `gov module` has details on the governance process for submitting proposals, but these are not relevant to this specific chunk.

**Focus:**

The focus of this chunk is primarily technical and provides information on how to use the `cw-storage-plus` library within a CosmWasm smart contract. The surrounding context includes examples of how to use the library in different scenarios.
