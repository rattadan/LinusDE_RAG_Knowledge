## cosmwasm - Chunk 11

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

To extract it, you can use the following command: RESP=$(wasmd q tx 2C19314D369E7EF3C77CBD1B33E02DB0401619B5C8E1B1E5BD15AB46C3704E96 -o json) echo "$RESP" | jq -r '.events[]| select(.type=="store_code").attributes[]| select(.key=="code_id").value' Below is the full script that uploads the code and fetches the code ID: # Upload the contract RESP=$(wasmd tx wasm store "./x/wasm/keeper/testdata/hackatom.wasm" \ --from alice \ --gas 1500000 \ -y \ --chain-id=docs-chain-1 \ -o json \ --keyring-backend=test) # Wait for the transaction to be processed sleep 6 # Fetch the transaction details RESP=$(wasmd q tx $(echo "$RESP"| jq -r '.txhash') -o json) # Extract the code ID CODE_ID=$(echo "$RESP" | jq -r '.events[]| select(.type=="store_code").attributes[]| select(.key=="code_id").value') # Print code id echo "* Code id: $CODE_ID" Query Code ID Metadata To query the metadata of a specific code ID, use the following command: wasmd q wasm code-info $CODE_ID -o json The command will return a JSON object similar to the

---

**LLM Contextual Output:**

Here's a focused analysis of the provided text chunk:

**Technical Details and Parameters**

1. **cw-storage-plus**: A library that builds on top of the CosmWasm framework for binary key-value storage.
2. **Type-Safe Interface**: Simplifies the process of storing and retrieving data by providing a type-safe interface.
3. **Key Management**: Ensures unique keys and manages namespace conflicts using prefixes.

**Connection to Surrounding Context**

1. The chunk builds upon the CosmWasm framework, specifically its raw API for binary key-value storage.
2. It also references other components of the CosmWasm ecosystem, such as `cw-storage-plus` and `serde-json-wasm`.
3. The context is focused on implementing persistent data storage in smart contracts using CosmWasm.

**Specific Requirements, Conditions, or Constraints**

1. **On-chain Storage Limits**: Requires careful consideration when storing large datasets.
2. **Key Conflicts**: Ensuring unique keys and managing namespace conflicts.
3. **Performance**: Optimizing for performance while maintaining type safety.

**Analysis of the Chunk**

The chunk provides a detailed explanation of how `cw-storage-plus` works, including:

1. The type-safe interface it provides
2. Key management mechanisms to ensure uniqueness and manage namespace conflicts
3. The use of prefixes to generate keys

It also explains how to fetch data from stored contracts using the `cw-storage-plus` library.

The chunk's context is focused on implementing persistent data storage in smart contracts using CosmWasm, which is essential for complex functionalities such as token balances, voting systems, or games.

To extract this information, you can use the following command:
```bash
RESP=$(wasmd q tx 2C19314D369E7EF3C77CBD1B33E02DB0401619B5C8E1B1E5BD15AB46C3704E96 -o json) echo "$RESP" | jq -r '.events[]| select(.type=="store_code").attributes[]| select(.key=="code_id").value'
```
