## Chunk 10

**Original Text:**

On the Ethereum mainnet side, it is different - a security council will have control over contract upgradeability, pausing and light client upgrades. ​
Security council
The Eureka Security Council is designated as a 5-of-7 council that can take actions such as:

upgrading the ICS20Transfer, ICS26Router, IBCERC20 and Escrow contracts
migrating light clients in case of freezing due to misbehaviour, expiration or security vulnerabilities/incidents
designating specific canonical names for IBC applications and light clients on Ethereum mainnet
The security council cannot take these actions instantly - the actions are timelocked using a standard OpenZeppelin TimelockController contract with a minimum delay of three days. The delay gives an opportunity for the Cosmos Hub to halt inbound / outbound transfers in case of a malicious action taken by the Security Council. The security council is composed of individuals associated with well-respected and trusted entities in the Ethereum and Cosmos communities:

Wildcat Finance
Informal
Hypha
ZK Validator
Chorus One
Coinbase Cloud
Interchain Labs
​
Pausing council
The pausing council is designated for rapid-response to a security incident. The only actions that the pausing council can take are pausing and unpausing transfers out of the Ethereum-side contracts.

---

**LLM Contextual Output:**

It seems like you're providing information about the different roles within the Ecosystem Security Council on both the mainnet and Cosmos Hub sides, outlining their responsibilities and capabilities in a clear and concise manner.

The Eureka Security Council is composed of 5 members who can perform various actions such as upgrading contracts, pausing/uncaging light client upgrades, designing canonical names for IBC applications and light clients, and more. However, these actions are delayed to allow for security audits and investigations, ensuring that malicious actions cannot be carried out immediately.

The Security Council's timelocked mechanism is designed to prevent rapid-fire action on sensitive issues, allowing for a measured response to potential threats. This helps maintain the integrity of the network and ensures transparency in decision-making processes.

The pausing council, which includes representatives from well-respected entities like Wildcat Finance, Informal, Hypha, ZK Validator, Chorus One, Coinbase Cloud, Interchain Labs, is specifically tasked with responding to security incidents quickly. Their limited ability to act on these matters allows for swift halting of malicious activities.

This information highlights the importance of robust security measures in blockchain networks and emphasizes the need for transparent decision-making processes that prioritize network safety and integrity.
