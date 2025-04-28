## cosmwasm - Chunk 40

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

{ "type": "submit_proposal", "attributes": [ { "key": "proposal_id", "value": "2", "index": true }, { "key": "proposal_proposer", "value": "wasm10gftgfm8my3f3hymne8327rrzyvy7dqrkucej5", "index": true }, { "key": "proposal_messages", "value": ",/cosmwasm.wasm.v1.MsgPinCodes", "index": true }, { "key": "msg_index", "value": "0", "index": true } ] } ] } Once you have the proposal ID, you can fetch the full proposal details using the following command: wasmd q gov proposal 2 -o json The command will return a JSON object similar to the following: { "proposal": { "id": "2", "messages": [ { "type": "wasm/MsgPinCodes", "value": { "authority": "wasm10d07y265gmmuvt4z0w9aw880jnsr700js7zslc", "code_ids": ["1"] } } ], "status": 1, "final_tally_result": { "yes_count": "0", "abstain_count": "0", "no_count": "0", "no_with_veto_count": "0" }, "submit_time": "2024-08-08T16:48:32.640792888Z", "deposit_end_time": "2024-08-10T16:48:32.640792888Z", "total_deposit": [ { "denom": "stake", "amount": "100000" } ], "title": "Pin Code

---

**LLM Contextual Output:**

This is a technical analysis of the provided text chunk, which appears to be an excerpt from a documentation or guide on using `cw-storage-plus` in CosmWasm smart contracts.

Here's a breakdown of the technical details, parameters, and processes described in this chunk:

1. **Type-Safe Interface**: The `cw-storage-plus` library provides a type-safe interface for storing and retrieving data, which simplifies the process of working with binary key-value storage.
2. **Key Management**: Key management is crucial when working with storage containers. In this context, unique keys are used to manage namespace conflicts, and single-character ASCII prefixes (e.g., "a", "b", "c") are recommended for better performance.
3. **Persistence and Off-Chain Solutions**: The chunk mentions the importance of persisting data across contract calls and recommends using off-chain solutions like IPFS for larger datasets.

Regarding processes:

1. **Usage Examples**: The chunk provides examples of how to use `cw-storage-plus` in different scenarios, such as saving a balance value, loading a balance value, pushing elements into a deque, and populating the history.
2. **Command Syntax**: It explains that using `cw-storage-plus`, you can fetch proposal details by calling the `wasmd q gov proposal <proposal_id> -o json` command.

To build upon the surrounding context:

1. **CosmWasm Framework**: The chunk assumes familiarity with the CosmWasm framework, which provides a raw API for binary key-value storage.
2. **Storage Containers**: Understanding how to work with different types of storage containers (e.g., `Item`, `Map`, `Deque`) is essential in this context.
3. **Key Serialization**: Knowledge of JSON serialization via serde-json-wasm is necessary for storing and retrieving data using `cw-storage-plus`.
4. **Command Syntax**: Familiarity with the command syntax provided, such as the `wasmd` tool and its options (`-o json`), is required to execute commands like fetching proposal details.

Specific requirements, conditions, or constraints mentioned:

1. **Unique Keys**: Ensuring unique keys is crucial for managing namespace conflicts in storage containers.
2. **Performance Optimization**: Using single-character ASCII prefixes can improve performance by reducing the number of possible keys.
3. **Off-Chain Solutions**: Considering off-chain solutions like IPFS can help with larger datasets and improve performance.

By analyzing this specific section, we can better understand how to use `cw-storage-plus` in CosmWasm smart contracts, including key management, persistence, and command syntax.
