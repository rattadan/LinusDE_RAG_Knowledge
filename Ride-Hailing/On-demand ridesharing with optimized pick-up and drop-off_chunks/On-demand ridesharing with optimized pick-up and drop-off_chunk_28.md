## On-demand ridesharing with optimized pick-up and drop-off - Chunk 28

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

Furthermore, P3 can be picked up at his origin O3 or at O3 ′ , and dropped off at D3 or D3 ′ . Dashed lines represent the chance of walking. (For
interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

2.2.1. Definition of the GV-Graph
Solving AP rests on building the “Groups-Vehicles” GV-graph defined in6 Alonso-Mora et al. (2017). This graph has as nodes the set
T ∪ V. Each τ ∈ T is a set of requests, which forms a group, and T⊆℘(R) is the set of feasible groups, where ℘(R) stands for the power set
of R. Each arc τv (defined as a trip) in the graph represents a potential matching between a group and a vehicle, and is characterized by
the cost induced to the system when v serves τ. To compute this cost, note that there might be several feasible ways to match τ and v,
depending on the route followed by the vehicle and the PUDO points for the requests in the group.

---

**LLM Contextual Output:**

This text chunk provides detailed technical details and parameters within the context of ridesharing systems, specifically focusing on the rebalancing strategies, modeling, optimization heuristics, simulation, and service design.

1. **Technical Details:**
   - The GV-graph is defined as a graph with nodes representing sets of requests (T) and vehicles (V), and edges indicating potential matching between groups and vehicles.
   - Each arc in the graph represents a trip with a corresponding cost induced to the system.
   - The problem-solving approach for AP involves building the GV-graph using the power set of R (R being the request space).
   - A key concept is PUDO points, which represent possible destinations or pick-up locations.

2. **Context Connection and Building Upon Surrounding Context:**
   - This chunk connects to the surrounding context by discussing various aspects of ridesharing systems, including rebalancing strategies, modeling, optimization heuristics, simulation, and service design.
   - The text assumes a basic understanding of these topics, providing additional technical details within the ridesharing system.

3. **Requirements, Conditions, or Constraints:**
   - There are no explicit requirements, conditions, or constraints mentioned in this chunk regarding the use of PUDO points, request spaces, power sets, or other related concepts.
   - The context does not explicitly state any operational limitations, scalability concerns, or specific data requirements for the GV-graph.

Overall, this chunk provides technical details on rebalancing strategies within ridesharing systems, connecting to broader topics and assuming a foundation in mathematical modeling, optimization techniques, and simulation.
