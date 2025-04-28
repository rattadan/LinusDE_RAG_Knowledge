## On-demand ridesharing with optimized pick-up and drop-off - Chunk 38

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

4: Compute the set Gv,q = {τ⊆R, |τ| = q : ∀r ∈ τ, τ⧹{r } ∈ Fv } %Gv,q contains the groups τ that might be feasible according to the feasible groups of size q − 1. 5: if Gv,q = ∅then
6: Break; %Stop when no new trips are found. 7: end if
8: for allτ ∈ Gv,q do
9: if cost(τ, v) < ∞then Fv ← Fv ∪ τ
10: end if
11: end for
12: end for
′

′

2.2.3. Exact ILP formulation of the Assignment Problem AP
Once the GV-graph has been obtained, we proceed exactly as Alonso-Mora et al. (2017), i.e., we solve the integer linear problem
described by Eqs. (8)–(11), minimizing the sum of the costs of the selected τv arcs (trips) plus a penalization pKO for each unassigned
request. This is represented by Eq. (8), in which a binary variable xτv is equal to 1 if the group τ is assigned to the vehicle v, and a binary
variable zr is equal to 1 if r is rejected. Each unassigned request is marked as rejected (Eq. (9), that will be an active constraint for any
optimal solution), and each vehicle is assigned to not more than one trip (Eq.

---

**LLM Contextual Output:**

This specific text chunk appears to be explaining the exact technical details, parameters, or processes described in the document about ridesharing and mobility-on-demand systems. Here's a focused analysis of what this section is explaining:

**Exact ILP formulation of the Assignment Problem AP**: The chunk describes the process of formulating an Integer Linear Program (ILP) for solving the Assignment Problem (AP). This involves creating a graph representation, which includes nodes or groups (GV-graph) and edges between them (τ⊆R), where τ represents feasible groups. The ILP aims to minimize the sum of costs assigned to selected trips (τv arcs) while penalizing rejected requests (unassigned request).

**Key components:**

1. **Computing GV-queue**: The chunk mentions computing the set Gv,q, which contains all feasible groups τ that might be assigned to vehicle v.
2. **Breaking and end-of-loop conditions**: It outlines a termination condition for breaking when no new trips are found in the queue (τ∈Gv,q).
3. **Assignment process**: For each feasible group τ, it checks if the cost of assigning τv is less than infinity. If so, the assignment is added to the solution set Fv.

**Connection to surrounding context:**

This chunk builds upon and extends the concepts introduced in the previous sections, which focus on rebalancing strategies, modeling and mathematical frameworks, optimization heuristics, simulation and service design, flexible transport services, ride-sharing systems with meeting points, vehicle rebalancing for mobility-on-demand systems, and reinforcement learning approaches.

**Requirements and conditions:**

The ILP formulation is a specific method used to solve the Assignment Problem. To use this approach, one would need:

* A feasible group (GV) graph representing the possible assignments
* Binary variables xτv (assignment status) indicating whether each trip τv is assigned to vehicle v
* Integer coefficients for penalties and costs
* A termination condition for breaking when no new trips are found

Overall, this chunk provides a technical foundation for solving Assignment Problems in ridesharing and mobility-on-demand systems.
