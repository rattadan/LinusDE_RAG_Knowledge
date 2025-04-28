## cosmwasm - Chunk 13

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

It is optional, and the default value is Everybody, which means everybody can create an instance of the uploaded Wasm code
Download code
You can download the code associated with a specific code ID by running the following command:

wasmd q wasm code $CODE_ID downloaded_code.wasm
This command retrieves the Wasm code from the blockchain and saves it to a file named downloaded_code.wasm. Instantiation
In this section, you will create a new instance of the uploaded Wasm contract. This involves using the wasmd tx wasm instantiate command to instantiate the contract, and then querying the blockchain to obtain the contract’s address.

---

**LLM Contextual Output:**

This text chunk is explaining how to use the `cw-storage-plus` library in CosmWasm smart contracts to manage data persistently.

**Technical Details:**

* The chunk describes the type-safe interface provided by `cw-storage-plus`, which simplifies storing and retrieving data.
* It mentions the key management system, including unique prefixes for keys, value serialization using JSON, and support for single-character ASCII prefixes.
* The example usage demonstrates how to create an instance of a storage container (`Item`) and use it to store values.

**Context:**

The text is part of an introduction or documentation section in CosmWasm that explains the basics of storing data in smart contracts. It assumes some basic knowledge of Wasm and its ecosystem, as well as familiarity with JSON serialization using `serde` libraries.

**Connections to Surrounding Context:**

* The chunk builds upon the idea of on-chain storage limits discussed earlier in the introduction.
* It provides an overview of the key concepts and features introduced in this section, which is likely a new concept for readers who are not familiar with Wasm or its ecosystem.
* The example usage shows how to use `cw-storage-plus` in practice, demonstrating its potential applications in smart contract development.

**Requirements, Conditions, or Constraints:**

* None mentioned.
