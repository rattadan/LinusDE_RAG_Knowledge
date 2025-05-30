## hydro_docs - Chunk 30

**Document Summary:**

**Hydro: A Comprehensive Summary**

**Background and Context**

Hydro is a decentralized platform built for the Cosmos Hub, which enables ATOM stakers to lock their ATOM to gain voting power and vote on bids for Protocol-Owned Liquidity (PoL) deployments. Hydro's smart contracts handle the liquidity deployments, and rewards from tribute are distributed back to voters.

**Pilot Rounds and Objectives**

The Pilot Rounds aim to test critical features of Hydro, including the voting mechanism, bidding process, and liquidity deployment. The objective is to ensure that everything is working as expected before re-deploying the complete PoL available to Hydro.

**Key Components and Processes**

1. **Global and Wallet Caps**: The Hydro committee has set global caps for the maximum PoL deployable in a given round and the maximum ATOM a single wallet can lock up.
2. **PoL Cap**: The total liquidity rerouted to Hydro is expected to be close to 2.5M ATOM, but pilot rounds will start with a conservative amount of 200K native ATOM.
3. **Tribute Floor**: Round 3 introduced a minimum tribute floor, capping the maximum liquidity a bid can receive based on the tribute it distributes to voters.
4. **Custom Deployment Durations**: Projects can bid for PoL deployments lasting up to 3 months, allowing users to secure longer-term liquidity while providing flexibility in allocating voting power.
5. **Committee Oversight**: The Committee will oversee the allocation and deployment processes, intervening directly to mitigate potential risks.
6. **Tribute Refunds**: The smart contract will refund tribute to bids that receive less than 5% of the votes.
7. **Bid Submissions**: Projects submit their bid details via GitHub, and the Hydro Committee reviews and approves or rejects the bid.
8. **Voting Power**: Users can lock their staked ATOM for deployment durations of up to 3 months, granting them flexibility in participating in multi-month deployments.

**Lockups and Voting Power**

1. **Liquid Staking Module (LSM) Shares**: LSM shares represent tokenized, staked ATOM on the Cosmos Hub, which can be used to gain voting power and Hydro rewards.
2. **Locking and Unlocking ATOM**: Users can lock their staked ATOM for a specified duration to gain voting power, which can then be unlocked and converted back to staked ATOM.
3. **Voting Power Calculation**: The amount of voting power received depends on the amount of LSM shares locked and the duration of the lockup.

**APRs and Rewards**

1. **Staking APR**: The standard inflationary reward earned from staking ATOM.
2. **Voter APR**: The additional yield from tributes paid to voters by bidders seeking liquidity through Hydro.
3. **Total APR**: The yield generated by liquidity deployed into DeFi protocols, plus the voter APR.

**User and Bidder Guides**

1. **User FAQ**: Provides answers to common questions for users, including information on Protocol-Owned Liquidity, voting power, and tributes.
2. **Bidder Guide**: Outlines the process of creating and submitting bids, including requirements, bid templates, and deployment tests.

**FAQs and Deployment Process**

1. **How long do projects keep a liquidity deployment?**: Projects receive liquidity at the end of each round and keep it for the duration specified in the bid.
2. **What happens to the PoL yield generated by the liquidity?**: The yields are sent back to the Hydro Treasury for redeployment as additional capital.
3. **What are the key requirements for submitting a bid?**: Projects must use the bid template and ensure bids meet the Hydro committee's guidelines.
4. **What is the timeline for submitting and processing a bid?**: Draft the bid, schedule a review meeting, finalize the bid, and upload it to the Hydro smart contract.

Overall, Hydro aims to provide a decentralized, community-driven, and efficient platform for managing the Cosmos Hub's liquidity while generating value for ATOM holders.

**Original Text:**

At launch, the strategies most likely to be allowed are Liquid Staking DEX Provision (pairing liquid ATOM with a Liquid Staking Token) and Lending (with a 60% Loan-to-Value ratio). Over time, the Hydro committee is expected to be willing to allow riskier strategies. ================================================================================
Document: Bidding process
Source: https://hydro.cosmos.network/docs/projects/bidding
================================================================================


# Bidding process
---------------

## Bid submission
--------------

At the beginning of the auction round, projects submit their bid to the Hydro smart contract and post their Tribute token. Projects can choose any type of token for bidding purposes; it does not have to be the project’s native token. For example, a project could pay a tribute in USDC. After the auction round ends, the tribute is automatically distributed to all voters who supported the Project’s bid.

---

**LLM Contextual Output:**

Here's a strict, pragmatic, and fact-based analysis of the provided text chunk and its context:

**1. Technical Details:**

- The bidding process involves submitting bids to the Hydro smart contract.
- Projects can choose any token for bidding purposes, but it must be posted as a Tribute token.
- For example, a project can pay a tribute in USDC.
- The auction round ends after bidding, and the tribute is automatically distributed to all voters who supported the project's bid.

**2. Connection to Surrounding Context:**

- This chunk connects to the previous sections by explaining the bidding process in the Hydro platform.
- The bidding process is part of the overall objective of testing critical features of Hydro, including the voting mechanism, bidding process, and liquidity deployment (as mentioned in the "Pilot Rounds and Objectives" section).
- The bidding process also aligns with the Hydro committee's oversight and the distribution of rewards to voters, as explained in the "Committee Oversight" and "Tribute Refunds" sections.

**3. Specific Requirements, Conditions, or Constraints:**

- Projects must submit their bids to the Hydro smart contract at the beginning of the auction round.
- Projects must post a Tribute token for their bid, which can be any token, but it must be distributed to voters at the end of the auction round.
- The auction round must end for the tribute to be distributed to voters.

**Ambiguity:**

- There is no ambiguity regarding the technical details and requirements mentioned in the text chunk. However, without more context, it's unclear how the bidding process handles various edge cases, such as a project failing to post a Tribute token or a voter not receiving their tributes.

In summary, this text chunk explains the bidding process in the Hydro platform, where projects submit their bids to the Hydro smart contract, choose any token for bidding purposes, and distribute a Tribute token to voters after the auction round ends.
