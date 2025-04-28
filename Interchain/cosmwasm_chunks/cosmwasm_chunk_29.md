## cosmwasm - Chunk 29

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

We can decode the contract state using the following command:

wasmd query wasm contract-state all "$CONTRACT" -o json | jq -r '.models[0].value' | base64 -d
The output will be similar to the following:

{
  "verifier": "wasm1hvgm6p76gccgg4dl4caa8a7v03dsqww6r9sk4g",
  "beneficiary": "wasm1pa29lac5s85kgj7pn9z6gc0t4sqgzllcguhf24",
  "funder": "wasm1hvgm6p76gccgg4dl4caa8a7v03dsqww6r9sk4g"
}
Migration
Migration is the process of upgrading an existing contract to a new version without changing its address or losing its state. This ensures that the contract can evolve over time while preserving the data of the original contract.

---

**LLM Contextual Output:**

The current text chunk is explaining the technical details and parameters, processes, and requirements associated with using the `cw-storage-plus` library in CosmWasm smart contracts.

Here's a breakdown of what this specific section is explaining:

1. **Technical Details**:
	* The library provides a type-safe interface for storing and retrieving data.
	* It uses JSON serialization via serde-json-wasm to store values.
2. **Processes and Requirements**:
	* The library simplifies the process of storing and managing data in CosmWasm smart contracts, making it easier to implement complex stateful functionalities.
	* It ensures unique keys for storage containers, with single-character ASCII prefixes being used for better performance.
3. **Contextual Connection**:
	* This chunk is connected to the surrounding context, which discusses the importance of persistent data in CosmWasm smart contracts and how on-chain storage can be costly.

To analyze this section further, here are some specific requirements, conditions, or constraints mentioned:

1. **Unique Keys**: The library ensures that keys are unique for storage containers.
2. **Performance Optimization**: The library aims to optimize performance by using single-character ASCII prefixes for better performance.
3. **Data Types and Serialization**: The library is designed to work with various data types, including `u128` values, which need to implement `serde::Serialize` and `serde::Deserialize`.
4. **Specific Requirements for CosmWasm**:
	* The library likely requires knowledge of the CosmWasm framework and its API.
	* It may also require an understanding of how on-chain storage works in CosmWasm.

Overall, this section provides detailed information about the technical aspects of using `cw-storage-plus` in CosmWasm smart contracts, including its features, processes, and requirements.
