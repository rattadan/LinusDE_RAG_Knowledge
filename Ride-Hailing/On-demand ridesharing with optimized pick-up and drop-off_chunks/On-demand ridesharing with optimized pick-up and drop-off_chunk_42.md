## On-demand ridesharing with optimized pick-up and drop-off - Chunk 42

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

′
′
′
′
′
Consider an instance of GTSP, i.e., a graph G = (V ,E ), with costs ce over each arc, V = V1 V2 …Vq , and starting node v ; for each

u ∈ V , let us denote f(u) = i iff u ∈ Vi . Define then an instance of calculating cost(τ, v) over the same graph with an extra drop-off node
′
w; the vehicle v is located in v , has capacity q and is currently carrying no passengers: in-vehicle costs cV equal to ce ,∀e ∈ E, and cV (u,
′
′
′
w) = 0, ∀u ∈ V. The extra node w has only one departing edge e that goes to v , with cV (e ) = 0; Ωa = 1 (the other Ω’s are not relevant
′

8

Transportation Research Part C 126 (2021) 103061

A. Fielbaum et al. for the reduction) and walking costs are given by:
⎧
⎨ 0 if f (u) = f (v),
cW (e = uv) = 2
otherwise. ⎩

(12)

Furthermore, we have q requests, one per subset of nodes, such that the origin of ri is any node in Vi , and all the destinations are w. What Eq.

---

**LLM Contextual Output:**

This text chunk appears to be discussing the concept of General Traveling Salesman Problems (GTSP) and a specific instance of calculating the cost of transporting passengers in this context.

The exact technical details being described include:

* Graph representation: G = (V, E), where V is the set of nodes (originating points), and E is the set of edges (transportation routes)
* Cost function: cV(e) for each edge e = uv, where u and v are nodes in Vi
* Optimization objective: minimizing the total cost τ of transporting q requests over the graph G

The context builds upon the surrounding discussion on rebalancing strategies, modeling and mathematical frameworks, optimization heuristics, simulation and service design, flexible transport services, ride-sharing systems with meeting points, vehicle rebalancing for mobility-on-demand systems, and reinforcement learning approaches in ridesharing systems.

This chunk is connecting to or building upon the surrounding context by:

* Referencing previous discussions on GTSP, modeling, optimization, and simulations
* Introducing a new instance of calculating cost for transporting passengers with an extra drop-off node
* Providing technical details on graph representation, cost function, and optimization objective

Specific requirements, conditions, or constraints mentioned include:

* The need to calculate the cost of transporting q requests over a specific instance of GTSP
* The use of reinforcement learning approaches in ridesharing systems
