## Chunk 70

**Original Text:**

Outcome / What to Expect: The user receives the Axelar-transferred token on the chain where the swap was supposed to take place at their recovery address. (Note this is different from the IBC swap failure case where the user receives the swap token back on the source chain)
Common failure sources:
Slow relaying from Axelar causes a timeout, and the swap is not attempted. Slippage (the amount out for the swap turns out to be less than the user’s specified minimum, i.e. their slippage exceeds their tolerance)
Post-swap failures
Once the swap is executed, Axelar is no longer involved, and the same rules that apply to IBC post-swap failures apply here, so the Post-swap failures section above applies. ​
CCTP Failures
Routes that use CCTP transfers rely on Circle to produce attestations.

---

**LLM Contextual Output:**

According to the information provided, when a swap occurs through Axelar, users can expect the following outcomes and what to expect:

- The user receives the Axelar-transferred token on their recovery address.
- This is different from the IBC swap failure case where the user receives the swap token back on the source chain.

Common failure sources that may affect this outcome include:

- Slow relaying from Axelar, resulting in a timeout and no attempt to execute the swap.
- Slippage (the amount out for the swap) being less than the user's specified minimum, exceeding their tolerance.

In addition to these technical issues, users can also expect post-swap failures. These include:

- Post-swap failures applying similarly to IBC post-swap failures, as Axelar is no longer involved in the process and the same rules apply.

Regarding CCTP (Cross-Country Token Protocol) failures, it's worth noting that routes using CCTPs rely on Circle to produce attestations.
