# Documentation Analysis - Chunk chunk_36.txt

## Source Context
*From: https://polygon.technology/*

### Document Overview  
The content discusses NFTs (Non-Fungible Tokens), their characteristics, and related concepts like Soulbound Tokens (SBTs) and Verifier Credentials (VCs), focusing on their roles in digital identity and blockchain technology.  

### Key Technical Concepts  
- **NFTs**: Blockchain-based assets with unique identifiers, transferable, tradable, and traceable.  
- **SBTs**: Non-transferable NFTs tied to individual owners, used for secure, private data storage.  
- **VCs**: Cryptographic credentials stored in user wallets, provable upon request, and potentially verifiable via zero-knowledge technology.  
- **Blockchain-specific features**: Wallet addresses, minting fees, public visibility, and standards limited to Web3.  

### Implementation Details  
- **NFTs**: Require blockchain minting fees for creation, with identifiers as wallet addresses.  
- **SBTs**: Permanently tied to owners, public on the blockchain, and non-transferable.  
- **VCs**: Stored in user wallets, private by default, and provable via zero-knowledge proofs (e.g., Privado ID).  
- **Standards**: NFTs lack universal standards, while VCs rely on issuer-defined revocability and duration.  

### Related Topics  
- **Blockchain technology**: The document references blockchain-specific features like wallet addresses and minting fees.  
- **Digital identity**: SBTs and VCs are discussed in the context of secure, private data storage and verification.  
- **Web3 standards**: NFTs are tied to Web3 industry standards, while VCs are governed by issuer-defined rules.

---

## Original Text
```
asset on a blockchain. NFTs have frequently been speculative âassetsâ used to represent community memberships, profile pictures, art, metaverse land, and more. In digital identity, NFTs are used primarily as a form of purchasable membership pass or as a certificate. Some characteristics of Â NFTs are:â-Identifier is a wallet address:NFTs are associated with static, public wallet addresses.-Transferable: NFT can be transferred to another address therefore to another user.-Tradable: NFTs facilitate the seamless buying and selling of digital assets.-Traceable: Anyone can see on the blockchain how an NFT has been transferred.-Blockchain specific: An NFT is tied to a specific blockchain.-Public:NFTs are public on the blockchain; anyone can see them.-Costs: If you were to issue an NFT, you would have to pay blockchain minting fees.-Standards: NFTs standards are limited to Web3 industry.

â¢Soulbound Tokens (SBTs): are NFTs thatcan't be transferredand are permanently tied to an individual owner. They are designed to store personalized data in a secure and non-transferable, non-tradable way. Although SBTs have more potential than NFTs to digitize identities, they still have the downside of being public on the blockchain and therefore are not suitable to hold sensitive data.

â¢Verifier Credentials (VC): are a type of credential that an Issuer cryptographically signs about a user. These credentials (e.g., KYC, credit score, masterâs degree, etc.) are stored in the userâs identity wallet and not on the blockchain. These credentials are therefore private by default and are proven upon request, and in the case of Privado ID, thanks to zero-knowledge technology, they can be proven without revealing any information, unless the user decides to do so via Selective Disclosure. Verifiable credentials can be programmed to be verifiable for specific durations of time or revocable by the Issuer. Some characteristics of VCs are:

```