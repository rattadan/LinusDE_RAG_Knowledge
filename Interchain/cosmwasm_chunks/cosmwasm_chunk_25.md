## cosmwasm - Chunk 25

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

In this example we want to call the release function of the contract:

MSG='{"release":{}}'
Run the following command to execute the message on the contract:

wasmd tx wasm execute "$CONTRACT" "$MSG" \
  --from alice \
  --gas 1000000 \
  -y \
  --chain-id=docs-chain-1 \
  -o json \
  --keyring-backend=test
"$CONTRACT" specifies the address of the contract
"$MSG" specifies the message to execute
--from alice specifies Alice as the sender of the transaction
--gas 1000000 sets the gas limit for the transaction
-y automatically accepts the transaction without prompting for confirmation
--chain-id=docs-chain-1 specifies the chain ID of the blockchain
-o json outputs the result in JSON format
--keyring-backend=test specifies the keyring backend to use
By querying the transaction using the txhash, we can check the events emitted by the contract. The output will look similar to the following:

{
  ... "events": [
    ...

---

**LLM Contextual Output:**

This text chunk is discussing a specific aspect of storing and managing data in CosmWasm smart contracts, specifically highlighting how `cw-storage-plus` library simplifies this process.

Here's a breakdown of the technical details, parameters, or processes described in this chunk:

* **Key Management**: The key management system used by `cw-storage-plus` ensures unique keys are provided for each stored value. Key prefixes are used to generate keys for individual values.
* **Storage Containers**: Storage containers (Item, Map, Deque) are implemented using the `cw-storage-plus` library, providing a simple and raw API for binary key-value storage.
* **Key Serialization**: Values in `cw-storage-plus` are stored using JSON serialization via serde-json-wasm, requiring the implementation of `serde::Serialize` and `serde::Deserialize` traits for data types to be compatible with this method.

This chunk connects to the surrounding context by:

1. Providing a high-level overview of how smart contracts can store complex data structures like token balances, voting systems, or games.
2. Explaining the importance of persistent storage in contract development.
3. Discussing off-chain storage solutions (IPFS) and their limitations on on-chain storage.

The chunk also builds upon:

1. The CosmWasm framework itself, which provides a simple, raw API for binary key-value storage.
2. Other existing libraries or frameworks that may be used to store data in smart contracts, such as `cw-storage-plus`.

Specific requirements, conditions, or constraints mentioned include:

* Ensuring unique keys are provided for each stored value
* Using JSON serialization via serde-json-wasm for storing and retrieving data
* Considering the impact of long keys on storage performance

Overall, this text chunk is providing a detailed explanation of how `cw-storage-plus` simplifies the process of storing complex data structures in CosmWasm smart contracts.
