## approach and analysis for dynamic ride-hailing - Chunk 77

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

The question arises whether matching-based approaches can
still provide a benefit compared to the nearest strategy, when the
response delay is limited to, e.g., 15 or 30 s. We tested the matchingbased approaches with three different combinations of matching intervals 𝛿𝑀 and maximum notification times 𝑇𝑁 , with (𝛿𝑀 , 𝑇𝑁 ) ∈
{(15 s, 15 s), (15 s, 30 s), (30 s, 30 s)}. All three combinations were applied
to the different problem settings from Table 2, whereby only the
specification with all vehicles available for assignment was used. The
results show that matching-based approaches with premature notification (𝑇𝑁 < 𝑇𝑊 ) can provide a benefit only in very few settings
compared to the nearest strategy with immediate notification. In terms
of service rate, the combination (𝛿𝑀 , 𝑇𝑁 ) = (15 s, 30 s) outperformed
the nearest strategy by 0.3% to 3.0% for highly utilized fleets (𝐷𝑆𝑅 ∈
{70, 100}) and long maximum waiting times 𝑇𝑊 = 1029, increasing with
larger fleets and higher fleet utilization.

---

**LLM Contextual Output:**

This text chunk is discussing the comparison between matching-based approaches and nearest-neighbor strategies in ride-hailing systems.

**Technical Details:**

* Matching-based approaches involve assigning rides to vehicles based on their location and availability.
* Nearest-neighbor strategy involves assigning rides to the closest vehicle to the request location.
* Parameters mentioned:
	+ 𝛿𝑀 (matching interval): the time window within which a vehicle must be available for assignment. The possible values are 15 seconds, 30 seconds, or both.
	+ 𝑇𝑁 (maximum notification time): the maximum time delay before an empty vehicle is notified to reposition or adjust its strategy. Possible values are 15 seconds and 30 seconds.
* Process: The text compares matching-based approaches with and without premature notification (∝𝑇𝑊) in various problem settings.

**Context Building:**

This chunk builds upon the surrounding context by providing an overview of related research on dynamic dispatch, real-time management, and ride-hailing systems. It also discusses specific methodologies and parameters used to evaluate their effectiveness. The text mentions key references, simulation platforms (DIMACS Center for Discrete Mathematics: Hailing Challenge), and problem settings from Table 2.

**Requirements and Conditions:**

* The comparison aims to investigate the impact of premature notification on matching-based approaches in various scenarios.
* The results are compared to those using the nearest-neighbor strategy with immediate notification (∝𝑇𝑊).
* Specific requirements include:
	+ Matching intervals 𝛿𝑀 and maximum notification times 𝑇𝑁 (15 seconds, 30 seconds, or both)
	+ Problem settings from Table 2
	+ High utilization of fleets (𝐷𝑆𝑅 ∈ {70, 100})
	+ Long maximum waiting times 𝑇𝑊 = 1029
