## On-demand ridesharing with optimized pick-up and drop-off - Chunk 48

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

In the top matrix, request A can be served by four vehicles. In the bottom matrix, the trip (A, v4 )
is erased (marked as red) because it is too costly, which discards automatically any assignment between v4 and any group containing A. Groups
Vehicles

{A}

{A, B}

{A, C}

{A, B, C}

v1

1

1.5

1.7

2

v2

1.5

–

–

–

v3

1

–

1.8

–

2

2.2

2.1

2.6

v4

Groups
Vehicles

{A}

{A, B}

{A, C}

{A, B, C}

v1

1

1.5

1.7

2

v2

1.5

–

–

–

v3

1

–

1.8

–

2

–

–

–

v4

2.4.1. Optimization of the sequence and the PUDO points
In order to reduce the time required to compute cost(τ,v), we do not perform an exhaustive search to calculate the sequence, but we
use a so-called insertion heuristic, that adapts to the allowing-walks case the heuristic used by Alonso-Mora et al. (2017) when solving
larger instances. An insertion heuristic means that the requests in τ will be inserted one by one into the vehicle (in some arbitrary
order).

---

**LLM Contextual Output:**

This text chunk describes an optimization approach for scheduling vehicles to reduce travel time and costs.

**Technical Details:**

* The context is ridesharing and mobility-on-demand systems, where vehicles are used to transport passengers between locations.
* The optimization goal is to minimize the total travel time (τ) and cost for all requests.
* A heuristic approach is adopted, which involves inserting individual requests into a vehicle in an arbitrary order.

**Context Connection:**

This chunk builds upon the surrounding context by explaining how request A can be served by four vehicles. The top matrix illustrates the available options for each request (A), with the trip being erased due to its high cost.

The subsequent lines describe the optimization approach:

1. An insertion heuristic is used, which adapts to the allowing-walks case.
2. The algorithm selects requests in an arbitrary order by inserting them one by one into a vehicle.
3. This approach aims to reduce the time required for computing the sequence of vehicles and points.

**Requirements and Conditions:**

* The problem statement involves minimizing travel time (τ) and cost for all requests.
* The optimization goal is achieved through an insertion heuristic, which adapts to specific cases (allowing-walks).
* The algorithm selects requests in an arbitrary order by inserting them into a vehicle.

Overall, this chunk provides insight into a practical optimization approach for scheduling vehicles in ridesharing systems, highlighting the importance of adaptability and flexibility.
