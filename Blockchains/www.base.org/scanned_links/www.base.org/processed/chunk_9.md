# Documentation Analysis - Chunk chunk_9.txt

## Source Context
*From: https://www.base.org/*

### Document Overview  
The content covers Ethereum blockchain fundamentals, development tools, deployment processes, and interaction with external platforms like Etherscan and Hardhat.  

### Key Technical Concepts  
- **Ethereum Blockchain**: Decentralized ledger with smart contracts, gas, and a Turing-complete Virtual Machine (EVM).  
- **Web2 vs Web3**: Web2 focuses on centralized services (e.g., APIs), while Web3 emphasizes decentralized, permissionless networks (e.g., blockchain).  
- **Gas**: Fee for transaction processing on Ethereum, measured in wei, required to execute operations.  
- **EVM (Ethereum Virtual Machine)**: Runtime environment for executing smart contracts.  
- **Hardhat**: Declarative development framework for Ethereum, supporting TypeScript and deployment.  
- **TypeChain**: Tool for generating TypeScript interfaces and contracts from Solidity code.  
- **Forking**: Local network simulations for testing.  
- **Etherscan**: Platform for viewing transaction data, contracts, and network interactions.  

### Implementation Details  
- **Hardhat Setup**:  
  ```bash
  npx hardhat init
  npx hardhat setup --typescript
  ```  
  Creates a project with `hardhat.config.ts`, `contracts/`, `test/`, and `scripts/`.  
- **Gas Calculation**:  
  Gas is required to execute operations (e.g., `transfer`, `call`, `payable`).  
- **EVM Diagram**:  
  Shows the EVM’s components (state, transactions, storage, etc.).  
- **Deployment Commands**:  
  ```bash
  npx hardhat deploy --network sepolia
  npx hardhat verify --network sepolia <contract-address> <function-name>
  ```  
- **Etherscan Interactions**:  
  Use `ethers` library to read/write data (e.g., `readContract`, `writeContract`).  

### Related Topics  
- **Hardhat Forking**: Configures local networks for testing (e.g., `--network mainnet`).  
- **TypeChain**: Integrates with Hardhat for contract testing and interface generation.  
- **Etherscan**: Connected to Ethereum networks for contract verification and transaction data.  
- **Base Sepolia Testnet**: Used for deploying contracts with `hardhat-deploy`.

---

## Original Text
```
covers the following topics. If you're looking for quickstarts, or deeper guides on advanced topics, check out ourBase Builder Tutorials!

- Describe the origin and goals of the Ethereum blockchain
- List common types of applications that can be developed with the Ethereum blockchain
- Compare and contrast Web2 vs. Web3 development
- Compare and contrast the concept of "ownership" in Web2 vs. Web3
- Explain what gas is in Ethereum
- Explain why gas is necessary in Ethereum
- Understand how gas works in Ethereum transactions
- Diagram the EVM
- Install and create a new Hardhat project with Typescript support
- Describe the organization and folder structure of a Hardhat project
- List the use and properties of hardhat.config.ts
- Set up TypeChain to enable testing
- Write unit tests for smart contracts using Mocha, Chai, and the Hardhat Toolkit
- Set up multiple signers and call smart contract functions with different signers
- List some of the features of Etherscan
- Read data from the Bored Ape Yacht Club contract on Etherscan
- Write data to a contract using Etherscan.
- Deploy a smart contract to the Base Sepolia Testnet with hardhat-deploy
- Deploy a smart contract to the Sepolia Testnet with hardhat-deploy
- Use BaseScan to view a deployed smart contract
- Verify a deployed smart contract on Etherscan
- Connect a wallet to a contract in Etherscan
- Use etherscan to interact with your own deployed contract
- Use Hardhat Network to create a local fork of mainnet and deploy a contract to it
- Utilize Hardhat forking features to configure the fork for several use cases
- List the features, pros, and cons of using Remix as an IDE
- Deploy and test the Storage.sol demo contract in Remix
- Deploy and test the Storage.
```