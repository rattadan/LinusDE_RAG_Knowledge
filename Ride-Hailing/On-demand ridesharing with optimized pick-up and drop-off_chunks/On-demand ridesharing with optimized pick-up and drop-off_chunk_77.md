## On-demand ridesharing with optimized pick-up and drop-off - Chunk 77

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

If we
raise pa to 3pv , the average walk diminishes together with waiting and delay, at the cost of increasing rejections and VHT. Resulting
costs should not be compared directly, because increasing one of the cost parameters will obviously yield higher costs. As a synthesis, both parameters affect the system in the expected directions: they reduce the amount of walking, which increases
VHT because vehicles require higher detours, which on turn increases the rejection rate because vehicles require longer times to
become available. 3.2. Results over Manhattan
3.2.1. Description of the Manhattan dataset
As in Alonso-Mora et al. (2017), we use the publicly available dataset of taxi travels in Manhattan, New York City (Donovan and
Work, 2017); with this dataset, we have the exact coordinates of the origin and destination, together with the time when the passengers
boarded the taxi and how many, for each taxi travel in Manhattan during 2013.

---

**LLM Contextual Output:**

This text chunk appears to be discussing the technical details behind ride-sharing systems, specifically focusing on the impact of increasing waiting time (VHT) and reduced walking distances (as a result of increased detours due to vehicles requiring higher speeds).

Here's a focused analysis:

1. **Technical details:** The chunk mentions the use of taxi travel data in Manhattan from 2013 to provide a dataset for the simulations.
2. **Context connection:** This section connects to or builds upon the surrounding context by:
   - Providing an example of a specific dataset (Manhattan taxi travels) that will be used for simulation purposes.
   - Introducing the concept of waiting time and its effects on efficiency in ride-sharing systems.
3. **Requirements, conditions, or constraints:**
   - The need to raise the average walk distance to 3pv while increasing rejections and VHT costs suggests a focus on optimizing system performance under specific constraints.

Some additional observations:

* The text appears to be discussing the benefits of using mathematical modeling and simulation techniques in ride-sharing systems, specifically highlighting the importance of considering various factors such as waiting time, walking distances, and vehicle speeds.
* The mention of "reinforcement learning approaches" (Wen et al.) suggests that this research might explore how agents can adapt and improve their behavior in response to changing conditions, potentially leading to more efficient ride-sharing systems.
