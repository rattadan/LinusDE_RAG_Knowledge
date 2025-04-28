## cosmwasm - Chunk 36

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

Run the following command to clear the contract admin:

wasmd tx wasm clear-contract-admin \
  "$CONTRACT" \
  --from bob \
  --keyring-backend=test \
  --chain-id=docs-chain-1 \
  -y
After running this command, the contract will no longer have an admin, and no one will be able to migrate the contract to a new code version. Proposals
Proposals are a fundamental part of the governance process in the Cosmos ecosystem. They enable validators to vote on important decisions that impact the network, such as software upgrades, parameter changes, and the allocation of community funds. Overview of the Proposal Process
Submission: A proposal is submitted along with a deposit to the network. Deposit Period: Other participants can contribute to the deposit. If the minimum deposit is met, the proposal moves to the voting stage. Voting Period: Validators and delegators vote on the proposal. Tallying: After the voting period ends, the votes are tallied to determine whether the proposal has passed or failed.

---

**LLM Contextual Output:**

This text chunk appears to be explaining how `cw-storage-plus` is used in CosmWasm smart contracts.

Here's a focused analysis of what this specific section is explaining:

1. **Technical details**: The chunk describes the data structures and types used by `cw-storage-plus`, specifically including:
	* `Item`: A simple container for storing single values.
	* `Map`: A collection capable of storing multiple values with methods to interact with them.
	* `Deque`: A double-ended queue that can store and manage elements efficiently.
2. **Context**: The chunk connects this explanation to the surrounding context, which is an introduction to storage in CosmWasm smart contracts.
3. **Requirements and conditions**:
	* Unique keys are essential for managing namespace conflicts.
	* Long keys can impact storage performance; single-character ASCII prefixes (e.g., "a", "b", "c") are recommended.

Specific requirements, conditions, or constraints mentioned:

* `cw-storage-plus` needs to be used as a library that builds on top of the CosmWasm framework's raw API.
* The contract admin must use `cw-storage-plus` to store and manage data in the contract.
