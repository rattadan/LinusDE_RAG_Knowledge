## On-demand ridesharing with optimized pick-up and drop-off - Chunk 50

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

To solve this problem, we keep in memory the best L > 1 solutions when searching in Sp for every p = 1,…,q, and we search in
Sq+1 using all the possible combinations for the previous requests, meaning that we have to compare at most |Sq+1 | ⋅ Lq possible
combinations. For details, see Algorithm 2. In practice, we use L ∈ {2, 3}. Algorithm 2. Optimization of the PUDO points and the vehicle’s route. 1: Z1 = … = Z|τ|− 1 = ∅ %Z will store the L best solutions. 2: forq = 1…|τ|do
3: Compute Sq %The set of feasible sequence and PUDO points for rq , that might be exhaustive or obtained with some heuristic procedures. 4: Define the feasible set of solutions as F = Z1 × … × Zq− 1 × Sq ;
5: ifq = |τ|then
6: Return the best solution in F;
7: else
8: Find the best L solutions in F. Define Zq as the variables corresponding to Sq ;
9: end if
10: end for

2.4.2. Additional heuristics
Besides the previous heuristic (adapted from (Alonso-Mora et al.

---

**LLM Contextual Output:**

Based on the provided text chunk, I will analyze and explain the exact technical details, parameters, or processes described in this chunk:

**Technical Details:**

1. **Algorithm 2:** This is a recursive algorithm for solving the vehicle routing problem with stochastic demand (VRPTSD), which is used to optimize routes for vehicles that need to pick up and deliver customers in a given area.
2. **L > 1:** The algorithm takes L > 1 as an input parameter, where L represents the number of vehicles and riders. This suggests that the algorithm is designed to handle scenarios with multiple vehicles or riders.

**Parameters:**

1. **|τ|:** The size of the transportation network (in this case, τ = |τ|).
2. **L:** The number of vehicles or riders.
3. **Sq+:** The maximum number of possible sequence and PUDO points that can be used in the algorithm.

**Processes:**

1. **Initialization:** The algorithm initializes an empty set `Z` to store the best solutions, which is denoted by `Z0 = ∅`.
2. **Recursive search:** The algorithm iterates over each request (rq) from 1 to |τ|.
3. **Compute feasible sequence and PUDO points:** For each request rq, the algorithm computes the set of feasible sequence and PUDO points that might be used.
4. **Define feasible set of solutions:** The algorithm defines the feasible set of solutions as F = Z0 × … × Zq−1 × Sq, where Q represents the number of requests.
5. **Base case (L=1):** If there are no more vehicles or riders (rq = |τ|), the algorithm returns the best solution in `F`.
6. **Recursive case:** Otherwise, the algorithm finds the best L solutions in `F` and defines `Zq` as the variables corresponding to Sq.

**Additional heuristics:**

The algorithm includes additional heuristics:

1. **Finding the best L solutions:** The algorithm iterates over all possible combinations of sequence and PUDO points for each request rq.
2. **Define Zq:** The algorithm defines `Zq` as the variables corresponding to Sq, indicating that it is used in a recursive manner.

**Context:**

The context of this chunk refers to the problem of optimizing routes for vehicles that need to pick up and deliver customers in a given area, which is known as Vehicle Routing Problem with Stochastic Demand (VRPTSD). The reference list covers various aspects of ridesharing and mobility-on-demand systems, including rebalancing strategies, modeling and mathematical frameworks, optimization heuristics, simulation and service design, flexible transport services, ride-sharing systems with meeting points, vehicle rebalancing for mobility-on-demand systems, and benefits of meeting points in ride-sharing systems.
