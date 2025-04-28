## On-demand ridesharing with optimized pick-up and drop-off - Chunk 82

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

The
comparison of the first two scenarios suggests that allowing walks has a larger impact when the fleet is smaller (and the quality of
service is worse): while users’ costs are reduced in about 30% in both scenarios, the reduction of VHT is larger in the second one. As discussed above, a central aspect of the optimization of PUDO points is the possible increase in computational times. In our
simulations, the experiments that include walking take approximately ten times longer (from about one hour per iteration to ten
hours). Nevertheless, in both cases, a centralized calculation is too slow, but a distributed one is fast enough. In fact, each vehicle can
determine which trips it might serve: in the case we are studying, this would reduce the computational time required to compute the
GV-graph by thousands (because the fleet sizes are 2,000 or 3,000 in the different scenarios). Admitting walks increases the number of
edges in the GV-Graph (i.e. the number of feasible trips) from about 6,000 to 40,000.

---

**LLM Contextual Output:**

This text chunk provides a detailed analysis of two scenarios related to ridesharing and mobility-on-demand systems:

1. **Technical Details:** The first scenario compares the impact of allowing walks in both smaller (fleets are 2,000) and larger fleets (fleets are 3,000), evaluating how it affects user costs. In both cases, the reduction in VHT is greater when walks are allowed.
2. **Contextual Connection:** This chunk builds upon the surrounding context by discussing key themes related to ridesharing and mobility-on-demand systems. The comparison of the two scenarios serves as a case study for understanding the impact of walking on ride-sharing systems.
3. **Specific Requirements and Conditions:**
 
The required computational time is significant, with simulations showing that allowing walks can reduce it tenfold compared to not having any walking (hence, the need for distributed calculations). This highlights the challenges associated with incorporating new features or behaviors into existing systems without compromising performance.

Key points:

* Allowing walks in smaller fleets increases user costs but reduces VHT.
* In larger fleets, allowing walks has a greater impact on user cost and reduced VHT.
* Computational time is significant when walking is allowed, requiring distributed calculations.
