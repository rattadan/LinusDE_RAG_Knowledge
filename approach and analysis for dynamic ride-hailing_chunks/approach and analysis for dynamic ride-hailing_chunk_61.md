## approach and analysis for dynamic ride-hailing - Chunk 61

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

We use the previously introduced
calculations in two different situations:

The aim of this computational study is to analyze and compare
the quality of the presented strategies and design decisions depending
on varying problem characteristics. First, we describe in Section 6.1
the instances and configurations used in the study. Then, we perform
the analysis of the assignment strategies in Section 6.2 and of the
repositioning strategies in Section 6.3. 6.1. Instances and configuration
For the instance generation and the execution of the implemented
strategies, we use the pyhailing framework (Kullman, 2021) with custom
modifications to allow different problem settings. The general setting
is close to the one used in Kullman et al. (2021). The considered
service area is the district of Manhattan in New York City. Therefore,
we use Manhattan distances instead of Euclidean distances.

---

**LLM Contextual Output:**

The current text chunk describes a computational study that analyzes and compares strategies for dynamic dispatch and repositioning in ride-hailing systems, focusing on varying problem characteristics.

**Technical Details:**

* The study uses the pyhailing framework with custom modifications to accommodate different problem settings.
* A general setting is established using Manhattan distances instead of Euclidean distances due to a specific service area (the district of Manhattan in New York City).
* The instance generation and execution of implemented strategies involve the use of pyhailing framework.

**Context:**

The chunk builds upon the surrounding context by:

1. Introducing the topic of dynamic dispatch and real-time management in ride-hailing systems, including various references to relevant literature.
2. Providing a detailed description of the computational study's approach, methodology, and tools (pyhailing framework).
3. Establishing the specific problem setting for Manhattan district of New York City.

**Requirements, Conditions, or Constraints:**

The chunk requires:

* Access to the pyhailing framework with custom modifications
* A general setting that can be adapted to different problem settings
* Specific knowledge of ride-hailing systems and dynamic dispatch/repositioning strategies

Note that there are no explicit requirements for data availability (e.g., dataset/challenge link), but rather a reliance on existing tools (pyhailing framework) and methods (custom modifications).
