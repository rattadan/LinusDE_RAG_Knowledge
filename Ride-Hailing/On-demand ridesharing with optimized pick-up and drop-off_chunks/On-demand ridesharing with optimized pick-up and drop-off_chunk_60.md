## On-demand ridesharing with optimized pick-up and drop-off - Chunk 60

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

Most requests will be assigned to
the same vehicle over and over again until they are picked up, but some requests will be reassigned due to the changes induced by the
new requests. This reassignment process is related to the chance of walking, because any change regarding the pick-up time is more annoying if
the user is waiting on the street rather than at his exact origin, so the system should try to avoid those reassignments. Therefore, the
reassignment rules might depend on the request, posing some design decisions. Note that a trade-off emerges here: although the chance
of walking should improve the system, as it increases the number of feasible solutions through new decision variables (the PUDO
points), it might also have negative effects when reducing the flexibility to reassign. How to limit reassignments due to walking is somewhat arbitrary. We will impose rules that stress out the said trade-off. By doing
so, good results in the numerical simulations remain robust regarding this trade-off.

---

**LLM Contextual Output:**

**Technical Details and Parameters:**

1. **Reassignment Process:** The text describes a reassignment process where a vehicle might be assigned to pick up another request due to changes induced by new requests.
2. **Probability of Walking:** The system aims to avoid reassignments that are inconvenient for users, specifically those who walk rather than being picked up at their exact origin.
3. **Trade-off:** A trade-off emerges between the potential benefits of reducing reassignments (improving user satisfaction) and the negative effects on flexibility (reducing the number of feasible solutions).

**Connections to or Building upon Surrounding Context:**

1. The text is part of a broader reference list covering various aspects of ridesharing and mobility-on-demand systems, providing a comprehensive overview of current research trends.
2. The reference list includes papers that discuss different topics related to reassignment strategies in ride-sharing systems, such as modeling, optimization heuristics, simulation, and reinforcement learning approaches.

**Specific Requirements, Conditions, or Constraints:**

1. **Design Decisions:** The text implies that the system must balance the trade-off between reducing reassignments (improving user satisfaction) and increasing flexibility to reassign.
2. **User Experience:** The design decisions should aim to minimize negative effects on users, such as making it less convenient for them to walk rather than being picked up at their exact origin.

This analysis focuses on the specific technical details, parameters, and connections discussed in the provided text chunk, highlighting the trade-off between reassignment benefits and user experience.
