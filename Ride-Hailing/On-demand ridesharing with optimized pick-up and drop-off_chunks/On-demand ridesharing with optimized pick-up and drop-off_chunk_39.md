## On-demand ridesharing with optimized pick-up and drop-off - Chunk 39

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

(10)). If the GV-graph contains all feasible assignments
(which is the case unless some heuristics are used, as discussed in Section 2.4), this ILP represents exactly the optimization problem
underlying AP. Solving the ILP can be more complex than in Alonso-Mora et al. (2017) because allowing walks increases the number of
feasible assignments, i.e., the number of binary variables. In large instances, this is tackled with a heuristic explained in Section 2.4. ∑
∑
min
xτv cost(τ, v) +
zr pKO
(8)
τv∈E(GV)

r∈R

∑∑
s.t. xτv + zr ⩾1, ∀r ∈ R

(9)

τ:r∈τ v

∑
xτv ⩽1, ∀v ∈ V

(10)

τ

(11)

xτv , zr ∈ {0, 1}, ∀τv ∈ E(GV), ∀r ∈ R

After deciding the assignments, i.e. after solving AP, we perform a re-balancing process in order to leave the system better prepared for
the next iteration: Those vehicles that are not moving (i.e., that had no assignments before and neither received one now), are assigned
to the rejected requests, with maximum one request per vehicle.

---

**LLM Contextual Output:**

The current text chunk is explaining how a ridesharing system optimizes its assignments of drivers to passengers using an Graphical Vehicle Routing Optimization (GV-graph) algorithm.

**Technical Details:**

* The GV-graph represents the graph of available locations, which are represented as nodes, and the edges represent possible assignments between drivers and passengers.
* The ILP (Integer Linear Program) model is a mathematical formulation of the optimization problem that aims to minimize the total cost of assigning drivers to passengers while respecting certain constraints.
* The heuristic used in Section 2.4 suggests an approximation algorithm for solving the ILP, which can be computationally expensive.

**Context:**

This text chunk builds upon the surrounding context by providing a detailed explanation of how GV-graph is used to optimize ridesharing assignments. It discusses various aspects of ridesharing systems, including rebalancing strategies, modeling and mathematical frameworks, optimization heuristics, simulation and service design, flexible transport services, ride-sharing systems with meeting points, vehicle rebalancing for mobility-on-demand systems, and reinforcement learning approaches.

**Requirements, Conditions, or Constraints:**

The primary requirement is to optimize ridesharing assignments using an ILP model with a heuristic. The context includes various papers that address challenges in ridesharing systems, such as the use of meeting points and vehicle rebalancing strategies.
