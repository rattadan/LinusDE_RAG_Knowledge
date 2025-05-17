# Documentation Analysis - Chunk chunk_10.txt

## Source Context
*From: https://polygon.technology/*

### Document Overview  
The content discusses Privado ID's identity management system, focusing on revocation mechanisms, NFTs, and SBTs as key components for decentralized identity verification.  

### Key Technical Concepts  
- **Privado ID**: A decentralized identity system using DID (decentralized identifiers) and verifiable credentials (VC).  
- **Revocation Tree**: On-chain structure for revoking credentials, enabling users to embed revocation or non-revocation info in zero-knowledge proofs.  
- **Zero-Knowledge Proof (ZKP)**: A cryptographic method to prove identity without revealing sensitive data.  
- **NFTs (Non-Fungible Tokens)**: Unique digital assets tied to blockchain, used as purchasable membership passes or certificates.  
- **SBTs (Soulbound Tokens)**: Non-transferable, persistent NFTs storing personalized data securely.  
- **DID (Decentralized Identifier)**: Unique, public identifiers for digital identities.  
- **Verifiable Credentials (VC)**: W3C-standard credentials used in Privado ID to authenticate attributes.  

### Implementation Details  
- **Revocation Tree**: The Issuer publishes a revocation tree on-chain, allowing users to include revocation information in ZKP proofs.  
- **Identity Representation**: Identity is defined by an identifier (e.g., wallet address) and attributes (e.g., NFTs, VC).  
- **NFT Characteristics**:  
  - **Identifier**: Linked to a blockchain-specific wallet address.  
  - **Transferable**: NFTs can be moved between addresses.  
  - **Traceable**: Blockchain logs track NFT ownership.  
  - **Standards**: Limited to Web3 industry.  
- **SBTs**: Non-transferable NFTs tied to an individual, storing personal data securely.  

### Related Topics  
- **Video**: The content references a video for further information.  
- **DID (Decentralized Identifier)**: Linked to the identity system described.  
- **Verifiable Credentials (VC)**: Used as attributes in the identity model.  
- **On-chain Revocation**: Key to the revocation tree mechanism.

---

## Original Text
```
will be built for Privado ID, such as to enable revocation of credentials, where the Issuer publishes the revocation tree on-chain so the user (Identity Holder) can include the revocation (or non-revocation) information inside the zero-knowledge proof they send to the Verifier.

For further information please seethis video.

An identity is represented by its identifier and a set of attributes. For example, your identifier could be your wallet address and your attributes could be non-fungible tokens (NFTs) or soulbound tokens (SBTs). Or your identifier could be your DID (decentralized identifier) and your attributes could be verifiable credentials (VC), the W3C standard used in Privado ID.

Non-Fungible Tokens (NFTs): are unique representations of an asset on a blockchain. NFTs have frequently been speculative assets used to represent community memberships, profile pictures, art, metaverse land, and more. In digital identity, NFTs are used primarily as a form of purchasable membership pass or as a certificate. Some characteristics of NFTs are:-Identifier is a wallet address:NFTs are associated with static, public wallet addresses.-Transferable: NFT can be transferred to another address therefore to another user.-Tradable: NFTs facilitate the seamless buying and selling of digital assets.-Traceable: Anyone can see on the blockchain how an NFT has been transferred.-Blockchain specific: An NFT is tied to a specific blockchain.-Public:NFTs are public on the blockchain; anyone can see them.-Costs: If you were to issue an NFT, you would have to pay blockchain minting fees.-Standards: NFTs standards are limited to Web3 industry.

Soulbound Tokens (SBTs): are NFTs thatcan't be transferredand are permanently tied to an individual owner. They are designed to store personalized data in a secure and non-transferable, non-tradable way.
```