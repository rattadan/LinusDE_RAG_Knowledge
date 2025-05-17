# Documentation Analysis - Chunk chunk_8.txt

## Source Context
*From: https://polygon.technology/*

### Document Overview  
The content outlines Privado ID’s tools and features for managing identity wallets, including issuer nodes, verifier SDKs, JS SDKs, and tools like Schema Builder and Query Builder, focusing on zero-knowledge technology for privacy and verification.  

### Key Technical Concepts  
- **Issuer Node**: A self-hosted application for controlling data issuance, exposing API methods for issuing Verifiable Credentials.  
- **Verifiable Credentials**: Credentials with privacy-preserving proofs, allowing verifiers (e.g., dApps) to validate claims without exposing sensitive data.  
- **Zero-Knowledge Technology**: Used to enable privacy-preserving proofs, where users can prove knowledge of a credential’s content without revealing the data itself.  
- **Schema Builder**: A tool for creating and managing credential schemas, enabling public contribution to standardize interoperable credentials.  
- **Query Builder**: A dApp-friendly tool for constructing verification queries, simplifying complex cryptographic proofs without requiring deep technical knowledge.  

### Implementation Details  
- **Privado ID JS SDK (Beta Version)**: JavaScript libraries for browser extensions, enabling users to issue credentials, store them, and generate proofs. Example use cases include dApps verifying user claims.  
- **Issuer Node**: Requires developers to host their own node, which allows full control over credential issuance and data management.  
- **Verifiable Credentials**: Implemented via cryptographic proofs (e.g., zk-SNARKs) to ensure authenticity and integrity.  
- **Schema Builder**: Users can create and share schemas as public goods, fostering ecosystem-wide interoperability.  
- **Query Builder**: Simplifies complex verification logic by abstracting de zkQuery language, allowing dApps to focus on user validation.  

### Related Topics  
- **Schema Builder** and **Query Builder** are explicitly mentioned as accessible tools, linking to their respective documentation sections.  
- The document connects to **zero-knowledge technology** principles, which are foundational to the ecosystem’s privacy claims.  
- The **Privado ID Verifier SDK** is referenced as a critical component for dApp developers, aligning with broader SDK documentation.

---

## Original Text
```
into their existing crypto wallet offerings. As a reference implementation of an identity wallet, you can find the Privado ID Wallet App, which has been created by the Privado ID team to help builders understand one way to incorporate the Wallet SDK into their wallets.

 Privado ID Issuer NodeThe Issuer Node is an application that Issuers can host themselves to keep control of their data. It exposes API methods that can be used by Issuers to issue Verifiable Credentials and a user interface.

 Privado ID Verifier SDKAllows developers, for example dApps, to set verification criteria and construct queries for users.

 Privado ID JS SDK (Beta Version)Java Script Libraries to create client applications as browser extensions, which allows users to issue credentials about themselves, to store credentials and a key, and then to generate proofs of having those credentials.

Moreover you have two additional tools created to facilitate the work of Privado ID developers:

 Schema BuilderSchema Builder is an indispensable tool for developers looking to streamline the creation and management of credential schemas. The schema builder not only makes it easier for developers but also empowers them to create schemas as public goods, contributing to the standardization and interoperability of credentials in our ecosystem. The Schema Builder is accessiblehere.

 Query BuilderIf you're developing a dApp and need to verify user credentials, our Query Builder is here to assist you. The Query Builder eliminates the need for developers to have in-depth knowledge of de zkQuery language, providing a more intuitive and user-friendly way to create queries. The Query Builder is accesiblehere.For further information please seethis video.

The main two uses of zero-knowledge technology used in Privado ID are:1. Preserve privacy: the user (Identity Holder) can send a proof of any information inside a credential to the Verifier (dApp) without revealing the information inside the credential.
```