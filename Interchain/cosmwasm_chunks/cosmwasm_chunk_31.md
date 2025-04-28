## cosmwasm - Chunk 31

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

RESP=$(wasmd tx wasm migrate "$CONTRACT" "$BURNER_CODE_ID" "$MIGRATION_MSG" \
  --from alice \
  --chain-id=docs-chain-1 \
  -y \
  -o json \
  --keyring-backend=test)
Finally, query the transaction to check its status and view the results

wasmd q tx $(echo "$RESP" | jq -r '.txhash') -o json
The output will be similar to the following:

{
  ... "events": [
    ... {
      "type": "migrate",
      "attributes": [
        {
          "key": "code_id",
          "value": "3",
          "index": true
        },
        {
          "key": "_contract_address",
          "value": "wasm1wug8sewp6cedgkmrmvhl3lf3tulagm9hnvy8p0rppz9yjw0g4wtqhs9hr8",
          "index": true
        },
        {
          "key": "msg_index",
          "value": "0",
          "index": true
        }
      ]
    },
  ]
}
In this case, the contract was migrated to use code ID 3.

---

**LLM Contextual Output:**

This text chunk is explaining a section of a CosmWasm smart contract documentation, specifically:

1. **Technical details and parameters**:
   - `cw-storage-plus` library: A library that builds upon top of CosmWasm's raw API for binary key-value storage.
   - Type-safe interface: The library provides a type-safe interface to store and retrieve data.
   - Key management: Unique keys are used to manage namespaces, prefixes are provided to generate unique keys for individual values.

2. **Connection to the surrounding context**:
   - This chunk connects to the surrounding context of the CosmWasm smart contract documentation section.
   - It discusses how `cw-storage-plus` is building upon top of the raw API and provides a type-safe interface, key management, and persistent data structures like maps and deques.

3. **Specific requirements and conditions**:
   - Long keys can impact storage performance, suggesting that single-character ASCII prefixes should be used for better performance.
   - Key conflicts are mentioned as a consideration when ensuring unique keys.

4. **Purpose of the section**:
   - The purpose is to explain how `cw-storage-plus` simplifies the process of storing and managing data in CosmWasm smart contracts, making it easier to implement complex stateful functionalities while maintaining type safety and performance optimization.

5. **Example usage**:
   - An example usage of the library is provided at the end of the section.

Overall, this chunk explains how `cw-storage-plus` improves data storage and management in CosmWasm smart contracts by providing a simplified interface, key management, and persistent data structures.
