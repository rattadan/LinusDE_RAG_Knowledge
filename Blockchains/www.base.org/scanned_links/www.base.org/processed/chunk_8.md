# Documentation Analysis - Chunk chunk_8.txt

## Source Context
*From: https://www.base.org/*

### Document Overview  
Base Learn provides a comprehensive guide to smart contract development on the Base blockchain, covering core Solidity concepts, standards (e.g., ERC-20, ERC-721), and tools like hooks and contracts.  

### Key Technical Concepts  
- **Solidity Features**: Arrays, mappings, function visibility, modifiers, structs, inheritance, and hooks (e.g., `useReadContract`, `useWriteContract`).  
- **Web3/Web2 Contrast**: Differences in ownership, state management, and application models (e.g., decentralized vs. centralized systems).  
- **Token Standards**: ERC-20 (fungible tokens), ERC-721 (non-fungible tokens), and the use of `Address and Payable` in Solidity.  
- **Contract Interactions**: "The New Keyword" for dynamic contract interactions and "Contract to Contract" interactions.  
- **Hooks and Tools**: `useAccountHook`, `useReadContractHook`, and `useSimulateContractHook` for interacting with contracts.  

### Implementation Details  
- **ERC-20 Implementation**: Examples of token creation, transfer, and balance queries using Solidity.  
- **Minimal Token**: A simplified token contract demonstrating basic functionality (e.g., `transfer`, `balanceOf`).  
- **Hooks**: Code examples for `useReadContract` (e.g., querying contract functions) and `useWriteContract` (e.g., writing to contracts).  
- **Address and Payable**: Handling addresses in Solidity, including payable functions and interactions with external contracts.  
- **The New Keyword**: Usage in dynamic contract interactions (e.g., `new` for creating new contract instances).  

### Related Topics  
- **ERC-20/ERC-721 Standards**: Covered in the "ERC-20 Implementation" and "The ERC-721 Token Standard" sections.  
- **Web3/Web2 Comparison**: Highlighted in the welcome message, linking to broader blockchain development contexts.  
- **Contract Development Tools**: Connected to the "Building an Onchain App" and "TheuseAccountHook" sections.  
- **Solidity Best Practices**: Mentioned in the "Function Modifiers" and "Function Visibility and State Mutability" sections.

---

## Original Text
```
Works

h3: Arrays

h3: Filtering an Array

h3: Mappings

h3: Function Visibility and State Mutability

h3: Function Modifiers

h3: Structs

h3: Inheritance

h3: Multiple Inheritance

h3: Abstract Contracts

h3: Imports

h3: Error Triage

h3: The New Keyword

h3: 'Contract to Contract Interaction'

h3: Events

h3: Address and Payable in Solidity

h3: Minimal Token

h3: The ERC-20 Token Standard

h3: ERC-20 Implementation

h3: The ERC-721 Token Standard

h3: ERC-721 Token

h3: Wallet Connectors

h3: Building an Onchain App

h3: TheuseAccountHook

h3: TheuseReadContractHook

h3: ConfiguringuseReadContract

h3: TheuseWriteContracthook

h3: TheuseSimulateContracthook

Welcome to Base Learn, your guide to learning smart contract development. Base Learn's curriculum has been expertly crafted to equip you with the skills and knowledge needed to build and deploy smart contracts on Base, or any EVM-compatible chain, including Ethereum, Optimism, and many more. Plus, you'll be eligible to earn NFTs as you complete each module, showcasing your mastery of the material.

Whether you're a curious novice or a seasoned pro looking to stay ahead of the game, our dynamic lessons cater to all levels of experience. You can start with the basics and work your way up, or dive straight into the more advanced concepts and push your limits to new heights.

Begin your journey today!

Base Learn covers the following topics. If you're looking for quickstarts, or deeper guides on advanced topics, check out ourBase Builder Tutorials!

- Describe the origin and goals of the Ethereum blockchain
- List common types of applications that can be developed with the Ethereum blockchain
- Compare and contrast Web2 vs. Web3 development
- Compare and contrast the concept of "ownership" in Web2 vs.
```