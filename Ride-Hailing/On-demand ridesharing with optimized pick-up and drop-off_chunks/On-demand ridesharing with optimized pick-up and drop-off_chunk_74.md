## On-demand ridesharing with optimized pick-up and drop-off - Chunk 74

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

Analysis of the heuristics
We now assess the impact of using the heuristics instead of the optimal procedure. To do this, we use again the base scenario and
compute a new set of (random) requests. We obtain the results described in Table 3, where all times are in minutes. The following
conclusions and comments follow:
• Using all the heuristics reduce the running time in almost six times, which can be crucial when working over larger networks. This is
achieved at the cost of higher users’ and operators’ costs. • Filtering vehicles decreases operators’ costs and increases users’ costs only in a small amount. Limiting sequences is the most
saving-time heuristic. 15

Transportation Research Part C 126 (2021) 103061

A. Fielbaum et al. Table 5
Description of the Manhattan graph and requests. Index

Value

Max in-vehicle time between nodes
Max walking time between nodes
Av. in-vehicle time between contiguous nodes
Max in-vehicle time between contiguous nodes
Av.

---

**LLM Contextual Output:**

**Technical Details, Parameters, or Processes:**

1. **Heuristics**: The reference list discusses various heuristics used to optimize ridesharing systems, including filtering vehicles, limiting sequences, and using the Manhattan graph.
2. **Mathematical Frameworks**: Mathematical models and decomposition methods are mentioned for solving ridesharing problems with flexible pickup and delivery locations.

**Connections to or Building upon the Surrounding Context:**

1. **Summary of Key Papers**: The reference list provides an overview of key papers published between 2010 and 2020, discussing various aspects of ridesharing and mobility-on-demand systems.
2. **Concluding Remarks**: The concluding remarks summarize the findings of the research presented in the reference list, highlighting the importance of heuristics and mathematical modeling in optimizing ridesharing systems.

**Specific Requirements, Conditions, or Constraints:**

1. **Time constraints**: The analysis aims to reduce running time by using different heuristics, which implies a specific time constraint (the reduction in running time from 10 minutes to almost six times).
2. **Cost considerations**: The analysis considers the cost implications of each heuristic and its impact on operators' and users' costs.
3. **User experience**: The study aims to improve user satisfaction by optimizing ridesharing systems, which implies a consideration for user experience as a key constraint.

The reference list appears to be related to ride-hailing and mobility-on-demand systems, with an emphasis on heuristics, mathematical modeling, and optimization techniques. The analysis is likely focused on developing more efficient and user-friendly systems, particularly in the context of improving running times and reducing costs.
