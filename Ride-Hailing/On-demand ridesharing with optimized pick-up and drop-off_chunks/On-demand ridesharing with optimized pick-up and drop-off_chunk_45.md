## On-demand ridesharing with optimized pick-up and drop-off - Chunk 45

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

• pKO is high enough such that it is never optimal to reject a request (which can be done because we know that the original set-cover
instance is feasible). Therefore, choosing which trips to serve is equivalent to chose which subsets to select. It is straightforward to see that this is indeed a
reduction that preserves the costs of the solutions. 2.3.3. Analysis
The two sub-problems mentioned above that extend set-cover affect the solution procedure in different ways. • The calculation of cost(τ, v) has to be performed for each feasible trip τv. The number of such trips can increase exponentially with
the size of the input (number of requests and vehicles). Therefore, the lack of an efficient optimal algorithm is relevant, and some
heuristics are needed when solving large instances, which is true even if each trip presents a small size (recall that, in theory, it
could be possible to have very large trips, but this is not the usual case and the size of a trip rarely exceeds the capacity of the
vehicles).

---

**LLM Contextual Output:**

This text chunk is describing the process of selecting which rides to serve from a list of requests. Here's a detailed analysis:

**Technical details and parameters:**

* The problem can be modeled as a set-covering problem, where each request corresponds to a subset in the universe.
* The goal is to select the subsets (or trips) that cover all requests while minimizing costs.
* The cost function is given by `cost(τ, v)` for each feasible trip `τv`.
* The size of the input can be large, with thousands of requests and vehicles.

**Connecting to or building upon surrounding context:**

This chunk provides a foundation for further analysis of ridesharing systems. It outlines the basic framework for solving set-covering problems, which are common in optimization and machine learning applications. By extending this problem to include additional challenges (like large input sizes), researchers can investigate how to improve solution procedures.

**Requirements, conditions, or constraints:**

* The calculation of `cost(τ, v)` must be performed for each feasible trip `τv`.
* There is a limit on the number of trips that can be served (due to capacity constraints).
* If each request has only one possible subset (i.e., it's a single-vehicle problem), the cost function becomes trivial and does not need to be optimized.

Overall, this chunk provides a starting point for analyzing the challenges and opportunities in solving set-covering problems in ridesharing systems.
