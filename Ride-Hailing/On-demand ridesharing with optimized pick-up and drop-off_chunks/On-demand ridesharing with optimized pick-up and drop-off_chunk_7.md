## On-demand ridesharing with optimized pick-up and drop-off - Chunk 7

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

When PUDO points are optimized together with the rest of the system, the scale of the
problem increases significantly, as each feasible requests-vehicle combination presents now several solutions (by changing the PUDO
points for each passenger), and new feasible combinations might emerge (walking can bring some passengers/vehicles closer). In this paper, we extend the model proposed by Alonso-Mora et al. (2017) (that matches requests and vehicles and can be applied
over large instances) by admitting walks. We show that the problem gains complexity and propose several heuristics to solve it. We
then apply our model to the real trips that were performed during one representative hour in Manhattan, and compare the results
obtained admitting walking or not, finding that when walks are considered, the system improves strongly, inducing short average
walking times. The paper is organized as follows.

---

**LLM Contextual Output:**

This specific section of the text chunk focuses on:

1. **Technical details**: The context implies a modeling and mathematical framework for ridesharing systems, specifically addressing the issues of scalability, optimization, and user satisfaction.
2. **Contextual connection**: This chunk builds upon the surrounding context by exploring how various aspects of ridesharing are interconnected and how incorporating walking as an option can improve system performance.
3. **Specific requirements**: The mention of optimizing problems with walks implies that this section is concerned with developing a method or heuristic for solving complex combinatorial optimization problems, likely using advanced mathematical modeling techniques.

The specific technical details described in this chunk include:

* Mathematical models and decomposition methods for ridesharing problems
* Advanced simulation techniques for evaluating system performance
* Heuristics for addressing the added complexity of incorporating walking into ridesharing systems

This section is connecting to or building upon the surrounding context by highlighting the importance of scalability, optimization, and user satisfaction in ridesharing systems. It also provides specific requirements for developing a method that can effectively address these challenges.

The requirements mentioned are:

* Scalability: The system must be able to handle large numbers of requests and vehicles.
* Optimization: The model must provide efficient solutions for finding feasible combinations of requests and vehicles.
* User satisfaction: Incorporating walking as an option must lead to improved user experience.
