## approach and analysis for dynamic ride-hailing - Chunk 105

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

10 depicts an example of the noise
factor for one specific point in time for the whole service area. B.1. Euclidean distances
Fig. 7 shows the overlap of two zones for Euclidean distances. The
overlapping area consists of two equally sized circular segments. Let 𝑑
be the distance between the center of both zones and ℎ = 𝑇𝑊 − 𝑑2 be
the segment’s height. Based on the general formula for the area of a
circular segment (Weisstein, 2002), the area of each of the segments
can be calculated as follows:
)
(
√
ℎ
− (𝑇𝑊 − ℎ) 2 𝑇𝑊 ℎ − ℎ2
(8)
𝐴segment = 𝑇𝑊 2 cos−1 1 −
𝑇𝑊
By doubling this value to get the full overlap area and putting this into
relation to the total area of the zone, we get the overlap proportion by
the following formula:
overlap =

2 𝐴segment
𝜋 𝑇𝑊 2

(9)

B.2. Manhattan distances
Fig. 8 shows the overlap of two zones for Manhattan distances. Here,
the overlap always forms a rectangle.

---

**LLM Contextual Output:**

**Technical Details, Parameters, or Processes Described:**

The current text chunk describes two distinct mathematical concepts:

1. **Euclidean Distance and Segment Calculation:** The chunk explains how to calculate the area of a circular segment using Euclidean distance (B.1) and then uses this formula to find the overlap proportion between two zones.

2. **Manhattan Distance and Segment Calculation:** The same chunk describes how to calculate the area of a rectangle formed by Manhattan distances (B.2), again using the calculated overlap proportion from Euclidean distances.

**Connection to or Building upon Surrounding Context:**

The text builds upon the context provided earlier, which discusses dynamic dispatch and real-time management in ride-hailing systems. The chunk connects this topic to the following areas:

- Dynamic dispatch and repositioning strategies (e.g., Geng et al. (2019), Jiao et al. (2021))
- Rebalancing strategies (e.g., Guo et al. (2021), Dandl et al. (2019))

**Specific Requirements, Conditions, or Constraints:**

The text mentions the following requirements or conditions:

- The reference to bischoff & maciejewski (2016) and their simulation of autonomous taxi deployment in Berlin suggests that dynamic dispatch is a relevant topic.
- The mention of empty-car routing for ridesharing indicates that rebalancing strategies are also relevant.

**Focused Analysis:**

This chunk provides insight into how dynamic dispatch and real-time management involve:

- Calculating the overlap proportion between two zones using different distance metrics (Euclidean vs. Manhattan)
- Applying this calculation to find the overlap area, which is essential for rebalancing strategies
- Using these calculations in conjunction with other dynamic dispatch methods to optimize repositioning strategies
