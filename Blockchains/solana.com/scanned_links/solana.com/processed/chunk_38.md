# Documentation Analysis - Chunk chunk_38.txt

## Source Context
*From: https://solana.com/*

### Document Overview  
This content outlines Solana's program development ecosystem, covering deployment, writing methods, updating mechanisms, verifiable builds, and tools for ensuring program integrity.  

### Key Technical Concepts  
- **Solana Programs**: Self-contained executable binaries deployed to accounts for smart contract functionality.  
- **Rust**: Primary language for writing programs, with two approaches: **Anchor** (simplified framework) and **Native Rust** (full control).  
- **Upgrade Authority**: Account responsible for modifying programs; if revoked, programs become immutable.  
- **Verifiable Builds**: Public source code verification via cryptographic hashing, enabling auditability and discrepancy detection.  
- **BPF (Berkeley Packet Filter)**: Low-level virtual machine for efficient, hardware-accelerated program execution.  
- **Built-in Programs**: Predefined utilities (e.g., Ed25519, Secp256k1) for cryptographic operations.  

### Implementation Details  
- **Anchor Framework**: Reduces boilerplate code using Rust macros, enabling faster development for beginners.  
- **Native Rust**: Requires manual management of program lifecycle, offering flexibility but higher complexity.  
- **Verifiable Builds**: Programs are hashed and linked to public source code via `solana-program` tools, ensuring code integrity.  
- **Upgrade Authority**: Programs can be upgraded by an account designated as the "upgrade authority," which is typically the original deployer.  
- **BPF**: Programs are executed in a lightweight virtual machine, optimized for performance and efficiency.  

### Related Topics  
- **Deploying Programs**: Details on how programs are deployed and managed on the Solana network.  
- **Verifiable Builds Tools**: Documentation on tools like `solana-program` and `solana-validator` for code verification.  
- **BPF and Core Programs**: Connections to Solana’s low-level execution environment and built-in cryptographic utilities.

---

## Original Text
```
========================================================================

h1: Programs

h2: Key Points

h2: Writing Solana Programs

h2: Updating Solana Programs

h2: Verifiable Programs

h2: Berkeley Packet Filter (BPF)

h2: Built-in Programs

h3: Loader Programs

h3: Precompiled Programs

h4: Ed25519 Program

h4: Secp256k1 Program

h4: Secp256r1 Program

h3: Core Programs

h3: Table of Contents

On Solana, "smart contracts" are called programs.Programsare deployed on-chain to
accounts that contain the program's compiled executable binary. Users interact
with programs by sending transactions containinginstructionsthat tell the program what
to do.

Solana programs are predominantly written in theRustprogramming language,
with two common approaches for development:

Anchor: A framework designed for Solana
program development. It provides a faster and simpler way to write programs,
using Rust macros to reduce boilerplate code. For beginners, it is recommended
to start with the Anchor framework.

Native Rust: This approach involves writing Solana
programs in Rust without leveraging any frameworks. It offers more flexibility
but comes with increased complexity.

To learn more about deploying and upgrading programs, see thedeploying programspage.

Programs can bedirectly modifiedby an account designated as the "upgrade authority", which is typically the
account that originally deployed the program. If theupgrade authorityis revoked and set toNone, the program becomes immutable and can no longer be
updated.

Verifiable builds allow anyone to check if a program's on-chain code matches its
public source code, making it possible to detect discrepancies between source
and deployed versions.

The Solana developer community has introduced tools to support verifiable
builds, enabling both developers and users to verify that on-chain programs
accurately reflect their publicly shared source code.

```