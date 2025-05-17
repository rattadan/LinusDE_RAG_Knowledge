## Chunk 63

**Original Text:**

their slippage exceeds their tolerance)
The user / frontend provides an invalid recovery address
An IBC client on the destination chain has expired
Examples: Consider a route where the source asset is ATOM on Neutron, the destination asset is STRIDE on Stride, and the swap takes place on Osmosis:
The user’s tokens transfer from Neutron to the Hub to Osmosis. The swap initiates but the price of STRIDE has gotten so high that the swap exceeds slippage tolerance and fails. A sequence of error acks is propagated back to the Hub then Neutron, releasing the user’s ATOM to their address on Neutron where they started
The user attempts to transfer tokens from Neutron to the hub, but the packet isn’t picked up by a relayer for more than 5 minutes (past the timeout_timestamp). When a relayer finally comes online, it relays a timeout message to Neutron, releasing the user’s ATOM back to their address on Neutron where they first had it. For transfer-only routes: This is the only kind of failure that may happen on a route that only contains transfers.

---

**LLM Contextual Output:**

This text describes an error scenario in the InterPlanetary Communication Protocol (IPC), specifically for transferring assets between networks, such as Neutron and Osmosis. Here's a breakdown of each point:

1. **Slippage exceeds tolerance**: The network determines if the asset transfer is within the acceptable slippage threshold. If it exceeds this limit, the swap fails.

2. **Invalid recovery address**: The user provides an incorrect or invalid recovery address for the asset being transferred. This would prevent the assets from moving as intended between networks.

3. **Destination chain IBC client has expired**: An IBC (Inter-Blockchain Communication) client on the destination network has reached its expiration date, preventing it from handling the asset transfer. This could be due to various reasons such as configuration issues or maintenance.

4. **Examples of route scenarios**: The text provides specific examples of routes where an asset transfer fails due to these conditions:
   - A Neutron (ATOM) source-to-Hub swap to Osmosis.
   - A transfer-only route between Neutron and the Hub, which fails after 5 minutes due to a timeout.

These scenarios highlight critical issues in the IPC protocol for transferring assets securely and efficiently across networks.
