## approach and analysis for dynamic ride-hailing - Chunk 26

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

As we are considering deterministic travel times, the
final waiting time of assigned customers can already be computed when
the assignment happens. The reward is the negative sum of the waiting
times for each assigned customer in seconds. Rejected requests receive
a value equal to the maximum waiting time 𝑇𝑊 . 𝑅𝑅 determines the
monetary reward, which is calculated using the reward received for
serving the assigned requests as well as the costs associated with all
distances driven by all vehicles. All three objectives can be used at
the same time and can be weighted via appropriately dimensionalized
parameters 𝛼, 𝛽, and 𝛾. If only one objective is to be considered, the
other weights can be set to 0. If a lexicographical order is preferred
instead, the weights can be adapted accordingly. Note in this context
that the number of served requests is limited by the total number of
requests 𝑅 per episode and the sum of waiting times over all requests
is limited by 𝑇𝑊 ⋅ 𝑅.

---

**LLM Contextual Output:**

I'll provide a focused analysis of the specific section.

**Technical Details, Parameters, or Processes:**

The technical details described in this chunk are as follows:

* The reward function is defined as the negative sum of waiting times for each assigned customer in seconds.
* The objective functions to be used are:
	+ Determining the monetary reward based on serving assigned requests and costs associated with driving distances.
	+ Calculating a reward for receiving rejected requests, which is equal to the maximum waiting time 𝑇𝑊 .
* Weighted parameters 𝛼 , 𝛽, and 𝛾 are used to adjust the objectives.

**Connection to or Building upon Surrounding Context:**

This chunk connects to the surrounding context by:

* Providing a specific example of how dynamic dispatch and real-time management in ride-hailing systems can be implemented.
* Offering a detailed explanation of the reward function and objective functions, which is essential for understanding the problem being addressed.

**Requirements, Conditions, or Constraints:**

The requirements mentioned in this chunk are as follows:

* The number of served requests is limited by both the total number of requests 𝑅 per episode and the sum of waiting times over all requests.
* The reward function is designed to be multi-objective and can be weighted using dimensionalized parameters 𝛼, 𝛽, and 𝛾.
