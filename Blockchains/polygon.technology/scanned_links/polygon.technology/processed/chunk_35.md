# Documentation Analysis - Chunk chunk_35.txt

## Source Context
*From: https://polygon.technology/*

### Document Overview  
This content explains how Privado ID leverages blockchain and zero-knowledge proofs (ZKPs) for secure identity verification, including on-chain credential issuance, verification, and future features like revocation.  

### Key Technical Concepts  
- **Zero-Knowledge Proofs (ZKPs)**: Used to prove computations are correct without revealing sensitive data.  
- **Merkle Tree Proof (MTP)**: A cryptographic mechanism to verify credential validity on-chain.  
- **On-chain Verification/Issuance**: Smart contracts enable trusted, decentralized credential validation and issuance.  
- **Non-Fungible Tokens (NFTs)**: Unique digital assets used as membership passes or certificates in identity management.  
- **Decentralized Identifiers (DIDs)**: Unique, decentralized representations of identities (e.g., wallet addresses or DID documents).  
- **Revocation Trees**: On-chain structures to manage credential validity and revocation.  

### Implementation Details  
- **Use Cases**:  
  1. **MTP Signatures**: Issuers embed Merkle Tree Proofs in credentials to verify state transitions.  
  2. **On-chain Verification**: Verifiers use smart contracts to validate credentials (e.g., NFTs or verifiable credentials).  
  3. **On-chain Issuance**: Issuers deploy smart contracts to issue credentials (e.g., DID documents or NFTs).  
- **Attributes**: Credentials include identifiers (e.g., wallet addresses) and attributes (e.g., NFTs, verifiable credentials).  
- **Future Features**: Revocation trees will enable credential revocation via on-chain publishing.  

### Related Topics  
- **Video Link**: The document references a video for further details.  
- **DID/Attribute Pairing**: The example ties DID identifiers to attributes like NFTs or verifiable credentials.  
- **On-chain Contracts**: The three use cases highlight the role of smart contracts in decentralized identity management.

---

## Original Text
```

2. Verification of computation:Â zero-knowledge proofs can be used to prove that a computation has been performed correctly without the Verifier having to recompute it. For example, within Privado ID, it is used to prove that an identity is performing a state transition correctly.

For further information please seethis video.

There are three main uses of the blockchain for Privado ID.

1. Issuing a Merkle Tree Proof (MTP) signature to a credential: The Issuer can issue a credential with an MTP which holds information about the Issuer state tree published on-chain.

2. On-chain verification: The Verifier can use an on-chain smart contract to verify credentials.

3. On-chain issuer: The issuer can use an on-chain smart contract to issue credentials.

In the future, additional uses of blockchain will be built for Privado ID, such as to enable revocation of credentials, where the Issuer publishes the revocation tree on-chain so the user (Identity Holder) can include the revocation (or non-revocation) information inside the zero-knowledge proof they send to the Verifier.

For further information please seethis video.

An identity is represented by its identifier and a set of attributes. For example, your identifier could be your wallet address and your attributes could be non-fungible tokens (NFTs) or soulbound tokens (SBTs). Or your identifier could be your DID (decentralized identifier) and your attributes could be verifiable credentials (VC), the W3C standard used in Privado ID.

â¢Non-Fungible Tokens (NFTs): are unique representations of an asset on a blockchain. NFTs have frequently been speculative âassetsâ used to represent community memberships, profile pictures, art, metaverse land, and more. In digital identity, NFTs are used primarily as a form of purchasable membership pass or as a certificate. Some characteristics of Â NFTs are:â-Identifier is a wallet address:NFTs are associated with static, public wallet addresses.
```