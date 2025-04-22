## Chunk 9

**Original Text:**

To improve protocol and fund safety at launch, IBC Eureka is going to launch in stages, delineated by improved security properties at each stage. ​
Launch stage (0)
At launch, IBC Eureka is going to be deployed on two blockchains: Ethereum and Cosmos Hub mainnet. On the Cosmos Hub side, the security properties remain the same as in IBC Classic - governance has ultimate control over the chain, light client and channels. On the Ethereum mainnet side, it is different - a security council will have control over contract upgradeability, pausing and light client upgrades. ​
Security council
The Eureka Security Council is designated as a 5-of-7 council that can take actions such as:

upgrading the ICS20Transfer, ICS26Router, IBCERC20 and Escrow contracts
migrating light clients in case of freezing due to misbehaviour, expiration or security vulnerabilities/incidents
designating specific canonical names for IBC applications and light clients on Ethereum mainnet
The security council cannot take these actions instantly - the actions are timelocked using a standard OpenZeppelin TimelockController contract with a minimum delay of three days.

---

**LLM Contextual Output:**

It appears you're describing an upcoming project, IBC Eureka, which will be launched in stages to improve protocol and fund safety. Here's a breakdown of your description:

1. **Launch Stage (0)**: This is the initial launch phase where IBC Eureka will start as a separate blockchain entity on both Ethereum and Cosmos Hub mainnets.

2. **Security Properties**: The security features are different at this stage:
   - On the Cosmos Hub side, it's similar to the Classic version but with governance control over light client upgrades and channels.
   - On the Ethereum mainnet side, there's a Security Council that has more control than in IBC Classic, including contract upgradeability, pausing, and migrating light clients.

3. **Eureka Security Council**: This council consists of 5 members out of a total of 7 (thus making it a governing body) who can perform specific actions:
   - Upgrade ICS20Transfer, ICS26Router, IBCERC20, and Escrow contracts.
   - Migrate light clients in case of freezing due to misbehavior, expiration, or security vulnerabilities.
   - Designate canonical names for IBC applications and light clients on Ethereum mainnet.

4. **Action Timelock**: These actions are delayed by a minimum of three days using an OpenZeppelin TimelockController contract, ensuring that the council cannot act instantly.
