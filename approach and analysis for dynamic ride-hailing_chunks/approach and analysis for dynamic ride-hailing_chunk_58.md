## approach and analysis for dynamic ride-hailing - Chunk 58

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

This expected missed reward could
be collected when an additional vehicle is sent to this parking lot. Therefore, a repositioning order is expected to be profitable if the travel
costs for going to that parking lot are lower than the expected missed
7

EURO Journal on Transportation and Logistics 12 (2023) 100109

C. Ackermann and J. Rieck

6. Computational study & discussion

reward. In settings where the repositioning costs can be ignored, this
trade-off can simply be removed by ignoring the restriction to only
perform the repositioning if the expected profit is positive. Handling overlapping zones. Since each lot has its own lot zone,
these zones might overlap. While this is conceptually a benefit of this
approach, it also increases computational complexity when calculating
the expected demand and the current supply. All vehicles in a specific
lot zone are considered the supply of this lot zone. However, not all of
the vehicles are actually able to serve all requests arising in this zone.

---

**LLM Contextual Output:**

This specific section is explaining the concept of dynamic dispatch and repositioning in ride-hailing systems. Here's a focused analysis:

**Technical Details:**

* Dynamic dispatch refers to the process of assigning tasks or jobs (in this case, rides) to vehicles based on demand forecasts.
* Repositioning refers to the movement of vehicles from one location to another to optimize their usage.
* The expected profit is determined by the travel costs for going to a specific parking lot and the revenue generated from repositioning.

**Parameters:**

* The cost of traveling to a parking lot is an essential parameter in dynamic dispatch and repositioning, as it directly affects the expected profit.
* The demand forecast is also crucial, as it determines the number of vehicles needed to satisfy passenger requests within a given time frame.

**Processes:**

* Dynamic dispatch involves analyzing the current supply and demand for each vehicle's location and assigning tasks accordingly.
* Repositioning requires identifying suitable locations for each task, which may involve calculating travel costs and revenue generated from repositioning.

**Context Connection:**

This section connects to the surrounding context by discussing the trade-off between missed rewards (e.g., lost revenue due to delayed or non-existent rides) and expected profits. The authors mention that ignoring this restriction can lead to a computational complexity increase, highlighting the importance of balancing reward with cost in dynamic dispatch.

**Requirements and Conditions:**

* The authors emphasize the need for careful analysis of demand forecasts and supply/ demand balance to optimize dynamic dispatch and repositioning.
* Computational complexity is mentioned as an issue when calculating expected demand and current supply, indicating that efficient algorithms are required to handle overlapping zones efficiently.
