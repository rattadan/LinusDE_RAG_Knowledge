# Documentation Analysis - Chunk chunk_4.txt

## Source Context
*From: https://solana.com/*

### Document Overview  
This content explains how to set up a Solana Playground wallet, fund it with devnet SOL using the Devnet Faucet, and provides steps for airdropping SOL via terminal commands.  

### Key Technical Concepts  
- **Devnet Faucet**: A tool to obtain devnet SOL for testing without real assets.  
- **Playground Wallet**: A browser-based wallet for interacting with Solana networks.  
- **Solana Playground (Solpg)**: A browser-based development environment for building Solana programs.  
- **Airdrop Command**: A terminal command to distribute SOL to a wallet (e.g., `solana airdrop`).  
- **Web Faucet**: An alternative to airdrop for users facing rate limits.  
- **Local Storage**: Browser-based storage for saving Playground Wallet keys.  
- **Devnet Cluster**: A sandbox network for testing without real assets.  

### Implementation Details  
- **Create Playground Wallet**: Users click "Not connected" to save a wallet keypair in local storage.  
- **Airdrop Command**: Run `solana airdrop` in the terminal to distribute devnet SOL.  
- **Web Faucet Alternative**: If airdrop fails, users can use the Web Faucet (e.g., [https://faucet.solana.com/](https://faucet.solana.com/)) to obtain SOL.  
- **Devnet Cluster**: Default cluster for testing; users can switch to mainnet or other networks.  
- **Wallet Address & Balance**: Displayed in the browser after wallet creation.  

### Related Topics  
- **Solana Playground Documentation**: The content connects to the broader Solana Quick Start Guide and Playground wallet setup instructions.  
- **Devnet Network**: References the Devnet cluster as part of the Solana network architecture.  
- **Browser-Based Development**: Highlights Solpg’s role in enabling interactive, real-time development without installations.

---

## Original Text
```
Terminal

h4: Option 2: Using the Devnet Faucet

h3: Table of Contents

Welcome to the Solana Quick Start Guide. This hands-on guide introduces you to
the core concepts for building on Solana, regardless of your prior experience.

In this tutorial, you'll learn about:

The best part? You don't need to install anything. This guide uses Solana
Playground, a browser-based development environment. Follow along, copy, and
paste code, and see results immediately, all from your web browser. Basic
programming knowledge helps but isn't required.

Time to dive in and start building on Solana.

Solana Playground (Solpg) provides a browser-based development environment that
allows you to quickly develop, deploy, and test Solana programs.

Open a new tab in your web browser and navigate tohttps://beta.solpg.io/.

New Solana Playground users should first create a Playground Wallet. This wallet
enables you to interact with the Solana network right from your browser.

Click the "Not connected" button at the bottom left of the screen.

The system prompts you to save your wallet's keypair. Once ready, click
"Continue" to proceed.

Create Playground Wallet

You should now see your wallet's address, SOL balance, and connected cluster
(devnet by default) at the bottom of the window.

Your browser's local storage saves your Playground Wallet. Clearing your
browser cache removes your saved wallet. Use your Playground Wallet only for
testing and development. Don't send real assets (from mainnet) to this
address.

Some definitions you may find helpful:

Before starting development, you need to get some devnet SOL.

As a developer, you need SOL for two main use cases:

Two methods to fund your wallet with devnet SOL:

To fund your Playground wallet with devnet SOL. In the Playground terminal, run:

If the airdrop command doesn't work (due to rate limits or errors), you can use
theWeb Faucet.

Is this page helpful?

Reading from Network

```