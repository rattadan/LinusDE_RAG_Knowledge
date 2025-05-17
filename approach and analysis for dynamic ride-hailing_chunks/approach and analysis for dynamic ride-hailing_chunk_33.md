## approach and analysis for dynamic ride-hailing - Chunk 33

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

Furthermore, 𝛿𝑀 should never be greater than the maximum
notification time 𝑇𝑁 , as we must ensure that every request is
considered at least once in a matching epoch. Requests that did
not receive an assignment in one matching epoch, while the next
matching epoch would be after 𝑇𝑁 , are rejected prematurely. • FCFS integration: In undersupply scenarios with more open requests than available vehicles, some of the requests will not
receive an assignment. To increase fairness, Hyland and Mahmassani (2018) modify the purely cost-based matching approach
by giving priority to earlier requests. Let us assume we have 𝑛
available vehicles but 𝑛+𝑐 (with 𝑐 > 0) open requests. In this case,
only the oldest 𝑛 open requests are considered in the matching,
resulting in an 𝑛 × 𝑛 cost matrix, while the newest 𝑐 requests
are ignored in this decision epoch. By that, it can be guaranteed
that no customer will be matched later than another one that
requested service later.

---

**LLM Contextual Output:**

This specific text chunk appears to be explaining a concept related to dynamic dispatch and real-time management in ride-hailing systems.

**Technical Details:**
The chunk discusses the importance of ensuring every request is considered at least once during a matching epoch, where requests are matched with available vehicles. The authors suggest using a fairing mechanism to handle cases where some requests are not assigned due to undersupply or open requests.

**Context Connection and Building Upon Surrounding Context:**

This chunk builds upon the context provided earlier by discussing fairness in dynamic dispatch, particularly when there are more requests than available vehicles (undersupply scenario). The authors highlight the need for a matching approach that considers all requests at least once during each epoch. This is an important aspect of ride-hailing systems, where ensuring fairness and responsiveness to customer requests is crucial.

**Requirements, Conditions, or Constraints:**

* The chunk requires a maximum notification time (`𝑇𝑁`) to ensure every request is considered at least once in a matching epoch.
* The authors suggest using a fairing mechanism to handle cases where some requests are not assigned due to undersupply or open requests.

Overall, this text chunk provides guidance on how to design a dynamic dispatch and real-time management system that ensures fairness and responsiveness in ride-hailing applications.
