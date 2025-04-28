## On-demand ridesharing with optimized pick-up and drop-off - Chunk 55

**Document Summary:**

This reference list covers a wide range of works from 2010 to 2020, focusing on various aspects of ridesharing and mobility-on-demand systems. Here's a summary of the key themes:

### Key Themes:
1. **Rebalancing Strategies**:
   - Wallar et al., van Engelen et al.
   - Wen et al.

2. **Modeling and Mathematical Frameworks**:
   - Zhao et al.
   - Stiglic et al.
   - Tirachini, A. & Gomez-Lobo (2020)
   - Tirachini, A. et al. (2010)

3. **Optimization Heuristics**:
   - Stiglic et al.

4. **Simulation and Service Design**:
   - Vosooghi et al.
   - Spieser et al., Samaranayake et al.

5. **Flexible Transport Services**:
   - van Engelen et al.

6. **Ride-Sharing Systems with Meeting Points**:
   - Zheng et al.

7. **Vehicle Rebalancing for Mobility-on-Demand Systems**:
   - Wallar et al.
   - Vosooghi et al.

8. **Flex-Route Services and Ride-Sharing**:
   - Zhao, M. et al.
   - Stiglic et al.

9. **Reinforcement Learning Approaches**:
   - Wen et al.

10. **Benefits of Meeting Points in Ride-Sharing Systems**:
    - Stiglic et al.
    - Zheng et al.

### Summary of Key Papers:

- **Vosooghi, R., Puchinger, J., Jankovic, M., Vouillon, A. (2019)**: Focuses on shared autonomous vehicle simulation and service design.
- **Zhao, M., Yin, J., An, S., Wang, J., Feng, D. (2018)**: Develops mathematical modeling and decomposition methods for ridesharing problems with flexible pickup and delivery locations.
- **Stiglic, M., Agatz, N., Savelsbergh, M., Gradisar, M. (2015)**: Analyzes the benefits of meeting points in ride-sharing systems.
- **Zheng, Y., Li, W., Qiu, F., Wei, H. (2019)**: Evaluates the benefits of introducing meeting points into flex-route transit services.

### Concluding Remarks:
The papers collectively address critical challenges and opportunities in ridesharing and mobility-on-demand systems through various methodologies, from heuristic optimization to advanced simulation techniques. The inclusion of meeting points is highlighted as a significant factor for improving efficiency and user satisfaction in these systems. The use of reinforcement learning and mathematical modeling further underscores the growing sophistication in managing such dynamic systems.

This reference list provides a comprehensive overview of current research trends and can serve as a basis for further analysis or application development in ridesharing technologies.

**Original Text:**

Instead of an exhaustive computation over all the possible PUDO points, we consider a
limited set of “candidates”, found through a local search from the exact origins and destinations: in simple words, we consider as
candidates those neighbours of the exact origin (respectively, exact destination) that decrease the total costs, to then analyze their
neighbours; we continue doing so until no new neighbour is included as a candidate (i.e., total costs cannot be decreased with any
candidate’s neighbour). This is explained in detail in Algorithm 4, where X(u) stands for the walking-neighbors of u, X(u) =
′
′
′
{u ∈ 𝒱 : uu ∈ E ∨ u u ∈ E}. To understand this heuristic better, consider a given order in which to insert the request in the vehicle’s route, defined by (i, j). Without the heuristic, if the origin of the request is or , the set of pick-up candidates is {u ∈ 𝒱 : tw (or ,u)⩽Ωa }.

---

**LLM Contextual Output:**

This specific section appears to be explaining a technical process or algorithm used in ridesharing systems. Here's a focused analysis:

**Exact Technical Details:** The algorithm, as described in the text chunk, is a local search-based heuristic for finding optimal routes that minimize total costs (represented by Ωa). Specifically, it involves considering a limited set of "candidates" identified through a local search from the exact origins and destinations. These candidates are then evaluated based on their proximity to both the origin and destination.

**Connection to or Build-up upon surrounding context:** This chunk builds upon the key themes discussed in the surrounding reference list, which focuses on various aspects of ridesharing and mobility-on-demand systems. The algorithm described is a critical component of this theme, addressing the challenge of optimizing routes while considering constraints such as proximity and distance.

**Specific requirements or conditions:** None are explicitly mentioned in this chunk, but it assumes access to an existing vehicle's route (represented by tw (or ,u)), which implies that the algorithm requires some form of spatial or geographic data to operate. Additionally, the algorithm is designed for ridesharing systems with multiple vehicles and destinations, suggesting that it may be used in scenarios where optimization is necessary across a large number of locations.

**Reinforcement Learning Approaches:** The text mentions reinforcement learning as one of several approaches discussed in the summary of key papers (e.g., Wen et al. "Reinforcement Learning Approaches"). However, this connection is not explicitly made in this chunk. It is worth noting that reinforcement learning can be used to optimize routes under various constraints, and may be considered an additional aspect of ridesharing system optimization.

In summary, this specific section explains a technical process (algorithm) for optimizing routes in ridesharing systems based on local search and proximity considerations, and builds upon the surrounding context by addressing challenges in ridesharing and mobility-on-demand systems.
