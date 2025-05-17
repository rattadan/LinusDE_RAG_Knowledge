## cosmwasm - Chunk 42

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

messages: This array contains the specific actions or commands the proposal intends to execute. status: Indicates the current status of the proposal. final_tally_result: Shows the results of the voting on the proposal. submit_time: The timestamp indicating when the proposal was submitted. deposit_end_time: The timestamp indicating when the deposit period ends. total_deposit: This is the amount of tokens that has been deposited to support the proposal. title: Title of the proposal. summary: Summary of the proposal. proposer: The address of the entity that submitted the proposal. After the deposit period and voting period, if the proposal passes and is executed, the code is then pinned. You can verify the pinned codes by querying them with the following command:

wasmd q wasm pinned -o json
The command will return a JSON object similar to the following:

{
  "code_ids": [1, 2, 3],
  "pagination": {
    "next_key": null,
    "total": "0"
  }
}
The code_ids array lists all the code IDs that are currently pinned.

---

**LLM Contextual Output:**

This text chunk is analyzing a section of documentation for CosmWasm smart contracts, specifically describing the technical details and processes related to storage in these contracts.

Here's a breakdown of what this chunk is explaining:

1. **Technical Details**: The chunk discusses various technical aspects of storing data in CosmWasm smart contracts, including:
	* Type-safe interface: `cw-storage-plus` provides a simplified way to store and retrieve data.
	* Key management: Ensuring unique keys and managing namespace conflicts is crucial.
	* Persistent data structures: Implementing feature-rich collections like maps, deques, etc.
2. **Connecting to the Surrounding Context**: The chunk builds upon the surrounding context of CosmWasm smart contracts by:
	* Mentioning the importance of persisting data across contract calls
	* Discussing on-chain storage limits and off-chain solutions (e.g., IPFS)
3. **Requirements and Conditions**: This section outlines specific requirements, conditions, or constraints for using `cw-storage-plus`, including:
	* Ensuring unique keys
	* Considering long keys that may impact performance

The chunk's focus is on the technical details and processes related to storing data in CosmWasm smart contracts, specifically building upon the framework's base API and providing features like type-safe interface, key management, and persistent data structures.

The following specific requirements are mentioned:

* Ensuring unique keys (mentioned as a crucial aspect of key management)
* Considering long keys that may impact performance
* Using single-character ASCII prefixes for better performance

Overall, this chunk is explaining how `cw-storage-plus` can be used to simplify the process of storing and managing data in CosmWasm smart contracts.
