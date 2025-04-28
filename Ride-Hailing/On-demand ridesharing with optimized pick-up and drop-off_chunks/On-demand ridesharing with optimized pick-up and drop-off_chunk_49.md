## On-demand ridesharing with optimized pick-up and drop-off - Chunk 49

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

As this idea has been previously used and shown to work properly, this heuristic will be taken as a basis for the other ones. Assume that we have already decided where to include the first q requests in τ, and we are now inserting the q + 1-th one, i.e., we
search for (iq+1 , jq+1 , oq+1 , dq+1 ): How to alter the vehicle’s sequence and the PUDO points for the q + 1-th request in τ. To do so, we
optimize over a subset Sq+1 of possible sequences and PUDO points. Sq+1 can be exhaustive or might be built using the heuristics
“Limiting sequences” and “Searching for PUDO nodes” explained below in this section. Nevertheless, such a procedure, that considers the previous requests’ positions and PUDO points as fixed, would have a relevant
drawback: the optimal PUDO points selected for the previous requests in the trip might be inefficient when the following requests are
inserted.

---

**LLM Contextual Output:**

**Technical Details and Parameters:**

* The heuristic is designed to optimize over a subset Sq+1 of possible sequences and PUDO points, which can be either exhaustive or built using heuristics "Limiting sequences" and "Searching for PUDO nodes".
* The goal is to find an optimal solution that takes into account the previous requests' positions and PUDO points in τ.
* The optimization process involves searching through a subset of possible sequences and PUDO points, which can be either exhaustive or built using heuristics.

**Context:**

The current text chunk builds upon the surrounding context by providing a detailed explanation of the heuristic used to optimize ridesharing systems. Specifically, it:

* Introduces the idea that previous requests' positions and PUDO points in τ should be considered when optimizing for q + 1-th request.
* Describes the use of heuristics "Limiting sequences" and "Searching for PUDO nodes" to build a subset Sq+1 of possible sequences and PUDO points.
* Emphasizes that such an approach would have a relevant drawback: inefficiently selecting optimal PUDO points when inserting new requests.

**Requirements, Conditions, or Constraints:**

None explicitly mentioned in this section. However:

* The heuristic relies on the previous requests' positions and PUDO points in τ to optimize for q + 1-th request.
* This requires some knowledge of ridesharing systems and optimization techniques.

Overall, this chunk explains how a specific heuristic is used to optimize ridesharing systems, taking into account previous requests' positions and PUDO points.
