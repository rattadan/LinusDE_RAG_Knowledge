## approach and analysis for dynamic ride-hailing - Chunk 43

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

Benchmark strategies
In what follows, we describe selected benchmark strategies from the
literature in more detail. Please note that most of these strategies had
to be slightly adapted to work in settings where repositioning jobs have
to end in pre-defined parking lots. Nearest parking lot. The first benchmark strategy is only used
to create a feasible solution. This nearest parking lot strategy sends
a vehicle that is currently in state null and has not yet received a
request assignment to the parking lot closest to its current position,
where it will stay idling until it receives a new request to serve. Therefore, no explicit supply–demand-balancing is done. This strategy
would represent the no repositioning strategy in settings without fixed
parking lots. While this is the simplest strategy tested in our study,
we want to point out that there are cases in which the even simpler
random parking lot strategy could actually lead to better results.

---

**LLM Contextual Output:**

This text chunk provides specific technical details and parameters for a dynamic dispatch problem, including:

1. **Spatial-temporal multi-graph convolution network**: This is a deep learning approach used in demand forecasting, which involves creating a spatial-temporal graph to represent the dynamics of vehicle movements and passenger requests.
2. **Nearest parking lot strategy**: As mentioned, this is one of the benchmark strategies described in the text, where vehicles are repositioned to nearest parking lots when they receive no new request assignments.
3. **Dynamic dispatch with or without supply-demand balancing**: The text discusses various dynamic dispatch strategies that do and don't explicitly balance supply and demand. The "nearest parking lot" strategy is explicitly unbalanced (i.e., does not adjust vehicles' locations based on requests), while other strategies may use some form of supply-demand balancing.

This chunk connects to or builds upon the surrounding context by:

1. Providing specific technical details: The text provides a detailed explanation of a dynamic dispatch approach, including its underlying assumptions and characteristics.
2. Building upon existing research: The description is built upon previous studies on demand forecasting and dynamic dispatch in ride-hailing systems.

The requirements and conditions mentioned include:

* **Fixed parking lots**: The problem assumes that there are no fixed parking lots or constraints on vehicle movement.
* **No explicit supply-demand balancing**: The nearest parking lot strategy does not adjust vehicles' locations based on requests, which is a common requirement for effective dynamic dispatch.
* **Real-time management in ride-hailing systems**: The text is focused on developing strategies for real-time management in ride-hailing systems.

Overall, this chunk explains the technical details of a specific dynamic dispatch problem and its characteristics, providing context for understanding the surrounding research and requirements.
