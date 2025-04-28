## On-demand ridesharing with optimized pick-up and drop-off - Chunk 61

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

Concretely, we make significant differences when
a user has been told to walk:
1. Users waiting to be picked up at their exact origin are kept as pending requests for the following iteration. This means that when
new requests arrive, they could be re-assigned to a different vehicle, or they can stay assigned to the same one but their waiting time
might increase (always bounded by Ωw ) due to detours induced by new passengers. In the most extreme case, they could even
become rejected if that reduces the total costs of the system. 2. Users that are told to walk towards a different pick-up node cannot be reassigned to a different vehicle, cannot be rejected, and their
waiting time cannot increase. 3. Drop-off points cannot be changed once a user has boarded a vehicle. The first of these rules is similar to the one used by Alonso-Mora et al. (2017) in the no-walking scheme, but admitting extra waiting
time for passengers that don’t walk at their origins.

---

**LLM Contextual Output:**

This text chunk focuses on the technical details and parameters of a specific aspect of ridesharing systems: managing user waiting times when users are told to walk instead of being picked up directly.

The exact technical details described in this chunk include:

1. A method for handling pending requests that remain at an origin after a user is instructed to walk.
2. Parameters for the model, including:
* The number of users (w) and the maximum waiting time for each user (Ωw).
* The impact of detours on waiting times.

The connection between this chunk and the surrounding context is as follows:

This chunk builds upon the broader topic of ridesharing systems and their challenges in managing user waiting times. By focusing specifically on a specific technical aspect, such as handling pending requests that remain at an origin after a user is instructed to walk, we can gain insights into how these systems can be optimized.

The requirements, conditions, and constraints mentioned in this chunk include:

1. The need for efficient management of user waiting times.
2. The impact on the system's performance due to detours and the inability to reass_assign users to different vehicles.
3. The constraint that drop-off points cannot be changed once a user has boarded a vehicle.

Overall, this text chunk provides technical details on a specific aspect of ridesharing systems, connecting it to broader themes and challenges in these systems.
