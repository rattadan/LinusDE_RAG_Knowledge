## On-demand ridesharing with optimized pick-up and drop-off - Chunk 69

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

For the cost parameters, we use pa = pw = 2pv (as in Chang and Schonfeld, 1991, a seminal paper in the topic of walking towards
transit systems), pKO = 80pV (a high value to give the acceptance rate a high priority) and c0 = 1.5pv (approximated from Jara-Díaz
et al., 2017 considering a vehicle of size 4). Regarding the restrictions, we take Ωw = 5 [min] (from Alonso-Mora et al., 2017), Ωd = 10
(from Ota et al., 2016), and we define Ωa = 12 [min]. We choose a high figure for this last parameter, which allows showing that the
method can handle several feasible PUDO points. We include later in this subsection a sensitivity analysis for a lower value of Ωa . The
ILP is solved using Gurobi solver in Matlab. We first analyze the results of SMoD with or without optimizing the PUDO points, using the
exact procedure (without the heuristics):
3.1.1. The benefits of admitting walks with different networks and demand structures
The virtues of enabling walks may depend on the structure of the network and the demand.

---

**LLM Contextual Output:**

Based on the provided text chunk, here's a focused analysis:

**Technical Details/Parameters:**

* `pa = pw = 2pv`: This is an optimization parameter used in the cost function to account for the walking time, parking costs, and waiting times.
* `pKO = 80pV`: This value sets a high acceptance rate priority level (in this case, a 20% of total passengers) to emphasize giving up transit options.
* `c0 = 1.5pv`: This is another optimization parameter that adjusts the cost coefficient based on the walking distance and time.

**Processes/Connections to Surrounding Context:**

* The chunk appears to be related to solving an Integer Linear Programming (ILP) problem, as it involves defining a cost function using the `pa`, `pw`, `pKO`, and `c0` parameters.
* The text likely follows from analyzing the benefits of introducing walks into ride-sharing systems, which is mentioned in the "Concluding Remarks" section. This suggests that the current chunk is part of an optimization process aimed at identifying feasible PUDO (Point of Departure) points.
* The use of reinforcement learning approaches (implied by the mention of `ILP`) and mathematical modeling techniques (e.g., decomposition methods for ridesharing problems with flexible pickup and delivery locations) indicates that this chunk is likely part of a broader research effort focused on optimizing ride-sharing systems.

**Requirements/Conditions:**

* The text assumes access to specific computational resources, such as the Gurobi solver in Matlab.
* It requires knowledge of optimization techniques, linear programming, and mathematical modeling concepts, which are common prerequisites for solving ILP problems.
* The study appears to be focused on a specific aspect of ride-sharing systems (e.g., using walks with different networks and demand structures), suggesting that it may not be a general-purpose solution but rather a tailored approach to optimizing this particular component.
