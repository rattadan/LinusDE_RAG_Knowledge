## approach and analysis for dynamic ride-hailing - Chunk 52

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

The zone with the highest quotient will receive the next repositionable
vehicle. After that, this zone’s quotient is updated, and the process
repeats until all vehicles are assigned. An optional addition is to prevent
more repositioning than necessary. For that, we set the quotient of a
zone to 0, once the number of vehicles matches the expected demand. In case all zones are saturated, the procedure stops early. We refer to
this addition as the restricted global matching strategy. After finishing this
step, the current number of vehicles assigned to each zone (already
including the absolute minimum supply) is called the target supply. By
comparing the current supply with the target supply per zone, the surplus/shortage of vehicles per zone can be determined. The remaining
repositioning problem can be formulated as a standard transportation
problem. Zones with a surplus of vehicles form the supply nodes; zones
with a shortage of vehicles form the demand nodes.

---

**LLM Contextual Output:**

This specific section of text is explaining the technical details and parameters used in the dynamic dispatch process for repositioning vehicles in ride-hailing systems.

Here are some key points to focus on:

1. **Zone assignment**: The section explains how zones with higher quotients (representing areas with more demand) receive additional vehicles, while those with lower quotients have their vehicles reassigned.
2. **Quotient calculation**: The process of updating the quotient is outlined, taking into account factors such as vehicle supply and expected demand. When a zone's quota reaches 0, it becomes saturated and no further repositioning occurs until all zones are saturated or the system stops early due to excess vehicles.
3. **Target supply**: The target supply for each zone is calculated by comparing the current number of assigned vehicles with the absolute minimum supply required to meet demand.

The section builds upon the surrounding context, which discusses dynamic dispatch and real-time management in ride-hailing systems, as well as various methodologies for solving the repositioning problem. It also references specific requirements and constraints mentioned in the document, such as:

* Preventing more repositioning than necessary
* Setting a restricted global matching strategy to prevent over-assignment

To connect this chunk to its surrounding context, it highlights the importance of zone assignment and quotient calculation in managing demand and supply in ride-hailing systems.
