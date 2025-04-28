## cosmwasm - Chunk 43

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

Unpin codes
To remove a code from the cache and unpin it, you can submit an unpin proposal using the following command:

wasmd tx wasm submit-proposal unpin-codes $CODE_ID \
  --title "Pin Code $CODE_ID" \
  --summary "Pin Code $CODE_ID Proposal" \
  --from alice \
  --gas 1500000 \
  -y \
  --chain-id=docs-chain-1 \
  -o json \
  --keyring-backend=test \
  --deposit 100000stake
The rest of the process follows the same steps as pinning codes, so we won’t go into detail again. After the proposal is executed, you can confirm that the code is no longer pinned by using the wasmd q wasm pinned command. ICS20: Fungible Token Transfer
The ICS20 protocol defines a standard for transferring fungible tokens between two chains using IBC. It is one of the most widely used IBC protocols and is supported by pretty much all chains in the Cosmos.

---

**LLM Contextual Output:**

Here's a focused analysis of what this specific section explains:

**Technical Details/Parameters:**

1. The text chunk discusses the `cw-storage-plus` library, which provides an interface for binary key-value storage in CosmWasm smart contracts.
2. It mentions the following technical details:
	* Type-safe interface
	* Key management (unique keys and namespace conflicts)
	* Persistent data structures (maps and deques)
3. The chunk also explains how to use `cw-storage-plus` with a specific example, demonstrating its usage for storing balance values.

**Context:**

The text is part of an introduction to storage in CosmWasm smart contracts. It sets the stage by highlighting the importance of persisting data across contract calls and the limitations of on-chain storage due to its cost.
The chunk follows the typical structure of a documentation section, explaining how `cw-storage-plus` can be used to implement complex stateful functionalities.

**Connection to Building Upon the Surrounding Context:**

This chunk builds upon the surrounding context by introducing `cw-storage-plus` as an alternative solution for binary key-value storage in CosmWasm smart contracts. It explains how this library provides a more convenient and efficient way of managing data, which is essential for implementing complex functionalities like token balances and voting systems.
The text also references the previous sections, which discussed on-chain storage limitations and the importance of using off-chain solutions for larger datasets.

**Requirements, Conditions, or Constraints:**

There are no specific requirements, conditions, or constraints mentioned in this chunk. However, the text assumes that the reader has a basic understanding of CosmWasm smart contracts and their use cases. Additionally, it mentions that the code should be submitted using the `wasmd` command with an unpin proposal to demonstrate pinning codes, which may require additional setup or configuration depending on the local environment.

Overall, this chunk provides an introduction to `cw-storage-plus` as a suitable solution for storing data in CosmWasm smart contracts and sets the stage for further exploration of its features and applications.
