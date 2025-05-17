# Documentation Analysis - Chunk chunk_37.txt

## Source Context
*From: https://polygon.technology/*

### Document Overview  
This content explains Verifiable Credentials (VCs) from Polygon, emphasizing their privacy, interoperability, and technical features like DID-based identifiers, non-transferability, and zero-knowledge proofs, while discussing their cost structure and adherence to W3C standards.  

### Key Technical Concepts  
- **Verifiable Credentials (VCs)**: Decentralized digital credentials that can be proven securely.  
- **Decentralized Identifier (DID)**: A unique, persistent identifier (not a wallet address) used to own and manage VC data.  
- **Non-Transferable/Non-Tradable**: VCs cannot be transferred or traded, ensuring ownership and data integrity.  
- **Private by Default**: VCs are stored in users' wallets and only shared with explicit consent, using zero-knowledge proofs to protect sensitive info.  
- **Selective Disclosure**: Users can choose to reveal specific details of a VC without disclosing all data.  
- **Interoperability**: VCs standardize data formats, enabling cross-platform sharing (e.g., KYC credentials across apps).  
- **Zero-Knowledge Proofs (ZKPs)**: Cryptographic methods to prove knowledge without revealing underlying data.  
- **Revocable Credentials**: VCs can be revoked by the issuer, ensuring accountability.  

### Implementation Details  
- **Storage**: VCs are stored in users' wallets (not on the blockchain), with data ownership fully controlled by the user.  
- **Revocable**: Issuers can revoke VCs, allowing users to update or remove their credentials.  
- **Time-Based Validity**: VCs can be programmed to expire after specific durations, ensuring时效性 (timeliness).  
- **Selective Disclosure**: Users can choose to reveal only certain details of a VC (e.g., KYC info) via "Selective Disclosure."  
- **Interoperability Standards**: VCs follow W3C standards, enabling seamless sharing across platforms (e.g., blockchain, web apps).  
- **Cost Structure**: No minting or transfer costs apply, as VCs are non-transferable and not stored on the blockchain.  

### Related Topics  
- **Cost of Privado ID**: The document references a question about operational costs, indicating connections to the "What is the cost of Privado ID?" section.  
- **Privacy Features**: The content ties to Privado ID’s anti-tracking capabilities and multi-DID profiles, which are described in the "Privacy and Security" section of the documentation.

---

## Original Text
```
are therefore private by default and are proven upon request, and in the case of Privado ID, thanks to zero-knowledge technology, they can be proven without revealing any information, unless the user decides to do so via Selective Disclosure. Verifiable credentials can be programmed to be verifiable for specific durations of time or revocable by the Issuer. Some characteristics of VCs are:

-Identifier is a DID: The identifier is not a wallet address, but a DID (decentralized identifier). The VCs are owned by the DID.-Non-transferable: VCs are issued to a specific identity (i.e. the user/Identity Holder) and cannot be transferred.-Non-tradable: As the VCs cannot be transferred, they cannot be traded. You cannot sell your credentials. They are part of who you are.-Not traceable: With the profiles anti-tracking feature of Privado ID, you can interact with different vendors via multiple DIDs generated from the main DID.-Interoperable: VCs standardize the format of information allowing Identity Holders to own their data and selectively share it with relevant parties across the internet, including between different blockchains. For example, once you have your KYC credentials, you can reuse them to authenticate you in different applications.-Private by default: VCs are not publicly viewable as they are stored in the userâs digital wallet (you own your data), and will only be shared upon user consent and without necessarily revealing any information, thanks to zero-knowledge proofs.-Costs: as the VC is not transferable and is not stored on the blockchain, there are no minting or transfer costs as with NFTs. For more details about the costs of running Privado ID, see the question âWhat is the cost of Privado ID?â.-Standards: VCs are globally recognized for their adherence to W3C standards, widely embraced in the enterprise sector compared to the more specialized adoption of NFTs and SBTs within Web3.
```