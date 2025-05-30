## hydro_docs - Chunk 11

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

Initiate Unlocking: Click on the “Unlock” button to begin the process. Approve Transactions: The system will guide you through the necessary transaction approvals to complete the conversion. ATOM Restaked: Once the process is complete, your LSM shares will be converted back into ATOM in your original staked position on the Cosmos Hub, preserving your staking status. This seamless process ensures that your assets are returned to their original state with minimal effort, maintaining flexibility and usability across Hydro and the Cosmos ecosystem. ### Example Scenarios
-----------------

#### Short Lock-Up
-------------

A user locks 1000 LSM shares for 1 month on 7-Oct. They receive 1000 in voting power. By the end of the one month, their voting power has diminished, and they can either refresh or unlock their shares. #### Long Lock-Up
------------

A user locks 5000 LSM shares for 6 months during a round on 7-Oct. They receive 10,000 voting power.

---

**LLM Contextual Output:**

Analysis of the Text Chunk:

**1. Technical Details**

- The initiation process for unlocking LSM shares involves two steps: 
  1. Clicking the "Unlock" button to start the conversion process.
  2. Approving necessary transactions for the conversion to be completed.
- The system will automatically convert LSM shares back into staked ATOM, returning it to the user's original position on the Cosmos Hub.
- The conversion process includes preserving staking status and maintaining flexibility in asset usage across the Hydro and Cosmos ecosystem.

**2. Connection to Surrounding Context**

- The text chunk leverages the functionality described in earlier sections, specifically:
  - "Locking and Unlocking ATOM" from the **Lockups and Voting Power** section.
  - The concept of LSM shares mentioned in the same section.
- It demonstrates the practical application of Hydro's features, showcasing how users can unlock and convert LSM shares, as well as the difference in behavior based on the duration of the lockup.

**3. Specific Requirements, Conditions, or Constraints**

- The conditions mentioned for the unlocking process are:
  - User must initiate the "Unlock" process through the system. 
  - User must approve necessary transactions to complete the conversion.

The text chunk primarily exemplifies the consequences of different lockup durations on voting power and the automated process for converting back into staked ATOM, highlighting a critical aspect of Hydro's voting mechanism.
