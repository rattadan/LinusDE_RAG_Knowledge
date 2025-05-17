## Chunk 32

**Original Text:**

The form will help us scope how much work is required on our side to add support, guide our implementation, and inform our decision for how quickly to prioritize it in our roadmap (e.g. based on swapping volume + liquidity, and clarity of the technical information)

CW20 Tokens & Their Limitations
Information about performing CW20 swaps

This page covers the basics of CW20s and the limitations around performing cross-chain actions with CW20 tokens — compared to tokenfactory and “native” Cosmos assets (aka Bank Module assets). ​
CW20 Token Denom Formatting In API Requests
To use CW20 tokens in the Skip Go API, specify the denom as “cw20:” + the token contract address. Example denom for Astro on Terra2: cw20:terra1nsuqsk6kh58ulczatwev87ttq2z6r3pusulg9r24mfj2fvtzd4uq3exn26

​
Background
​
What is a CW20 token? CW20 is the fungible token spec for the CosmWasm (i.e.

---

**LLM Contextual Output:**

It seems like you're looking to understand more about CW20 tokens and their limitations, as well as how to use them in your application. You've provided some relevant information, but I can try to summarize it and provide additional guidance on how to scope the work required.

**What is a CW20 token?**

A CW20 token is a type of fungible token that is designed for cross-chain interactions, specifically between different blockchain platforms or networks. It's called "fungible" because its value can be exchanged for another identical token of the same type.

**Limitations of using CW20 tokens in your application**

Based on what you've provided, it seems like you're planning to use CW20 tokens for cross-chain swaps with other assets, such as Cosmos tokens (represented by Bank Module assets). However, you mentioned that you need to inform your decision on how quickly to prioritize this feature in your roadmap based on swapping volume and liquidity.

To scope the work required, you might want to consider the following:

1. **Research**: Determine the technical requirements for supporting CW20 tokens, including any necessary API integrations or modifications to your existing infrastructure.
2. **SWAP calculations**: Estimate the number of swaps that can be performed using CW20 tokens per unit time (e.g., based on swapping volume and liquidity).
3. **Priority determination**: Consider factors like prioritization based on:
	* Swap volume
	* Liquidity
	* Technical complexity
	* Business impact (e.g., revenue, user acquisition)
4. **Communication with stakeholders**: Inform your team members about the scope of work, estimated timeline, and potential risks or challenges.

Some potential next steps could be:

1. Research existing solutions for supporting CW20 tokens.
2. Develop a detailed plan outlining the technical requirements and implementation details.
3. Create a rough estimate of the time required to complete the work.
4. Schedule regular check-ins with your team members to ensure progress and address any questions or concerns.

Let me know if you'd like more specific guidance or help with the next steps!
