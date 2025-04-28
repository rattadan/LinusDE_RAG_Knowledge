## On-demand ridesharing with optimized pick-up and drop-off - Chunk 21

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

Contribution
The main contributions of this paper are threefold: Firstly, we theoretically analyze the advantages and potential of optimizing the
PUDO points in a ridesharing system, and we formulate the associated optimization problem, showing that it contains two subproblems that extend set cover. Secondly, we propose a methodology able to solve this relevant problem over large instances and
run simulations over a real-life study case, showing that the proposed method leads to relevant improvements over the original system
without walking. Finally, we analyze how the quality of service changes in space to understand these emerging SMoD systems better. 4

Transportation Research Part C 126 (2021) 103061

A. Fielbaum et al. 2. An assignment method that allows walking
2.1. The optimization problem
Consider a strongly connected digraph3 G = (𝒱, E). Each arc e has two positive functions tV (e) and tW (e), representing the time
required to cross it over a vehicle and walking, respectively.

---

**LLM Contextual Output:**

The current text chunk is describing a mathematical optimization problem in ridesharing systems. Here's a focused analysis of what this specific section is explaining:

1. **Exact technical details:** The problem statement involves optimizing transportation routes for passengers and vehicles in a system with two subproblems that extend set cover.

Technical Details:
- The problem is formulated as an instance of the 0/1 Knapsack Problem, where each arc e has two positive functions tV (e) and tW (e), representing the time required to cross it over a vehicle and walking.
- The optimization problem aims to minimize the total time spent on transportation, subject to constraints that ensure efficient routing.

2. **Contextual connection:** This chunk builds upon the surrounding context of ridesharing systems, which has been discussed as a key theme in various papers.

Contextual Connection:
The text mentions several papers that have explored the challenges and opportunities in ridesharing systems, including rebalancing strategies, modeling and mathematical frameworks, optimization heuristics, simulation and service design, flexible transport services, ride-sharing systems with meeting points, vehicle rebalancing for mobility-on-demand systems, flex-route services and ride-sharing, and reinforcement learning approaches.

3. **Specific requirements and conditions:** The technical details provided in this chunk do not specify any particular requirements or conditions that need to be met.

Requirements and Conditions:
- None are mentioned.

4. **Conclusions and connections to surrounding context:** This chunk provides a summary of the main contributions of the paper, which summarize threefold: optimizing transportation routes, proposing an assignment method for walking in SMoD systems, and analyzing the impact of quality of service on space.

Connections to Surrounding Context:
The text mentions that this reference list covers a wide range of works from 2010 to 2020, focusing on various aspects of ridesharing and mobility-on-demand systems. This summary highlights the key themes discussed in the surrounding context, including rebalancing strategies, modeling and mathematical frameworks, optimization heuristics, simulation and service design, flexible transport services, ride-sharing systems with meeting points, vehicle rebalancing for mobility-on-demand systems, flex-route services and ride-sharing, and reinforcement learning approaches.
