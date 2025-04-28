## cosmwasm - Chunk 21

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

SALT=10 Run the following command to instantiate the contract with predictable address: wasmd tx wasm instantiate2 "$CODE_ID" "$INIT" "$SALT" \ --admin="$ALICE_ADDR" \ --from alice \ --amount="100stake" \ --label "local0.1.0" \ --gas 1000000 \ -y \ --chain-id=docs-chain-1 \ -o json \ --keyring-backend=test wasmd tx wasm instantiate2 "$CODE_ID" "$INIT" "$SALT" instantiates a new contract instance with the specified code ID, initialization parameters, and the salt value --admin="$ALICE_ADDR" specifies Alice as the admin who can later update the contract --from alice specifies Alice as the sender of the transaction --amount="100stake": Sends 100 stake to the contract upon instantiation --label "local0.1.0" assigns a label to this contract instance for easy identification --gas 1000000 sets the gas limit for the transaction -y automatically accepts the transaction without prompting for confirmation --chain-id=docs-chain-1 specifies the chain ID of the blockchain -o json outputs the result in JSON format

---

**LLM Contextual Output:**

The current text chunk provides an introduction to storage solutions for CosmWasm smart contracts, specifically highlighting the benefits and limitations of using `cw-storage-plus` versus traditional on-chain storage methods.

Technical Details:

* `cw-storage-plus`: A library that builds upon the CosmWasm framework's binary key-value storage API by providing a type-safe interface, key management, persistent data structures (maps and deques), and efficient containerization.
* `cw_storage_plus::Item`, `Map`, and `Deque`: Data structures that store values in a structured manner.

Context:

The text chunk is building upon the introductory section of the documentation for CosmWasm smart contracts. The provided context establishes a foundation for understanding the importance of persistent data storage, on-chain limitations, and the need for a robust solution like `cw-storage-plus`.

Connection to Surrounding Context:

* The text chunk assumes familiarity with the basic concepts of CosmWasm smart contract development, including the use of `cw_storage_plus` libraries and the binary key-value storage API.
* The context provides examples of using `cw-storage-plus` for simple data storage scenarios (e.g., saving balance values), demonstrating its applicability in various use cases.

Requirements, Conditions, or Constraints:

None mentioned.
