## Chunk 62

**Original Text:**

TypeScript

Copy
await skipClient.executeRoute({
  route:route,
  userAddresses: userAddresses
});


Cross-chain Failure Cases
This page covers the different ways our cross-chain swaps + transfers might fail to help identify failures and manage user expectations

​
Failures during IBC Transfers and Swaps
There are two types of IBC failures that may occur when a user attempts to traverse a swap / transfer route produced by the Skip Go API. Pre-Swap / swap failures
What: These are failures in the sequence of ICS-20 transfers leading up to the swap or a failure in the swap itself (usually due to slippage). Outcome / What to Expect: The users’ original source tokens are returned their starting address on the source chain
Common causes:
Inactive relayers on a channel allow a packet to timeout
Slippage (the amount out for the swap turns out to be less than the user’s specified minimum, i.e. their slippage exceeds their tolerance)
The user / frontend provides an invalid recovery address
An IBC client on the destination chain has expired
Examples: Consider a route where the source asset is ATOM on Neutron, the destination asset is STRIDE on Stride, and the swap takes place on Osmosis:
The user’s tokens transfer from Neutron to the Hub to Osmosis. The swap initiates but the price of STRIDE has gotten so high that the swap exceeds slippage tolerance and fails.

---

**LLM Contextual Output:**

It looks like you're discussing a topic related to cross-chain swaps and transfers using Inter-Blockchain Communication (IBC) on the Skid Go API. Here's a breakdown of what you've provided:

**Overview**

The article discusses potential failures that can occur during IBC transfers and swaps, which may impact user experience and expectations.

**Failures in IBC Transfers and Swaps**

There are two types of IBC failures mentioned:

1. **Pre-Swap/Swap Failures**: These involve issues in the sequence of ICS-20 transfers (e.g., slippage) that lead up to or during the swap itself.
2. **Cross-chain Failure Cases**: This section provides a more comprehensive list of potential failure scenarios, including common causes and examples.

**Common Causes of Pre-Swap/Swap Failures**

The article mentions several potential causes for IBC failures:

* Inactive relayers on a channel that cause packets to timeout
* Slippage (price difference between the user's specified minimum and actual price)
* Invalid recovery addresses provided by the user or frontend
* Expired IBC clients on the destination chain

**Examples**

The article provides specific examples of how these failures can occur, such as:

* A swap initiated with a high price for the destination asset (STRIDE) due to slippage.
* The user's tokens transferring from Neutron to the Hub to Osmosis, which fails due to slippage.

**Managing User Expectations**

The article suggests that these failures can help identify and manage user expectations by providing insight into potential issues and allowing users to adjust their strategies accordingly.
