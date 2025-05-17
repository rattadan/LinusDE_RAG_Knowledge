# Documentation Analysis - Chunk chunk_22.txt

## Source Context
*From: https://www.base.org/*

### Document Overview  
This content explains Basenames as onchain identifiers for wallet addresses, their pricing model, discounts, and integration with the Base ecosystem.  

### Key Technical Concepts  
- **Basenames**: Onchain names for wallet addresses, priced by length, and globally accessible.  
- **ENS-like Technology**: Built on the same infrastructure as ENS, enabling interoperability with onchain apps.  
- **Registration Fees**: Based on name length, with free Basenames for 5+ letters and discounts for extended terms.  
- **Discounts**: Applied once per address, with limits on per-name discounts (e.g., 0.001 ETH for shorter names or longer terms).  
- **Onchain Publishing**: Any information published via Basenames is recorded onchain and composable with other ecosystem components.  
- **OnchainKit**: Tool for integrating Basenames into apps, enabling seamless use across Base ecosystem services.  

### Implementation Details  
- **Pricing Model**: Free Basenames (5+ letters) for 1 year, with discounts for shorter names or longer terms.  
- **Discount Rules**:  
  - Apply only once per address.  
  - Highest-value discount (e.g., 0.01 ETH) for BNS name owners.  
  - Example: A 4-letter name with a 0.001 ETH discount vs. a 5-letter name with a 0.001 ETH discount.  
- **Integration**: OnchainKit provides tutorials for integrating Basenames into apps, enabling use across Base ecosystem services (e.g., base.org, Onchain Registry).  
- **Onchain Publishing**: Users must explicitly publish data onchain, ensuring transparency and composability.  

### Related Topics  
- **OnchainKit**: Tutorial for integrating Basenames into apps.  
- **Base Ecosystem**: Integration with base.org, Onchain Registry, and Onchain Summer Pass.  
- **ENS Interoperability**: Shared technology with ENS, enabling cross-chain use.

---

## Original Text
```

Basenames are a core onchain building block that enable builders to establish their identity on Base by registering human-readable names for their wallet address(es). They are fully onchain, built on the same technology powering ENS names, and deployed on Base. These human-readable names can be used when connecting to onchain apps, and sending and receiving on Base and any other EVM chain.

Basenames are priced based on name length, and are designed to be globally accessible. Annual registration fees are as follows:

You can get one free Basename (5+ letters) for one year if you meet any of the below criteria:

An equivalent-value discount of 0.001 ETH will be applied if registering a shorter name, or registering for more than 1 year, with the exception of the BNS name owner discount (valued at 0.01 ETH per unique address). You will need to pay the standard registration fees if you wish to keep your Basename after your initial discount has been fully applied.

Discounts are only applied once, and are limited to one per address. Even if you meet multiple criteria, you will only be eligible for a single discount on one Basename. If you satisfy multiple criteria, we will automatically apply the highest-value discount to your registration.

We are always looking to add more discounts. If you or your project have ideas for more discounts, please reach out to our team.

You can use your Basename across apps in the Base ecosystem, starting with base.org, Onchain Registry, and Onchain Summer Pass. You can also use it for sending and receiving on Base and other EVM chains.

Basenames are fully onchain, and therefore any information you publish is recorded onchain, requires a transaction, and will be broadly composable with the rest of the ecosystem. Please do not publish any information you do not wish to be onchain.

If you're a builder looking to integrate Basenames into your app,OnchainKitis the easiest way to get started (tutorial here).
```