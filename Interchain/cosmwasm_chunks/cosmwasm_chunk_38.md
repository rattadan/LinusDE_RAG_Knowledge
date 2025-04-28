## cosmwasm - Chunk 38

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

Instead, we’ll focus on the commands that are only available through a proposal such as pin-codes, unpin-codes and sudo-contract. Pin Codes
Pinning a code means keeping a specific Wasm code stored in the cache. This improves the performance of frequently used contracts by avoiding the need to reload the code from the blockchain, which leads to lower gas costs during contract execution. For more details about code pinning you can check the Contract pinning section. To submit a proposal for pinning a code, you can use the following command:

wasmd tx wasm submit-proposal pin-codes $CODE_ID \
  --title "Pin Code $CODE_ID" \
  --summary "Pin Code $CODE_ID Proposal" \
  --from alice \
  --gas 1500000 \
  -y \
  --chain-id=docs-chain-1 \
  -o json \
  --keyring-backend=test \
  --deposit 100000stake
You can pin multiple codes by providing a list of code IDs instead of just a single code_id.

---

**LLM Contextual Output:**

Let's break down the given text chunk:

**Context:** The provided text appears to be related to CosmWasm smart contracts, specifically discussing the `cw-storage-plus` library and its features for storing data in a more efficient and scalable manner.

**Technical details:**

1. **Type-Safe Interface**: `cw-storage-plus` provides a type-safe interface for storing and retrieving data, which is achieved through a simple, raw API.
2. **Key Management**: The library ensures unique keys by providing a prefix system, where the provided string acts as a key under which the value will be saved. Long keys are also considered to impact storage performance.
3. **Persistent Data Structures**: `cw-storage-plus` implements feature-rich collections like maps and deques.

**Connection to surrounding context:**

1. The text is part of an introduction or documentation section related to CosmWasm smart contracts, discussing the importance of persisting data across contract calls and providing examples of how `cw-storage-plus` can be used.
2. The provided code snippet demonstrates how to use `cw-storage-plus` for storing and managing data in a smart contract.

**Specific requirements, conditions, or constraints:**

1. **Performance considerations**: Long keys are considered a performance bottleneck due to the need to store them on-chain. `cw-storage-plus` aims to optimize this by using single-character ASCII prefixes.
2. **Gas costs**: Using pin-codes can lead to lower gas costs during contract execution, as frequently used contracts will be stored in the cache instead of being reloaded from the blockchain.

**Analysis and focused explanation:**

This section is explaining how `cw-storage-plus` simplifies the process of storing and managing data in CosmWasm smart contracts. The focus is on providing a more efficient and scalable solution for persisting data across contract calls, with an emphasis on performance optimization and gas cost considerations.
