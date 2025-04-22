## Chunk 37

**Original Text:**

We can’t atomically send them to you. ​
How do CW20 tokens compare to “native” (aka bank module) tokens? “Native” tokens are tokens where minting, burning, balances, and transfer functionality are managed by the bank module, instead of by contracts. Unlike CW20s, native tokens are directly compatible with ICS20 and IBC modules. One can send a native token to another chain over a transfer channel just using a MsgTransfer — no conversion contracts or anything of the sort required.

---

**LLM Contextual Output:**

It seems like you're discussing different types of tokens used in blockchain systems, specifically comparing CW20 tokens and "native" tokens.

CW20 is a type of token that uses a specific smart contract framework to manage its functionality, including minting, burning, balances, and transfers. One of the key features of CW20 is that it can be transferred between chains using the MsgTransfer message, which allows for seamless communication between different blockchain networks.

On the other hand, native tokens are typically managed by a central bank or module, where all their functionality is handled through smart contracts. The advantages of native tokens include direct compatibility with ICS20 and IBC modules (Inter-Chain Bridge), making it easier to send them across different blockchain networks without needing to convert them.

In summary, CW20 tokens rely on external contract management, while native tokens have a more centralized approach, relying on a bank module for their functionality. The MsgTransfer feature allows native tokens to be transferred between chains directly, whereas CW20 requires conversion contracts or other mechanisms to achieve the same goal.

Do you have any specific questions about these token types or their applications in blockchain systems?
