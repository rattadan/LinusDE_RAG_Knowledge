# Documentation Analysis - Chunk chunk_36.txt

## Source Context
*From: https://ethereum.org/en/*

### Document Overview  
The content lists block explorers (e.g., Ethplorer, Otterscan) and technical block metrics (e.g., block height, timestamp, gas usage, and fees), providing insights into blockchain data structures and tools for analysis.  

### Key Technical Concepts  
- **Block Explorers**: Tools for visualizing blockchain data (e.g., block height, timestamp, transactions, and fees).  
- **Block Metrics**: Technical details like block reward, gas used, base fee per gas, and burnt fees.  
- **Merkle Trie**: A data structure storing the entire state of the blockchain (e.g., `StateRoot`).  
- **Gas Pricing**: Estimated gas units for transactions (slow, average, fast) and their associated prices/durations.  
- **Gas Limit**: Maximum gas allowed in a block, distinguishing between gas used and gas limit.  

### Implementation Details  
- **Block Metrics**:  
  - **Block Height**: Block number and length (in blocks) at creation.  
  - **Timestamp**: Time when a block was proposed.  
  - **Transactions**: Count of transactions in the block.  
  - **Block Reward**: ETH awarded to validators for proposing blocks.  
  - **Gas Used**: Total gas consumed by transactions in the block.  
  - **Base Fee per Gas**: Minimum gas price required for transactions to be included.  
  - **Burnt Fees**: ETH burned in the block (not returned to senders).  
- **Technical Structure**:  
  - **Hash**: Cryptographic hash of the block header (unique identifier).  
  - **Parent Hash**: Hash of the previous block.  
  - **Gas Limit vs. Gas Used**: Difference between the maximum gas allowed and the actual gas consumed.  

### Related Topics  
- **Ethereum Block Explorers**: Connections to tools like Ethplorer, Otterscan, and lazy-etherscan.  
- **Blockchain Data Structures**: Links to Merkle trie (e.g., `StateRoot`) and gas pricing mechanisms.  
- **Gas Pricing Models**: References to estimated gas units for transactions (slow, average, fast) and their associated prices/durations.

---

## Original Text
```
tab)
- Chainlens(opens in a new tab)
- DexGuru Block Explorer(opens in a new tab)
- Etherchain(opens in a new tab)
- Ethernow(opens in a new tab)
- Ethplorer(opens in a new tab)-Also available in Chinese, Spanish, French, Turkish, Russian, Korean and Vietnamese
- EthVM(opens in a new tab)
- OKLink(opens in a new tab)
- Rantom(opens in a new tab)
- Ethseer(opens in a new tab)
- Otterscan(opens in a new tab)
- lazy-etherscan(opens in a new tab)
- Block height - The block number and length of the blockchain (in blocks) on creation of the current block
- Timestamp - The time at which a block was proposed
- Transactions - The number of transactions included within the block
- Fee recipient - The address that received gas fee tips from transactions
- Block Reward - The amount of ETH awarded to the validator who proposed the block
- Size - The size of the data within the block (measured in bytes)
- Gas used - The total units of gas used by the transactions in the block
- Gas limit - The total gas limits set by the transactions in the block
- Base fee per gas - The minimum multiplier required for a transaction to be included in a block
- Burnt fees - How much ETH is burned in the block
- Extra data - Any extra data the builder has included in the block
- Hash - The cryptographic hash that represents the block header (the unique identifier of the block)
- Parent hash - The hash of the block that came before the current block
- StateRoot - The root hash of Merkle trie which stores the entire state of the system
- Estimated units of gas needed for a safe but slow transaction (+ estimated price and duration)
- Estimated units of gas needed for an average transaction (+ estimated price and duration)
- Estimated units of gas needed for a fast transaction (+ estimated price and duration)
- Average confirmation time based on gas price
- Contracts that are consuming gas - in other words, popular products that are seeing lots of usage on the network
- Accounts that are spending gas -
```