# Documentation Analysis - Chunk chunk_6.txt

## Source Context
*From: https://polygon.technology/*

### Document Overview  
This content explains Privado ID's role in managing identity wallets, credentials, and verifications using PKI and zero-knowledge proofs, enabling secure authentication for dApps and smart contracts.  

### Key Technical Concepts  
- **Identity Wallets**: Secure storage of identity keys and credentials (e.g., for proving user attributes).  
- **Credentials/Proofs**: Digital artifacts (e.g., age, biometrics) used by verifiers to authenticate users.  
- **Wallet SDK**: Tools for developing mobile/web wallets to request, store, and present credentials (via ZKP).  
- **Verifier SDK**: Libraries for composing verification queries (e.g., age, uniqueness) without complex cryptographic complexity.  
- **PKI (Public Key Infrastructure)**: Ensures secure key exchange and authentication via blockchain.  
- **Zero-Knowledge Proofs (ZKP)**: Privacy-preserving verification that allows proving a statement without disclosing sensitive data.  
- **On-Chain/Off-Chain Verification**: Separation of verification logic (on-chain) from credential storage (off-chain).  

### Implementation Details  
- **Wallet SDK**: Example usage includes mobile wallets requesting credentials and presenting them via ZKP.  
- **Verifier SDK**: Enables custom verification logic (e.g., age checks) without requiring deep cryptographic expertise.  
- **PKI Integration**: Credentials are signed with public keys and stored on blockchain for tamper resistance.  
- **ZKP Mechanisms**: SDKs support zero-knowledge proofs to validate claims (e.g., "I am 18+") without exposing personal data.  

### Related Topics  
- **Privado ID Ecosystem**: The content emphasizes the broader value of Privado ID beyond tools, highlighting its role in building secure identity ecosystems.  
- **SDK Documentation**: References to the Wallet SDK and Verifier SDK (likely linked to other technical documentation).  
- **Blockchain Security**: Connections to PKI and blockchain’s tamper-resistant properties, which may align with related security guides or technical articles.

---

## Original Text
```
prove something. The user then has to request, collect and store the credential. This is done through an identity wallet. In the same way a crypto wallet holds your crypto private keys, an identity wallet holds your identity keys and your credentials.

For these identity wallets (and for crypto wallets willing to expand to hold identity keys and credentials), Privado ID includes the Wallet SDK. The Wallet SDK can be used to develop mobile wallets that request, store and present credentials or proof of credentials (using zero-knowledge proofs). Privado ID also includes a JavaScript SDK for developing web-based wallets, browser extensions and dApps.

Last but not least, these credentials are meant to give the user some power - the power to prove something about him/herself to a dApp or SmartContract (the Verifers of the credential).

The process is like a question-answer dialog. A dApp needs to verify that Im older than 18 to give me access to some content, or a SmartContract needs to verify that Im human and unique before giving me an airdrop. These Verifiers can ask my wallet these questions and my wallet will produce a valid answer using my credentials.

The entire process is highly resistant to tampering - thanks to the use of PKI (public key infrastructure) and blockchain, and privacy preserving - thanks to the use of zero knowledge proofs.

For the verification part of the process, Privado ID includes the Verifier SDK and smart contracts for off-chain and on-chain verification. These libraries allow the Verifier to compose different queries (questions) without having to deal with the complexity of reconfiguring the underlying cryptography.

For further information please see thisplaylist.

Although technically speaking Privado ID is a set of tools - its value is much more than that - its all about the ecosystem.

```