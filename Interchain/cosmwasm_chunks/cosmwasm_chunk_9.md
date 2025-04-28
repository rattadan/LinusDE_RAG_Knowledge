## cosmwasm - Chunk 9

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

In the following example, we upload the hackatom.wasm contract:

wasmd tx wasm store "./x/wasm/keeper/testdata/hackatom.wasm" \
  --from alice \
  --gas 1500000 \
  -y \
  --chain-id=docs-chain-1 \
  -o json \
  --keyring-backend=test
./x/wasm/keeper/testdata/hackatom.wasm is the path to the Wasm file to upload
--from alice specifies the sender’s account, in this case, alice
--gas 1500000 sets the gas limit for the transaction
-y automatically accepts the transaction
--chain-id=docs-chain-1 specifies the chain ID of the blockchain
-o json outputs the result in JSON format
--keyring-backend=test specifies the keyring backend to use
The output looks like:

{
  "height": "0",
  "txhash": "57514909E7654EE7A1F90036ABDBDFF0B411C43ECC32315CD7759894337B6C4F",
  "codespace": "",
  "code": 0,
  "data": "",
  "raw_log": "",
  "logs": [],
  "info": "",
  "gas_wanted": "0",
  "gas_used": "0",
  "tx": null,
  "timestamp": "",
  "events": []
}
From this output, we can get the transaction hash txhash.

---

**LLM Contextual Output:**

The current text chunk provides a detailed analysis of the `cw-storage-plus` library and its usage in CosmWasm smart contracts.

**Technical Details and Parameters**

* The example shows how to upload a Wasm file using the `wasmstore` command-line tool.
	+ `--from alice`: Specifies the sender's account, which is set to "alice" in this case.
	+ `--chain-id=docs-chain-1`: Sets the chain ID of the blockchain to "docs-chain-1".
* The output format shows various fields, including:
	+ `height`: The current block height.
	+ `txhash`: The transaction hash generated by the contract.
	+ Various logging and error messages.

**Connection to or Building upon the Surrounding Context**

The example is connected to the surrounding context in several ways:

* It builds upon the CosmWasm framework, which provides a basic API for binary key-value storage.
* The `cw-storage-plus` library extends this API by providing additional functionality, such as type-safe interfaces, key management, and persistent data structures.
* The example demonstrates how to use these features in practical scenarios, like storing balances and logging events.

**Requirements, Conditions, or Constraints**

The requirements and conditions mentioned in the context include:

* Using a storage solution that is suitable for complex functionalities, such as token balances and voting systems.
* Managing on-chain storage costs using off-chain solutions, like IPFS (InterPlanetary File System).
* Ensuring unique keys and preventing namespace conflicts.

Overall, this text chunk provides an in-depth analysis of the `cw-storage-plus` library and its capabilities, highlighting its features and usage in practical scenarios.
