# Documentation Analysis - Chunk chunk_5.txt

## Source Context
*From: https://solana.com/*

### Document Overview  
This content provides guidance on funding a Solana Playground wallet with devnet SOL, explains network concepts (devnet, testnet, mainnet-beta), and outlines technical terms related to Solana accounts, transactions, and program interactions.  

### Key Technical Concepts  
- **Devnet**: A development network for experimentation and testing.  
- **Testnet**: A network reserved for validator testing (not for app developers).  
- **Mainnet-beta**: The live Solana network for real transactions.  
- **Wallet Address**: A 32-byte public key (e.g., `7MNj7pL1y7XpPnN7ZeuaE4ctwg3WeufbX5o85sA91J1`) used to identify accounts.  
- **Program Derived Addresses (PDAs)**: Deterministic addresses created via keypairs for program accounts.  
- **Cross-Program Invocations (CPIs)**: Mechanisms to call other programs within a Solana program.  
- **Connected Cluster**: The Solana network environment (devnet, testnet, mainnet-beta) for current interactions.  
- **Transaction Fees**: Costs incurred when interacting with the Solana network.  

### Implementation Details  
- **Funding Wallet**: Use the airdrop command in the Playground terminal (`solana airdrop 3` for 3 SOL) or the Web Faucet for alternative funding.  
- **Wallet Address Example**: `7MNj7pL1y7XpPnN7ZeuaE4ctwg3WeufbX5o85sA91J1` (base-58 encoded).  
- **Cluster Selection**:  
  - `devnet`: For development and experimentation.  
  - `testnet`: For validator testing (not for app developers).  
  - `mainnet-beta`: For live transactions.  
- **Transaction Fees**: Paid via Solana's proof-of-stake system, with gas fees calculated per transaction.  

### Related Topics  
- **Sending Transactions**: Covered in the "Sending Transactions" section.  
- **Program Derived Addresses (PDAs)**: Explained in the "Program Derived Addresses (PDAs)" section.  
- **Cross-Program Invocations (CPIs)**: Discussed in the "Cross-Program Invocations (CPIs)" section.  
- **Account Creation**: Mentioned in the "Creating new accounts to store data or deploy programs on the network" section.

---

## Original Text
```
helpful:

Before starting development, you need to get some devnet SOL.

As a developer, you need SOL for two main use cases:

Two methods to fund your wallet with devnet SOL:

To fund your Playground wallet with devnet SOL. In the Playground terminal, run:

If the airdrop command doesn't work (due to rate limits or errors), you can use
theWeb Faucet.

Is this page helpful?

Reading from Network

- Solana Accounts: Learn how the Solana network stores data.
- Sending Transactions: Learn to interact with the Solana network by sending
transactions.
- Building and Deploying Programs: Create your first Solana program and
deploy it to the network.
- Program Derived Addresses (PDAs): Learn how to use PDAs to create
deterministic addresses for accounts.
- Cross-Program Invocations (CPIs): Learn how to call other programs from
within your program, enabling complex interactions and composability between
different programs on Solana.
- wallet address: a 32-byte public key from a Ed25519 keypair, generally
displayed as a base-58 encoded string (e.g.,7MNj7pL1y7XpPnN7ZeuaE4ctwg3WeufbX5o85sA91J1). The corresponding private key
signs transactions from this address. On Solana, an address serves as the
unique identifier for a user's wallet, a program (smart contract), or any
other account on the network.
- connected cluster: the Solana network for your current interactions. Common
clusters include:devnet: A development network for developer experimentationtestnet: A network reserved for validator testing (don't use as app
developer)mainnet-beta: The main Solana network for live transactions
- devnet: A development network for developer experimentation
- testnet: A network reserved for validator testing (don't use as app
developer)
- mainnet-beta: The main Solana network for live transactions
- Creating new accounts to store data or deploy programs on the network
- Paying transaction fees when interacting with the Solana network
- Enter your wallet address (found at the bottom of the 
```