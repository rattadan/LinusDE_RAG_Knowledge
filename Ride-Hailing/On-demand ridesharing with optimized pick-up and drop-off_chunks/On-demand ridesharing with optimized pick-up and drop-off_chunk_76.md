## On-demand ridesharing with optimized pick-up and drop-off - Chunk 76

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

Sensitivity analysis
Two parameters might play a key role in how much walking is introduced in the system, so we change them and show the respective
results in Table 4:
• The maximum walking time affects the feasible PUDO points. Although the average walking time in the base case is far from its
upper bound, some specific requests might face long walks. We now study the more prohibitive case in which no user can walk more
than Ωa = 5 [min] at the origin or destination. Running time diminishes, because there are fewer feasible PUDO points, but the
change is not very relevant. As expected, results get worse, because we reduce the number of feasible solutions. Users’ reduction in
walking times is outbalanced by the increase in the number of rejections and total delay. Operators’ costs also increase. • There are some papers (such as Fielbaum et al., 2020) that assume that walking is more annoying than waiting, i.e., pa > pw .

---

**LLM Contextual Output:**

Analysis of the text chunk:

**Technical details and parameters:**

* Two variables, `max_walking_time` and `Omega_a`, are mentioned as potential sensitivity factors in the analysis. `max_walking_time` likely represents the maximum amount of time a user is willing to walk, while `Omega_a` represents a threshold value (5 minutes) above which users will experience long walks.
* The "feasible PUDO points" variable is also discussed, implying that it represents a set of locations or routes that are considered acceptable by operators for passengers.

**Connection to surrounding context:**

This text chunk builds upon the broader theme of ridesharing and mobility-on-demand systems discussed in the provided reference list. The analysis focuses on the impact of sensitivity factors (e.g., `max_walking_time`) on system performance, specifically in terms of delay reduction or increase due to walking requirements.

**Requirements, conditions, or constraints:**

* The text assumes that there are specific parameters (e.g., `max_walking_time` and `Omega_a`) that affect the behavior of users and operators within a ridesharing system.
* It also suggests that certain assumptions about user preferences (e.g., `pa > pw`) may be applied to model the impact of walking on the system.

Overall, this chunk provides technical details and context for analyzing the effect of sensitivity factors on system performance in the context of ridesharing systems.
