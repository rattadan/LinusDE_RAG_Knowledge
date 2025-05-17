# Documentation Analysis - Chunk chunk_7.txt

## Source Context
*From: https://solana.com/*

### Document Overview  
This content explains Solana's commitment levels for transaction safety, their trade-offs, and how to configure them in node settings, along with details about RPC responses and filters.  

### Key Technical Concepts  
- **Commitment Levels**: `confirmed` (balanced speed/rollback safety) and `finalized` (total safety), with `finalized` as the default unless specified.  
- **Commitment Parameter**: Only applicable to methods querying bank state (e.g., `get_account`), which can return parsed data with the `encoding` parameter.  
- **RpcResponse**: Includes `finalized` and `confirmed` states, with filters like `memcmp` for pre-filtering data.  
- **Account/Instruction Parsers**: Solana supports JSON parsing for native and SPL programs, with specific lists provided in the API Reference.  

### Implementation Details  
- **Default Commitment**: Nodes use `finalizedcommitment` unless explicitly configured.  
- **Encoding Parameter**: Methods like `get_account` allow `encoding: "jsonParsed"` to return parsed data if the node supports the program’s parser.  
- **Filters**: `memcmp` compares program account data offsets, and `filters` enable pre-filtering of RPC responses.  
- **Supported Parsers**: JSON parsing is available for native and SPL programs (e.g., SPL Token, NFTs), with details in the API Reference.  

### Related Topics  
- **API Reference**: Details about `encoding` and `filters` are linked to the Solana RPC documentation.  
- **Data Structures**: The `finalized` and `confirmed` states are explained in the "Data Structures as JSON" section.  
- **Node Configuration**: The commitment parameter’s role in node settings is tied to the "RPC Response" and "Filters" sections.

---

## Original Text
```
many dependent transactions in series, it's recommended to useconfirmedcommitment, which balances speed with rollback safety. For total
safety, it's recommended to usefinalizedcommitment.

If commitment configuration is not provided, the node willdefault tofinalizedcommitment

Only methods that query bank state accept the commitment parameter. They are
indicated in the API Reference below.

Many methods that take a commitment parameter return an RpcResponse JSON object
comprised of two parts:

Some methods support anencodingparameter, and can return account or
instruction data in parsed JSON format if"encoding":"jsonParsed"is requested
and the node has a parser for the owning program. Solana nodes currently support
JSON parsing for the following native and SPL programs:

The list of account parsers can be foundhere,
and instruction parsershere.

Some methods support providing afiltersobject to enable pre-filtering the
data returned within the RpcResponse JSON object. The following filters exist:

memcmp: object- compares a provided series of bytes with program account
data at a particular offset. Fields:

dataSize: u64- compares the program account data length with the provided
data size

Is this page helpful?

Data Structures as JSON

- finalized- the node will query the most recent block confirmed by
supermajority of the cluster as having reached maximum lockout, meaning the
cluster has recognized this block as finalized
- confirmed- the node will query the most recent block that has been voted on
by supermajority of the cluster.It incorporates votes from gossip and replay.It does not count votes on descendants of a block, only direct votes on that
block.This confirmation level also upholds "optimistic confirmation" guarantees in
release 1.3 and onwards.
- It incorporates votes from gossip and replay.
- It does not count votes on descendants of a block, only direct votes on that
block.
```