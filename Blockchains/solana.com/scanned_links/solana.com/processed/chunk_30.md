# Documentation Analysis - Chunk chunk_30.txt

## Source Context
*From: https://solana.com/*

### Document Overview  
This content discusses Solana's verifiable builds, deployment mechanisms, and the role of loaders in managing custom programs. It explains how programs can be upgraded, verified, and compiled using LLVM and ELF files.  

### Key Technical Concepts  
- **Verifiable Builds**: A feature allowing users to verify that on-chain programs match their public source code, detecting discrepancies.  
- **Upgrade Authority**: An account authorized to modify programs, typically the original deployer.  
- **Loader**: A program that owns and manages custom programs, enabling modifications after deployment.  
- **ELF (Executable and Linkable Format)**: Solana uses this format to compile programs into binary files, stored on-chain.  
- **sBPF (Solana Bytecode Format)**: Solana’s custom variant of eBPF bytecode used in compiled programs.  

### Implementation Details  
- **Verifiable Build CLI**: A tool by Ellipsis Labs to verify on-chain programs against published source code.  
- **LLVM/ELF Compilation**: Solana compiles programs into ELF files, which contain the program’s binary and are stored in executable accounts.  
- **Loaders**: Five loaders (Loader-v3, Loader-v4) manage program ownership and enable post-deployment modifications via upgrade authority.  
- **Immutable Programs**: When an upgrade authority is revoked, programs become immutable and cannot be updated.  

### Related Topics  
- **Anchor Documentation**: Solana’s Anchor framework provides built-in support for verifiable builds.  
- **Solana Explorer**: Users can search for verified programs by address to verify their on-chain code.  
- **LLVM/ELF Architecture**: Solana’s use of LLVM for compiling programs into ELF files aligns with standard eBPF practices.

---

## Original Text
```
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

Searching for Verified Programs: To quickly check for verified programs,
users can search for a program address onSolana Explorer. View an example of a verified
programhere.

Verification Tools: TheSolana Verifiable Build CLIby Ellipsis Labs enables users to independently verify on-chain programs
against published source code.

Support for Verifiable Builds in Anchor: Anchor provides built-in support
for verifiable builds. Details can be found in theAnchor documentation.

Solana usesLLVM(Low Level Virtual Machine) to compile
programs intoELF(Executable
and Linkable Format) files. These files contain Solana's custom version ofeBPFbytecode, called "Solana Bytecode
Format" (sBPF). The ELF file contains the program's binary and is stored
on-chain in an executable account when the program is deployed.

Every program itself is owned by another program, which is its loader.
Currently, five loaders programs exist:

These loaders are necessary to create and manage custom programs:

Loader-v3 and loader-v4 support modifications to programs after their initial
deployment. Permission to do so is regulated by the authority of a program
because the account ownership of each program resides with the loader.

```