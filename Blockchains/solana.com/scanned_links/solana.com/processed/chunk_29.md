# Documentation Analysis - Chunk chunk_29.txt

## Source Context
*From: https://solana.com/*

### Document Overview  
This content covers Solana programs, their deployment, interaction via transactions, and development approaches (Anchor vs. Native Rust), along with concepts like BPF, upgrade authorities, and verifiable programs.  

### Key Technical Concepts  
- **Solana programs**: Executable binary code deployed on-chain to handle account operations.  
- **BPF (Berkeley Packet Filter)**: A virtual machine for program execution, enabling efficient and secure interactions.  
- **Upgrade authority**: An account authorized to modify a program, typically the original deployer.  
- **Anchor framework**: A Rust-based tool for rapid program development with macros to reduce boilerplate.  
- **Native Rust**: Full Rust implementation for program writing, offering flexibility but requiring more complexity.  
- **Verifiable programs**: Programs that can be audited and verified for correctness.  

### Implementation Details  
- **Development approaches**: Anchor (faster, simpler) vs. Native Rust (more flexible but complex).  
- **BPF execution**: Programs are compiled into BPF objects and executed via the BPF virtual machine.  
- **Upgrade authority**: Programs can be locked (immutable) if the upgrade authority is revoked or set to `None`.  
- **Instruction sets**: Transactions include instructions for program execution (e.g., data transfer, state changes).  

### Related Topics  
- **Deploying programs**: Linked to the "deploying programs" page for details on deployment workflows.  
- **Built-in programs**: Mentioned in the "Built-in Programs" section, highlighting precompiled functions.  
- **Verifiable programs**: Connected to the "Verifiable Programs" section for auditability.

---

## Original Text
```
- The specifiedtransactionsare those included in the entry
- The entry's position with respect to other entries inledger

================================================================================
Document: Programs | Solana
Source: https://solana.com/docs/core/programs#berkeley-packet-filter-bpf
================================================================================

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

```