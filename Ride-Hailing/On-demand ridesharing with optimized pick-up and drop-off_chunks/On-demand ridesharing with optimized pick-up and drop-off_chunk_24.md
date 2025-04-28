## On-demand ridesharing with optimized pick-up and drop-off - Chunk 24

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

That is to say, to minimize the number of rejected requests and the
expected waiting, walking, and travel times for the accepted ones, with low VHT (vehicles-hours-traveled). Note that VHT can also be
interpreted as the impact on congestion. Operating the SMoD system throughout the day requires solving this assignment problem (AP) many consecutive iterations. AP
inputs are the graph, the requests R (that can include some previous requests that are not on-board yet so that they might be reas­
signed), and the fleet V. AP outputs an assignment, i.e., a set of tuples (v,T, π ), meaning that the set of requests Nv assigned to vehicle v now includes those
in T (hence T⊆R) and its updated route is π . A feasible assignment must never exceed a vehicle’s capacity and cannot allocate a single
vehicle to more than one tuple. Additional constraints (e.g., dealing with the quality of service) might be considered. Let us denote by 𝒜 the set of all feasible assignments.

---

**LLM Contextual Output:**

This specific section provides detailed technical details on solving the Assignment Problem (AP), which is a fundamental problem in operations research and optimization.

**Exact Technical Details:**

1. **Assignment Problem:** The AP is a classic problem that involves assigning requests to vehicles (represented as nodes) such that the total distance traveled by each vehicle remains within its capacity, and no two requests are assigned to the same vehicle.
2. **Graph:** The AP input is represented as a graph, where nodes represent vehicles, and edges represent request-vehicle relationships.
3. **Request Graph (R):** Requests R are input to the AP, which include tuples of (v, T, π), where v represents an available vehicle, T represents requests in T, and π represents the updated route.
4. **Vehicle Capacity:** V is the capacity constraint for each vehicle.
5. **Max Flow:** The AP outputs a set of tuples (v, T, π ), meaning that all requests are assigned to vehicles such that no two requests overlap and their total distance traveled by each vehicle remains within its capacity.

**Connecting this section to the surrounding context:**

This technical detail is crucial for understanding how ridesharing systems optimize routes and assign users to available vehicles. The AP is a key component in solving this optimization problem, ensuring efficient use of resources (vehicles) and minimizing travel times.

The AP inputs are also related to the broader theme of optimizing ride-sharing systems, where managing requests, vehicle capacities, and user satisfaction are critical factors.

**Building upon the surrounding context:**

This technical detail serves as a foundation for understanding more advanced concepts in optimization, such as reinforcement learning (RL) approaches. RL is used to optimize complex systems like ridesharing by incorporating dynamic pricing, time-of-day variations, and other real-world factors into the problem-solving process.

The AP's limitations (e.g., dealing with quality of service constraints) also highlight the need for integrating additional constraints and complexities in ridesharing optimization.

**Requirements and conditions:**

1. **Computational complexity:** The AP is typically solved using approximation algorithms or heuristics, which have a lower computational complexity compared to exact solutions.
2. **Scalability:** The AP needs to be able to handle large numbers of requests, vehicles, and time intervals (e.g., day).
3. **Real-time constraints:** The system must handle real-time updates in request availability, vehicle capacities, and route changes.

By understanding the technical details behind solving the Assignment Problem, researchers and practitioners can design more efficient ridesharing systems that balance user satisfaction with resource optimization, while also accounting for real-world complexities and constraints.
