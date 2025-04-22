## Chunk 68

**Original Text:**

Often, Axelar transfers are delayed by Axelar’s relayer or execution services. If a transaction is taking longer than expected, users can visit Axelarscan, find their transaction, and manually execute the steps needed to get the transfer through. See the Axelar docs for details on how to use Axelarscan. Internally, the Skip Go API may use Axelar’s General Message Passing service to move assets between EVM and Cosmos. There are similar failure modes for Axelar as there are for IBC:

Swap failures
What: Axelar GMP takes user assets from an EVM chain to the swap chain.

---

**LLM Contextual Output:**

It appears that Axelar transfers, particularly those involving asset swaps, can be delayed due to issues with its relayer or execution services. If a transaction is taking longer than expected, users may need to manually execute steps in Axelarscan to resolve the issue.

Additionally, I've found some information about Axelar's internal failure modes, specifically related to Swap failures:

Axelar's General Message Passing (GMP) service uses a relayer or execution services, which can lead to delays in asset transfers. This is a common issue with Inter-Blockchain Communication (IBC) and Axelar too.

It seems that similar issues may exist for Axelar, potentially impacting both EVM ( Ethereum Virtual Machine) and Cosmos-based assets.

To resolve the issue, users may need to manually execute steps through Axelarscan or explore other alternatives. It's also worth noting that there are existing documentation on using Axelarscan, which can provide more information on how to troubleshoot and resolve issues related to this service.
