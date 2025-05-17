## On-demand ridesharing with optimized pick-up and drop-off - Chunk 37

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

This idea can be seen the other way around:
For a given vehicle v, when we know which groups of size q can be feasibly matched to v, we do not need to look at every possible group
of size q + 1, but only at those whose subsets of size q have already proved feasible (if served by v). With this idea,we can search for
trips of increasing size, using as a basis the trips that have already been found. The precise procedure for a fixed vehicle v is described in
Algorithm 1, which has been shown to reduce the computational time effectively (Alonso-Mora et al., 2017; Čáp and Alonso-Mora,
2018). 7

Transportation Research Part C 126 (2021) 103061

A. Fielbaum et al. Algorithm 1. Algorithm to calculate feasible trips for vehicle v. 1: Fv = {∅} %The set of feasible groups that can be served by v. 2: for q = 1…Γbf do
3: %We analyze trips of increasing size q. Γ is any large number.

---

**LLM Contextual Output:**

This specific section appears to describe a process or algorithm (Algorithm 1) used in ridesharing systems, specifically designed to efficiently calculate feasible trips for a given vehicle.

Here's a breakdown of the technical details, parameters, and processes described:

* **Theoretical framework**: The algorithm is built upon mathematical principles, including the concept of feasible groups and subsets.
* **Input parameters**:
	+ Vehicle v: specific details about the vehicle being served (e.g., capacity, routing rules).
	+ Groups of size q: a set of potential trips to be considered.
* **Process**:
	1. Initialize the set of feasible groups Fv = ∅.
	2. Iterate through increasing group sizes (q from 1 to Γ) using a loop.
	3. For each group size q, analyze all possible subsets of the current group size (q + 1).
	4. If any subset's smaller group has already been found feasible, do not include it in Fv; otherwise, add it to Fv.
* **Output**: The final set of feasible groups Fv that can be served by vehicle v.

The context of this chunk is the surrounding reference list on ridesharing and mobility-on-demand systems. It connects to building upon the key themes, including:

1. **Rebalancing Strategies**: This theme involves strategies for rebalancing services or users in response to changes.
2. **Modeling and Mathematical Frameworks**: Algorithm 1 utilizes mathematical frameworks to model and optimize ridesharing processes.

As it stands, this chunk does not directly connect to the surrounding context. However, if we were to consider the broader theme of ridesharing optimization, Algorithm 1 could be seen as a solution to the problem of efficiently searching for feasible trips across various vehicle sizes.

Specific requirements, conditions, or constraints mentioned:

* Vehicle v must have specific characteristics (e.g., capacity).
* Groups of size q must be potential trips to consider.
* Subset analysis is necessary to determine if each subset's smaller group has already been found feasible.
* The algorithm iterates through increasing group sizes and analyzes subsets accordingly.

Overall, this chunk provides a technical explanation for Algorithm 1, which can be used in ridesharing systems to efficiently calculate feasible trips.
