## cosmwasm - Chunk 56

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

In storey, you would use composition: multiple maps within a map, which would look like this: Map<Addr, Map<Token, Item<u128>>>. Here’s a simple example:

use cw_storage_plus::Map;
 
type Address = String;
type Token = String;
 
let balances: Map<(Address, Token), u128> = Map::new("b");
 
balances
    .save(
        &mut storage,
        ("alice".to_string(), "uusd".to_string()),
        &100,
    )
    .unwrap();
 
assert_eq!(
    balances
        .load(&storage, ("alice".to_string(), "uusd".to_string()))
        .unwrap(),
    100
);
For more features and examples, see the map documentation. Introduction
Not being able to persist data across calls would limit the utility of smart contracts. Think of these problems:

How could a smart contract implement a token if it could not keep track of balances? How could a smart contract implement a voting system if it could not keep track of votes? How could a smart contract implement a game if it could not keep track of scores?

---

**LLM Contextual Output:**

The current text chunk is explaining the technical details and parameters used in `cw-storage-plus`, which is a library for storing data in CosmWasm smart contracts. Here's a focused analysis:

1. **Technical Details:**

* The example demonstrates how to create multiple maps within a map using composition.
* Each map has three fields: `Addr` (address), `Token` (token name), and `Item` (data type).
* The `balances` map is an example of a simple store, where each address is associated with a token balance.

2. **Context Connection:**

This chunk builds upon the surrounding context by introducing new concepts and technologies:

* CosmWasm smart contracts have limitations in terms of persisting data across contract calls.
* `cw-storage-plus` provides a library for storing data using a composition approach, which is more efficient than storing data directly on the blockchain.

3. **Requirements, Conditions, or Constraints:**

The requirements mentioned are:

* **Type Safety**: The code requires the data types to implement `serde::Serialize` and `serde::Deserialize`.
* **Performance Optimization**: The use of single-character ASCII prefixes for better performance.
* **Unique Keys**: Ensuring that keys are unique and do not conflict with other parts of the contract.

Overall, this chunk is explaining how to store data in CosmWasm smart contracts using a library like `cw-storage-plus`, which provides a simpler way to implement complex stateful functionalities while maintaining type safety and performance optimization.
