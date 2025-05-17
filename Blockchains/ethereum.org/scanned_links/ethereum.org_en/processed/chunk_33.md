# Documentation Analysis - Chunk chunk_33.txt

## Source Context
*From: https://ethereum.org/en/*

### Document Overview  
This content outlines block explorers for Ethereum, explaining their role in providing real-time data on blocks, transactions, validators, and other on-chain activities. It divides data into execution and consensus layers and mentions testnets.  

### Key Technical Concepts  
- **Execution Data**: Real-time data on blocks, transactions, accounts, and tokens (e.g., gas prices, transaction hashes).  
- **Consensus Data**: Information about validators, attestations, and network state (e.g., slots, epochs).  
- **Data Structure**: Data is divided into execution (transactions, gas, accounts) and consensus (validators, attestations).  
- **Testnets**: Support for testnets, which are not part of the main Ethereum network.  
- **APIs/Interfaces**: Block explorers provide interfaces to retrieve data via APIs or web interfaces.  

### Implementation Details  
- **Code Examples**:  
  - Hex strings like `X>Un4"|fs^\$b!@{J$B[EW8n]ASZv,m;G(r8"4/3d10Bxvi/xn1<!e=dn hK="0,/x` (likely raw data or cryptographic hashes).  
  - Code snippets like `q*_Q2vO=FurWThueY1Pph1;KLf{WX:|X?p{>!'+9{ZQzVk\\GiS`m6)U*gGbO_QOq'fZmw`d6|?ig:"GO<?53 2Wc7F#3+w}O8J,lO9.k` (potential API calls or data structures).  
- **Data Formats**: Use of hexadecimal encoding for addresses, transactions, and metadata.  
- **Network Support**: Mention of testnets (e.g., `#d\aKI@=w +ze7v#N{3T+=z7mge}` as a placeholder for testnet data).  

### Related Topics  
- **Data and Analytics**: The document connects to the "Data and Analytics" section of the Ethereum documentation.  
- **Introduction to Ethereum**: References to the "Intro to Ethereum" section for context.  
- **Block Explorers**: The content is part of a broader series on block explorers, linking to related topics like "Further reading" and "Related topics."

---

## Original Text
```
>X>Un4"|fs^\$b!@{J$B[EW8n]ASZv,m;G(r8"4/3d10Bxvi/xn1<!e=dn hK="0,/x
ep\7D
!|PFQeI+V:>YeZ|:1PC
q*_Q2vO=FurWThueY1Pph1;KLf{WX:|X?p{>!'+9{ZQzVk\\GiS`m6)U*gGbO_QOq'fZmw`d6|?ig:"GO<?53 2Wc7F#3+w}O8J,lO9.k
/#d\aKI@=w +ze7v#N{3T+=z7mge}
~3P_,pW-kl[:|8R)_{YD^LGl;}2Ly8Ny8"VTc)36P~aOE27vgXFnBf]L([w)3QyK$ct>p9/FYa^xMlBU- .0(UC~O?NOHS^(ovqx>*.P-YDM^LO8K}f")<((C6gR;<?|X3D B,Zhh|%lU<x|1{L<Xa)75tcUX1xsAC&s3<3k?KSQ6gyK5uUygyvcaygkJEg3<|2<3wnXgy/(R<3<|=gyaQ@gy/eYyg+WTA \Tyqyg+
K`Lw5A`yg<;*,*,//gyK
U*BaErkWh<3dUK
\C3<T*rzyg1?~|L)_RAm3<(^voEz,YHO=-^Qyg^!vO#,d3<_>Xh?)LMlBs*JNJ-gy/ xDz"ca4FCo0Bl7?TbN\% 3<z,3<_Pcayg3<Xgy|Jgy/|PX)v0<3|p(A`ygLZ.IENDB`

================================================================================
Document: Block explorers
Source: https://ethereum.org/en/developers/docs/data-and-analytics/block-explorers/
================================================================================

h1: Block explorers

h2: Prerequisites

h2: Services

h2: Open source tools

h2: Data

h3: Execution data

h3: Gas

h3: Transactions

h3: Accounts

h3: Tokens

h3: Network

h2: Consensus layer data

h3: Epoch

h3: Slot

h3: Blocks

h3: Validators

h3: Attestations

h3: Network

h2: Block explorers

h2: Further reading

h2: Related topics

h4: Was this article helpful?

Last edit:@corwintines(opens in a new tab),April 14, 2025

Block explorers are your portal to Ethereum's data. You can use them to see real-time data on blocks, transactions, validators, accounts, and other onchain activity.

You should understand the basic concepts of Ethereum so you can make sense of the data that a block explorer gives you. Start withan intro to Ethereum.

Ethereum is transparent by design so everything is verifiable. Block explorers provide an interface for getting this information. And this is for both the main Ethereum network and the testnets, should you need that data. Data is divided into execution data and consensus data.
```