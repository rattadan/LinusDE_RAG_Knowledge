## cosmwasm - Chunk 51

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

use external_contract::sv::Executor;
use cw_storey::containers::Item;
 
use sv::SubMsgMethods;
 
pub struct ReplyContract {
    remote: Item<Remote<'static, ExternalContract>>,
}
 
#[entry_points]
#[contract]
#[sv::features(replies)]
impl ReplyContract {
    pub fn new() -> Self {
        Self {
            remote: Item::new(0),
        }
    }
 
    #[sv::msg(instantiate)]
    fn instantiate(&self, ctx: InstantiateCtx, remote_addr: Addr) -> StdResult<Response> {
        self.remote
            .access(ctx.deps.storage)
            .set(&Remote::new(remote_addr))?;
        Ok(Response::new())
    }
 
    #[sv::msg(exec)]
    fn exec(&self, ctx: ExecCtx) -> StdResult<Response> {
        let sub_msg = self
            .remote
            .access(ctx.deps.storage)
            .get()? .ok_or_else(|| StdError::generic_err("Remote not instantiated"))? .executor()
            .external_exec()?

---

**LLM Contextual Output:**

This text chunk is a detailed explanation of the technical details, parameters, and processes described in the surrounding context, specifically:

1. **Technical Details**:
   - The use of `cw-storey` as an external storage system.
   - The implementation of the `Item` struct from `cw-storey`.
   - The serialization mechanism using `serde-json-wasm`.

2. **Context Connection and Building upon the Surrounding Context**:
   - This chunk connects to the context by explaining how the `cw-storage-plus` library is used in a CosmWasm smart contract.
   - It builds upon this context by demonstrating examples of using the `Item`, `Map`, and `Deque` structs from `cw-storey_plus`.

3. **Specific Requirements, Conditions, or Constraints**:
   - The requirements for key management to ensure unique keys across different parts of the contract.
   - The performance implications of long keys on storage efficiency.

Breaking down this text chunk:

### Use External Contract: sv::Executor

This section explains that an external `sv::Executor` is required for interacting with the CosmWasm smart contract from outside. This is necessary because CosmWasm requires a separate process to manage interactions with contracts, unlike traditional WebAssembly where it can run directly.

```rust
use external_contract::sv::Executor;
```

### cw-storey Interface

This section introduces `cw-storey` as an external storage system that provides the `Item`, `Map`, and `Deque` structs for storing and managing data. These are used to interact with CosmWasm smart contracts.

```rust
use cw_storey::containers::Item;
```

### sv::SubMsgMethods Implementation

This section demonstrates how `sv-storey_plus` (a part of the `cw-storey` library) implements methods for interacting with storage in a `sv::SubMsgMethods` trait. This allows external contracts to access and interact with the stored data.

```rust
use sv::SubMsgMethods;
```

### ReplyContract Struct

This section defines a new struct called `ReplyContract` that has a single field, `remote`, of type `Item<Remote<'static, ExternalContract>>`. The `remote` field is used to access and interact with the external contract.

```rust
pub struct ReplyContract {
    remote: Item<Remote<'static, ExternalContract>>,
}
```

### entry_points and sv::features(replies) Attribute

This section defines an entry point for the contract using the `#[contract]` attribute. Additionally, it includes a feature that enables support for external contracts using the `sv::features(replies)` macro.

```rust
#[entry_points]
#[contract]
#[sv::features(replies)]
impl ReplyContract {
    // ...
}
```

### Instantiate and Exec Functions

The `instantiate` function is used to instantiate the contract, and the `exec` function is used for external execution of contracts. The `remote` field is accessed through these functions.

```rust
pub fn new() -> Self {
    Self { remote: Item::new(0) }
}

#[sv::msg(instantiate)]
fn instantiate(&self, ctx: InstantiateCtx, remote_addr: Addr) -> StdResult<Response> {
    self.remote
        .access(ctx.deps.storage)
        .set(&Remote::new(remote_addr))?
        Ok(Response::new())
}
```

```rust
#[sv::msg(exec)]
fn exec(&self, ctx: ExecCtx) -> StdResult<Response> {
    let sub_msg = self
        .remote
        .access(ctx.deps.storage)
        .get()??.executor()
        .external_exec()?;
}
```

### Key Management and Performance Considerations

The `cw-storey_plus` library provides a way to manage keys in the storage. The key management is based on unique prefixes that are used for creating containers, maps, and deques.

```rust
use cw_storey_plus::{Map, Item};

pub static BALANCES: Map<String, u128> = Map::new("balances");
```

The performance implications of long keys on storage efficiency can be observed in the example usage code:

```rust
let mut storage = Storage::new();
BALANCES.save().unwrap();

// If key length is 256 characters or more, it will not fit into the buffer and an error is returned.
// The same will happen if trying to save a string longer than 255 characters.
```

### Conclusion

This text chunk provides a detailed explanation of how `cw-storey_plus` is used in a CosmWasm smart contract. It covers technical details, context connection and building upon the surrounding context, specific requirements for key management, and performance considerations.
