## On-demand ridesharing with optimized pick-up and drop-off - Chunk 36

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

These strategies are studied in more detail in Fagnant and Kockelman (2018), Daganzo and Ouyang (2019), Čáp and
Alonso-Mora (2018), among others. The number of possible trips can be large. In principle, it can be as high as O(m ⋅ nρ ), with ρ the size of the largest feasible group,
which might be larger than vehicles’ capacities. Therefore, the computation of the GV-graph can represent a burden for the whole
solution method. In order to face this issue, we take advantage of the intuitive Lemma 1, which is also used (and proven) in AlonsoMora et al. (2017), Čáp and Alonso-Mora (2018). As they explain, the set of trips has a structure that can be exploited to make an
efficient computation of the GV-graph. Lemma 1. Let τ ⊆τ. If τv is an arc in the GV-graph, then τ v also is. ′

′

Lemma 1 entails that for a trip to be feasible, each “subtrip” must be feasible as well.

---

**LLM Contextual Output:**

**Technical Details and Parameters:**

The technical details described in this chunk are:

* The formulation of Lemma 1, which states that if a trip τ ⊆τ is feasible (i.e., it has no restrictions), then its subtrips τv also have feasibility.
* The use of "subtrip" to denote an intermediate segment of a larger trip.

**Processes and Connections:**

This chunk builds upon the surrounding context by:

* Referencing previous papers on ridesharing and mobility-on-demand systems, such as Fagnant and Kockelman (2018) and Daganzo and Ouyang (2019), indicating that these strategies are studied in more detail.
* Providing a summary of key papers on ridesharing problems with flexible pickup and delivery locations, including Zhao et al. (2018) and Stiglic et al. (2015).
* Highlighting the importance of meeting points in ride-sharing systems, as emphasized by Zheng et al. (2019).

**Requirements and Constraints:**

There are no specific requirements or constraints mentioned in this chunk.

The context is a reference list covering various aspects of ridesharing and mobility-on-demand systems, with a focus on rebalancing strategies, modeling and mathematical frameworks, optimization heuristics, simulation and service design, flexible transport services, ride-sharing systems with meeting points, vehicle rebalancing for mobility-on-demand systems, flex-route services and ride-sharing, reinforcement learning approaches, and benefits of meeting points in ride-sharing systems.
