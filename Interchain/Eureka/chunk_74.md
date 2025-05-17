## Chunk 74

**Original Text:**

In the case where the set of Validators have not hit the required signature threshold to successfully process a Hyperlane message on the receiving chain, funds will not be accessible by the user on either chain until the threshold is met (once met, funds will be sent to the user on the destination chain). This generalizes to the different requirements for different ISMs. The Hyperlane documentation explains the different types of ISMs in more detail: https://docs.hyperlane.xyz/docs/reference/ISM/specify-your-ISM

​
Go Fast Failures
If a transfer timeout occurs, meaning a user’s intent does not receive a response from solvers within a predefined time frame, the solver initiates a refund process to ensure that users do not lose funds. Here’s a breakdown of what happens in the event of a timeout:

Intent Expiration: When a user initiates an intent by calling the submitOrder function on the source chain, a time limit is specified. Solvers monitor the intent and assess whether they can fulfill it within this period.

---

**LLM Contextual Output:**

The text describes how Hyperlane handles situations where validators haven't met the required signature threshold to process a message on the receiving chain. It also explains a specific case called "Go Fast Failures" which occurs when a transfer timeout is reached, prompting solvers to initiate a refund process to prevent users from losing funds.

To summarize:

- If a user's intent doesn't receive a response from solvers within a predefined time frame, a timeout occurs.
- Solvers initiate a refund process to protect users' funds.
- The refund process ensures that users don't lose money due to network failures or other issues.
