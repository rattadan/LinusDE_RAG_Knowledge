## On-demand ridesharing with optimized pick-up and drop-off - Chunk 33

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

Building the GV-Graph
An edge τv exists in the GV-graph iff the group τ can be served by the vehicle v meeting the following conditions: (i) All users in τ
have enough time to walk towards their pick-up node before the vehicle arrives, (ii) the vehicle’s capacity is never exceeded, and (iii)
the following constraints related to the quality of service are satisfied:
tw (r, τ, v)⩽Ωw , ∀r ∈ τ ∪ Nv

(2)

D(r, τ, v)⩽ΩD , ∀r ∈ τ ∪ Nv

(3)

tia (r, τ, v)⩽Ωa , ∀r ∈ τ, i = O, D

(4)

Where Ωh are some exogenous parameters (h = w,D,a) defining the maximum waiting time, delay and access time, respectively. Note
that Eqs. (2) and (3) are applied to the requests in τ, but also to the requests that are currently being served by v, as new requests might
impose extra detour to the vehicle. Eq. (4) only applies to the new requests, as in our model, to avoid extra-annoyance, the drop-off
point remains unchanged once a passenger has boarded a vehicle (this assumption is discussed and justified further in Section 2.6).

---

**LLM Contextual Output:**

I'll provide a focused analysis of the current text chunk, which appears to be explaining the technical details behind the "GV-Graph" model used in ridesharing systems.

**Technical Details:**

1. The GV-Graph is an undirected graph representing the relationships between vehicles (v) and their associated requests (τ).
2. An edge τv exists in the GV-graph if the group τ can be served by vehicle v, satisfying three conditions:
   a. All users in τ have enough time to walk towards their pick-up node before the vehicle arrives.
   b. The vehicle's capacity is never exceeded.
   c. The following constraints related to the quality of service are satisfied: tw (r, τ, v) ≤ Ωw , ∀r ∈ τ ∪ Nv ; tia (r, τ, v) ≤ Ωa , ∀r ∈ τ, i = O, D ; where Ωh are some exogenous parameters.

**Context and Connection to Surrounding Context:**

1. This chunk is located within a reference list covering ridesharing and mobility-on-demand systems from 2010 to 2020.
2. The surrounding context likely discusses various aspects of these systems, including rebalancing strategies, modeling and mathematical frameworks, optimization heuristics, simulation and service design, flexible transport services, and ride-sharing systems with meeting points.
3. This chunk builds upon the existing context by providing a detailed explanation of the GV-Graph model's technical details.

**Specific Requirements, Conditions, or Constraints:**

1. The parameters mentioned in the text include:
   - Ωw (maximum waiting time)
   - ΩD (maximum delay)
   - Ωa (maximum access time)
2. The conditions and constraints discussed in the chunk relate to ensuring that vehicles can serve groups of requests efficiently, without exceeding capacity or imposing excessive wait times.

Overall, this text chunk provides a technical explanation of the GV-Graph model, its components, and how they work together to support ridesharing systems.
