# Documentation Analysis - Chunk chunk_25.txt

## Source Context
*From: https://solana.com/*

### Document Overview  
This content discusses Solana's blockchain architecture, focusing on accounts, programs, transaction fees, compute budgets, proofs, and validator components, while explaining concepts like rent, garbage collection, and block validation.  

### Key Technical Concepts  
- **Program Execution**: Validators handle program execution, enabling on-chain programs to run independently of the blockchain.  
- **Compute Budget**: Users can specify compute units (CU) for transactions, with fees calculated based on requested CU and price per CU.  
- **Proofs**: A stack of time-verified proofs (e.g., Proof of History) for transaction ordering, verified faster than production time.  
- **Rent**: Accounts must pay rent to store data; insufficient balance may lead to garbage collection.  
- **Garbage Collection**: Accounts with below-rent thresholds are automatically deleted.  
- **Block Slots**: Validators track blocks with maximum lockouts; the root is the highest ancestor of active forks.  
- **Lamports**: The native currency unit in Solana, used for fees and rent.  

### Implementation Details  
- **Compute Budget**: Transactions request minimum CU to minimize fees, with fees calculated as `ceil(maxCU * computeUnitPrice)`.  
- **Proofs**: Each proof proves data existence and time elapsed since the previous proof, enabling efficient transaction ordering.  
- **Program Execution**: Validators handle program execution, allowing on-chain programs to run independently.  
- **Signature Format**: 64-byte ed25519 signature for transactions, with R (32-byte) and S (32-byte) components.  
- **Block Validation**: Validators track block slots and roots, excluding blocks not ancestor/descendant of the root for consensus.  

### Related Topics  
- **Rent**: Connected to the explanation of rent exemption thresholds and garbage collection.  
- **Transactions**: Related to compute budget instructions and prioritization fees.  
- **Validator Components**: Linked to the role of validators in program execution and block validation.  
- **Block Structure**: Connected to the description of block slots and roots in validator operations.

---

## Original Text
```
whose signing authority is a program and thus is not controlled by a
private key like other accounts.

The public key of theaccountcontaining aprogram.

A stack of proofs, each of which proves that some data existed before the proof
was created and that a precise duration of time passed before the previous
proof. Like aVDF, a Proof of History can be
verified in less time than it took to produce.

An additional fee user can specify in the compute budgetinstructionto prioritize theirtransactions.

The prioritization fee is calculated by multiplying the requested maximum
compute units by the compute-unit price (specified in increments of 0.000001
lamports per compute unit) rounded up to the nearest lamport.

Transactions should request the minimum amount of compute units required for
execution to minimize fees.

The public key of akeypair.

Fee paid byAccountsandProgramsto store data on the
blockchain. When accounts do not have enough balance to pay rent, they may be
Garbage Collected.

See alsorent exemptbelow. Learn more about rent here:What is rent?.

Accounts that maintain a minimum lamport balance that is proportional to the
amount of data stored on the account. All newly created accounts are stored
on-chain permanently until the account is closed. It is not possible to create
an account that falls below the rent exemption threshold.

Ablockorslotthat has reached maximumlockouton avalidator. The root is the highest block that is an ancestor
of all active forks on a validator. All ancestor blocks of a root are also
transitively a root. Blocks that are not an ancestor and not a descendant of the
root are excluded from consideration for consensus and can be discarded.

The component of avalidatorresponsible forprogramexecution.

Solana's parallel run-time foronchain programs.

A fraction of ablock; the smallest unit sent betweenvalidators.

A 64-byte ed25519 signature of R (32-bytes) and S (32-bytes).
```