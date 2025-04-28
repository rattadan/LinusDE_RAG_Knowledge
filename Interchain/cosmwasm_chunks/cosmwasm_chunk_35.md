## cosmwasm - Chunk 35

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

"updated" contains information about when the operation was performed. "msg" is the message payload associated with the operation. Set contract admin
The admin is the only address that can migrate a contract. The admin can be updated by the current admin with the following command:

wasmd tx wasm set-contract-admin \
  "$CONTRACT" \
  "$BOB_ADDR" \
  --from alice \
  --keyring-backend=test \
  --chain-id=docs-chain-1 \
  -y
After running this command, Bob will be the new admin of the contract, and only he will have the authority to migrate the contract to a new code version or further update the admin role. Clear contract admin
Clearing the admin address from a Wasm contract removes the ability to migrate the contract to a new code version. This action effectively locks the contract, preventing any further migrations.

---

**LLM Contextual Output:**

This specific section of text is explaining how `cw-storage-plus` fits into the surrounding context of smart contract storage and management in CosmWasm.

**Technical details and parameters:**

* The section describes the key features and capabilities of `cw-storage-plus`, including:
	+ A type-safe interface for storing and retrieving data
	+ Key management, specifically prefixes used to generate unique keys for individual values or collections
	+ Persistent data structures, such as maps and deques, with methods for interacting with them
* The section also mentions the importance of ensuring key uniqueness, performance optimization, and error handling in smart contract storage

**Connections to surrounding context:**

* This chunk builds upon previous sections that discuss on-chain storage limits and the CosmWasm framework.
* It explains how `cw-storage-plus` can be used as a library or module within these larger discussions about smart contract storage.
* The example usage provided at the end shows how to use `cw-storage-plus` in a practical scenario, demonstrating its applicability in real-world smart contract development.

**Requirements and conditions:**

* There are no specific requirements mentioned in this chunk. However, it assumes some basic knowledge of smart contract development and CosmWasm framework.
* The section also notes that long keys can impact storage performance, which is an important consideration when designing and optimizing smart contract storage solutions.

Overall, this chunk provides a comprehensive overview of the key features and capabilities of `cw-storage-plus` within the context of smart contract storage in CosmWasm.
