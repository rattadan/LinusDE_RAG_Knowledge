## On-demand ridesharing with optimized pick-up and drop-off - Chunk 51

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

(2017)), we propose three additional ones, that are used in
different steps of the optimization process and pursuing specific targets: reducing the number of trips (“Filtering vehicles”), hastening
the definition of the sequence in which the requests are served (“Limiting sequences”), and hastening the definition of the PUDO points
(“Searching for PUDO nodes”), respectively. The last two heuristics build the set Sq+1 just explained in Algorithm 2. The performance of
these heuristics is shown in Section 3.1. • Filtering vehicles: The GV-Graph is supposed to include all feasible trips, but this could be a huge set, requiring a very long time to
be computed. To face this, we discard some feasible arcs in the GV-graph that link single-request groups with vehicles.

---

**LLM Contextual Output:**

This text chunk is explaining three specific technical details or processes related to ridesharing and mobility-on-demand systems:

1. **Filtering Vehicles**: This process involves discarding certain feasible trips from a larger set of all possible trips, which can be computationally expensive.
2. **Limiting Sequences**: This heuristic aims to limit the number of requests served in a sequence by defining specific targets for reducing the number of trips or improving service efficiency.
3. **Searching for PUDO Nodes**: This heuristic is used to find specific nodes (PUDO points) in the transportation network that are relevant to the optimization process.

These processes are built upon and connect to the surrounding context in several ways:

* The text mentions the overall theme of rebalancing strategies, modeling, and optimization heuristics discussed in the reference list.
* The technical details are presented within the context of a specific research proposal or problem statement (Section 1.2) that outlines goals for improving ridesharing systems.
* The text also provides a summary of key papers related to these topics, highlighting their relevance to the overall theme.

The required constraints and conditions mentioned in this chunk include:

* The need for efficient computational processes, particularly for filtering feasible trips.
* The importance of optimizing ride-sharing systems by reducing unnecessary requests or improving service efficiency.
* The use of mathematical models and simulation techniques to analyze ridesharing problems.
* The relevance of heuristic optimization methods to addressing specific challenges in the problem statement.
