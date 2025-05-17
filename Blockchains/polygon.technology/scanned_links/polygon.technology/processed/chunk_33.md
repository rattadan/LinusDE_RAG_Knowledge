# Documentation Analysis - Chunk chunk_33.txt

## Source Context
*From: https://polygon.technology/*

### Document Overview  
This content outlines Privado ID's open-source tools for decentralized identity, focusing on Verifiable Credentials, DID (Decentralized Identifier) standards, and EVM-compatible blockchain integration.  

### Key Technical Concepts  
- **Verifiable Credentials**: Digital credentials (e.g., IDs, certificates) that can be authenticated and verified.  
- **Decentralized Identifier (DID)**: Unique, decentralized identifiers for users, managed via cryptographic keys.  
- **W3C/DIF Standards**: Industry-compliant protocols for credential issuance and verification.  
- **Open Source Licensing**: Tools (e.g., Wallet SDK, Issuer Node) are available under open-source licenses.  
- **EVM-Compatible Blockchains**: Tools support interoperability with Ethereum Virtual Machine (EVM) networks.  

### Implementation Details  
- **Privado ID Wallet SDK**: A reference implementation for identity wallets, enabling developers to create or integrate identity solutions into crypto wallets.  
- **Privado ID Issuer Node**: A self-hosted application for issuers to issue Verifiable Credentials via API and UI.  
- **Privado ID Verifier SDK**: Allows dApps to define verification criteria and construct queries for users.  
- **Privado ID JS SDK (Beta)**: JavaScript libraries for browser extensions, enabling users to issue, store, and generate proofs of credentials.  
- **Schema Builder**: Tools for creating and managing credential schemas, simplifying the process of defining credential structure.  

### Related Topics  
- **Privado ID Wallet App**: A sample implementation of the Wallet SDK, demonstrating how to integrate identity tools into wallets.  
- **EVM-Compatible Blockchains**: Tools are designed to work with Ethereum-compatible networks (e.g., Ethereum, Binance Smart Chain).  
- **Decentralized Identity Ecosystem**: The documentation connects to broader themes of interoperability, open-source tools, and Web3 identity solutions.

---

## Original Text
```
across multiple Verifiers, using different wallets.

The Privado ID team is committed to creating an open, interoperable and decentralized space for the community to exchange verifiable credentials for Web3. Thatâs why Privado ID follows the industry standards (W3C, DIF), offers all of the tools under open source licenses and makes the tooling work with any EVM-compatible blockchain.

The core Privado ID technology stack is available under an open source license in a self-service/self-hosted fashion with support for DID and verifiable credentials.

The following tools help developers integrate decentralized identity solutions into their applications:ââ¢ Privado ID Wallet SDKAllows builders to create identity wallets or to incorporate identity solutions into their existing crypto wallet offerings. As a reference implementation of an identity wallet, you can find the Privado ID Wallet App, which has been created by the Privado ID team to help builders understand one way to incorporate the Wallet SDK into their wallets.

â¢ Privado ID Issuer NodeThe Issuer Node is an application that Issuers can host themselves to keep control of their data. It exposes API methods that can be used by Issuers to issue Verifiable Credentials and a user interface.

â¢ Privado ID Verifier SDKAllows developers, for example dApps, to set verification criteria and construct queries for users.

â¢ Privado ID JS SDK (Beta Version)Java Script Libraries to create client applications as browser extensions, which allows users to issue credentials about themselves, to store credentials and a key, and then to generate proofs of having those credentials.

Moreover you have two additional tools created to facilitate the work of Privado ID developers:

â¢ Schema BuilderSchema Builder is an indispensable tool for developers looking to streamline the creation and management of credential schemas.
```