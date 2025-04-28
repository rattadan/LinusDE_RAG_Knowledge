## On-demand ridesharing with optimized pick-up and drop-off - Chunk 16

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

Let us describe some of the algorithmic ones in more detail, as this is the approach we follow
in this paper: Alonso-Mora et al. (2017) identify the feasible sets of requests that can be matched together and which vehicles can carry
them, to then solve an ILP that decides how to assign them; Simonetto et al. (2019) modify that model by assuming that at most one
new request can be assigned to each vehicle at a time, which reduces the number of feasible combinations and turns the ILP into an LP,
decreasing the computational load; Tsao et al. (2019) focus on edge-flows induced by the vehicles, which makes a problem that can be
computed fast, but managing only vehicles of capacity 2; and Ota et al. (2016) use a greedy algorithm to assign requests to vehicles
sequentially.

---

**LLM Contextual Output:**

This specific text chunk is explaining the technical details behind some algorithmic approaches used in ridesharing systems, specifically in the context of matching requests with available vehicles.

**1. The exact technical details:**

* Alonso-Mora et al. (2017): Identifies feasible sets of requests that can be matched together and which vehicles can carry them.
* Simonetto et al. (2019): Modifies the model by assuming at most one new request can be assigned to each vehicle at a time, reducing the number of feasible combinations.
* Tsao et al. (2019): Focuses on edge-flows induced by the vehicles, making the problem computationally faster but managing only vehicles of capacity 2.

**2. How this chunk connects to or builds upon the surrounding context:**

This chunk is building upon the context provided earlier, which discussed various themes in ridesharing and mobility-on-demand systems, including rebalancing strategies, modeling and mathematical frameworks, optimization heuristics, simulation and service design, flexible transport services, and more. The technical details are presented as solutions to specific challenges identified within this broader context.

**3. Any specific requirements, conditions, or constraints mentioned:**

None specifically mentioned in this text chunk. However, the context provided earlier implies that the reader is expected to have a basic understanding of ridesharing systems and algorithms, with some familiarity with mathematical modeling and optimization techniques.
