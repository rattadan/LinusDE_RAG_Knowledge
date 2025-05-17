# Documentation Analysis - Chunk chunk_7.txt

## Source Context
*From: https://polygon.technology/*

### Document Overview  
This content discusses Privado ID's tools for decentralized identity verification, focusing on off-chain and on-chain smart contracts, ecosystem integration, and open-source technologies for verifiable credentials.  

### Key Technical Concepts  
- **Off-chain/on-chain verification**: Separation of credential storage (off-chain) from verification (on-chain).  
- **Smart contracts**: Automated execution of verification logic on blockchain.  
- **Decentralized Identifiers (DIDs)**: Unique, verifiable identifiers for participants.  
- **Verifiable credentials**: Credentials stored and verified using cryptographic methods.  
- **Open-source licensing**: Tools are available under licenses like MIT and GPL.  
- **EVM-compatible blockchains**: Support for interoperability across Ethereum-compatible networks.  

### Implementation Details  
- **Privado ID Wallet SDK**: Enables developers to create identity wallets or integrate them into existing crypto wallets.  
- **Issuer Node**: A self-hosted application for Issuers to manage their data securely.  
- **Open-source tools**: Tools are available under licenses like MIT and GPL, allowing self-hosting and DID/verifiable credential support.  
- **Ecosystem integration**: Tools are integrated by issuers, verifiers, and wallet providers, fostering a decentralized network effect.  
- **Smart contract libraries**: Enable composition of verification queries without complex cryptographic reconfiguration.  

### Related Topics  
- **Interoperability**: Connection to W3C (Web3C) and DIF (Decentralized Identifier Format) standards for credential exchange.  
- **EVM-compatible blockchains**: Alignment with Ethereum Virtual Machine (EVM) ecosystems for cross-chain functionality.  
- **Open-source tools**: Reference to the Privado ID Wallet App as a reference implementation for identity wallet integration.

---

## Original Text
```
smart contracts for off-chain and on-chain verification. These libraries allow the Verifier to compose different queries (questions) without having to deal with the complexity of reconfiguring the underlying cryptography.

For further information please see thisplaylist.

Although technically speaking Privado ID is a set of tools - its value is much more than that - its all about the ecosystem.

Privado ID tooling is continuously being integrated by new Issuers, Verifiers and Wallet providers (you can see the growing Privado ID ecosystemhere, creating a positive network effect where everyone benefits from the addition of new builders.

As a Web3 developer, your users will soon have access to a big market of credentials (from Issuers in the broader Privado ID ecosystem). Your users will be able to reuse their credentials across multiple Verifiers, using different wallets.

The Privado ID team is committed to creating an open, interoperable and decentralized space for the community to exchange verifiable credentials for Web3. Thats why Privado ID follows the industry standards (W3C, DIF), offers all of the tools under open source licenses and makes the tooling work with any EVM-compatible blockchain.

The core Privado ID technology stack is available under an open source license in a self-service/self-hosted fashion with support for DID and verifiable credentials.

The following tools help developers integrate decentralized identity solutions into their applications: Privado ID Wallet SDKAllows builders to create identity wallets or to incorporate identity solutions into their existing crypto wallet offerings. As a reference implementation of an identity wallet, you can find the Privado ID Wallet App, which has been created by the Privado ID team to help builders understand one way to incorporate the Wallet SDK into their wallets.

 Privado ID Issuer NodeThe Issuer Node is an application that Issuers can host themselves to keep control of their data.
```