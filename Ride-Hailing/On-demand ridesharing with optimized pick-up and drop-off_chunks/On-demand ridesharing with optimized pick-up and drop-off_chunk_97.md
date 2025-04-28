## On-demand ridesharing with optimized pick-up and drop-off - Chunk 97

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

Length of the route followed by v to visit the points in Sv . Binary variable that determines if vehicle v is serving group τ. Binary variable that determines if request r is rejected. Cost of rejecting a request. pKO

Parameter of the “Filtering vehicles” heuristic. β
X(u)

Set of walking-neighbours of node u

WD(u)

Set of nodes at walking distance from node u

References
Agarwal, S., Mani, D., Telang, R., 2019. The impact of ride-hailing services on congestion: Evidence from indian cities. Available at SSRN 3410623 (2019). Alonso-Mora, J., Samaranayake, S., Wallar, A., Frazzoli, E., Rus, D., 2017. On-demand high-capacity ride-sharing via dynamic trip-vehicle assignment. Proc. Natl. Acad. Sci. 114 (3), 462–467. Alonso-Mora, J., Wallar, A., Rus, D., 2017. Predictive routing for autonomous mobility-on-demand systems with ride-sharing. In: 2017 IEEE/RSJ International
Conference on Intelligent Robots and Systems (IROS) (Sept. 2017), pp. 3583–3590. Badia, H., Estrada, M., Robusté, F., 2014.

---

**LLM Contextual Output:**

**Analysis of the Text Chunk:**

The given text chunk describes a specific algorithm or process for routing vehicles in a ridesharing system, which is built upon various technical parameters and processes. Here's a breakdown of the exact technical details, parameters, or processes described in this chunk:

1. **Binary variable**: `pKO` ( rejected requests) - This indicates that the chunk is describing an optimization heuristic used to determine whether a request should be accepted or rejected.
2. **Parameter β**: The parameter `β` likely represents the threshold value for determining when to reject a request based on cost, which is crucial in ridesharing systems where vehicle costs may vary.
3. **Set of walking-neighbours X(u)** and **WD(u)**: These variables represent the sets of nodes at walking distance from node u (X(u)) and the set of nodes at walking distance from node u (WD(u)), respectively.

**Connection to or Building upon Surrounding Context:**

This chunk connects to and builds upon the surrounding context by:

1. Providing technical details on algorithms used for routing vehicles in ridesharing systems.
2. Discussing various mathematical frameworks and optimization heuristics employed in these systems.
3. Highlighting the importance of reinforcement learning approaches and benefits of meeting points.

**Requirements, Conditions, or Constraints:**

No specific requirements, conditions, or constraints are mentioned in this chunk. However, it is implied that:

1. The algorithm should be efficient to handle large numbers of requests and vehicle positions.
2. The system should be able to accommodate a wide range of walking distances between nodes.
3. The rejection decision should be based on a cost-related criterion.

**Focused Analysis:**

This section provides a detailed description of the technical parameters, processes, and algorithms involved in routing vehicles in ridesharing systems. It highlights various approaches used for optimization and reinforcement learning, and emphasizes the importance of meeting points in improving efficiency and user satisfaction.
