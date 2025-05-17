# Documentation Analysis - Chunk chunk_20.txt

## Source Context
*From: https://www.dydx.xyz/*

### Document Overview  
The content discusses the transition from Proof of Work (PoW) to Proof of Stake (PoS) in Ethereum 2.0, highlighting its environmental impact, fee structure changes, reduced energy consumption, and technical features like the Beacon Chain and EIP-1559.  

### Key Technical Concepts  
- **PoS (Proof of Stake)**: Ethereum 2.0 uses this consensus mechanism instead of PoW, reducing energy consumption.  
- **PoW (Proof of Work)**: Traditional blockchain consensus, requiring massive computational power (rigs) and high energy consumption.  
- **Fee Structures**: Ethereum 2.0 maintains the same fee structure post-transition, while EIP-1559 introduces a burn mechanism to reduce inflation.  
- **Energy Efficiency**: Ethereum 2.0 consumes 99.95% less energy than its PoW predecessor.  
- **Issuance Schedule**: Ethereum 2.0 reduces daily ETH issuance from ~14,700 ETH to ~1,700 ETH.  
- **Beacon Chain**: The PoS execution layer launched on September 15, 2022, during the "The Merge."  
- **EIP-1559**: A 2021 upgrade that burns transaction fees, making ETH a deflationary asset.  

### Implementation Details  
- **Energy Consumption**: Ethereum 2.0’s consensus layer consumes 99.95% less energy than the execution layer (e.g., 1,700 ETH/day vs. Bitcoin’s high energy use).  
- **Fee Burning**: EIP-1559 burns a portion of transaction fees, with daily burn rates exceeding 1,700 ETH triggering deflationary behavior.  
- **Issuance Reduction**: Daily ETH issuance dropped from ~14,700 ETH to ~1,700 ETH after the PoS transition.  
- **Beacon Chain**: The PoS execution layer (Beacon Chain) was launched on September 15, 2022, during the "The Merge."  
- **Validator Requirements**: PoS validators must run the blockchain software and stake ETH, avoiding reliance on mining rigs.  

### Related Topics  
- **Comparison with Bitcoin**: The content highlights Ethereum 2.0’s environmental advantages over PoW blockchains like Bitcoin.  
- **Ethereum Foundation**: The Ethereum Foundation’s role in implementing EIP-1559 and the Beacon Chain is emphasized.  
- **Future of Ethereum 2.0**: The document notes the long-term implications of reduced issuance and energy efficiency.

---

## Original Text
```

The key difference between Ethereum and Ethereum 2.0 is that the latter uses PoS rather than PoW. However, this doesnât mean Ethereum 2.0 instantly becomes a faster and cheaper version of the original blockchain. Immediately following its transition to PoS, Ethereum 2.0 experienced no change in its fee structure and onlynegligibly quicker transaction speeds.

However, the shift to Ethereum 2.0 dramatically affects the blockchainâs environmental impact. On one hand, PoW blockchains, such as Bitcoin, need significant electrical power to figure out the protocolâs advanced computations. Conversely, PoS blockchains donât require large computers (ârigsâ) solely to solve complex equations and post new transactions. Instead of running crypto mining rigs day and night, Ethereumâs PoS validators install and run the blockchainâs software on their computer, link theircrypto wallet, and stake ETH on the blockchain. Although Ethereum validators need to keep their computers constantly running to validate blocks, they donât have to use as much energy to solve the equations in a PoW model. In fact, the Ethereum Consensus Layer consumes99.95% less energythan the execution layer, according to the Ethereum Foundation.

Another significant difference between Ethereum and Ethereum 2.0 is that the latter has a lower coin issuance schedule. Pre-ETH2, the Ethereum protocol mintedapproximately 14,700ETH every day. After switching to PoS, daily issuance dropped to 1,700 ETH. Also, thanks to the EIP-1559 upgrade in 2021, Ethereum destroys or burns a portion of every transaction fee on the blockchain. Whenever the burn rate on Ethereum 2.0 exceeds 1,700 ETH per day, ETH becomes a deflationary digital asset.

Ethereum 2.0 launched on September 15, 2022, during âThe Merge,â when Ethereumâs execution layer transitioned all its data to a PoS chain called the âBeacon Chain.
```