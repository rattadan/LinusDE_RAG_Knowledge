## approach and analysis for dynamic ride-hailing - Chunk 102

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

For Manhattan distances, however, the zones form a
square standing on its corner, with the square’s diagonals
having the
√
length of 2 ⋅ 𝑇𝑊 and the square’s side length being 2 ⋅ 𝑇𝑊 . Because the
overlap calculation differs completely depending on the used distance
metric, we show the formula for both cases. Appendix C. Demand estimation error generation
To test the influence of demand estimation errors, some noise
has to be added to the exact demand estimation usually used in the
repositioning approaches. This demand estimation is done by taking
the real future demand sampled by the framework at the beginning
of each planning horizon, mapping all requests to zones, and then
counting the requests per zone for all 30 min intervals of the planning
horizon. The zones correspond to the zones used in the respective
repositioning approaches. Please note that these zones differ between
the benchmark approaches and our proposed approach. Additionally,
the zones in our approach are overlapping.

---

**LLM Contextual Output:**

Analysis of the provided text chunk:

**Exact technical details, parameters, or processes described:**

* Manhattan distances and their square shape with diagonals having a length of 2 * TW (where TW is the side length)
* The overlap calculation between the squares due to different distance metrics
* The formula for both scenarios: using √ length of diagonal = 2 * TW and using other methods

**Connection to or building upon the surrounding context:**

The text chunk provides a theoretical foundation for dynamic dispatch in ride-hailing systems by addressing the challenge of accurately estimating demand based on Manhattan distances. It is connected to the broader topic of dynamic dispatch, real-time management, and simulation models.

The following references are mentioned as contributing to this discussion:

* Bischoff & Maciejewski (2016): Simulation of autonomous taxi deployment in Berlin
* Braverman et al. (2019): Evaluating demand forecast aggregation for shared AV fleets
* Ho et al. (2018): Survey on dial-a-ride problems

These references highlight the importance of accurate demand estimation, simulation models, and real-world applications.

**Specific requirements, conditions, or constraints mentioned:**

* Noise addition to exact demand estimation for testing influence of demand estimation errors
* Differences in zones between benchmark approaches and proposed approach (overlapping zones)
* The need for a formula that works for both scenarios (√ length of diagonal = 2 * TW)

These constraints underscore the importance of finding an accurate method for estimating demand based on Manhattan distances, as well as considering differences in zone layouts across various approaches.
