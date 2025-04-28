## approach and analysis for dynamic ride-hailing - Chunk 106

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

Because this has an angle of
45◦ to the coordinate axes (similarly to the square zones themselves),
we propose to rotate the coordinate system by 45◦ to simplify the
calculations. Fig. 9 shows the rotated version. The area of the rectangle
can be calculated using the following formula:
(√
) (√
)
𝐴rect =
2 𝑇𝑊 − 𝛥𝑥 ⋅
2 𝑇𝑊 − 𝛥𝑦
(10)
15

EURO Journal on Transportation and Logistics 12 (2023) 100109

C. Ackermann and J. Rieck

References

Jin, G., Cui, Y., Zeng, L., Tang, H., Feng, Y., Huang, J., 2020. Urban ride-hailing demand
prediction with multiple spatio-temporal information fusion network. Transp. Res. C 117, 102665. Kleywegt, A.J., Papastavrou, J.D., 1998. The dynamic and stochastic knapsack problem. Oper. Res. 46 (1), 17–35. Kullman, N.D., 2021. The pyhailing framework. https://pypi.org/project/pyhailing. Kullman, N.D., Cousineau, M., Goodson, J.C., Mendoza, J.E., 2021. Dynamic ride-hailing
with electric vehicles. Transp. Sci. 56 (3), 775–794.

---

**LLM Contextual Output:**

I'll provide a focused analysis of the specific section explaining what this chunk is explaining.

**The exact technical details, parameters, or processes described in this chunk:**

This chunk describes a mathematical formula used to calculate the area of a rectangle that can be determined using coordinate geometry and spatial information. The formula involves the lengths of two sides (TW) and their difference (∛x^2 + y^2), which are calculated first. Then, the area is found by multiplying the result with the difference between these values.

**How this chunk connects to or builds upon the surrounding context:**

This chunk appears to be describing a mathematical approach or methodology used in urban transportation planning and management, specifically for predicting ride-hailing demand. The text mentions that the proposed method simplifies calculations and uses spatial information (coordinate geometry) to calculate the area of a rectangle. This suggests that the chunk is building upon a larger context of dynamic dispatch, real-time management, and simulation of autonomous taxi deployment in Berlin, as mentioned in the surrounding references.

**Any specific requirements, conditions, or constraints mentioned:**

There are no explicit requirements, conditions, or constraints mentioned in this chunk. The text only provides technical details about a mathematical formula used to calculate the area of a rectangle.
