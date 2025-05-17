## On-demand ridesharing with optimized pick-up and drop-off - Chunk 63

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

Note that these rules do not apply within a single iteration, so the system will always achieve a better assignment (i.e., it yields a
lower value for the objective function) when walking is admitted because we are enlarging the feasible set of solutions. They are
relevant when chaining consecutive iterations, because without walking there will be some extra degrees of freedom. Therefore, this
design helps us to see if admitting walks improves the system even in such an environment. 3. Numerical simulations
In this section, we run the method over two different scenarios. The first one (Section 3.1) is a toy network, which is useful because
it allows solving the problem without the heuristics, and compare that solution with the ones obtained when the heuristics are used. Therefore, we can study if the heuristics effectively reduce computational time and what is their effect on the quality of the results.

---

**LLM Contextual Output:**

This text chunk provides a detailed analysis of the technical details, parameters, or processes described in it.

The exact technical details mentioned include:

* Mathematical modeling and decomposition methods for ridesharing problems with flexible pickup and delivery locations (Zhao et al., 2018)
* Analysis of benefits of meeting points in ride-sharing systems (Stiglic et al., 2015) and evaluation of the benefits of introducing meeting points into flex-route transit services (Zheng et al., 2019)

The process described is a numerical simulation, where the method is applied to two different scenarios:

1. A toy network scenario: This allows solving the problem without using heuristics, providing insight into whether the use of heuristics effectively reduces computational time and improves the quality of results.
2. Real-world scenarios (Section 3.1): In this section, the method is run on a real-world network to compare solutions obtained with and without heuristics.

The connection between this chunk and the surrounding context is that it builds upon the discussion of rebalancing strategies in ridesharing and mobility-on-demand systems, which was presented earlier (Key Themes: 1. Rebalancing Strategies).

The specific requirements, conditions, or constraints mentioned include:

* Admitting walks to improve system efficiency and user satisfaction
* Utilizing heuristics to reduce computational time
* Studying the impact of heuristics on problem solutions and quality of results

This chunk explains how the numerical simulations will be used to evaluate the effectiveness of different approaches in ridesharing systems.
