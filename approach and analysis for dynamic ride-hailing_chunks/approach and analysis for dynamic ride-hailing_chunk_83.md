## approach and analysis for dynamic ride-hailing - Chunk 83

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

Negative values can occur when the strategy under consideration
has worse quality and higher costs (highlighted in italic typeface) or
better quality and lower costs than the nearest strategy. Please note

Fig. 4. Waiting time of the best assignment strategy in different settings with varying
fleet sizes. 6.3. Repositioning analysis
In this section, we compare the quality of the repositioning strategies presented in Section 5 for different problem settings. For all
experiments, the best assignment strategy according to the results from
Section 6.2 is used. Unless stated otherwise, we set the repositioning
interval to 𝛿𝑅 = 15 min. Because our undersupply probability strategy
requires a defined radius for the parking lot zones (which is usually set
to 𝑇𝑊 ), we must select a specific value for settings without a maximum
waiting time. In our experiments, we use the average waiting time of
the best benchmark strategy. Which repositioning strategy works best in which setting?

---

**LLM Contextual Output:**

This text chunk provides detailed technical information and context related to dynamic dispatch strategies in ride-hailing systems.

**Technical Details:**

- **Metrics and Parameters:** The specific metrics and parameters mentioned include:
  - Fleet size (different settings)
  - Waiting time of the best assignment strategy
  - Repositioning interval (𝛿𝑅 = 15 min)
  - Average waiting time of the best benchmark strategy

**Context Connection:**

- This section builds upon the previous context by focusing on the implementation details and specific scenarios tested in the experiments mentioned (e.g., simulation platforms, dataset/challenge availability).
- The comparison between repositioning strategies is central to understanding which strategy works best in different problem settings.

**Requirements and Conditions:**

- The quality of a repositioning strategy depends on its worse-case scenario (negative values highlighting when it has higher costs or better cost without waiting time) but also considers the overall performance metrics such as average waiting times.
- The experiments were run for varying fleet sizes to account for different problem settings.
