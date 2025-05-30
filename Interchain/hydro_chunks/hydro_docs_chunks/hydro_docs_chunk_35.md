## hydro_docs - Chunk 35

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

This is acceptable as long as points-based bids are structured transparently and equitably, allowing Hydro voters to assess their value confidently. The requirements are:

APR Calculation: The Hydro team must be provided with a straightforward method for determining the APR of the points. Since fair auction dynamics require comparability between token-based and point-based bids, the project must include in their bid:

The percentage (a % range) of the total token supply that will be allocated to points. The percentage of total points that will be used for bidding in Hydro. The expected market cap of the project A short justification for this market cap (see example below)

Predicting the marketplace of a crypto project is obviously a very difficult task, so projects should just use the last private valuation or a simple comparable valuation method. Let’s take an example with the liquid staking protocol Drop.

---

**LLM Contextual Output:**

**Analysis of the Text Chunk:**

1. **Technical Details and Parameters:**
   - The text chunk focuses on a set requirement for projects bidding on Hydro.
   - The key technical detail is the necessity for delivering transparent and equitable points-based bids.
   - Specific parameters to be included in the bid:
     - Percentage of total token supply allocated to points.
     - Percentage of total points used for bidding in Hydro.
     - Expected market cap of the project.
     - A short justification for the market cap.
   - An example is given for predicting the market cap (last private valuation or a simple comparable valuation method).
   - A liquid staking protocol named "Drop" is used for an example.

2. **Contextual Connection:**
   - The section appears to be building upon previous information on Hydro, focusing now on a specific requirement for bidder projects.
   - The requirement aims to ensure transparency and fairness in the bidding process by standardizing how points-based bids are structured and evaluated.
   - This requirement appears to be part of an overall effort to test and ensure the critical features of the Hydro platform work as expected.

3. **Requirements, Conditions, and Constraints:**
   - The key requirement for projects is to structure their points-based bids in a way that allows for transparent and equitable evaluation.
   - The project must provide specific information about their points-based allocation and market expectations.
   - The example given suggests using the last private valuation or a simple comparable valuation method to predict the market cap, with "Drop" as an illustrative example.
