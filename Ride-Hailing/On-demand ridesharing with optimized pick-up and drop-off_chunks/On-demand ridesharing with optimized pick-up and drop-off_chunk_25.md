## On-demand ridesharing with optimized pick-up and drop-off - Chunk 25

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

The set of previous requests currently being served by the system is denoted by
R0 . We aim to find an assignment that minimizes the resulting total costs, defined as the sum of users’ costs cU for new passengers
(including the costs of being rejected), the extra users’ costs ΔcU for previous passengers induced by new detours, and the operators’
costs cO due to the new routes. Walking costs are included in cU . ∑
∑
min cU (r, A) +
ΔcU (r0 , A) + cO (A)
(1)
A∈𝒜,

r∈R

r0 ∈R0

2.2. The solution method
We now explain how do we solve AP (Problem 1), together with the specific model we consider, i.e., which are the operational
constraints and how do we compute users’ and operators’ costs. We build upon the method proposed by Alonso-Mora et al. (2017) and
adapt it to include the possibility of walking. We now describe the main changes, which we explain in detail in the upcoming
subsections. The most relevant changes relate to the identification of feasible assignments between groups of users and vehicles.

---

**LLM Contextual Output:**

This text chunk describes a mathematical optimization problem related to ridesharing systems, specifically how to assign riders to drivers based on their availability and preferences.

Here's a focused analysis of what this specific section is explaining:

1. **Technical details**: The chunk mentions the following technical details:
	* The objective function cU (r, A) represents the total cost for an assignment r, including users' costs cU, extra users' costs ΔcU, and operators' costs cO.
	* The constraint ∑∑min cU (r, A) + ΔcU (r0 , A) + cO (A) indicates that the total cost of the assignment should be minimized for all possible assignments r and routes r0.
2. **Context**: The context provided is a ridesharing system with various challenges and opportunities, including:
	* Optimization problems: The goal is to find an optimal solution that minimizes costs while satisfying operational constraints.
	* Mathematical frameworks: The problem involves mathematical modeling and decomposition methods for ridesharing problems with flexible pickup and delivery locations.
3. **Connection to surrounding context**: This chunk builds upon the broader context of the reference list, which discusses various aspects of ridesharing and mobility-on-demand systems.

Specific requirements, conditions, or constraints mentioned:

* Operational constraints: The problem assumes that users' availability and preferences are already known and factored into the assignment decision.
* Mathematical modeling methods: The solution method involves adapting a previous approach proposed by Alonso-Mora et al. (2017) to include walking costs.
* Feasible assignments: The chunk mentions identifying feasible assignments between groups of users and vehicles, which is a crucial aspect of optimization problems in ridesharing systems.

Overall, this chunk provides technical details about the mathematical optimization problem at hand, connects it to broader context, and outlines the specific requirements and constraints involved.
