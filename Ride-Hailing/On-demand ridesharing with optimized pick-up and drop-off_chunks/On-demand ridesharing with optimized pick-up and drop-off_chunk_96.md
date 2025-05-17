## On-demand ridesharing with optimized pick-up and drop-off - Chunk 96

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

V = {v1 , …, vm }

Set of vehicles. Pv

Current position of vehicle v. Capacity of vehicle v. νv

Nv

Set of requests currently being served by vehicle v. Sv

Set of future stops of vehicle v. VHT
AP
𝒜

“Vehicles-Hour-Traveled”
“Assignment Problem”
Set of feasible assignments between the sets of requests and vehicles. R0

Previous requests that are currently being served by the system. cU

Users’ costs. cO

Operators’ costs. GV
T
tw

Requests-Groups-Vehicles graph. Set of feasible groups. Waiting time

tv

In-vehicle time

ta

Access time

th (r, v, i, j, o, d)

h-time of r if served by v, inserted in the sequence in (i, j), PUDO points (o, d) (h = w, v, a). D
Ωh

Delay. Maximum admissible h-time (h = w, v, a). th (r, τ, v)

h-time of r ∈ τ if the group τ is served by v (h = w, v, a). ph

Users’ perceived cost of one unit of time in state h (h = w, v, a). Δth
c0

L(Sv )
xτv
zr

Increase in h-time (h = w, v, a). Operators’ cost of one vehicle moving during one minute of time.

---

**LLM Contextual Output:**

This text chunk is analyzing the technical details and parameters associated with ridesharing systems.

Here's a focused analysis:

1. **Exact technical details**: The chunk discusses various mathematical concepts, such as:
   - Mathematical modeling for ridesharing problems with flexible pickup and delivery locations (Zhao et al., 2018)
   - Decomposition methods for ridesharing problems (Vosooghi et al., 2019)

2. **Parameters or processes described**: This chunk highlights the parameters used in ridesharing optimization heuristics, such as:
   - Assignment problem parameters (cU) and operators' costs (GV)
   - Vehicle capacity (νv), request groups (R0), previous requests (cU), users' costs (cO), and operators' costs ( GV)

3. **Context connections**: This chunk is building upon the surrounding context, which discusses various aspects of ridesharing and mobility-on-demand systems.

4. **Requirements, conditions, or constraints**: The text mentions specific requirements related to ridesharing systems, such as:
   - Meeting points for improving efficiency and user satisfaction
   - Reinforcement learning approaches for managing dynamic systems

The chunk is providing an in-depth analysis of the technical details associated with ridesharing systems, highlighting key concepts and parameters used to model and optimize these systems.
