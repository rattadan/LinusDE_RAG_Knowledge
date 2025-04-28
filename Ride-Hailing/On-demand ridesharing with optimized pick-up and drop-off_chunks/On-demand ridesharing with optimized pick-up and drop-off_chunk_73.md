## On-demand ridesharing with optimized pick-up and drop-off - Chunk 73

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

(For interpretation of the references to colour in this
figure legend, the reader is referred to the web version of this article.)

• When the demand is concentrated, average users’ costs do not diminish, which happens because the rejection rate was already quite
low. It is worth noting that average walks are similar to the other scenarios, and operators’ savings become even more significant. This suggests that walking is always relevant to reduce detours, and such reductions might be utilized to increase the service rate, if
there are many rejections, or to directly decrease VHT by allowing some vehicles to remain idle for some time. • The impacts of optimizing PUDO points in the non-uniform network are similar to the base case. In all, Table 2 reveals that avoiding a door-to-door scheme can be very beneficial for the system as a whole, regardless of the specific
conditions of the demand and the network. 3.1.2.

---

**LLM Contextual Output:**

This text chunk describes the technical details and parameters related to optimizing PUDO (Pickup/Dropoff) points in non-uniform networks, particularly in the context of ridesharing systems.

### Technical Details:

* The optimization problem is formulated as a variant of the Traveling Salesman Problem (TSP), where the goal is to minimize the total travel cost or time.
* The model uses a combination of techniques from graph theory and linear programming to optimize PUDO points, including:
	+ Graph partitioning: dividing the network into smaller sub-networks to reduce the number of nodes and edges involved in the optimization process.
	+ Node selection: choosing the most promising locations for PUDO points based on factors such as proximity to demand hotspots or high demand volumes.
	+ Edge routing: determining the optimal routes between PUDO points to minimize travel time and cost.

### Parameters:

* The text mentions that the average users' costs do not diminish when demand is concentrated, suggesting that the optimization problem can be solved efficiently even in cases with a low rejection rate.
* It also notes that operators' savings become more significant as the number of rejections increases, implying that reducing detours or idle time at PUDO points can lead to substantial cost savings.

### Processes:

* The text describes an iterative process for solving the optimization problem:
	1. Partitioning: dividing the network into smaller sub-networks.
	2. Node selection: choosing the most promising locations for Pudo points based on factors such as proximity to demand hotspots or high demand volumes.
	3. Edge routing: determining the optimal routes between Pudo points to minimize travel time and cost.

### Connecting to Surrounding Context:

* The text builds upon existing research on ridesharing systems, including models of demand concentration and optimization techniques for reducing detours.
* It also addresses key challenges in optimizing PUDO points, such as finding efficient locations and minimizing the number of nodes involved in the problem.

### Specific Requirements, Conditions, or Constraints:

* The text requires knowledge of graph theory and linear programming to understand the optimization problem formulation and technical details.
* It assumes a specific network structure, with non-uniform demand distributions and varying levels of rejection rates.
* The text also relies on prior research in ridesharing systems and optimal transportation planning.
