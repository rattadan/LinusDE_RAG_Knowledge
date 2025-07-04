# 📊 Osmosis-Lab-OSMO - 2024-11-16
**226 messages** from **18 contributors**

## 📝 AI-Generated Summary
<think>
Okay, let's tackle this summary. First, I need to go through the provided chat messages and pick out the key points and decisions. The user wants a concise summary focusing on those elements.

Looking at the text, there are several threads here. The main ones seem to be about issues with IBC transfers, specifically involving Osmosis, Noble, and Shido chains. Users are having trouble with transactions getting stuck, especially when using Wormhole. There's also a mention of Union's upcoming launch in Q4 and discussions about IBC adoption.

Starting from the top, GPKwee and axag13 are discussing that IBC isn't enabled yet for certain chains, which is why they can't swap UWU tokens on Unicorn Chain to Osmo or other Cosmos tokens. axag13 tried to ask others about swapping, but the response was that it's not possible yet. 

Then there's a part where users like Chessmany3k and BasementNodes talk about SUI blockchain not using Cosmos SDK but wondering if IBC can still work with it. They mention that any chain with state proofs could use IBC, but SUI might be relying on Wormhole for now. Chessmany3k is frustrated with Wormhole's reliability and suggests promoting IBC more for PoS chains. 

The bulk of the text is about mctokendegen's stuck IBC transfer from Osmosis via Noble to Shido. BasementNodes is helping them troubleshoot, pointing out issues with the channel IDs and the relayer being stuck. They tried flushing the relayer, but there were errors related to the chain ID mismatch. BasementNodes asks for a small test transaction to help resolve the stuck packets. Eventually, they manage to clear the packets, and mctokendegen gets their funds back, thanking BasementNodes. 

Other points include Osmosis Statbot directing users to support sites, some discussions about rewards distribution on Osmosis happening daily at 17:15 UTC, and complaints about Wormhole's delays. There's also a mention of a Union initiative launching in Q4, which might be relevant.

I need to make sure the summary captures the main issues: stuck IBC transfers due to relayer problems, the use of Wormhole vs IBC, the discussion on IBC adoption, and the resolution steps taken. Also note the support links and the Union project. Avoid including too much technical detail but highlight the key

## 💬 Key Messages
- **03:15** @ndcast: what makes you say so
- **05:13** @BasementNodes: 
- **06:19** @vta108: Mantra DAO is amazing while OSMO is pretty slow ;(
- **06:19** @vta108: Need to catch up soon
- **07:29** @Chessmany3k: day 4 and still no progress on stuck wormhole transfer

## 🔍 Topics & Themes
*AI-identified topics:*
> <think>
Okay, let me try to figure out how to extract the main topics from this text. The user provided a list of chat messages, some from individuals and some from a bot. The task is to list the main topics as a comma-separated string.

First, I'll go through each message and see what they're talking about. The earliest message is from osmosis_statbot on Nov 16 at 16:31:33, mentioning joining a Discord server. Then there's a discussion between Chessmany3k and BasementNodes about whether SUI is an IBC chain. They talk about SUI using Move language and not Cosmos SDK, but IBC compatibility for PoS chains. So that's a topic: SUI and IBC compatibility.

Then, there's a conversation about Union, with griffin_web3 suggesting looking into Union, launching in Q4. So Union (Q4 launch) is another topic.

Next, Yusungsang asks MAX about Polaris, so Polaris is a topic.

Chessmany3k also mentions issues with Wormhole, saying they're not responsive and stuck transfers. So Wormhole bridge issues and reliability.

There's a lot of discussion about IBC transfers, especially from Osmosis to Shido, with problems like stuck transactions and relayer issues. So IBC transfer issues, Osmosis-Shido transfers, and relayer problems.

BasementNodes and mctokendegen talk about using Noble for USDC transfers, which worked before but now are stuck. So Noble chain, USDC transfers.

Other topics include staking rewards on Osmosis, Epoch timing, validator fees. So Osmosis staking rewards, Epoch timing, validator fees.

Chessmany3k also mentions marketing IBC to PoS chains, so promoting IBC adoption.

There's a mention of a scam warning and reporting, so scam warnings.

Also, links to support sites and checking balances via a tool from BasementNodes. So Osmosis support resources, balance checking tools.

Putting all these together, the main topics seem to be:

- IBC transfer issues
- Osmosis-Shido transfers
- Wormhole bridge reliability
- SUI and IBC compatibility
- Union (Q4 launch)
- Polaris
- Osmosis staking rewards
- Epoch timing
- Validator fees
- Promoting IBC adoption
- Scam warnings
- Support resources
- Balance checking

*Frequently mentioned terms:*
- shido (39 mentions)
- can (17 mentions)
- there (17 mentions)
- now (15 mentions)
- osmo (15 mentions)

## 😊 Sentiment Analysis
<think>
Okay, let's tackle this sentiment analysis. The user provided a bunch of chat messages and wants to know the overall sentiment—positive, negative, or neutral. First, I need to go through each message and determine its sentiment.

Starting from the top, GPKwee says "my pleasure" which sounds positive. Then axag13 uses "Ok. Thanks for the reply 😎🤝" which is definitely positive with the emojis. GPKwee mentions they can't do anything because IBC isn't turned on yet—neutral, just stating a fact. axag13 asks about using Uwu on unicorn chain, which seems neutral. GPKwee tells them to block and report, which is a negative instruction. axag13's next message is a greeting, neutral. GPKwee talks about picasso uwu on Osmosis, neutral. axag13 asks about swapping UWU, which is a neutral question.

Looking at the bot messages, they're just providing links or info, so neutral. Then Chessmany3k says "thnx....ill check this out...lord knows something like this is needed" which is positive. BasementNodes asks if it's launched yet, neutral. griffin_web3 shares a link, neutral. Yusungsang's message about MAX⚡️ and Polaris is neutral. Chessmany3k asks about Union's website, neutral. griffin_web3 mentions Union, neutral. BasementNodes says they didn't get scammed yet, seems legit—positive. Then a discord link, neutral. "discord only :/" sounds a bit negative. "I'll find it" is neutral. Warrior2101 asks about Sui community, neutral. "next gen IBC looks nice" is positive. 

Chessmany3k talks about Axelar taking over, which is negative. Then they mention using IBC as the best way, positive. They suggest marketing IBC, positive. BasementNodes links to a repo, neutral. He says any chain with state proofs can use IBC, neutral. Chessmany3k discusses SUI using Move lang but IBC possible, neutral. BasementNodes thought they used tendermint, neutral. Chessmany3k says "it should be" which is neutral. BasementNodes asks if Sui is an IBC chain, neutral. Then says "anyway no, it looks like only wormhole for now" which is negative.

## ✅ Key Decisions & Action Items
<think>
Okay, let's see. I need to extract action items, decisions, or next steps from this chat text. The user provided a long conversation with various messages. Let me start by reading through each message and identifying any tasks, decisions, or steps that need to be taken.

First, looking at the most recent messages. The last message is from ndcast asking "what makes you say so" but there's no prior context here. Let me go through the text step by step.

There's a user named mctokendegen who had an issue with an IBC transfer from Osmosis via Noble to Shido. The funds didn't show up, and the Acknowledgment is missing. BasementNodes helped them by flushing the IBC packets and mentioned that the Shido team needs to fix their relayer. So possible action items here: mctokendegen needs to contact the Shido team or open a ticket, and the Shido team should fix their relayer.

Another part: GPKwee says "yeah, we can't do anything about that, they haven't turned on their IBC yet" when axag13 asks about using Uwu on Unicorn chain. So next step here might be that the Unicorn chain needs to enable IBC for that to work.

Chessmany3k mentions issues with Wormhole transfers being stuck and suggests using IBC instead, and also talks about marketing IBC to other chains. So action items here could be to resolve the stuck Wormhole transfer, and consider initiatives to promote IBC adoption.

BasementNodes provided some chain details for Shido and also had a problem with the RPC node. They mentioned that the Shido team should fix their relayer. So maybe the Shido team needs to address their relayer issues.

There's a mention of sending a test transaction of $1 before sending more funds, so that's a next step for someone involved.

Also, users are directed to the Osmosis support site, so maybe opening a support ticket is an action item.

I need to make sure not to miss any other steps. Let me check again.

In the middle of the text, there's a part where BasementNodes says "please block and report" when axag13 asks about Uwu on Unicorn. So that's an action item for axag13 to block and report.

Chessmany3k also resolved a stuck Wormhole transfer themselves, so that's a past

## 👥 Top Contributors
- @BasementNodes: 112 messages
- @mctokendegen: 47 messages
- @Chessmany3k: 14 messages
- @GPKwee: 8 messages
- @Khuwarzmi: 8 messages