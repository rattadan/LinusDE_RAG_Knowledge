## hydro_docs - Chunk 36

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

Drop’s latest private valuation isn’t publicly available, but the Drop protocol is similar to the Stride protocol. If the STRD market cap is 20M,andtheDrop−assetsrepresentroughly4020M, and the Drop-assets represent roughly 40% of Stride-assets, DROP market cap may be closer to 20M,andtheDrop−assetsrepresentroughly4010M than 1Mor1M or 1Mor100M. Timely Distribution: Points should be distributed promptly after each round once the Hydro team provides the list of wallets that voted for the point-based bid. Token tributes are available for claim as soon as deployments for a round are completed, so it’s unfair to voters for points distributions to significantly lag. Delayed point distributions are not permitted, as they undermine trust in Hydro’s auction process.

---

**LLM Contextual Output:**

**Section Analysis:**

1. **Exact Technical Details:**
   - The Drop protocol is compared to the Stride protocol, referencing the STRD market cap (20M) and Drop assets (40% of Stride assets).
   - The potential DROP market cap is estimated (20M to 10M) based on the comparison with Stride assets.
   - The point distribution process is described, including:
     * Points should be distributed after each round based on the voting results provided by the Hydro team.
     * Token tributes are available for claim once deployments for a round are completed.
     * Delayed point distributions are not permitted, undermining trust in Hydro's auction process.

2. **Connection to Surrounding Context:**
   - The section is linked to the broader discussion of Hydro's platform, integrating notions of decentralized governance, voting power, and cash-rewards mechanisms.
   - This section touches upon reward structures and credit attributions bestowed upon users for liquidity deployment events through the Liquid Staking Module (LSM) Shares system.

3. **Specific Requirements or Constraints:**
   - A maximum delay of 0 time is permitted for point distribution following the voting results.
   - Token tributes are claimable within specified completion milestones for rounds.

**Pragmatic Summary:**
This section demarcates core aspects of liquidity management, governance structures, and the necessity of timely distribution to uphold trust and appeal within the Hydro endeavour.
