# Documentation Analysis - Chunk chunk_9.txt

## Source Context
*From: https://polygon.technology/*

### Document Overview  
This content explains Privado ID's use of zero-knowledge technology and blockchain to enhance privacy and verification, focusing on features like selective disclosure, on-chain verification, and Merkle Tree Proof (MTP) signatures.  

### Key Technical Concepts  
- **Zero-Knowledge Proofs (ZKPs)**: Enable secure verification of information without disclosing it.  
- **Selective Disclosure**: Users can share specific parts of a credential (e.g., via MTP) while proving their correctness.  
- **Merkle Tree Proof (MTP)**: A cryptographic signature that verifies the integrity of a credential’s data on-chain.  
- **On-Chain Verification**: Smart contracts verify credentials using blockchain data.  
- **Blockchain Use Cases**: Issuing credentials, revocation, and computation verification.  

### Implementation Details  
- **MTP Signature**: Issuers issue credentials with MTPs to prove their state tree on-chain.  
- **On-Chain Verification**: Verifiers use smart contracts to validate credentials by querying blockchain data.  
- **Selective Disclosure Mode**: Users choose which data to share (e.g., via MTP) and prove its correctness.  
- **Future Features**: Revocation trees will be published on-chain for credential revocation.  

### Related Topics  
- **Query Builder**: Accessible via the provided link, enabling intuitive credential creation.  
- **Video Content**: Links to videos explain technical concepts (e.g., MTP, on-chain verification).  
- **Blockchain Integration**: Connections to future features like revocation and credential issuance.

---

## Original Text
```
a more intuitive and user-friendly way to create queries. The Query Builder is accesiblehere.For further information please seethis video.

The main two uses of zero-knowledge technology used in Privado ID are:1. Preserve privacy: the user (Identity Holder) can send a proof of any information inside a credential to the Verifier (dApp) without revealing the information inside the credential. In the Selective Disclosure mode, the user can also select which information inside the credential he wants to share (without having to select the whole credential). While sharing this information, he also sends a proof about this information so the Verifier can check its correctness.

2. Verification of computation:zero-knowledge proofs can be used to prove that a computation has been performed correctly without the Verifier having to recompute it. For example, within Privado ID, it is used to prove that an identity is performing a state transition correctly.

For further information please seethis video.

There are three main uses of the blockchain for Privado ID.

1. Issuing a Merkle Tree Proof (MTP) signature to a credential: The Issuer can issue a credential with an MTP which holds information about the Issuer state tree published on-chain.

2. On-chain verification: The Verifier can use an on-chain smart contract to verify credentials.

3. On-chain issuer: The issuer can use an on-chain smart contract to issue credentials.

In the future, additional uses of blockchain will be built for Privado ID, such as to enable revocation of credentials, where the Issuer publishes the revocation tree on-chain so the user (Identity Holder) can include the revocation (or non-revocation) information inside the zero-knowledge proof they send to the Verifier.

For further information please seethis video.

An identity is represented by its identifier and a set of attributes.
```