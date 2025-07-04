# 📊 Osmosis-Lab-OSMO - 2024-08-03
**463 messages** from **31 contributors**

## 📝 AI-Generated Summary
<think>
Okay, let's tackle this summary. The user wants a concise summary focusing on key points and decisions. The original text is a chat log with multiple users discussing issues related to Osmosis, a blockchain platform. 

First, I need to identify the main issues. Svansy and cloudune are complaining about the platform automatically selecting random tokens, especially wormhole tokens from Solana, for gas fees. They find this problematic because it's unpredictable and could lead to using illiquid or unwanted tokens, causing losses. They suggest restricting gas payment to main coins only, not tokens or cross-chain ones.

WorkerBee_3 and BasementNodes mention that the gas fee calculation might use the base fee plus a percentage, but there's confusion about how rates are determined. There's also a mention of liquidity issues causing transactions to fail if pools are imbalanced or empty, which Svansy thinks is a risk when using tokens with low liquidity.

Another point is the new Withdraw UI being buggy, randomly setting QCK as the token. Solutions suggested include clearing cache, updating Keplr, or using the portfolio page. 

Privacy and usability of Penumbra come up. Svansy defends Penumbra as a privacy chain despite its complexity, while others like GPKwee find it too slow and user-unfriendly. There's a discussion about IBC transfers and issues with chains like Juno not showing up properly in Keplr, possibly due to communication problems.

Technical issues with transactions failing, like the QCK problem and IBC stuck tokens, are mentioned. Users are advised to check error logs, use specific tools, or reach out to support. 

The statbot links to support pages and mentions epoch rewards for liquidity providers, distributed daily. Regular pools give fees every epoch, supercharged pools every block. Users are confused about tracking earned fees before withdrawal, needing to check portfolio after epochs.

Also, some off-topic stuff about a token swap on Streamswap and a user's airdrop loss due to high slippage. 

I need to structure this into key points: gas token issues, UI bugs, Penumbra's role, IBC problems, and reward distribution. Decisions or suggestions from the chat include restricting gas tokens, improving UI, using specific tools for IBC, and understanding reward mechanisms. 

Make sure to keep it concise, avoid minor details, and highlight the main problems and proposed solutions. Check for any other critical issues I might have missed

## 💬 Key Messages
- **00:04** @rick_yldr: Hi everybody. I'm very new to Osmosis, and I'm a bit confused about something, if someone could h...
- **00:05** @GPKwee: in pool #744 you only get swap fee, bonding unavailable, because there is no incentive in the poo...
- **00:07** @rick_yldr: Swap fees is what I'm after, so I'm happy with that. How do I get them? Does the number of shares...
- **00:09** @GPKwee: You only need to fill the liquidity in the pool, and you will get your share when you withdraw yo...
- **00:13** @rick_yldr: I fully understand it is variable and depending on what is going on. Ok, so that "difference" you...

## 🔍 Topics & Themes
*AI-identified topics:*
> <think>
Okay, let's tackle this. The user wants me to extract the main topics from the provided chat messages as a comma-separated list. First, I need to go through each message and figure out what the key points are. 

Looking at the text, there are several recurring themes. The main one seems to be issues with gas fees on Osmosis, especially the automatic selection of random tokens like wormhole or shitcoins from Solana for gas. Users are frustrated because they can't control which token is used, leading to confusion and potential loss of value. There's also discussion about the lack of integration with BTC, which might be another topic.

Another thread is about IBC (Inter-Blockchain Communication) problems, like channels not showing up and transactions failing. There's mention of specific chains like Juno and Penumbra, so maybe those are part of the topics. The new Withdraw UI being buggy and redirecting to QCK is another issue. 

Privacy and usability of Penumbra come up a few times, with users comparing it to other privacy chains and noting its complexity. There's also talk about swap fees and liquidity pools, particularly how rewards and fees are distributed in regular vs. supercharged pools, and the difficulty in tracking earned fees. 

Additionally, there are references to technical support, like checking error logs, clearing cache, and using specific tools or links. Some messages mention specific tokens (COOK, QCK) and their redemption processes. Scammers and support links are also mentioned, indicating a need for caution.

I need to make sure I'm not missing any topics. Let me list them out:

1. Gas fee issues with random token selection (wormhole tokens, Solana shitcoins)
2. IBC transfer problems (channels not showing, transactions failing)
3. Penumbra's privacy features and usability challenges
4. Osmosis UI/UX bugs (new Withdraw UI, QCK redirection)
5. Swap fees and liquidity pool rewards (regular vs supercharged pools)
6. Technical support and troubleshooting (clearing cache, checking RPCs)
7. Integration with BTC (lack of BTC support)
8. Token-specific discussions (COOK, QCK)
9. Scam warnings and security
10. Cross-chain token liquidity and slippage issues
11. Wallet abstraction and user experience (Keplr wallet issues, wallet design)
12. Liquidity depth and pool imbalances affecting transactions

Wait

*Frequently mentioned terms:*
- can (34 mentions)
- osmosis (34 mentions)
- https (29 mentions)
- just (29 mentions)
- get (29 mentions)

## 😊 Sentiment Analysis
<think>
Okay, let's tackle this sentiment analysis. The user provided a bunch of chat messages from Osmosis, which is a decentralized exchange on the Cosmos network. The task is to determine the overall sentiment as positive, negative, or neutral.

First, I'll scan through the messages. The conversation starts with Svansy and cloudune discussing issues with the platform. Svansy mentions that the system is picking random tokens for gas fees, specifically Wormhole tokens from Solana, which they find frustrating. Cloudune agrees, saying it "has a mind of its own" and they had similar problems. There's a lot of technical jargon here—tokens, gas fees, IBC transfers, liquidity pools. 

WorkerBee_3 and BasementNodes chime in, talking about possible solutions like refreshing the cache or checking specific settings. But the main sentiment from Svansy is negative: they don't like the random token selection for gas, call it dangerous, and mention that it's making shitcoin trading impossible. They also bring up issues with the new UI, like it randomly selecting QCK tokens and not allowing them to use their preferred tokens. There's frustration about the user experience, with terms like "highly confusing," "rekt," and emojis like 🤭 and 🤔 indicating annoyance.

Other users like GPKwee criticize Penumbra for being slow and not user-friendly, comparing it to the 90s internet. There's a mention of a scammer and some technical errors when trying to connect wallets or perform transactions. However, some messages are neutral or even positive. For example, cloudune says they like being able to pay gas in various assets for trading strategies, and WorkerBee_3 mentions that the team is working on improvements. The statbot links to support pages and there's a part about a new feature being "ready to serve."

But the majority of the messages are complaints. Users are upset about the platform's instability, unexpected token selection for gas, UI bugs, and difficulties with transactions. Words like "dangerous," "bad," "annoying," "worst," and phrases like "this space is not for the faint of heart" lean negative. Even when there's a positive note, like WorkerBee_3's "one step at a time" approach, the overall tone is more negative because the issues are recurring and frustrating.

I should also note that some messages are neutral,

## ✅ Key Decisions & Action Items
<think>
Okay, let me try to figure out how to extract the action items, decisions, or next steps from this text. The user provided a long list of chat messages, so I need to go through each one and see if there's anything that needs to be done, a decision made, or a next step mentioned.

Starting from the top, Svansy mentions that the system is picking random tokens for gas, which is causing issues. Cloudune had a similar problem with paying fees. They suggest using specific tokens like pepe.axl, boot, hydrogen for fees. So maybe an action item here is to use those tokens. But then Svansy asks why it's happening and if devs can do something. The statbot links to support. So possible next steps: report the issue to support, or check the support site.

Then there's a discussion about IBC integration with BTC, but no action item there. Cloudune talks about a personalized game UI, but that's more of a comment. BasementNodes shares a GitHub commit link, which might be for reference. Svansy says it's dangerous and wants to restrict gas tokens to coins only. So action item for devs to restrict tokens.

WorkerBee_3 and Svansy discuss gas rate calculation, with WorkerBee_3 suggesting checking how gas rates are determined. BasementNodes explains that during a swap, a min_out_amount is set, and if the pool is imbalanced, the tx fails. So next steps for users might be to check pool liquidity before swapping. Also, Svansy mentions that using random tokens for gas could lead to loss, so maybe a decision to avoid certain pools or tokens.

There's a suggestion to clear cache or update Keplr if the UI is buggy. Cloudune is having issues with the new Withdrawal UI randomly selecting QCK. So action items here could be to clear cache, update Keplr, or reach out to devs about the UI bug.

Other parts talk about Penumbra and privacy chains, but not sure if there's an action item. Then there's a user asking about tracking swap fees in pool #744. GPKwee explains that in regular pools, fees are distributed every epoch, not block, and you can't track them until withdrawal. So next step for the user is to wait until epoch or withdrawal to see rewards.

I need to make sure I don't miss any explicit requests or decisions. Also, some

## 👥 Top Contributors
- @Svansy: 163 messages
- @WorkerBee_3: 79 messages
- @BasementNodes: 55 messages
- @cloudune: 45 messages
- @GPKwee: 31 messages