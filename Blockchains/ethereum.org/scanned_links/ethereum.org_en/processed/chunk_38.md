# Documentation Analysis - Chunk chunk_38.txt

## Source Context
*From: https://ethereum.org/en/*

### Document Overview  
This content provides technical details about Ethereum accounts, including balances, token holdings, transaction histories, contract metadata, and metrics like market cap, ETH price, and transaction throughput.  

### Key Technical Concepts  
- **ETH Balance**: The amount of Ethereum held by an account.  
- **Token Holdings**: Tokens (e.g., ERC-20, ERC-721) and their values, including total supply, decimals, and market cap.  
- **Transaction History**: Logs of all transactions (send, receive, contract calls) associated with an account.  
- **Contract Creation**: Deployment addresses, ABI, bytecode, and event logs for smart contracts.  
- **Metrics**: Metrics like transactions per second, ETH price, and total ETH supply.  
- **ERC Standards**: Token types (ERC-20, ERC-721) and their specific properties (e.g., decimals, transfer events).  

### Implementation Details  
- **ETH Balance Calculation**: Derived from the account’s balance in the Ethereum blockchain.  
- **Token Metrics**: Market cap = price * total supply (for ERC-20 tokens).  
- **Contract ABI**: Application Binary Interface details (function signatures, data structures) for contract interactions.  
- **Transaction History**: Logs include sender/receiver addresses, transaction hashes, and timestamps.  
- **Epoch Number**: A sequential identifier for blockchain blocks (used in finalization processes).  
- **ETH Price**: Dynamic value based on market supply and demand (e.g., USD price).  
- **Transaction Throughput**: Measures the number of transactions processed per second (e.g., 10,000 TPS).  

### Related Topics  
- **Contract ABI/Code**: Linked to Ethereum’s Solidity/Vyper compiler outputs and interaction logs.  
- **Transaction History**: Connected to Ethereum’s blockchain explorer tools and analytics platforms.  
- **Epoch Number**: Related to Ethereum’s finalization process and blockchain validation.

---

## Original Text
```
address you can use to send funds to
- ETH balance - The amount of ETH associated with that account
- Total ETH value - The value of the ETH
- Tokens - The tokens associated with the account and their value
- Transaction history - A list of all the transactions where this account was either the sender or the recipient
- Contract creator - The address that deployed the contract to Mainnet
- Creation transaction - The transaction that included the deployment to Mainnet
- Source code - The solidity or vyper code of the smart contract
- Contract ABI - The Application Binary Interface of the contractthe calls the contract makes and the data received
- Contract creation code - The compiled bytecode of the smart contractcreated when you compile a smart contract written in Solidity or Vyper, etc.
- Contract events - A history of the methods called in the smart contractbasically a way to see how the contract is being used and how often
- Type - Whether they're an ERC-20, ERC-721 or another token standard
- Price - If they're an ERC-20 they'll have a current market value
- Market cap - If they're an ERC-20 they'll have a market cap (calculated by price*total supply)
- Total supply - The number of tokens in circulation
- Holders - The number of addresses that hold the token
- Transfers - The number of times the token has been transferred between accounts
- Transaction history - A history of all the transactions including the token
- Contract address - The address of the token that was deployed to Mainnet
- Decimals - ERC-20 tokens are divisible and have decimal places
- Total transactions - The number of transactions since Ethereum was created
- Transactions per second - The number of transactions processable within a second
- ETH price - The current valuations of 1 ETH
- Total ETH supply - Number of ETH in circulationremember new ETH is created with the creation of every block in the form of block rewards
- Market cap - Calculation of price*supply
- Epoch number
- Finalized s
```