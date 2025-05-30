## cosmwasm - Chunk 23

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

This will query the blockchain and return a JSON object containing the addresses of the contracts associated with the given Code ID. wasmd q wasm list-contract-by-code $CODE_ID -o json
The command will return a JSON object similar to the following:

{
  "contracts": [
    "wasm1wug8sewp6cedgkmrmvhl3lf3tulagm9hnvy8p0rppz9yjw0g4wtqhs9hr8",
    "wasm19ph090ka8tzrd2wrp8gnn7lachwt7r2npvf6rdnd3ha3jv5n5gqquzcpd0"
  ],
  "pagination": {
    "next_key": null,
    "total": "0"
  }
}
In this example, there are two contracts associated with the Code ID. Query contracts by creator
To get a list of contracts instantiated by a specific creator, you can use the following command. This will query the blockchain and return a JSON object containing the addresses of the contracts associated with the given creator’s address.

---

**LLM Contextual Output:**

This text chunk is explaining how to use the `cw-storage-plus` library in CosmWasm smart contracts to manage data storage efficiently.

Here's a focused analysis:

1. **Technical Details**: The chunk describes the JSON object returned by the `wasmd q wasm list-contract-by-code $CODE_ID -o json` command, which contains information about the addresses of the contracts associated with the given Code ID.
2. **Context Connection**: This chunk builds upon the surrounding context of an introduction to storage in CosmWasm smart contracts, explaining why persisting data across contract calls is essential and how on-chain storage can be costly.
3. **Requirements and Conditions**: The chunk mentions that long keys can impact storage performance, so it recommends using single-character ASCII prefixes for better performance.

Some specific points of interest:

* The use of `cw-storage-plus` library simplifies the process of storing and managing data in CosmWasm smart contracts by providing a type-safe interface.
* Key management is crucial to ensure unique keys and manage namespace conflicts.
* Performance optimization is essential, particularly when dealing with long keys.

The chunk does not mention any specific technical parameters or processes for persisting data across contract calls or implementing complex functionalities like token balances, voting systems, or games. It appears that these topics are discussed in the surrounding context of an introduction to storage in CosmWasm smart contracts.
