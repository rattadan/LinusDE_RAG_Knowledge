## On-demand ridesharing with optimized pick-up and drop-off - Chunk 26

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

When deciding
whether a vehicle can serve a group of users and which route to follow, one needs to consider all the possible PUDO points for each user
in the group, as explained in Section 2.2.1, and determine which PUDO points are feasible. We do this with additional constraints:
namely, bounds on the maximum walking time per user, and ensuring that users have enough time to walk towards the pick-up point. These constraints are detailed in Section 2.2.2 together with the changes in the objective function (Eq. (1)) that now reflects that
walking is uncomfortable for the users. The rest of the formulation of AP remains the same as in Alonso-Mora et al. (2017), although
some heuristics are now required to solve the problem efficiently, which are explained in Section 2.4. In the following we detail the full method, i.e., the original one with the modifications just stated. 3

In the appendix we provide a glossary, synthesizing the abbreviations and mathematical symbols used throughout the paper.

---

**LLM Contextual Output:**

The current text chunk focuses on a technical aspect of ridesharing systems:

**Exact Technical Details:**

1. **PUDO points**: A point is considered as a pickup or drop-off location for users to interact with each other, which can be in the form of a physical location (e.g., intersection) or a virtual representation (e.g., map marker).
2. **Walking time constraint**: The problem requires determining the optimal route that minimizes walking time for all users while satisfying additional constraints (maximum walking time per user and sufficient walk distance).
3. **Modified objective function**: The original objective function in Alonso-Mora et al. (2017) is adjusted to reflect the discomfort of users while walking, incorporating a new term representing this constraint.

**Contextual Connection:**

This technical aspect builds upon existing work in ridesharing systems, particularly in optimizing routes that minimize travel time and constraints on user behavior. The specific modification introduced adds a new layer of complexity by incorporating user comfort levels into the problem-solving process.

**Requirements, Conditions, or Constraints:**

* Ensures feasibility of PUDO points for each group of users
* Implements walking time constraint to prioritize efficient movement
* Incorporates additional walk distance constraints to ensure sufficient walking time

By providing a detailed technical approach to optimizing ridesharing routes under these conditions, the reference list offers a comprehensive solution methodology for managing dynamic systems in transportation networks.
