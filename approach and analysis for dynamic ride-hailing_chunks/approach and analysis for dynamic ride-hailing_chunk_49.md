## approach and analysis for dynamic ride-hailing - Chunk 49

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

Based on the relative demand per zone and the fleet
size, an optimal number of vehicles per zone can be calculated and
the vehicle movements are determined by solving a cost-minimum
matching problem. A similar idea is used, e.g., in Spieser et al. (2016). The downside of this approach is that the fleet is always repositioned to
6

EURO Journal on Transportation and Logistics 12 (2023) 100109

C. Ackermann and J. Rieck

zones too early, potentially resulting in unserved requests. From our
point of view, this parameter should be set to the ‘‘cycle length’’ of a
vehicle, which represents the average time between two requests served
by the same vehicle. Results from preliminary experiments to find the
optimal value for the timeframe support this assumption. match the demand distribution, even though a slightly imbalanced fleet
would also be able to serve all requests in times of low demand. This
unnecessarily increases the repositioning costs.

---

**LLM Contextual Output:**

I'll provide a focused analysis of the specific section explaining what this chunk is explaining.

**Technical details and parameters:**

The technical detail mentioned is the "cost-minimum matching problem", which is a classic problem in combinatorial optimization and operations research. The parameters described are:

* Relative demand per zone (R)
* Fleet size (Z)
* Cycle length (T) of a vehicle, representing the average time between two requests served by the same vehicle

**Connection to or building upon the surrounding context:**

This chunk is building upon the previous section that discussed dynamic dispatch and real-time management in ride-hailing systems. The current text chunk expands on this idea by introducing:

* Optimization-based strategy for shared AV fleet repositioning
* Robust vehicle rebalancing in ride-hailing systems with uncertain demand
* Evaluation of spatio-temporal demand forecast impact on shared mobility

The context is provided through the references, which cover various methodologies from simulation to deep learning approaches. The current text chunk is connected to these categories by its focus on optimizing dynamic dispatch and repositioning strategies.

**Specific requirements, conditions, or constraints:**

The specific requirement mentioned is setting the "cycle length" of a vehicle (T) to match the average time between two requests served by the same vehicle. This implies that the optimal value for T should be determined based on preliminary experiments to find the correct balance between repositioning costs and matching demand distribution, even with an imbalanced fleet.

Additionally, the text assumes that unserved requests will occur if the fleet is not repositioned too early (i.e., when T < T).
