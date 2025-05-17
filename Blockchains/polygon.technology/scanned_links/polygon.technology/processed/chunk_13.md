# Documentation Analysis - Chunk chunk_13.txt

## Source Context
*From: https://polygon.technology/*

### Document Overview  
This content provides an overview of Privado ID’s services, including their IDaaS platform, fee structures, and technical features, while also referencing Agglayer events at the ETHDenver conference.  

### Key Technical Concepts  
- **EVM-compatible chain**: A blockchain platform supporting Ethereum Virtual Machine (EVM) standards, enabling interoperability with Ethereum-based applications.  
- **Smart contracts**: Self-executing contracts on the blockchain, deployed on Polygon Testnet and PoS Mainnet.  
- **Payment rails**: Infrastructure for facilitating transactions, including fees for credential reuse, storage, and services.  
- **Credentials**: Fee-based system for verifiers (e.g., applications) to issue and reuse credentials, with issuers collecting a percentage.  
- **Identity Cloud Wallet**: One-time fee for verifiers to onboard users, covering storage and key custody services.  
- **Enterprise Support**: Tailored services for governments/corporations, governed by SLAs (service-level agreements).  
- **Agglayer**: A platform for managing identity and credentials, highlighted in the blog post.  

### Implementation Details  
- **Fee structures**: Credentials require payment rails for reuse, while cloud wallets charge one-time fees for user onboardings.  
- **Payment rails**: Facilitate transactions for fees, revocations, and additional services (e.g., compliant storage).  
- **EVM compatibility**: Privado ID supports deployment on any EVM-compatible chain, including CDK-based blockchains, expanding its ecosystem.  
- **SLAs**: Enterprise support is tied to service-level agreements, ensuring reliability and compliance.  

### Related Topics  
- **EVM-compatible chains**: The document connects to the broader context of blockchain interoperability and the EVM ecosystem.  
- **Agglayer events**: The blog post references Agglayer, a platform for identity management, which ties back to Privado ID’s services.  
- **Smart contracts**: The mention of deploying smart contracts on Polygon Testnet and PoS Mainnet aligns with the broader technical context of blockchain development.

---

## Original Text
```
EVM-compatible chain. At the moment, the necessary smart contracts are deployed onto Polygon Testnet (Amoy) and Polygon PoS Mainnet, but they could be deployed into any other EVM-compatible chain including any CDK-based blockchain very soon.

Privado ID is an open-source software and is free to use. However, Privado ID plans to generate revenue by offering additional infrastructure and services.

This structure allows Privado ID to support a wide range of use cases while maintaining its foundational open-source principles

Get our newsletter

- Credentials: Fees are charged for the use and reuse of credentials. Verifiers (e.g., Applications) will pay these fees to the issuers via a payment rails infrastructure, and Privado ID will collect a percentage of each transaction.
- Identity Cloud Wallet:Privado ID might charge charge a one-time fee to the verifier (e.g., Application) for each new user onboarded. This fee covers necessary services for the cloud wallet, such as storage and key custody.
- Enterprise Support:Privado ID provides tailored support and development services for systems requiring private infrastructure, such as those operated by governments or corporations. These contracts are typically based on service-level agreements (SLAs).
- Issuer Services: Fees are also collected for additional services provided to issuers, including revocations, on-chain issuance, trust registry, and compliant storage, using their payment rails to facilitate transactions.

================================================================================
Document: Your Guide to Agglayer Events at ETHDenver, Cryptos Premier Conference
Source: https://polygon.technology/blog/your-guide-to-agglayer-events-at-ethdenver-cryptos-premier-conference
================================================================================

h1: Your Guide to Agglayer Events at ETHDenver, Cryptos Premier Conference

```