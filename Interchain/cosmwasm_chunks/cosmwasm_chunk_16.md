## cosmwasm - Chunk 16

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

INIT="{\"verifier\":\"$ALICE_ADDR\", \"beneficiary\":\"$BOB_ADDR\"}" # Instantiate the contract RESP=$(wasmd tx wasm instantiate "$CODE_ID" "$INIT" \ --admin="$ALICE_ADDR" \ --from alice \ --amount="100stake" \ --label "local0.1.0" \ --gas 1000000 \ -y \ --chain-id=docs-chain-1 \ -o json \ --keyring-backend=test) # Wait for the transaction to be processed sleep 6 # Query the contract address CONTRACT=$(wasmd query wasm list-contract-by-code "$CODE_ID" -o json | jq -r '.contracts[-1]') # Print the contract address echo "* Contract address: $CONTRACT" Query Contract Metadata To query the metadata of a specific contract, use the following command: wasmd q wasm contract $CONTRACT -o json The command will return a JSON object similar to the following: { "address": "wasm14hj2tavq8fpesdwxxcu44rty3hh90vhujrvcmstl4zr3txmfvw9s0phg4d", "contract_info": { "code_id": "1", "creator": "wasm1zxevglcy90hq49x8vvdckfrgd9ffndxf70ut0z", "admin": "wasm1zxevglcy90hq49x8vvdckfrgd9ffndxf70ut0z", "label": "local0.1.0", "created": {

---

**LLM Contextual Output:**

This text chunk is describing the technical details and functionality of the `cw-storage-plus` library, which is used for persistent data storage in CosmWasm smart contracts.

The chunk provides a detailed overview of the library's features, including:

* A key management system that ensures unique keys and manages namespace conflicts
* Persistent data structures such as maps (dictionaries) and deques (double-ended queues)
* Key serialization using JSON with serde-json-wasm

This information is crucial for understanding how to use `cw-storage-plus` in a CosmWasm smart contract, particularly when implementing complex stateful functionalities that require persistent storage.

The chunk connects to the surrounding context by:

1. Providing an introduction to storage in CosmWasm smart contracts
2. Discussing the limitations of on-chain storage and the benefits of off-chain solutions like IPFS
3. Explaining how `cw-storage-plus` builds upon the CosmWasm framework and its raw API

The chunk also addresses specific requirements and conditions, including:

* Ensuring unique keys to prevent conflicts with other parts of the contract
* Optimizing performance by using single-character ASCII prefixes for better storage efficiency

Overall, this text chunk provides a comprehensive overview of the technical details and functionality of `cw-storage-plus`, making it an essential resource for developers working on CosmWasm smart contracts.
