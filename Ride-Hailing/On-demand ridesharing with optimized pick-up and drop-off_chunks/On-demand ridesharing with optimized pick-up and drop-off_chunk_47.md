## On-demand ridesharing with optimized pick-up and drop-off - Chunk 47

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

For example, if each node has ten nodes within the maximum walking-distance, then a group formed by a single request could be
served in a hundred different ways and a group formed by q users in 100q ways. This increase precludes an exhaustive search, as
performed by Alonso-Mora et al. (2017). 2.4. Heuristics
In the previous subsection, we conclude that heuristics are needed to apply the solution method over real-life instances. Moreover,
we have identified the computation of the GV-graph as the method’s bottleneck, because each of its many arcs requires optimizing the
route and the PUDO points for the corresponding group of requests. With this in mind, we propose four heuristics that aim precisely at
accelerating the computation of the GV-graph, by means of both reducing the number of trips (τ, v), and hastening the calculation of
cost(τ, v). 9

Transportation Research Part C 126 (2021) 103061

A. Fielbaum et al. Table 1
An example of the “Filtering Vehicles” heuristic.

---

**LLM Contextual Output:**

This specific section is explaining how to optimize the computation of the Graph Vehicle Ordering Problem (GV-graph), a problem in transportation and logistics that involves finding an efficient order for vehicles to transport requests across a network.

The technical details described include:

1. The GV-graph model, which consists of nodes representing locations, edges representing travel between locations, and arcs representing the request-route.
2. The concept of heuristics, which are algorithms or strategies used to improve the performance of search algorithms in real-world scenarios.
3. Four proposed heuristics for accelerating the computation of the GV-graph:
	* Reducing the number of trips (τ) by considering only relevant locations and requests
	* Hastening the calculation of cost(τ, v) by optimizing route and PUDO points

The connection to or building upon the surrounding context is:

This chunk builds upon the key themes discussed earlier in the reference list. The problem of computing the GV-graph has been identified as a significant challenge in ridesharing systems, and this section proposes new heuristics to address this issue.

Specifically, this chunk connects to the following parts of the reference list:

1. Modeling and Mathematical Frameworks (Zhao et al., Tirachini, A., & Gomez-Lobo 2020) - This section discusses mathematical modeling and optimization techniques in ridesharing systems.
2. Simulation and Service Design (Vosooghi et al., Spieser et al.) - This chunk uses simulation to demonstrate the effectiveness of a heuristic approach.
3. Benefits of Meeting Points in Ride-Sharing Systems (Stiglic et al., Zheng et al.) - This section highlights the importance of meeting points in improving efficiency and user satisfaction.

Requirements, conditions, or constraints mentioned:

1. Real-world instances - The heuristics proposed in this chunk are designed to accelerate computation for real-world instances.
2. Computational complexity - TheGV-graph model is a complex problem, requiring efficient algorithms to solve.
3. Scalability - The proposed heuristics aim to improve performance on large networks with many requests and locations.
