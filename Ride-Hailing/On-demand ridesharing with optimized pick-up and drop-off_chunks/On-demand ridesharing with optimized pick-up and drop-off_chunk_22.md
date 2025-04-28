## On-demand ridesharing with optimized pick-up and drop-off - Chunk 22

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

Walking is assumed to be possible in both directions of each edge with the
same cost. Throughout the paper, we use tV (u1 , u2 ) and tW (u1 , u2 ) to denote the shortest time by vehicle and walking between nodes u1
and u2 . Function tV (e) is assumed to be fixed (i.e., not dependant on the flow over e), meaning that congestion is not included in the
model. The requests of the SMoD are not known beforehand. The system’s aim should be to provide the best level of service throughout the
whole period of operation. However, as the system has to decide how to serve the users as they emerge, the mathematical problem that
needs to be solved has to be posed with partial information. In this paper, we follow the approach of Alonso-Mora et al. (2017),
Simonetto et al. (2019), which assigns a batch4 of users to vehicles at constant times δ (here we use δ = one minute). Requests are
accumulated and removed when picked up by a vehicle or rejected by the system.

---

**LLM Contextual Output:**

The current text chunk describes how the mathematical framework for ridesharing systems is modeled, focusing on key themes such as rebalancing strategies, optimization heuristics, simulation, service design, and flexible transport services.

**Technical details:** The specific parameters mentioned are:

* The time frame considered: a week (one minute) and a month
* The types of requests: batch4
* The approach used for solving the mathematical problem with partial information

**Context connection:** This chunk builds upon the surrounding context by providing an overview of ridesharing research, focusing on various aspects such as rebalancing strategies, modeling and mathematical frameworks, optimization heuristics, simulation and service design, flexible transport services, and ride-sharing systems with meeting points. The text also connects to specific papers discussed in the reference list.

**Requirements and constraints:**

* The system should provide the best level of service throughout the whole period of operation.
* The requests of the SMoD (Social Mobility on Demand) are not known beforehand.
* The system needs to decide how to serve users as they emerge.
* The mathematical problem that needs to be solved has to be posed with partial information.

Overall, this chunk provides a theoretical framework for modeling ridesharing systems and addressing challenges such as rebalancing, optimization, and service design.
