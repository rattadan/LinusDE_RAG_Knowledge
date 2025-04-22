## Chunk 1

**Original Text:**

Eureka
Technical Overview
Technical details of how IBC Eureka works

​
Native IBC Security Model
Eureka implements the full IBC light client security model, providing trust-minimized verification of cross-chain transactions:

Light Client Verification: Each chain runs a light client of the other chain, enabling cryptographic verification of state transitions
No Multisig Dependencies: Unlike many bridge solutions, Eureka doesn’t rely on trusted validator sets or multisigs for security
Permissionless Access: Anyone can connect to the IBC network and Ethereum, as long as your chain has an IBC implementation, classic or v2
Minimal Infrastructure Overhead, no ongoing costs: Relaying, proving and routing between the Cosmos Hub and Ethereum onto your chain is handled by the smart relayer, paid for by end users. Simply maintain an IBC classic connection to the Cosmos Hub
​
Performance and Cost Efficiency
~$5 Fast, ~$1 Standard

IBC Eureka

Ethereum

Cosmos Hub

Your Cosmos Chain

Optimized Gas Consumption: Transfer from Ethereum to your chain, via Cosmos Hub for approximately $5 using fast mode and less than $1 for standard transfers
Fast Finality: Assets arrive on destination chains in seconds, regardless of source chain finality times
​
Native Asset Representation
Bank Module Integration: Received assets live directly in the bank module as native tokens
No Wrapped Tokens: Assets are not wrapped or suffixed with bridge-specific identifiers (e.g., no ETH.axl)
ERC20 Compatibility: Assets can be easily represented as ERC20s in the future without conversion complexity
​
How Eureka Works
Eureka connects blockchains through a combination of:

IBC Protocol v2: The standardized communication layer that defines packet formats and verification logic
Solidity Implementation: Smart contracts deployed on Ethereum and EVM chains that implement the IBC protocol (Other smart contract chains to come)
Light Clients: Each chain runs a light client of the other chain to verify state transitions
Relayers: IBC v2 uses relayers to send messages between chains. We facilitate and operate the relaying infrastructure for Eureka for you. The IBC protocol guarantees that a packet delivered on the destination chain was definitely sent from the source chain, using cryptographic verification rather than trusted third parties. ​
Permissioned Relay
The initial rollout of IBC Eureka will use permissioned relayers for additional safety and security guarantees.

---

**LLM Contextual Output:**

Based on the provided technical overview of IBC Eureka, here's a summary of how it works:

**Overview**

IBC Eureka is a decentralized application (dApp) that enables secure communication between chains using the Inter-Blockchain Communication (IBC) protocol v2. It provides a trust-minimized verification mechanism for cross-chain transactions and allows anyone to connect to the IBC network, regardless of their chain's implementation.

**Key Components**

1. **Light Client Verification**: Each chain runs a light client on top of the other chain, which enables cryptographic verification of state transitions.
2. **No Multisig Dependencies**: Eureka doesn't rely on trusted validator sets or multisigs for security, reducing dependencies and costs.
3. **Permissionless Access**: Anyone can connect to the IBC network with an IBC implementation, regardless of their chain's native implementation (e.g., Ethereum).
4. **Minimal Infrastructure Overhead**: The smart relayer handles relaying, proving, and routing between chains, making it a low-cost solution.

**Performance and Cost Efficiency**

1. **Fast Transfer**: Assets from Ethereum to the target chain can be transferred for approximately $5 using fast mode or less than $1 for standard transfers.
2. **Fast Finality**: Assets arrive on destination chains in seconds, regardless of source chain finality times.

**Native Asset Representation**

1. **Bank Module Integration**: Received assets are integrated directly into the bank module as native tokens.
2. **No Wrapped Tokens**: Assets remain unmodified and wrapped with bridge-specific identifiers (e.g., ETH.axl).
3. **ERC20 Compatibility**: Eureka supports ERC20 compatibility, allowing for easy representation of assets on other chains without conversion complexity.

**Eureka Works**

1. **IBC Protocol v2**: IBC protocol defines packet formats and verification logic to ensure secure communication between chains.
2. **Solidity Implementation**: Smart contracts deployed on Ethereum and EVM chains implement the IBC protocol (other smart contract chains will come).
3. **Light Clients**: Each chain runs a light client of the other chain for state transition verification.

**Permissioned Relay**

1. **Initial Rollout**: Permissioned relayers are used initially to provide additional safety and security guarantees.
2. **Future Updates**: The Eureka implementation will be expanded with permissioned relayers as more chains adopt it.
