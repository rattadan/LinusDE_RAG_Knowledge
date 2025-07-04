# 📊 Osmosis-Lab-OSMO - 2025-05-14
**49 messages** from **16 contributors**

## 📝 AI-Generated Summary
<think>
Okay, let's tackle this summary. First, I need to go through the text and pick out the main points and decisions. The conversation seems to be on Discord or Telegram, with multiple users discussing technical issues related to Osmosis, specifically around alloyed pools and corrupted assets.

Starting from the top, Jeremy Parish mentions that SOL.pica and DOT.pica are corrupted in their alloys. The solution proposed is to withdraw them, but there's a restriction because withdrawing another asset would increase the relative share of the corrupted one. They're working on changing the restriction to absolute amounts instead of relative and draining the corrupted assets. So key points here are the corrupted assets, the current restriction, and the planned fixes.

Then there's a user asking how to drain them from the pool. Jeremy explains that adding SOL.wh to get the alloy and then withdrawing SOL.pica is a possible method. Another user, Mrtiahou, points out a liquidity issue with low volume vs. liquidity. Davidjgoosey tags Jeremy, maybe indicating he needs to be involved. Jasbanza shares a link about a corrupted base denom, possibly an arithmetic overflow error. He also mentions that the alloyed pool can't route through corrupted assets, causing errors, but direct swaps in other pools might work.

Hleb Albau asks about the corrupted asset meaning and which assets are affected (SOL and DOT). There's a discussion about the pool being out of commission this week unless they loop swaps to remove the corrupted assets. Liam from Astonic talks about their decentralized stablecoin platform, security measures like swap limits, collateral in reserve contracts, and plans for integration with other DeFi protocols. They mention over-collateralization and using funds from a presale to bolster reserves.

Other users discuss debates around using Rust vs. EVM, with BasementNodes saying Rust is better but requires coding knowledge. Nostradamus411 and Mrtiahou talk about Cosmos EVM's potential impact on Osmosis and developer choices. There's a mention of a mobile payment feature by Planq Network using their stablecoins.

The main decisions here are the plan to adjust alloy corruption handling from relative to absolute share restrictions, draining corrupted assets (SOL.pica and DOT.pica) from pools, and Astonic's strategies for stablecoin security and integrations. Also, the debate on tech stack choices (CosmWasm vs. EVM) and liquidity issues.

I need to

## 💬 Key Messages
- **00:41** @Mrtiahou: Who’s better than @sunnya97  and @Valardragon  among the 5k EVM devs in question? The number does...
- **00:47** @Nostradamus411: Well you asked why EVM, not if Sunny and Dev are cracked devs…
- **00:48** @Nostradamus411: Of course number doesn’t define quality…but based on statistical averages the more developers, yo...
- **00:49** @Mrtiahou: In any case, I think it’s a pointless debate. Every project picks what works best for them (even ...
- **01:10** @Nostradamus411: Didn’t know this was a debate, I wasn’t advocating one way or the other just giving my 

It’s gre...

## 🔍 Topics & Themes
*AI-identified topics:*
> <think>
Okay, let's tackle this query. The user wants the main topics extracted from the provided text as a comma-separated list.

First, I'll read through the text to understand the context. The conversation seems to be happening in a group chat, possibly related to blockchain or cryptocurrency, given the mentions of Osmosis, Cosmos, SOL, DOT, and terms like "alloy," "corrupted assets," "stablecoin platform," and "DeFi."

Looking at the messages, there are several recurring themes. The first one is about corrupted assets in the alloyed pools, specifically SOL.pica and DOT.pica. Users are discussing draining these assets from the pool and the restrictions in place. So "corrupted assets (SOL.pica, DOT.pica)" is a main topic.

Another user mentions a buy notification bot for Osmosis on Telegram, so that's a separate topic: "buy notification bot for Osmosis in Telegram." 

There's a discussion about a decentralized stablecoin platform called Astonic, which allows minting stablecoins and synthetic assets. That's a significant part of the conversation, so "Astonic decentralized stablecoin platform" should be included.

The topic of draining assets from the pool comes up multiple times, with users talking about the process and challenges. That's "draining corrupted assets from the pool."

The user liam_astonic talks about security measures like swap limits, slippage, and breaker contracts to handle volatility. So "security measures for stablecoin trading (swap limits, slippage, breaker contracts)" fits here.

Integration with other DeFi protocols is mentioned, including plans to work with lending protocols and mobile payment features. That's "integration with DeFi protocols and mobile payments."

There's a debate around programming languages, specifically Rust vs. CosmWasm and EVM. BasementNodes mentions Rust being better except for the learning curve. So "Rust vs. CosmWasm/EVM development debate" is another topic.

The mention of a community proposal to overcollateralize the reserve and the Streamswap presale contributing to it leads to "community proposal for overcollateralizing reserves."

Lastly, the base denom issue with an arithmetic overflow error is discussed by jasbanza, pointing to a technical problem in asset ID creation. That's "technical issues with base denom and asset ID creation."

I need to make sure these topics are distinct and cover all the main points without overlapping.

*Frequently mentioned terms:*
- asset (11 mentions)
- sol (9 mentions)
- osmosis (8 mentions)
- pool (8 mentions)
- corrupted (8 mentions)

## 😊 Sentiment Analysis
<think>
Okay, let me try to figure out the sentiment of this text. So, the user provided a bunch of chat messages from different people, mostly discussing technical issues related to Osmosis, some stablecoin platform, and maybe blockchain stuff. The task is to determine if the overall sentiment is positive, negative, or neutral.

First, I'll start by reading through each message to understand the context. The earliest message is from liam_astonic at 10:08 AM talking about building a decentralized stablecoin platform on Planq Network. That seems positive because they're introducing a project. Then there's a question from jasbanza asking about the stablecoin platform's purpose, which is neutral.

Looking further, there's a discussion about corrupted assets in the alloy pools. Users like jasbanza and hleb_albau mention issues with SOL.pica and DOT.pica being corrupted, which sounds negative. They talk about errors, restrictions, and the need to drain these assets. Jeremy Parish mentions that withdrawing another asset would increase the corrupted one's relative share, which is a problem. So that's definitely a negative point.

Then there's a part where they discuss security measures like swap limits and slippage controls, which might be positive because they're trying to improve resilience. But the user is also asking about potential pump and dump scenarios, which is a concern, so that might be neutral or slightly negative.

Another user, Nostradamus411, comments on funding leaving the building, which is a negative statement. BasementNodes has a back-and-forth about Rust vs EVM, with some humor ("hellish the tooling is lol") which could be negative or just critical. Mrtiahou mentions a debate about programming languages not being pointless, which is neutral. There's also a mention of Doge volume being high, which might be positive for some but not sure in context.

Putting this all together, the main themes are technical issues (corrupted assets, errors, needing to fix pools), some promotional content (Astonic's features), and discussions about development challenges. The negative aspects seem to be about specific problems they're facing, but there's also mention of working on solutions. However, the user's sentiment analysis should focus on the overall tone. The technical problems and errors are negative, but the fact that they're addressing them might add some neutrality. However, since the problems are current and the solutions are in

## ✅ Key Decisions & Action Items
<think>
Okay, let's tackle this query. The user wants me to extract action items, decisions, or next steps from the provided chat messages. 

First, I'll go through each message one by one. Starting with the most recent ones since they might have the latest updates.

Looking at jeremyparish's message at 2025-05-14T22:13:49: "I think it literally just needs to be withdrawn. One could add SOL.wh to obtain the alloy, then withdraw SOl.pica." So here, the action item is to add SOL.wh to get the alloy and then withdraw SOL.pica. That seems like a specific step someone should take.

Next, mikebarb's message says "Not currently" in response to a question about a buy notification bot. Not an action item, just a status update.

BrunoRDias's messages are greetings and a question about a bot, which don't have actions. 

user_5921741683 asks how to drain assets from the pool. The next message from jeremyparish explains that they're working on two things: improving alloy corruption handling and draining SOL.pica and DOT.pica from the pool. So those are two action items. The first is a decision to change the restriction from relative to absolute amount, and the second is the next step to drain those assets.

Kartoffelfren's #tip 1 juno is a tip, maybe an action item for others to tip 1 juno? But not sure if it's an action for someone specific. Maybe not, but I'll note it as a possible action.

osmosis_statbot provides a support link, which is more informational. 

Mrtiahou's message about volume and liquidity seems like a comment, not an action. 

Yusungsang's message about Doge volume is just a statement. 

davidjgoosey's message tags jeremyparish, but doesn't specify an action. 

jasbanza's messages from 15:23:41 onwards mention that the base denom looks corrupted, possibly due to an arithmetic overflow. They also say the alloyed pool needs the corrupted assets removed. So another action item here is to fix the corrupted assets by removing them. 

hleb_albau's message shows a link to a contract query, which might be

## 👥 Top Contributors
- @jasbanza: 11 messages
- @Nostradamus411: 7 messages
- @hleb_albau: 5 messages
- @liam_astonic: 5 messages
- @Mrtiahou: 4 messages