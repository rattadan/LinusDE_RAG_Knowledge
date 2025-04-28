## On-demand ridesharing with optimized pick-up and drop-off - Chunk 34

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
super-index i in Eq. (4) means that we are constraining walking times at the origin and the destination separately. The cost of each arc τv is calculated as follows:
∑
cost(τ, v) =
kr [pw tw (r, τ, v) + pa ta (r, τ, v) + pv (tv (r, τ, v) − tV (or , dr )) ]
(5)
r∈τ

∑
kr [pw Δtw (r, τ, v) + pv Δtv (r, τ, v)]
+

(6)

r∈v

(7)

+ c0 ⋅ ΔL(Sv )

Where pw , pa and pv are the unitary values of waiting, walking and traveling over the vehicle, respectively, and c0 is the unitary cost of
operating a vehicle. The first term in the sum (Eq. (5)) represents the waiting (tw ), access (ta ) and in-vehicle (tv ) costs faced by the new
users (cU in Eq. (1)): we subtract the fixed distance between the origin and destination tV (or , dr ) from the in-vehicle time because it does
not depend on the system’s optimization. The second term (Eq. (6)) represents the extra waiting and in-vehicle time induced to
passengers that were already being served by the vehicle (ΔcU in Eq.

---

**LLM Contextual Output:**

This specific section of the text chunk is explaining the mathematical framework for modeling ridesharing problems with flexible pickup and delivery locations, specifically as discussed in the papers summarized below:

**Modeling Mathematical Frameworks:**

The technical details described include:

* The use of a super-index i to separate the origin and destination times
* The calculation of the cost of each arc (τv) using the following formula:
∑
cost(τ, v) =
kr [pw tw (r, τ, v) + pa ta (r, τ, v) + pv (tv (r, τ, v) − tV (or , dr )) ]
where pw , pa and pv are the unitary values of waiting, walking, and traveling over the vehicle, respectively, and c0 is the unitary cost of operating a vehicle.
* The inclusion of additional terms in the sum:
(5)
r∈τ
∑
kr [pw Δtw (r, τ, v) + pv Δtv (r, τ, v)]
+

(6)
r∈v
+
c0 ⋅ ΔL(Sv )
where pw , pa and pv are the unitary values of waiting, walking, and traveling over the vehicle, respectively, and c0 is the unitary cost of operating a vehicle.

**Connecting to surrounding context:**

This section builds upon the concept of optimizing ridesharing systems with flexible pickup and delivery locations. The mathematical framework outlined in this chunk:

* Refers to the work by Zhao et al., Stiglic et al., Tirachini, A. & Gomez-Lobo (2020), Tirachini, A. et al. (2010) on modeling and optimization of ridesharing systems.
* Emphasizes the importance of using mathematical models to optimize these systems.

**Requirements, conditions, or constraints:**

None mentioned in this specific section. However, the context assumes a general understanding of mathematical modeling and optimization techniques in ridesharing systems. The reference list provided at the end of the document indicates that there are various methodologies and papers discussed throughout the text, suggesting that certain technical requirements or conditions may be present (e.g., access to computational resources, expertise in mathematical modeling).
