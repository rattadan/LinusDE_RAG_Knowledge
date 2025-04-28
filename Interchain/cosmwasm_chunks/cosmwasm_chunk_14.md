## cosmwasm - Chunk 14

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

Create a new contract instance First, set up the addresses for the accounts involved in the contract using wasmd keys show command: # Retrieve the address of Alice's account ALICE_ADDR=$(wasmd keys show alice -a --keyring-backend=test) # Retrieve the address of Bob's account BOB_ADDR=$(wasmd keys show bob -a --keyring-backend=test) # Define init parameters for the contract INIT="{\"verifier\":\"$ALICE_ADDR\", \"beneficiary\":\"$BOB_ADDR\"}" Run the following command to instantiate the contract: wasmd tx wasm instantiate "$CODE_ID" "$INIT" \ --admin="$ALICE_ADDR" \ --from alice \ --amount="100stake" \ --label "local0.1.0" \ --gas 1000000 \ -y \ --chain-id=docs-chain-1 \ -o json \ --keyring-backend=test wasmd tx wasm instantiate "$CODE_ID" "$INIT" instantiates the contract using the specified code ID and initial parameters --admin="$ALICE_ADDR" specifies Alice as the admin who can later update the contract --from alice specifies Alice as the sender of the transaction --amount="100stake": Sends 100 stake to the

---

**LLM Contextual Output:**

This text chunk is explaining how to use a library called `cw-storage-plus` to manage data in a CosmWasm smart contract. Here's a focused analysis of what this section is explaining:

**Technical Details:**

* `cw-storage-plus` is a library that provides a simple, raw API for binary key-value storage.
* The library builds upon the base API provided by the `cosmwasm-storage` framework.
* It adds type-safe interfaces for storing and retrieving data, key management, and persistent data structures like maps and deques.

**Parameters:**

* The chunk describes the following parameters:
	+ `Item`: a simple container for a single value.
	+ `Map`: a collection capable of storing multiple values with methods to interact with them.
	+ `Deque`: a double-ended queue that can store and manage elements efficiently.
* The chunk also mentions that keys must be unique and should not conflict with other parts of the contract.

**Processes:**

* The chunk explains how to use the library's functions to:
	+ Store data using `Item.save()`
	+ Load data from storage using `Item.load()`
	+ Create a map or deque using the `Map` or `Deque` types
* It also mentions that keys should be single characters and should not conflict with other parts of the contract.

**Context:**

* The chunk is part of an introduction to storing data in CosmWasm smart contracts.
* It explains why persistent data is necessary for complex functionalities like token balances, voting systems, or games.
* It also discusses on-chain storage limits and the importance of off-chain solutions for larger datasets.

**Connection to surrounding context:**

* The chunk builds upon the base API provided by `cosmwasm-storage`.
* It expands on the typesafe interfaces and key management features provided by the library.
* It provides examples of how to use the library in a CosmWasm smart contract, including creating a new instance, setting up accounts, and instantiating the contract.

**Specific requirements:**

* The chunk does not explicitly mention any specific requirements or conditions for using `cw-storage-plus`, such as testing environments or security measures.
* However, it suggests that long keys can impact storage performance, which may require optimization techniques to be applied in a production environment.
