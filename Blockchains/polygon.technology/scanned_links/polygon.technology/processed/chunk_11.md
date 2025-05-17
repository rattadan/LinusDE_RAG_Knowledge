# Documentation Analysis - Chunk chunk_11.txt

## Source Context
*From: https://polygon.technology/*

### Document Overview  
This content discusses NFTs (Non-Fungible Tokens), their limitations, and related concepts like Soulbound Tokens (SBTs) and Verifiable Credentials (VCs), emphasizing their blockchain-based nature, privacy features, and use cases.  

### Key Technical Concepts  
- **NFTs**: Public blockchain tokens with minting fees, limited standards, and no inherent ownership.  
- **SBTs**: Non-transferable, blockchain-anchored tokens tied to individual identities, but public and unsuitable for sensitive data.  
- **VCs**: Cryptographically signed credentials (e.g., KYC, degrees) stored in wallets, non-tradable, and privately secured.  
- **DIDs (Decentralized Identifiers)**: Unique, non-wallet address identifiers for VC ownership.  
- **Zero-Knowledge Technology**: Enables private credential verification without revealing sensitive data.  
- **Interoperability**: VCs standardize data formats for cross-chain identity sharing.  

### Implementation Details  
- **SBTs**: Immutable, public, and non-transferable, tied to a user’s unique DID.  
- **VCs**: Non-tradable, stored in wallet, and verifiable via DID, with optional selective disclosure.  
- **Blockchain Minting Fees**: Required for NFT creation, though not explicitly detailed in the text.  
- **Privacy Features**: VCs use zero-knowledge proofs (e.g., Privado ID) to hide sensitive data while enabling proof.  
- **Interoperability Standards**: VCs are designed to align with cross-chain identity protocols for data sharing.  

### Related Topics  
- **Blockchain Standards**: The text notes NFTs are limited to Web3 industry standards, contrasting with VC interoperability.  
- **Privacy vs. Transparency**: SBTs are public, while VCs prioritize privacy via zero-knowledge tech.  
- **Identity Management**: VCs connect to decentralized identity (DID) systems, linking to blockchain-based credentials.

---

## Original Text
```
are public on the blockchain; anyone can see them.-Costs: If you were to issue an NFT, you would have to pay blockchain minting fees.-Standards: NFTs standards are limited to Web3 industry.

Soulbound Tokens (SBTs): are NFTs thatcan't be transferredand are permanently tied to an individual owner. They are designed to store personalized data in a secure and non-transferable, non-tradable way. Although SBTs have more potential than NFTs to digitize identities, they still have the downside of being public on the blockchain and therefore are not suitable to hold sensitive data.

Verifier Credentials (VC): are a type of credential that an Issuer cryptographically signs about a user. These credentials (e.g., KYC, credit score, masters degree, etc.) are stored in the users identity wallet and not on the blockchain. These credentials are therefore private by default and are proven upon request, and in the case of Privado ID, thanks to zero-knowledge technology, they can be proven without revealing any information, unless the user decides to do so via Selective Disclosure. Verifiable credentials can be programmed to be verifiable for specific durations of time or revocable by the Issuer. Some characteristics of VCs are:

-Identifier is a DID: The identifier is not a wallet address, but a DID (decentralized identifier). The VCs are owned by the DID.-Non-transferable: VCs are issued to a specific identity (i.e. the user/Identity Holder) and cannot be transferred.-Non-tradable: As the VCs cannot be transferred, they cannot be traded. You cannot sell your credentials. They are part of who you are.-Not traceable: With the profiles anti-tracking feature of Privado ID, you can interact with different vendors via multiple DIDs generated from the main DID.-Interoperable: VCs standardize the format of information allowing Identity Holders to own their data and selectively share it with relevant parties across the internet, including between different blockchains.
```