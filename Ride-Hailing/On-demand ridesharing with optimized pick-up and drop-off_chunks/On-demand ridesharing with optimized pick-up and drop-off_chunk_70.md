## On-demand ridesharing with optimized pick-up and drop-off - Chunk 70

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

Therefore, in this subsection we present
simulation results for the base scenario and for three alternative ones in which the distances between consecutive nodes and the
distribution of the requests are no longer homogeneous:
• It is usual that cities are more concentrated towards the center and dispersed at the peripheries, which might lessen the benefits of
optimizing the PUDO points, as there are not many alternative PUDO points nearby for peripheral nodes. We represent this in the
scenario non-uniform network, where we still use a 10 × 10 network, but in which the distance between consecutive nodes
increases from 75[m] at the center of the network to 300[m] at the edges (recall that in the base scenario such distances are always
equal to 150[m]). • The optimal amount of walking may depend on the demand’s dispersion. If origins and destinations are concentrated, a door-todoor scheme might reduce the detours’ length, which was one of the main motivations to optimize the PUDO points.

---

**LLM Contextual Output:**

**Technical Details:**
The current text chunk focuses on the process of simulating ridesharing systems with varying configurations of request distribution and node placement.

- **Base Scenario:** The base scenario consists of a 10 × 10 grid representing the city network, where nodes are evenly spaced (150[m] apart). This configuration is used to evaluate optimization strategies for meeting points.
- **Alternative Scenarios:**
  - **Uniform Network:** A uniform network with 75[m] distances between consecutive nodes. This scenario is used to test the benefits of optimizing PUDO points in a less efficient network.
  - **Asymmetric Network:** An asymmetric network where node placements vary, increasing distances from central hubs (300[m] at edges) and maintaining equal spacing for nodes within the central area (150[m]). This scenario mimics real-world city layouts.

**Context:**
This text chunk connects to its surrounding context by discussing various aspects of ridesharing and mobility-on-demand systems. The inclusion of simulation results highlights the importance of optimizing meeting points in these systems, addressing benefits such as reducing detours, improving efficiency, and enhancing user satisfaction.

The specific requirements mentioned are:

- **Understanding of city networks:** The text assumes a basic understanding of grid-based city layouts and their characteristics.
- **Simulation tools or methods:** Familiarity with simulation techniques is implied to evaluate the effects of different network configurations on optimization strategies for meeting points.
- **Mathematical modeling:** Some mathematical concepts, such as distance calculations (e.g., 75[m] vs. 150[m]), are mentioned but not explicitly defined in this chunk.

The context also highlights that this text list covers a wide range of works from 2010 to 2020, focusing on various aspects of ridesharing and mobility-on-demand systems, reinforcing the idea that this analysis is part of a broader research project or study.
