# Documentation Analysis - Chunk chunk_39.txt

## Source Context
*From: https://solana.com/*

### Document Overview  
This content discusses Solana's introduction of verifiable builds, tools for code verification, and technical details about compiler workflows, bytecode formats, and program ownership structures.  

### Key Technical Concepts  
- **Verifiable Builds**: A mechanism to ensure on-chain code matches public source code, enabling discrepancy detection.  
- **Solana Verifiable Build CLI**: A tool for users to verify on-chain programs against published source code.  
- **LLVM/ELF**: Solana uses LLVM to compile programs into ELF files, which store custom "Solana Bytecode Format" (sBPF) for execution.  
- **Loaders (v3/v4)**: Programs that own and manage custom programs, allowing post-deployment modifications with restricted permissions.  
- **Ed25519 Signature Verification**: A cryptographic process to validate program instructions, involving a struct with signature counts and padding.  

### Implementation Details  
- **Verifiable Build CLI**: Enables users to verify programs using the `solana` CLI, comparing on-chain code with published source.  
- **LLVM Compilation**: Solana compiles programs into ELF files, which are stored in executable accounts.  
- **sBPF (Solana Bytecode Format)**: A custom ELF format optimized for Solana’s ecosystem, containing program binaries and custom eBPF bytecode.  
- **Signature Verification**: The pseudo-code processes a signature count and padding, followed by a serialized struct for each signature, ensuring cryptographic integrity.  
- **Loader Permissions**: Loaders (v3/v4) control post-deployment modifications via account ownership, with v3/v4 supporting dynamic updates.  

### Related Topics  
- **Anchor Documentation**: Anchor’s built-in support for verifiable builds, which is referenced in the content.  
- **Solana Explorer**: Users search for verified programs via the Solana Explorer, linking to examples of verified programs.  
- **LLVM/ELF Integration**: The content connects to Solana’s compiler workflow and custom bytecode format (sBPF).  
- **Loader Management**: The document ties to Solana’s program ownership and management strategies, relevant to Anchor’s deployment mechanics.

---

## Original Text
```
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

The ed25519 program processes an instruction. The firstu8is a count of the
number of signatures to check, which is followed by a single byte padding. After
that, the following struct is serialized, one for each signature to check.

The pseudo code of the signature verification:

```