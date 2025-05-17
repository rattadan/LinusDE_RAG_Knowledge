## cosmwasm - Chunk 24

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

wasmd q wasm list-contracts-by-creator $BOB_ADDR -o json
The command will return a JSON object similar to the following:

{
  "contract_addresses": [],
  "pagination": {
    "next_key": null,
    "total": "0"
  }
}
In this example, there are no contract addresses associated with Bob’s address. Execution
Executing a command on a Wasm contract involves sending a message to the contract. Execute a command on a wasm contract
First, we have to define the message to send to the contract.

---

**LLM Contextual Output:**

This text chunk is explaining the technical details and parameters of the `cw-storage-plus` library, specifically its key management features.

Here's a breakdown of the key points mentioned in this chunk:

1. **Type-Safe Interface**: The library provides a type-safe interface for storing and retrieving data.
2. **Key Management**: The key management system ensures unique keys and manages namespace conflicts by providing a prefix to generate keys for individual values.
3. **Persistent Data Structures**: `cw-storage-plus` implements feature-rich collections like maps, deques, etc., which can store multiple values.

The chunk also mentions the following requirements:

1. **Key Conflicts**: The library tries to manage key collisions through unique prefixes, but it's still essential to ensure that keys are unique and do not conflict with other parts of the contract.
2. **Performance**: Long keys can impact storage performance; use single-character ASCII prefixes for better performance.

The chunk connects this information to its surrounding context by:

1. **Linking to the CosmWasm Smart Contracts Introduction**: The text begins with an introduction to storage in CosmWasm smart contracts, providing context for understanding the library's features.
2. **Establishing Context**: The text assumes familiarity with CosmWasm and its concepts, such as on-chain storage limits, key management, and persistent data structures.

Overall, this chunk provides a detailed explanation of the `cw-storage-plus` library's technical features and requirements, which is essential for building complex stateful functionalities in CosmWasm smart contracts.
