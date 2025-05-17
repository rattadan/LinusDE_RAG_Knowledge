# Documentation Analysis - Chunk chunk_34.txt

## Source Context
*From: https://polygon.technology/*

### Document Overview  
The content discusses Privado ID's use of zero-knowledge technology for privacy and verification, along with two tools (Schema Builder and Query Builder) and blockchain applications.  

### Key Technical Concepts  
- **Zero-knowledge proofs (ZKPs)**: Enable verification of credentials without revealing sensitive data.  
- **Selective disclosure**: Users can share specific information from a credential while proving its correctness.  
- **Credential schemas**: Structured data models for storing credentials and keys, accessible via the Schema Builder.  
- **Query Builder**: Simplifies creating verification queries for dApps, abstracting zkQuery complexity.  
- **Blockchain integration**: Used for privacy, computation verification, and interoperability.  

### Implementation Details  
- **Schema Builder**: Allows developers to create and share credential schemas as public goods, enhancing standardization.  
- **Query Builder**: Enables dApp developers to verify user credentials without requiring expertise in zkQuery language.  
- **Blockchain uses**:  
  1. **Privacy**: Users share selective information via ZKPs.  
  2. **Verification of computation**: Prove state transitions or computations without reprocessing data.  

### Related Topics  
- Connections to the **Schema Builder** and **Query Builder** pages.  
- References to a **video** explaining the technical concepts.  
- Potential links to documentation about blockchain applications or privacy protocols in the ecosystem.

---

## Original Text
```
which allows users to issue credentials about themselves, to store credentials and a key, and then to generate proofs of having those credentials.

Moreover you have two additional tools created to facilitate the work of Privado ID developers:

â¢ Schema BuilderSchema Builder is an indispensable tool for developers looking to streamline the creation and management of credential schemas. The schema builder not only makes it easier for developers but also empowers them to create schemas as public goods, contributing to the standardization and interoperability of credentials in our ecosystem. The Schema Builder is accessiblehere.

â¢ Query BuilderIf you're developing a dApp and need to verify user credentials, our Query Builder is here to assist you. The Query Builder eliminates the need for developers to have in-depth knowledge of de zkQuery language, providing a more intuitive and user-friendly way to create queries. The Query Builder is accesiblehere.âFor further information please seethis video.

The main two uses of zero-knowledge technology used in Privado ID are:1. Preserve privacy: the user (Identity Holder) can send a proof of any information inside a credential to the Verifier (dApp) without revealing the information inside the credential. In the Selective Disclosure mode, the user can also select which information inside the credential he wants to share (without having to select the whole credential). While sharing this information, he also sends a proof about this information so the Verifier can check its correctness.

2. Verification of computation:Â zero-knowledge proofs can be used to prove that a computation has been performed correctly without the Verifier having to recompute it. For example, within Privado ID, it is used to prove that an identity is performing a state transition correctly.

For further information please seethis video.

There are three main uses of the blockchain for Privado ID.

1.
```