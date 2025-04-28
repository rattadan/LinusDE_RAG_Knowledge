## On-demand ridesharing with optimized pick-up and drop-off - Chunk 64

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

We
also take advantage of the short computational times required by this network to perform a sensitivity analysis regarding the network,
the demand structure, and the two relevant parameters dealing with walking, i.e. Ωa (the maximum walking time) and pa (the unitary
cost of walking). The second scenario (Section 3.2) is a real-life case in Manhattan, in which the heuristics are necessary. Here we show that the
method is able to deal with thousands of vehicles and requests, and analyze how the SMoD improves thanks to the optimization of the
PUDO points in a realistic environment. Recall that we need to decide on some rules to face the trade-off between which routes are admissible when updating the as­
signments (efficiency) and how many changes a user might face (reliability). Here we choose to allow the vehicle to serve new requests
before previous ones, because the location of the new origins and destinations were not known when the previous route was decided.

---

**LLM Contextual Output:**

**Analysis of the Technical Details, Parameters, or Processes Described in this Chunk:**

The technical details described in this chunk are related to the mathematical modeling and optimization of ridesharing systems with meeting points. Specifically, it appears that the author is using a combination of mathematical models (e.g., Mathematical Optimization Methods, SMoD) to analyze the efficiency and reliability of vehicles serving requests.

**Connection to or Building upon the Surrounding Context:**

This chunk is building upon the surrounding context by providing a detailed explanation of how ridesharing systems with meeting points can be optimized using mathematical modeling and simulation. The text also references specific papers (e.g., Zhao et al. 2018, Stiglic et al. 2015) that have been used to develop these models.

**Specific Requirements, Conditions, or Constraints:**

There are no explicit requirements, conditions, or constraints mentioned in this chunk. However, the context suggests that the author is working on a project that involves optimizing ridesharing systems with meeting points, which implies that there may be certain limitations, such as:

* Computational resources (e.g., short computational times)
* Demand structure and walking times
* Unitary costs of walking
* Realistic environment

Additionally, the text mentions that the analysis is performed using "real-life" data from Manhattan, suggesting a specific geographic context.
