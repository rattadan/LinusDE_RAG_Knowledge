## hydro_docs - Chunk 33

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

To add a tribute to a proposal, send the following transaction to the Tribute smart contract:

## Tribute Queries
---------------

To query all tributes for a given proposal, use the following query on the Tribute smart contract:

## Tribute Refunds
---------------

If a proposal is not among the top N by voted power for a given round, projects get refunded the tributes to the account that added the tribute. This is done by sending the following transaction to the tribute smart contract:

After the transaction is successfully executed, the entire amount of the tribute will be refunded to the sender’s account. ## Tribute Floor
-------------

The tribute floor feature helps balance fair rewards for users and equitable access to liquidity for projects. The tribute floor and the tribute amount submitted by a bidder determine a maximum allocation.

---

**LLM Contextual Output:**

**Analysis of the Given Text Chunk:**

1. **Technical Details and Parameters**: The text chunk explains the process for interacting with the Tribute smart contract in Hydro.
2. **Key Processes**: 
   - **Tribute Addition**: A transaction is sent to the Tribute smart contract to add a tribute to a proposal.
   - **Querying Tributes**: A query is sent to the Tribute smart contract to retrieve all tributes for a given proposal.
   - **Tribute Refunds**: A transaction is sent to the Tribute smart contract to refund a tribute if a proposal is not among the top N by voted power for a given round.
3. **Specific Requirements and Conditions**:
   - To add a tribute, send a transaction to the Tribute smart contract.
   - To query all tributes for a given proposal, use a query on the Tribute smart contract.
   - To refund a tribute, the proposal must not be among the top N by voted power for a given round.
4. **Connection to Surrounding Context**: This chunk is related to the tribute and lottery system described in the "APRs and Rewards" section, specifically the voter APR (additional yield from tributes paid to voters by bidders seeking liquidity through Hydro).

**Ambiguities**:

- There is no clear specification of what N is, referring to "the top N by voted power for a given round".
- It is not explicitly stated how the "tribute floor" feature is implemented and how it interacts with the tribute amount submitted by a bidder. 

**Strictly Practically Analyzed Outcome**:

This text chunk provides technical details for interacting with the Tribute smart contract in the Hydro platform. It is essential to follow the instructions for adding, querying, and refunding tributes to ensure proper functionality of the tribute and lottery system in Hydro.
