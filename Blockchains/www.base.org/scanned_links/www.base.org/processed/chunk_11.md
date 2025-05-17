# Documentation Analysis - Chunk chunk_11.txt

## Source Context
*From: https://www.base.org/*

### Document Overview  
This content covers key aspects of Solidity smart contract development, including storage management, variable declarations, function design, data structures, inheritance, and debugging techniques.  

### Key Technical Concepts  
- **Storage, Memory, and Calldata Arrays**: Differences in memory usage and persistence.  
- **Variable Order**: Optimization for storage efficiency.  
- **Structs**: User-defined types with members for storage efficiency.  
- **Modifiers**: Functional enhancements via access control.  
- **Inheritance**: Hierarchical contract relationships and byte code size impact.  
- **Events**: Triggers for state changes, with common use cases.  
- **Pure/View Functions**: Differences from modifying storage.  
- **Debugging Techniques**: Handling errors like transaction reverted, out-of-gas, and stack overflow.  

### Implementation Details  
- **Array Filtering**: A function like `filterSubset` returns a filtered array, e.g., `function filterSubset(uint256[] memory input) public pure returns (uint256[] memory)`.  
- **Map Data Type**: Uses `mapping` for key-value storage, with no flexibility in assignment.  
- **Modifiers**: Example: `function onlyOwner() public pure { ... }` restricts calls to `msg.sender`.  
- **Structs**: A `struct User` with fields `name` (string), `score` (uint256), and `timestamp` (uint256), declared with `storage` for efficiency.  
- **Inheritance**: A contract inherits from another using `contract Parent` and overrides methods.  
- **Byte Code Size**: Inheritance increases size due to additional methods and storage.  
- **OpenZeppelin Contracts**: Used in Remix for reusable code.  
- **Events**: `Event MyEvent(uint256 value)` triggers on state changes.  
- **Debugging**: `revert` for transaction errors, `gaslimit` for out-of-gas errors.  

### Related Topics  
- **Storage System**: Connected to the documentation on Solidity’s memory and storage models.  
- **Inheritance**: Linked to byte code size limits and multiple-contract inheritance examples.  
- **OpenZeppelin**: Tied to Remix usage and contract creation with `new`.  
- **Error Handling**: Connected to debugging techniques and Solidity’s error propagation.

---

## Original Text
```
data is stored on the blockchain (Contract -> Blockchain)
- Order variable declarations to use storage efficiently
- Diagram how variables in a contract are stored (Variable -> Contract)
- Describe the difference between storage, memory, and calldata arrays
- Write a function that can return a filtered subset of an array
- Construct a Map (dictionary) data type
- Recall that assignment of the Map data type is not as flexible as for other data types/in other languages
- Restrict function calls with themsg.senderglobal variable
- Recall that there is no collision protection in the EVM and why this is (probably) ok
- Categorize functions as public, private, internal, or external based on their usage
- Describe how pure and view functions are different than functions that modify storage
- Use modifiers to efficiently add functionality to multiple functions
- Construct astruct(user-defined type) that contains several different data types
- Declare members of thestructto maximize storage efficiency
- Describe constraints related to the assignment ofstructs depending on the types they contain
- Write a smart contract that inherits from another contract
- Describe the impact inheritance has on the byte code size limit
- Write a smart contract that inherits from multiple contracts
- Use the virtual, override, and abstract keywords to create and use an abstract contract
- Import and use code from another file
- Utilize OpenZeppelin contracts within Remix
- Debug common solidity errors including transaction reverted, out of gas, stack overflow, value overflow/underflow, index out of range, etc.
- Write a contract that creates a new contract with the new keyword
- Use interfaces to allow a smart contract to call functions in another smart contract
- Use thecall()function to interact with another contract without using an interface
- Write and trigger an event
- List common uses of events
- Understand events vs.
```