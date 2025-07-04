# 📊 Osmosis-Lab-OSMO - 2024-08-15
**184 messages** from **28 contributors**

## 📝 AI-Generated Summary
<think>
Okay, let's tackle this summary. The user wants a concise summary focusing on key points and decisions. First, I need to parse through the provided chat messages and identify the main topics discussed.

Looking at the timestamps, the conversation spans several hours. The participants include Svansy, BasementNodes, CozmoHydra, griffin_web3, IR09K, and others. 

Starting from the top, there's a discussion about Evmos. BasementNodes criticizes Evmos for having poor tooling and difficulty in finding information, suggesting that Solidity is outdated and that Cosmos SDK (CW) is better. They mention that competent EVM teams prefer Cosmos. There's a back-and-forth about whether Evmos has a purpose, with BasementNodes implying that Osmosis taking its place might remove Evmos's reason to exist. CozmoHydra clarifies that the goal is to enhance Evmos, not remove it.

Then, there's a proposal (Prop 827) related to Osmosis. The idea is to decouple OSMO from on-chain services to stabilize its price, focusing on major assets like BTC and ETH. This is compared to Thorchain's approach. IR09K and griffin_web3 discuss the potential benefits, noting that OSMO should be used for securing the chain and generating yield from revenue. The proposal aims to reduce OSMO exposure in pools to make it more resilient.

Another topic is the implementation of limit orders on Osmosis. Sharkiewhite and jasbanza discuss their interest in this feature, comparing it to Uni and 1inch. Svansy explains that Osmosis's limit orders work differently, using triggers rather than traditional order books, and mentions front-running risks and slippage issues.

There's also a part about liquidity pools (LPs). BasementNodes and Svansy talk about the challenges of making gains from swap fees alone, requiring high activity and stable prices. They note that LPs are usually incentivized, and without those incentives, returns might be negative. Oldi6 is confused about how rewards and fees are distributed when removing liquidity, and griffin_web3 clarifies that fees are converted to OSMO.

Additionally, there are mentions of technical issues, like stuck IBC transactions and UI bugs. Users report problems with swaps and transfers, seeking support. The statbot directs them to the support site

## 💬 Key Messages
- **00:28** @Valardragon: did this get answered
- **00:28** @Valardragon: Is this for stableswap?

We found that the iterative algo is far faster/more accurate than the ex...
- **00:29** @Valardragon: due to int precisions, and exponents time complexity
- **01:54** @osmosis_statbot: If you need help, visit our official support site, https://support.osmosis.zone
- **01:54** @GPKwee: #support

## 🔍 Topics & Themes
*AI-identified topics:*
> <think>
Okay, let's tackle this. The user wants me to extract the main topics from the provided chat messages and list them as a comma-separated string. First, I need to go through each message and identify recurring themes or subjects.

Looking at the earliest messages, there's a lot of discussion about Osmosis (OSMO), especially regarding a proposal (Prop 827) to decouple OSMO from on-chain services and focus on major assets like BTC and ETH. That seems like a significant topic. Then, there's mention of EVM (Ethereum Virtual Machine) and Cosmos, with some users comparing tooling and suggesting Cosmos (CW) is better than EVM. Solidity is called "ancient and dead" by someone, which points to a topic around blockchain development tools or languages.

Another thread is about liquidity pools (LPs), APRs, swap fees, and the challenges of making gains without high volume or price deviation. Users discuss the need for incentives for LPs and the risks involved. There's also a lot of talk about technical issues, like stuck IBC transactions, swap problems, UI bugs, and the lack of proper tools or documentation, especially in CLI vs browser-based IDEs.

Limit orders and front-running come up multiple times, with users asking about implementing limit orders on Osmosis and the issues with front-running when large orders are placed. The rug pull discussion around ISLM tokens and bots shilling them is another topic. Also, there's a mention of THORchain activating IBC, which relates to cross-chain functionality.

Some users mention specific projects like Evmos, Synternet, and Forge, and their interactions with Osmosis. There's a question about the status of blockchains (if they're "dead") and the role of governance in stabilizing pools. The idea of building tools from scratch versus existing tooling in EVM is also a point of comparison.

I should also note the references to community discussions, support links, and the overall sentiment about Osmosis's ecosystem and its future. The user's confusion about rewards and liquidity removal in pools is another aspect. Plus, there's a bit of humor and slang like "touching grass" and "diamond hands."

Putting this all together, the main topics seem to be:

1. Osmosis Decoupling Proposal (Prop 827)
2. Comparison of EVM and Cosmos (CW) tooling

*Frequently mentioned terms:*
- will (18 mentions)
- osmosis (17 mentions)
- osmo (17 mentions)
- like (16 mentions)
- just (15 mentions)

## 😊 Sentiment Analysis
<think>
Okay, I need to analyze the sentiment of the provided text, which is a series of chat messages. The options are positive, negative, or neutral. Let me start by reading through all the messages to get a sense of the overall tone.

First, looking at the earliest messages from Svansy and CozmoHydra, there's some casual talk about "touching grass" and smoking, which seems neutral or maybe a bit positive with emojis like 💪🏻 and 🫡. Then griffin_web3 mentions liking an airdrop, which is positive. However, the conversation shifts when discussing Evmos and Osmosis. BasementNodes calls Evmos "fucking impossible" to find good information and says Cosmos SDK (CW) is simpler and more powerful than EVM stuff. There's criticism of Solidity being "ancient and dead," which is negative. 

Later, there's a discussion about Osmosis' proposal to decouple OSMO from on-chain services. Users like IR09K mention it's a step in the right direction, comparing it to Thorchain, which seems positive. But griffin_web3 points out that pools often have low APRs and price volatility, which could be negative. BasementNodes talks about the difficulty of tracking fees and the need for better tooling, which is a negative sentiment towards the current state of things. 

There's also a lot of technical discussion about swap fees, liquidity pools, and front-running. Some users express frustration with the UI, swap fees, and bot issues, indicating negative feelings. However, others like CozmoHydra and Svansy seem engaged and provide constructive feedback, which might be neutral or positive. 

The repeated mentions of issues like "reverse lottery," "spiral" in pool dynamics, and "horrible" aspects of the system lean towards negative. But there are also acknowledgments of improvements and plans, which add a positive note. The sentiment isn't entirely one-sided. 

I should categorize each message and tally the sentiments. The majority of the critical comments come from BasementNodes and others discussing the problems with Evmos, tooling, and pool mechanics. Positive sentiments are from those supporting the decoupling proposal and appreciating certain features. Neutral parts are the technical explanations and casual remarks. 

However, the most intense language is negative ("fucking impossible," "ancient and dead," "horrible"), which might tip

## ✅ Key Decisions & Action Items
<think>
Okay, let's tackle this query. The user wants me to extract action items, decisions, or next steps from the provided chat messages. First, I need to go through each message and identify any explicit or implicit tasks, decisions made, or steps that need to be taken.

Starting from the top, Svansy's messages about EVM and tooling. They mention that EVM has browser IDEs, but other platforms require CLI or building tools. There's a comment about needing better tooling for CW and Cosmos. So maybe an action item here is to improve tooling for CW/Cosmos or provide documentation.

BasementNodes criticizes the lack of tooling and information sources. They suggest that competent EVM teams love CW/Cosmos. So perhaps a next step is to showcase CW's advantages to EVM developers or create better tools. Also, they mention that Solidity is outdated, which might not be an action item but a decision point for others to consider.

Looking at the Osmo decoupling discussion: griffin_web3 and IR09K talk about reducing OSMO exposure and focusing on major assets. The proposal 827 is mentioned, so action items here could involve implementing the decoupling plan, communicating the changes, and monitoring the impact. Also, there's a mention of THORchain's similar approach, so maybe researching that.

Technical issues: Users are having problems with stuck IBC transactions, swap failures, and UI bugs. These would require support teams to address, so action items like investigating IBC issues, fixing UI bugs, and providing support for swap problems.

Limit orders and functionality: sharkiewhite and others ask about limit orders on Osmosis. Svansy explains it's a stop market order. So next steps might be developing or improving limit order functionality, or better documentation on how to use existing features.

Scams and bots: Svansy points out bot activity promoting tokens like ISLM and DEEN. This suggests a need for the community or team to monitor and address scams or bot activity, maybe through moderation or user education.

Other points: Users mention the need for clearer information on fees, APR calculations, and pool strategies. So creating educational resources or tools to track fees and APRs could be action items.

I should also check for any decisions made by the team, like implementing new features, governance proposals, or partnerships. The mention of Proposal 827 breakdown

## 👥 Top Contributors
- @BasementNodes: 38 messages
- @Svansy: 34 messages
- @jasbanza: 19 messages
- @griffin_web3: 16 messages
- @oldi6: 11 messages