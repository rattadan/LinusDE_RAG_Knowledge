## On-demand ridesharing with optimized pick-up and drop-off - Chunk 65

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

This includes the requests being reassigned (that enters together with the new requests as input of AP), as deciding the routes is part of
the reassignment process. There could be significant losses on efficiency if the vehicle was forced to fulfill previous requests without
any change. For instance, in Fig. 3, the vehicle would require to go to D1 before going to O3 , inducing an unnecessary long detour. On
the other hand, we do not allow changes in the relative positions of the users that are currently in the vehicle. Such changes would
increase unreliability, and the benefits are expected to be lower, because those relative positions were decided with all the direct
information and, moreover, the vehicle is already following the associated route. In Fig. 3, for instance, this means that when the
vehicle has already visited O2 , it has to visit D2 before D1 .

---

**LLM Contextual Output:**

This specific section of text is focusing on two main aspects:

**Technical details:** The section mentions "rebalancing strategies," which refers to methods used in ridesharing and mobility-on-demand systems to optimize the performance of these systems. These strategies often involve reassigning requests between vehicles, ensuring that each vehicle serves all users simultaneously without unnecessary detours or losses.

**Process and connection to surrounding context:** This section builds upon the surrounding context by highlighting the importance of rebalancing strategies in improving efficiency and user satisfaction in ridesharing systems. The text assumes a background knowledge of the key themes mentioned earlier, which focuses on various aspects of ridesharing and mobility-on-demand systems.

**Specific requirements, conditions, or constraints:** None explicitly mentioned in this section, but the context implies that:

1. The system involves multiple vehicles and users.
2. Rebalancing strategies are necessary to optimize performance.
3. Changes in user positions can lead to significant inefficiencies (e.g., unnecessary detours).
4. The system requires real-time information about user locations.

Overall, this section is explaining the technical details behind rebalancing strategies, which is a crucial aspect of optimizing ridesharing and mobility-on-demand systems, connecting it to the surrounding context of the key themes mentioned earlier.
