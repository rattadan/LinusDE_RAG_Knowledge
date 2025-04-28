## On-demand ridesharing with optimized pick-up and drop-off - Chunk 40

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

These vehicles are not actually picking up those requests (which have
already been removed from the system). They are being directed from a zone in which there was oversupply of vehicles -which is why
they were idle- towards zones in which there was lack of available vehicles -which is why there were rejected requests-. To do this, we
solve the same linear program proposed in Alonso-Mora et al. (2017). Note that walking plays no role here, which is why we can use
the rebalancing process from Alonso-Mora et al. (2017) directly. 2.3. Mathematical complexity
In this subsection, we analyze the complexity that is entailed by optimizing the assignments jointly with the PUDO nodes, by
showing that the respective optimization problem contains two sub-problems that extend set-cover.

---

**LLM Contextual Output:**

The current text chunk focuses on the mathematical framework and optimization processes related to ridesharing systems.

**Exact technical details:**

* The system is optimized using linear programming.
* Specifically, it involves solving a PUDO (Public-Private Data Object) problem, which requires finding the optimal assignments of requests to vehicles while considering the availability of vehicles in different zones.
* Two sub-problems are identified that extend set-cover, suggesting an involved process for determining valid solutions.

**Connecting to or building upon the surrounding context:**

This chunk connects to the broader discussion on rebalancing strategies and modeling mathematical frameworks in ridesharing systems. It builds upon previous work by Alonso-Mora et al. (2017) and Zhao et al. (2018), which addressed similar topics, such as vehicle rebalancing and optimization heuristics.

**Specific requirements, conditions, or constraints:**

* The system must be designed to handle oversupply of vehicles in one zone and lack of available vehicles in another.
* Walking plays no role in the solution process, as it is assumed that walking does not contribute to the problem's complexity.
* The optimization process involves finding optimal assignments of requests to vehicles while considering their availability in different zones.

Overall, this chunk provides a technical framework for addressing the challenges of optimizing ridesharing systems and determining optimal vehicle assignments. It builds upon existing work on rebalancing strategies and mathematical frameworks and highlights the importance of considering factors like oversupply and lack of available vehicles.
