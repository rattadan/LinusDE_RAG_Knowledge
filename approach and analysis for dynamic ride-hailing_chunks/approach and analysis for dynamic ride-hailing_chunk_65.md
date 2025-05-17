## approach and analysis for dynamic ride-hailing - Chunk 65

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

The unselected vehicles
are then available for the profit calculation in the next iteration. Once all vehicles are repositioned or there are no more profitable
repositioning orders possible, the process is stopped and the
solution is executed. • Fleet size, in relation to the service area
• Demand-supply-ratio, as indication for over- and undersupply
• Maximum allowed customer waiting time before pickup or rejection
• Vehicle availability (all or only non-serving vehicles)
We consider three different fleet sizes, with 𝑉 ∈ {30, 100, 300}. The
number of requests depends on the fleet size. We define the demandsupply-ratio (𝐷𝑆𝑅) as the number of requests per day per vehicle. We
use 𝐷𝑆𝑅 ∈ {40, 70, 100}, representing fleets with low utilization, high
utilization, and overloaded fleets. For the maximum waiting time 𝑇𝑊 ,
we use three different settings: short waiting time, long waiting time,
and no waiting time.

---

**LLM Contextual Output:**

**Technical Details and Parameters**

1. The text mentions a fleet size (V ∈ {30, 100, 300}) and defines it as the number of vehicles.
2. Three specific fleet sizes are defined: V = 30, V = 100, and V = 300.
3. The demand-supply ratio (DSR) is defined as DSR ∈ {40, 70, 100}, which represents different levels of fleet utilization.
4. The maximum allowed customer waiting time before pickup or rejection (TW) is defined, but its exact value is not provided.

**Connections to the Surrounding Context**

1. The text assumes a ride-hailing system where vehicles are assigned requests based on demand and supply ratios.
2. It discusses various metrics used to evaluate the performance of such systems, including fleet size, DSR, TW, and vehicle availability (non-serving vs. serving).
3. The context also mentions simulation platforms like DIMACS Center for Discrete Mathematics: Hailing Challenge [2], which suggests that this text is part of a broader research effort.

**Requirements, Conditions, or Constraints**

1. The text requires the presence of specific metrics to evaluate fleet performance (V ∈ {30, 100, 300}, DSR ∈ {40, 70, 100}, TW).
2. The demand-supply ratio is an important factor in determining fleet efficiency and profitability.
3. The maximum allowed customer waiting time before pickup or rejection is a critical consideration for ensuring smooth operations.
4. The text implies that the system may need to handle varying levels of demand and supply ratios across different fleet sizes, indicating flexibility in its design.
