Welcome Back to General Communications: The Inside Scoop

Welcome back to General Communications, the inside scoop where we interview new and upcoming projects built on the General Network. I’m Throw Tellers, and today we have Dari and Martin from End Ride. They’ll be discussing their project on General. How are you guys doing?

Dari & Martin: Doing great, busy building in the bear market, smashing it!

Throw: First of all, thank you for coming on. I’m excited for the chat today. Before we get into the application and your inspiration behind it, Martin, if you’d like to start, I can jump in after.

What is nRide?
Martin: There are actually three main components to nRide:

Driver Registry: A smart contract deployed on Juno that contains a database or list of all drivers in the system, including information about their location, vehicle type, and networking address (where they receive messages). When you’re a rider and trying to go somewhere, you consult this registry to see which drivers are around you.
Messaging Protocol: Once you know which drivers are around you, this protocol defines the messages you need to exchange with drivers to agree on and coordinate the ride. We call this the End Ride Protocol.
Escrow Mechanism: A smart contract deployed on Juno that serves the same purpose as cancellation fees on centralized apps. Both users lock funds into the contract when they agree to a journey, and the funds are unlocked when the ride is complete or if someone cancels late.
Dari: Just to piggyback off what Martin said, we really feel that peer-to-peer applications pair well with gig economy-focused applications. If you stay plugged into the ride-hailing space, drivers talk about a slew of issues, from unfair pricing to a lack of transparency. For this reason, we believe peer-to-peer and the gig economy pair well together. What really piqued my interest is the ability to redistribute ownership in the form of DAOs and the various tools that decentralized applications and this technology can offer. That’s why they pair so well together. So, we’re really focusing on developing this and bringing it to the masses.

What is the Gig Economy?
Throw: When you say “gig economy,” what do you mean exactly?

Dari: When you think of the gig economy, you can think of freelance work or short-term contract work, whether people do it as a side hustle or as their main job. Popular platforms like Uber or DoorDash are examples where people offer these services peer-to-peer, but as things exist now, they’re controlled by central intermediaries. That’s what we’re trying to solve with End Ride.

Martin: Just to add on to the escrow smart contract I mentioned earlier, it serves as the cancellation policy. What’s cool and differentiating is that on platforms like Lyft and Uber, cancellation policies only extend to the rider. On End Ride, both the rider and driver have a stake in completing the pickup. So, the driver will also be affected.

Throw: That’s absolutely brilliant because there’s nothing worse than an Uber driver canceling on you. It’s so annoying when you’re trying to get home, and a driver cancels on you, and then you have to pay the £1 fee on top of that. So, you’ve solved that issue with the escrow contract. Very well done!

Why Blockchain?
Throw: Quick question—why does this even need blockchain? Why do we need blockchain to complete rides?

Martin: That’s a good question. A lot of it can be done through pure peer-to-peer message exchanges, but certain things require more permanent storage, like the token itself and the driver registry. That’s the shared database we all need to see the same version of at the same time. So, it could have been done without blockchain, but blockchain provides security and a validated dataset, giving consensus on what happened.

Throw: Absolutely. Feel free to demonstrate and share the screen to show the community what you’ve got.

Demonstration of End Ride
Martin: Let’s try this out. I’m going to share my screen. I’m running two emulators locally on my machine—one as a driver and one as a passenger.

Throw: What’s on the backend that gives you the app, the map, and stuff like that? Is it Google Maps?

Martin: Yes, it’s Google Maps. The map is served by Google APIs, which handle things like calculating distances and routes. On the right side, you’ll see the driver view. The little green spot means the driver is registered and ready to receive incoming requests from riders.

I also want to show you the account view. The app serves as a wallet for the End Ride token. Both the rider and driver have 200 End Ride tokens. As we discussed earlier about the escrow mechanism, we’ll see how these balances change as funds are locked and unlocked during the pickup process.

Throw: Got it. So, let’s get into it. Dari, why don’t you give me a destination where you want to go?

Dari: Let’s see—any address in Manchester. How about Old Trafford?

Martin: Sure, I’ll type in Old Trafford. Using Google APIs, it tells me it’s 300 kilometers away, about a 3-hour drive. I’ll broadcast the request to nearby drivers. As a side note, you see these hexagons? They organize users into areas, so you’ll only interact with users in the same area. This is for scalability.

Throw: So, if I’m in France or China, I won’t receive these requests?

Martin: Exactly. So, I broadcast the request, and the driver receives it. It says, “There’s a guy 3 minutes away who wants to go to Old Trafford, which is 3 hours away.” As a driver, I can accept this and name a price. For example, since it’s pretty far, I’ll say £1,000.

Dari: Just to quickly add, that’s a really powerful feature because a lot of riders complain about the lack of transparency in pricing. Receiving real-time bids from drivers allows price-sensitive riders to pick the lowest price.

Throw: What happens if two drivers bid on the same fare? Does the rider see conflicting bids?

Martin: At the moment, the driver doesn’t see the other bids. This prevents drivers from undercutting each other deliberately. The offers are private messages sent directly from the driver to the rider using an encrypted overlay network called NKN, which is another blockchain network. This ensures scalability, as sending messages on-chain would create bottlenecks.

Escrow Mechanism in Action
Martin: Now, the rider accepts the driver’s offer, and 10 End Ride tokens are locked into the escrow smart contract. The driver checks that the rider has locked the tokens and then locks their own tokens. This all happens under the hood. Now, the funds are locked, and the escrow contract is created. You can see the rider’s balance went from 200 to 190 because they locked 10 tokens in the smart contract.

To unlock these tokens, there are two options:

One party cancels, and the payouts are calculated accordingly.
Both parties complete the ride, and the tokens are unlocked.
Throw: So, the app only covers the ride-hailing part, not the payment for the ride itself?

Martin: Yes, the app only goes up to the pickup. The payment for the ride itself is outside the app at the moment.

Closing Remarks
Dari: What we’re building with End Ride is the End Ride Protocol. The core idea is that gig economy-based applications pair well with blockchain technology because of how it promotes ownership and permissionless innovation. We’re building an open-source protocol that others in the gig economy space can leverage to build their applications. The first application implementing this protocol is the End Ride app, which tackles issues in the ride-hailing industry.

Throw: That’s amazing. Thank you both for coming on the show. I’ve been really impressed, and I’m looking forward to testing out the free rides at AwesomeWasm. Where can people reach you?

Dari: You can join our Discord, email us through our website, or DM us on Twitter.

Throw: Fantastic. Thanks to the community for tuning in, and we’ll see you all at AwesomeWasm with some End Ride taxis. Thank you again, Dari and Martin!


Hello and welcome to a new video on my YouTube channel. Today, I want to introduce you to nRide, an exciting project that I believe is the best I’ll showcase this year. It might even be a life-changing opportunity because nride aims to empower mobility as a decentralized ride-hailing protocol. Currently, with a market cap of $21,000, which is minimal, I expect it to become a multi-billion dollar market cap project.

nRide is different from other taxi apps like Uber, Grab, or Bolt, which are centralized and charge high fees. nRide is decentralized, charging only a 0.5% fee, which is significantly lower. It’s based on blockchain, allowing payments with USDC and potentially its own ENR token in the future. The application is already developed and usable, allowing you to book rides if drivers are available.

The rider app is available on iOS TestFlight and Android, enabling decentralized rides without KYC, which is a significant innovation. Although there are no drivers yet, discussions with taxi companies are ongoing, and nRide is expected to grow as they save costs and improve efficiency.

nRide’s system allows drivers to propose prices for rides. For example, if three drivers offer different prices, you can choose based on your preference. This flexibility is something I haven’t seen before. The app is already functioning, as demonstrated at the Web 3 Global Media conference in May 2024 in Dubai, where a taxi company used it to transport attendees, and one user won 1,000 USDC in a giveaway.

Despite having less than 900 followers on Twitter, nRide is expected to gain traction and become a significant project in the next bull run. The app is built on the Cosmos network, utilizing Osmosis, and has shown promising growth, achieving a 5x increase since its launch in February 2023.

nRide’s tokenomics are also interesting, with a max supply of 1 billion tokens and no inflation due to the absence of staking rewards. The project is genuinely decentralized, with 60% of the tokens allocated to the ENR DAO. Unlike many projects, nRide had no pre-sale or VC funding, launching with a liquidity pool of 0.01 USDC.

The project is steadily growing, focusing on building partnerships and a strong community. Although it’s not a quick profit project, it has the potential to become viral and achieve significant market cap growth. nRide is not a taxi company but an IT solution for taxi companies to accept crypto payments, bridging the gap between them and crypto users.

Check out the app on the App Store, make a small deposit, and if you find this video helpful, please like and subscribe. The project links are in the video description, including the website, Twitter, and Discord for easy access.

Thank you for watching, and I hope you enjoyed the video. See you next time, bye-bye

