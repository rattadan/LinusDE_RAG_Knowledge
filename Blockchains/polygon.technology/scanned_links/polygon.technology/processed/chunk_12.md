# Documentation Analysis - Chunk chunk_12.txt

## Source Context
*From: https://polygon.technology/*

### Document Overview  
The content discusses Privado ID, a decentralized identity solution that enables verifiable credentials, interoperability, privacy, and cost-efficiency, with details on its deployment on EVM-compatible chains and open-source infrastructure.  

### Key Technical Concepts  
- **Verifiable Credentials (VC):** Digital credentials (e.g., KYC) that users can own and share selectively.  
- **Decentralized Identifiers (DIDs):** Unique, decentralized identifiers for users, enabling secure interactions via privacy-preserving protocols.  
- **Zero-Knowledge Proofs (ZKPs):** Techniques to prove identity without revealing sensitive data.  
- **EVM-Compatible Chains:** Blockchain platforms (e.g., Polygon) that support smart contracts and decentralized applications.  
- **Interoperability:** Standardized formats (e.g., W3C) for exchanging credentials across networks, including blockchains.  
- **Privacy by Default:** Credentials stored in users’ wallets, shared only with explicit consent.  

### Implementation Details  
- **Smart Contracts:** Deployed on Polygon Testnet (Amoy) and PoS Mainnet, with plans to support other EVM-compatible chains.  
- **Open-Source:** Free to use, with future revenue models for infrastructure/services.  
- **Costs:** No minting/transfer costs due to non-transferable VC format; privacy features minimize data exposure.  
- **W3C Standards:** Implementation of Verifiable Credentials (W3C standard) for cross-platform interoperability.  

### Related Topics  
- **Cost of Privado ID:** Connected to the question about pricing and infrastructure revenue models.  
- **Ecosystem Integration:** References projects already using Privado ID, highlighting its role in Web3 adoption.  
- **Technical Specifications:** Details on EVM compatibility, zero-knowledge proofs, and DID-based authentication.

---

## Original Text
```
They are part of who you are.-Not traceable: With the profiles anti-tracking feature of Privado ID, you can interact with different vendors via multiple DIDs generated from the main DID.-Interoperable: VCs standardize the format of information allowing Identity Holders to own their data and selectively share it with relevant parties across the internet, including between different blockchains. For example, once you have your KYC credentials, you can reuse them to authenticate you in different applications.-Private by default: VCs are not publicly viewable as they are stored in the users digital wallet (you own your data), and will only be shared upon user consent and without necessarily revealing any information, thanks to zero-knowledge proofs.-Costs: as the VC is not transferable and is not stored on the blockchain, there are no minting or transfer costs as with NFTs. For more details about the costs of running Privado ID, see the question What is the cost of Privado ID?.-Standards: VCs are globally recognized for their adherence to W3C standards, widely embraced in the enterprise sector compared to the more specialized adoption of NFTs and SBTs within Web3.Verifiable credentials, the W3C standard implemented in Privado ID, are the most practical technology to digitize our identities and finally allow people to prove who they are on the internet. The challenge is user adoption, and Privado ID is leading the way in the Web3 space.Join the ecosystemof projects already implementing Privado ID!

Privado ID can run on any EVM-compatible chain. At the moment, the necessary smart contracts are deployed onto Polygon Testnet (Amoy) and Polygon PoS Mainnet, but they could be deployed into any other EVM-compatible chain including any CDK-based blockchain very soon.

Privado ID is an open-source software and is free to use. However, Privado ID plans to generate revenue by offering additional infrastructure and services.

```