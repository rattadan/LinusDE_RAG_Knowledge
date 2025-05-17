## On-demand ridesharing with optimized pick-up and drop-off - Chunk 27

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

This approach is actually followed by some carsharing companies. See https://marketplace.uber.com/matching, accessed on 22/10/2020
5
This implies that the possible PUDO points (i.e., the spots in which the vehicles can stop) depend on how one defines the set of nodes. A natural
chance (that we use in the simulations over Manhattan in Section 3.2.2) is considering every corner and dead-end in the city, leading to a very
granular graph. However, this might be different if one wants to consider specialized infrastructure, such as dedicated lanes, where nodes might
better represent the only places the vehicle can stop. 4

5

Transportation Research Part C 126 (2021) 103061

A. Fielbaum et al. Fig. 3. A vehicle that is currently carrying passenger P1 and has already been assigned to serve P2 , following the solid black line.There are two
feasible updated sequences to serve the new request P3 , that are marked in purple: (O2 , D2 , O3 , D3 , D1 ) (top row) or (O2 , D2 , O3 , D1 , D3 ) (bottom row).

---

**LLM Contextual Output:**

This specific text chunk is explaining how the possible PUDO points (i.e., the spots in which the vehicles can stop) depend on the definition of nodes, as mentioned in the carsharing company approach.

Here's a focused analysis:

* The technical details mentioned are: "A natural chance" and "considering every corner and dead-end in the city". This suggests that the authors are using graph theory concepts to model the layout of the city and how vehicles can stop.
* The connection to the surrounding context is that this explanation provides an additional insight into the carsharing company approach, which uses a detailed analysis of the urban layout to optimize ride matching.
* The specific requirements or conditions mentioned include: "A natural chance" (the authors' method for defining nodes), and "considering every corner and dead-end in the city" (the scope of their graph).

In terms of constraints, there are no explicit constraints mentioned in this chunk. However, it's worth noting that the carsharing company approach is based on a detailed analysis of the urban layout, which might limit the possible PUDO points to those that can be realistically reached by vehicles.
