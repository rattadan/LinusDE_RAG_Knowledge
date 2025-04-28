## On-demand ridesharing with optimized pick-up and drop-off - Chunk 54

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

Instead of trying all possible (i, j) combinations, we only look at one ji for
each i, where ji is calculated through a local search: assuming no walking for this search, we start from ji = i +1 (i.e., dropping-off
right after picking up), and we increase ji only if it is feasible and if it makes the total cost to decrease. To understand this heuristic better, it is worth noting that we can express ji as follows:
′

′

′

ji = max{j > i : ∀j = i + 1, …, j, cost(r, v, i, j , or , dr ) < cost(r, v, i, j − 1, or , dr )}
j

This procedure is detailed in Algorithm 3. • Searching for PUDO nodes: We want an algorithm that can be used over very granular graphs, i.e., where nodes can be placed
close to their neighboring nodes. Although Eq. (4) limits the number of nodes that can be used as pick-up or drop-off points, this
number will still be high in detailed graphs.

---

**LLM Contextual Output:**

This specific section is explaining a technical detail within the context of ridesharing and mobility-on-demand systems.

The exact technical details described are:

1. **Heuristic Optimization**: The use of a local search algorithm to optimize ride-sharing schedules.
2. **Feasible Checking**: The process of determining whether it is feasible to assign a passenger to a particular vehicle (ji) at time step i, based on the current state of the system and the constraints imposed by the available vehicles and their locations.

This connection builds upon the surrounding context:

1. **Ridesharing Systems**: The section discusses ridesharing systems and mobility-on-demand services.
2. **Ride-Sharing Problems**: It addresses specific challenges in ride-sharing problems, such as optimizing schedules and assigning passengers to vehicles.
3. **Optimization Heuristics**: The inclusion of optimization heuristics like the one described indicates an attempt to solve complex optimization problems.

The specific requirements and conditions mentioned are:

1. **Feasibility Checking**: Ensuring that a given assignment is feasible (i.e., not violating any constraints).
2. **Local Search Algorithm**: Using a local search algorithm to explore the solution space and find good approximations.
3. **Granular Graphs**: Working with very granular graphs, where nodes can be placed close to their neighboring nodes.

Overall, this section provides a technical explanation of how ridesharing systems are optimized using heuristic optimization techniques.
