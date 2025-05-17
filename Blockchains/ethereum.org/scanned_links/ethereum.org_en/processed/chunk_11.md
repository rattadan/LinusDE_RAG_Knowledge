# Documentation Analysis - Chunk chunk_11.txt

## Source Context
*From: https://ethereum.org/en/*

### Document Overview  
This document discusses Ethereum's address formats, compatibility with EVM-compatible blockchains, the use of seed phrases, and security considerations for wallet usage.  

### Key Technical Concepts  
- **Address Formats**: Ethereum uses a specific format for addresses, while EVM-compatible blockchains (e.g., Bitcoin, Binance Smart Chain) have distinct formats.  
- **EVM-Compatible Blockchains**: Blockchains using Ethereum Virtual Machine (EVM) code (e.g., Polygon, Arbitrum) share similar address structures.  
- **WBTC (Wrapped Bitcoin)**: A custodial solution bridging Ethereum and Bitcoin, requiring a seed phrase for recovery.  
- **Seed Phrases**: Critical for wallet restoration; losing them renders funds inaccessible.  
- **Custodial Solutions**: Wallets like WBTC are controlled by third parties, introducing security risks.  
- **Self-Custody Risks**: Phishing, recovery phrase exposure, and accidental transaction approvals are warned against.  

### Implementation Details  
- **Address Compatibility**: EVM-compatible blockchains use similar address formats (e.g., 20-byte hashes) but differ in network rules (e.g., Ethereum vs. Bitcoin).  
- **Seed Phrase Recovery**: Users can restore wallets using seed phrases, but recovery requires offline storage to prevent online leaks.  
- **WBTC Integration**: WBTC is a custodial token (e.g., BTC pegged to USD) requiring a seed phrase for access.  
- **Wallet Support**: Wallets (e.g., MetaMask) must explicitly list supported blockchains to avoid address format mismatches.  

### Related Topics  
- **Security Best Practices**: Emphasizes the importance of securing wallets and avoiding phishing scams.  
- **Wallet Types**: Contrast between custodial (e.g., WBTC) and self-custody (e.g., hardware wallets) approaches.  
- **EVM Compatibility Lists**: The document references a list of EVM-compatible blockchains (e.g., Polygon, Arbitrum) for address compatibility.

---

## Original Text
```
each with their own bookkeeping and address formats. There have been various attempts to bridge the two different networks, of which the most active one is currentlyWrapped Bitcoin or WBTC(opens in a new tab). This is not an endorsement, as WBTC is a custodial solution (meaning a single group of people controls certain critical functions) and is provided here for informational purposes only.

You can use the sameon all blockchains that use similar underlying software to Ethereum (known as 'EVM-compatible'). Thislist(opens in a new tab)will show you which blockchains you can use with the same address. Some blockchains, like Bitcoin, implement a completely separate set of network rules and you will need a different address with a different format. If you have a smart contract wallet you should check its product website for more info on which blockchains are supported because usually those have limited but more secure scope.

Having your own wallet means you take responsibility for the security of your assets. There are unfortunately many examples of failed exchanges that lost their customers' money. Owning a wallet (with a recovery phrase) removes the risk associated with trusting some entity to hold your assets. However, you have to secure it on your own and avoid phishing scams, accidentally approving transactions or exposing recovery phrase, interacting with fake websites and other self-custody risks. The risks and benefits are different.

No, you can use a different wallet. As long as you have the seed phrase you can enter it into most wallets and they will restore your account. Be careful if you ever need to do this: it is best to make sure you are not connected to the internet when recovering your wallet so that your seed phrase is not accidentally leaked. It is often impossible to recover lost funds without the recovery phrase.

================================================================================
Document: 
Source: https://ethereum.
```