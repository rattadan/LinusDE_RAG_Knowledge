## On-demand ridesharing with optimized pick-up and drop-off - Chunk 23

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

We aim for an optimal assignment for that set of
requests, although heuristics will be needed in practice, as we show. Formally, we have a set of requests R = {r1 ,…,rn }, each one being a 4-tuple r = (or ,dr ,trr ,kr ), representing its origin, destination,
exact time of request, and number of passengers, respectively. Origins and destinations are assumed to be placed on the nodes of the
graph5. These requests have to be assigned to a set of vehicles V = {v1 , …, vm }, each one characterized by its current position Pv , a
capacity νv , a set of requests currently being served by the vehicle Nv , and a set of future stops Sv that the vehicle must visit, corre­
sponding to either pick-ups or drop-offs of the requests in Nv . The objective is to match requests together and with the vehicles,
providing good quality of service while restraining operators’ costs.

---

**LLM Contextual Output:**

**Technical Details, Parameters, or Processes:**

* A set of requests R = {r1 ,…,rn }, each one being a 4-tuple r = (or ,dr ,trr ,kr ), representing its origin, destination, exact time of request, and number of passengers, respectively.
* Graph5 representing the graph of origins and destinations.
* Vehicles V = {v1 , …, vm } with characteristics such as current position Pv , capacity νv , set of requests currently being served by each vehicle Nv , and set of future stops Sv .

**Context:**

The given text chunk appears to be part of a document that covers ridesharing and mobility-on-demand systems. The reference list provided at the beginning provides an overview of key themes, models, optimization heuristics, simulation, and service design approaches related to these systems.

In this specific context, the current text chunk is describing how to assign requests to vehicles in order to provide good quality of service while restraining operators' costs. This process involves matching requests together with available vehicle capacities, taking into account both the request's origin and destination (or pick-up/drop-off locations) as well as the number of passengers.

This process can be seen as a specific implementation or algorithm for the broader theme of optimization in ridesharing systems, where heuristics may also play a role to balance operator efficiency with user satisfaction. The technical details described in this chunk are fundamental to the operational functioning of such systems and highlight the importance of mathematical modeling and simulation techniques in optimizing their performance.

**Connections to or Building upon the Surrounding Context:**

* This chunk builds upon the theme of optimization heuristics discussed earlier, which was introduced in a separate section (Key Themes).
* The technical details described here are crucial for understanding how requests are matched with available vehicles, highlighting the importance of mathematical modeling and simulation techniques.
* The process outlined is also relevant to service design approaches mentioned later in the reference list.

**Requirements, Conditions, or Constraints:**

* Operators' costs being restrained through optimization algorithms.
* Good quality of service provided while considering request characteristics such as origin and destination locations, number of passengers, and vehicle capacities.
