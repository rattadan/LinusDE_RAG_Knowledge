## cosmwasm - Chunk 27

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

Below is the full script that combines all the steps for executing a command on a Wasm contract and querying the events:

# Define the message to send to the contract, in this case a "release" command
MSG='{"release":{}}'
 
# Execute the contract with the specified message
RESP=$(wasmd tx wasm execute "$CONTRACT" "$MSG" \
  --from alice \
  --gas 1000000 \
  -y \
  --chain-id=docs-chain-1 \
  -o json \
  --keyring-backend=test)
 
# Wait for the transaction to be processed
sleep 6
 
# Query the transaction using its hash to check the events emitted by the contract
wasmd q tx $(echo "$RESP" | jq -r '.txhash') -o json | jq
Query contract state
To query the state of a Wasm contract, you can use the following command.

---

**LLM Contextual Output:**

Here's a focused analysis of the specific section explaining what this chunk is explaining:

**Technical Details and Parameters:**

* The `cw-storage-plus` library provides a type-safe interface for storing and retrieving data.
* It implements key management by ensuring unique keys and managing namespace conflicts using prefixes.
* Data types must implement `serde::Serialize` and `serde::Deserialize` to be stored using JSON serialization via `serde-json-wasm`.

**Connection to or Building upon the Surrounding Context:**

This chunk builds upon the surrounding context of the "Introduction to Storage in CosmWasm Smart Contracts" section, which provides an overview of persistent data storage in CosmWasm smart contracts.

The specific requirements and conditions mentioned in this chunk include:

* Ensuring unique keys for data storage
* Managing namespace conflicts using prefixes
* Optimizing performance by avoiding long key strings
* Implementing type safety through serialization with `serde`
* Using a JSON-based serialization mechanism via `serde-json-wasm`

**Example Usage:**

The example usage demonstrates how to use the `cw-storage-plus` library to store and retrieve data in CosmWasm smart contracts. It shows how to:

* Create a storage container (e.g., an item, map, or deque) using the `Item`, `Map`, or `Deque` functions.
* Save data values using the `save` method and load them using the `load` method.
* Use the `cw-storage-plus` library to manage data types that implement `serde::Serialize` and `serde::Deserialize`.

Overall, this chunk provides a comprehensive explanation of how to use the `cw-storage-plus` library for storing and retrieving data in CosmWasm smart contracts.
