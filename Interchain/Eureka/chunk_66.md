## Chunk 66

**Original Text:**

Outcome / What to Expect: The user’s newly purchased destination asset tokens will be transferred to their address on the swap chain. (This is the address passed to chains_to_addresses in /fungible/msgs for the chain where the swap takes place, which is given by swap_venue.chain_id in the response from /fungible/route)
Common failure sources:
Inactive relayers on a channel allow a packet to timeout
The user / frontend provides an invalid address for the destination chain
An IBC client on the destination chain has expired
Examples: Consider a route where the source asset is ATOM on Neutron, the destination asset is STRIDE on Stride, and the swap takes place on Osmosis:
Suppose the swap took place and the transfer to Stride has been initiated, but the Relayer between Osmosis and Stride is down. So the packet’s timeout occurs after 5 minutes. When the Relayer comes back online after 8 minutes, it relays a timeout message to Osmosis, releasing the user’s STRIDE, which gets forwarded to their Osmosis address
In a post-swap error, the user will end up with their destination asset tokens in their address on the chain where the swap took place (e.g. STRIDE on Osmosis in this example)
In a post-swap error, the user will end up with their destination asset tokens in their address on the chain where the swap took place (e.g.

---

**LLM Contextual Output:**

Based on the provided information, here's what to expect when using the newly purchased destination asset tokens:

1. **Destination asset transfer**: The user's newly purchased destination asset tokens will be transferred to their address on the swap chain.

2. **Common failure sources**:
   - Inactive relayers on a channel: If there is an issue with the relay between the two chains, the packet may timeout.
   - Invalid address for the destination chain: If the user provides an invalid address for the destination chain, the transfer may fail.
   - IBC (Inter-Blockchain Communication) client on the destination chain having expired: An IBC client is used to communicate with other blockchains. If it has expired, the transfer may fail.

3. **Examples of failure scenarios**:
   - A route where the source asset is ATOM on Neutron and the destination asset is STRIDE on Stride.
     * The swap takes place on Osmosis, but the relayer between Osmosis and Stride is down.
     * After 5 minutes, the packet's timeout occurs.
     * When the relayer comes back online after 8 minutes, it releases the user's STRIDE to their Osmosis address.

4. **Post-swap error outcome**:
   - In a post-swap error, the user will end up with their destination asset tokens in their address on the chain where the swap took place.
   - In this example, the user would receive their STRIDE tokens back into their Osmosis address after 3 minutes.
