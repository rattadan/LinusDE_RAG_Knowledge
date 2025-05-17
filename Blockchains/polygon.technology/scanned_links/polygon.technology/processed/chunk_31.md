# Documentation Analysis - Chunk chunk_31.txt

## Source Context
*From: https://polygon.technology/*

### Document Overview  
This content outlines Privado ID, a privacy-focused identity system enabling verifiable credentials through cryptographic signing, trusted issuers, and secure wallets, with a focus on user data sovereignty and decentralized authentication.  

### Key Technical Concepts  
- **Verifiable Credentials**: Data that can be authenticated and verified via cryptographic signatures, compliant with W3C standards.  
- **Issuer Nodes**: Self-hosted APIs for creating credentials, managed by trusted entities (e.g., governments, KYC providers).  
- **Identity Wallets**: Secure storage for user identities and credentials, analogous to crypto wallets but tailored for privacy.  
- **Wallet SDKs**: Tools for developing mobile, web, and dApp wallets to request, store, and present credentials using zero-knowledge proofs.  
- **Zero-Knowledge Proofs (ZKPs)**: Cryptographic methods to prove knowledge without revealing underlying data.  
- **Credential Lifecycle**: Credentials are created when users request them, stored in wallets, and verified via dApps or smart contracts.  

### Implementation Details  
- **Issuer Node**: A self-hosted API for issuing credentials, requiring cryptographic signing and trust management.  
- **Wallet SDKs**:  
  - **Mobile**: SDKs for requesting credentials and presenting proofs (e.g., via zero-knowledge proofs).  
  - **Web/Browser**: JavaScript SDKs for dApps and extensions to verify credentials.  
- **Credential Verification**: Users interact with dApps/smart contracts via identity wallets, which generate answers to verification questions (e.g., "Are you 18+?") using their stored credentials.  
- **Privacy-Enhanced Design**: Credentials are not stored in the cloud; they are locally managed by wallets, ensuring user control over data.  

### Related Topics  
- **Wallet SDKs**: Connected to broader documentation on crypto wallet development and identity management.  
- **Zero-Knowledge Proofs**: Tied to related topics in privacy-focused blockchain frameworks (e.g., zk-SNARKs).  
- **Verifiable Credentials**: Linked to W3C standards and decentralized identity protocols (e.g., Verifiable Credentials specification).

---

## Original Text
```
Privado ID is designed for developers with a strong focus on privacy, decentralization and user data self-sovereignty.

Verifiable credentials are issued according to theW3C standardsand signed cryptographically to ensure they are tamper-proof. This is performed by Issuers, which are trusted organizations or companies. In the real world, this could include your government, university, or bank. In Web3, this could include KYC providers, oracles, DAOs, reputation services, etc.

For these Issuers, Privado ID includes the Issuer Node, a self hosted API capable of creating these credentials.

Credentials are not created in the void. They are created when a user requests them to prove something. The user then has to request, collect and store the credential. This is done through an identity wallet. In the same way a crypto wallet holds your crypto private keys, an identity wallet holds your identity keys and your credentials.

For these identity wallets (and for crypto wallets willing to expand to hold identity keys and credentials), Privado ID includes the Wallet SDK. The Wallet SDK can be used to develop mobile wallets that request, store and present credentials or proof of credentials (using zero-knowledge proofs). Privado ID also includes a JavaScript SDK for developing web-based wallets, browser extensions and dApps.

Last but not least, these credentials are meant to give the user some âpowerâ - the power to prove something about him/herself to a dApp or SmartContract (the Verifers of the credential).

The process is like a âquestion-answerâ dialog. A dApp needs to verify that Iâm older than 18 to give me access to some content, or a SmartContract needs to verify that Iâm human and unique before giving me an airdrop. These Verifiers can âaskâ my wallet these questions and my wallet will produce a valid answer using my credentials.

```