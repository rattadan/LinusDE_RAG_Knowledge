## approach and analysis for dynamic ride-hailing - Chunk 22

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

However, all vehicle movements
(with and without customers) induce an additional negative reward
proportional to the distance traveled. To limit customer inconvenience,
a maximum waiting time 𝑇𝑊 is introduced, requiring the designated
vehicle to arrive at the pickup location no later than 𝑡𝑖 + 𝑇𝑊 . If it is
not possible to serve the request in time, the customer gets rejected
by the system. To model problem settings without a maximum waiting
time, 𝑇𝑊 can be set to the length of the planning horizon (here:
86400 s). Please note that rejection of requests is just allowed, when
there is a real maximum waiting time constraint in place. Additionally,
there is a maximum notification time 𝑇𝑁 until which the customer
needs to be informed about the acceptance/rejection decision. In case
of acceptance, this includes information about the assigned driver as
well as the estimated arrival time. The notification constraint can be
removed by setting 𝑇𝑁 = 𝑇𝑊 .

---

**LLM Contextual Output:**

I'll provide a focused analysis of the text chunk and its context.

**Technical Details and Parameters:**

* The maximum waiting time (`𝑇𝑊`) is set to 86400 seconds (or 24 hours) for planning horizon.
* The notification time (`𝑇𝑁`) can be set to `𝑇𝑊` or `∞`, allowing rejection of requests without notification.

**Connection to the surrounding context:**

This chunk builds upon the concept of dynamic dispatch and real-time management in ride-hailing systems, as discussed in the provided references. It specifically addresses the issue of vehicle movements and customer inconvenience by introducing a maximum waiting time (`𝑇𝑊`) and allowing for rejection of requests without notification.

**Requirements, Conditions, or Constraints:**

* The system can accept requests with a real maximum waiting time constraint in place.
* The system allows for rejection of requests without notification if the vehicle is not available within the maximum waiting time.
* Notification can be set to occur at `𝑇𝑁`, which may be set to `𝑇𝑊` or `∞` to allow for no notification.

The chunk provides specific technical details and parameters related to dynamic dispatch, real-time management, and vehicle movements in ride-hailing systems. It also outlines the requirements and conditions for handling customer inconvenience and rejection of requests without notification.
