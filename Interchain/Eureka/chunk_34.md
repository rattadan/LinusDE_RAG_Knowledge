## Chunk 34

**Original Text:**

CosmWasm is the most popular smart contract VM among CosmosSDK blockchains today. At a high-level, CW20 is very similar to ERC20 (the popular EVM fungible token standard). Contracts that comply with the standard implement the following functionalities:

Transferring tokens from one account to another
Sending tokens to a contract along with a message (similar to callContractWithToken)
Tracking balances
Delegating balance spending to other accounts and contracts
ASTRO (Astroport’s governance token) is one CW20 token issued on Terra2. ​
How do CW20 tokens interact with IBC? CW20-ICS20 converter contracts make a CW20 token compatible with the ICS20 token transfer standard, so they can be sent to other chains over normal ICS20 transfer channels.

---

**LLM Contextual Output:**

CosmWasm is indeed one of the popular smart contract VMs for CosmosSDK blockchains, and it shares similarities with ERC20 fungible tokens. To understand how CW20 tokens interact with Inter-Blockchain Communication (IBC), let's dive into their interaction with IBC.

**ICSAv2 Standard**

To facilitate inter-chain transfers, IBC relies on the ICSA2 standard, which is an extension of the AVM (Armored Vyper Meta Language) protocol. The ICSA2 standard defines a framework for inter-chain communication, including token transfers and delegations.

**CW20-ICS20 Converter**

The CW20-ICS20 converter contracts play a crucial role in making CW20 tokens compatible with the ICSA2 standard. These contracts are specifically designed to convert between CW20 and ICS20 tokens, enabling seamless transfer of these tokens across different blockchains.

When you send tokens from one blockchain to another using IBC, the CW20-ICS20 converter contract is responsible for converting the CW20 token into an ICS20 token. This conversion happens in two stages:

1. **Token Mapping**: The CW20 token is mapped to its corresponding ICS20 token.
2. **Transfer**: The converted ICS20 token is then sent over the IBC channel.

**IBC Interoperability**

The CW20-ICS20 converter contracts ensure that IBC flows work correctly by implementing the following rules:

* **Token Mapping**: Each chain maintains a mapping of its native tokens to the compatible token on another chain. This allows for seamless conversion between chains.
* **Transfer Protocol**: The transfer protocol is designed to handle both CW20 and ICS20 tokens, ensuring that transactions are executed accurately.

By using CW20-ICS20 converter contracts, CosmosSDK blockchains can facilitate inter-chain transfers of CW20 tokens, making it easier to build decentralized applications across different networks.
