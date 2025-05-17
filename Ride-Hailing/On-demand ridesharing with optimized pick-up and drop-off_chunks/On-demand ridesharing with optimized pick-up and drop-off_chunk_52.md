## On-demand ridesharing with optimized pick-up and drop-off - Chunk 52

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

More
precisely, for each request r we consider the set of vehicles that can serve it, denoted Vr , and we discard rv arcs for those v ∈ Vr that
fulfill cost(r, v) > mean{cost(r, u) : u ∈ Vr } +β ⋅ std{cost(r, u) : u ∈ Vr } (std stands for standard deviation, and β is a parameter of the
heuristic), unless v cannot serve any other request, to prevent that discarding these arcs increases the number of rejected requests. Recall that in Algorithm 1 we search for feasible groups of increasing size, so limiting those groups of size 1 has a relevant impact: if
the arc rv is discarded, then no group containing r will be linked to v. 10

Transportation Research Part C 126 (2021) 103061

A. Fielbaum et al. To understand this heuristic better, it is useful to consider the example given by Table 1, that depicts the costs of all the trips
including passenger A without (top matrix) or with (bottom matrix) using this heuristic, using β = 1.

---

**LLM Contextual Output:**

This specific text chunk describes a transportation optimization process within ridesharing systems.

**Technical Details:**

* The process involves discarding arc requests that fulfill certain conditions, including:
	+ Cost(r, v) > mean{cost(r, u) : u ∈ Vr } +β ⋅ std{cost(r, u) : u ∈ Vr }
	+ If a discarded arc, no group containing r will be linked to v
* The goal is to find feasible groups of increasing size that can serve requests without increasing the number of rejected requests

**Context and Connection:**

This process is part of a broader set of transportation optimization techniques used in ridesharing systems. The context provided earlier suggests that this specific chunk is related to A. Fielbaum et al.'s "Transportation Optimization" work, which likely discusses similar methods for optimizing transportation networks.

The connection to the surrounding text can be inferred through the mention of various papers and themes mentioned (e.g., rebalancing strategies, modeling and mathematical frameworks, optimization heuristics) that are relevant to ridesharing systems. The specific chunk focuses on a specific technique used in these systems.

**Requirements, Conditions, or Constraints:**

* The process assumes availability of arc requests with their respective costs and the ability to calculate standard deviations
* The heuristic has a fixed parameter β that controls the trade-off between the cost of discarding an arc request and the potential benefits of including it in a group
* The process may require adjustments to be made based on the specific characteristics of the transportation network (e.g., demand, capacity) and the quality of the arcs

In summary, this chunk describes a transportation optimization technique used in ridesharing systems that involves discarding arc requests based on certain conditions. It is connected to broader themes discussed earlier and assumes availability of relevant data and parameters.
