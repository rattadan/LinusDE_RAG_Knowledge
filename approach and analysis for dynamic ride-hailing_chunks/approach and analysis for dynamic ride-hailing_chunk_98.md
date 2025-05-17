## approach and analysis for dynamic ride-hailing - Chunk 98

**Document Summary:**

Here are some key references on the topic of dynamic dispatch and real-time management in ride-hailing systems, organized by their focus:

Simulation and modeling:
- Bischoff & Maciejewski (2016): Simulation of autonomous taxi deployment in Berlin 
- Braverman et al. (2019): Evaluating demand forecast aggregation for shared AV fleets
- Ho et al. (2018): Survey on dial-a-ride problems

Dynamic dispatch and repositioning:
- Geng et al. (2019): Spatiotemporal multi-graph convolution network for demand forecasting 
- Jiao et al. (2021): Real-world ride-hailing vehicle repositioning using deep RL
- Al-Kanj et al. (2020): Approximate dynamic programming for autonomous fleets
- De Souza et al. (2020): Optimization-based strategy for shared AV fleet repositioning
- Hyland & Mahmassani (2018): Optimizing AV assignment to traveler demand

Rebalancing strategies:
- Guo et al. (2021): Robust vehicle rebalancing in ride-hailing systems with uncertain demand 
- Dandl et al. (2019): Evaluating spatio-temporal demand forecast impact on shared mobility
- Braverman et al. (2019): Empty-car routing for ridesharing

Demand forecasting:
- Geng et al. (2019): Spatiotemporal multi-graph convolution network 
- Ho et al. (2018): Survey of dial-a-ride problems
- Fagnant & Kockelman (2014): Shared autonomous vehicle travel and environmental implications

Simulation platforms:
- DIMACS Center for Discrete Mathematics: Hailing challenge [2]

I've organized them by their primary focus areas, but there is significant overlap between these categories. The references cover a range of methodologies from simulation to deep learning approaches.

[2] Note that the actual link provided in the original text was broken, so I removed it and just mentioned where the dataset/challenge can be found. Let me know if you need any other information or have questions about this topic!

**Original Text:**

Zone overlap using Euclidean distances. Acknowledgments
This work was supported by the Federal Ministry of Education and
Research of Germany in the framework of the research project ‘‘L2O:
Learning to Optimize’’ (01IS20013A). Appendix A. Modified undersupply probability calculation
The following formula shows the probability of more demand than
supply in a given zone based on the Poisson distribution:
𝑝undersupply =

∞
∑
𝑑 𝑘 𝑒−𝑑
𝑘! 𝑘=𝑠+1

=1−

𝑠
∑
𝑑 𝑘 𝑒−𝑑
𝑘=0

𝑘! In larger instances, the term 𝑘! can get bigger than most inbuilt
datatypes are able to handle. To prevent this problem, we replaced the
term 𝑘! with Stirling’s approximation. To prevent division by zero, we
only replace 𝑘! for 𝑘 > 0:
( )𝑘
√
𝑘
𝑘! ≈ 2𝜋𝑘
)
( 𝑒
𝑠
𝑑 0 𝑒−𝑑 ∑ 𝑑 𝑘 𝑒−𝑑
𝑝undersupply = 1 −
+
0! 𝑘! 𝑘=1

Fig. 8. Zone overlap using Manhattan distances. matching is close to zero, when there are only few requests (because of the small demand-supply-ratio and/or the short waiting
period for more requests).

---

**LLM Contextual Output:**

This specific text chunk:

**Zone overlap using Euclidean distances**

This chunk describes a technique used in simulation modeling, specifically for analyzing zone overlaps in ride-hailing systems. The method involves calculating the probability of zone overlap based on Euclidean distances.

The context is **Simulation and Modeling**, which covers topics like autonomous taxi deployment, demand forecasting, dynamic dispatch, rebalancing strategies, and simulation platforms.

Specifically:

1. **Technical details**: The formula used to calculate zone overlap using Euclidean distances is: `𝑝undersupply = 1 - ∑ 𝑘! (𝑒−𝑑)^(𝑘+1)`.
2. **Connection to surrounding context**: This chunk builds upon the previous section, which discussed simulation and modeling techniques for ride-hailing systems. The use of Euclidean distances is a common approach in spatial analysis.
3. **Requirements, conditions, or constraints**: There are no specific requirements mentioned in this chunk. However, the use of mathematical formulas and statistical approximations suggests that there may be limitations to the accuracy of the results (e.g., small demand-supply ratios or short waiting periods).

Overall, this chunk is explaining a simulation technique used for modeling ride-hailing systems, specifically for analyzing zone overlaps using Euclidean distances.
