## DRT_Pricing2 - Chunk 98

**Document Summary:**

Here is a summary of the key points from the reference text related to ride-hailing systems and their operations:

- Various studies have explored how autonomous taxis could replace private cars in urban areas (Bischoff, Maciejewski 2016; Al-Kanj et al. 2020).

- Dynamic trip-vehicle assignment is an important aspect of on-demand ride-sharing systems (Alonso-Mora et al. 2017). 

- Spatio-temporal demand forecasting and fleet management are critical for optimizing shared autonomous mobility fleets (Dandl et al. 2019; De Souza et al. 2020).

- Optimization-based strategies have been proposed for repositioning shared autonomous vehicle fleets to meet demand (De Souza et al. 2020). 

- Reinforcement learning techniques are being used for real-world vehicle repositioning in ride-hailing systems (Jiao et al. 2021; Guo et al. 2021).

- Empty-car routing and management is an important aspect of ridesharing operations (Braverman et al. 2019).

- Multi-taxi dispatch algorithms have been developed for mobile taxi-hailing systems (Gao et al. 2016). 

- Agent-based modeling has been used to study the travel and environmental impacts of shared autonomous vehicles (Fagnant, Kockelman 2014).

- Simulation studies have evaluated strategies for city-wide replacement with autonomous taxis (Bischoff, Maciejewski 2016).

- Various dynamic optimization models have been proposed to manage fleet operations in response to real-time demand signals (Ho et al. 2018; Hyland, Mahmassani 2018).

In summary, there is a substantial body of research focused on optimizing the operations of shared autonomous ride-hailing systems through advanced modeling and algorithmic approaches. The key areas include fleet management, vehicle repositioning, demand forecasting, and dynamic routing. Machine learning techniques are increasingly being applied to these problems.

**Original Text:**

Zone overlap using Euclidean distances. Acknowledgments
This work was supported by the Federal Ministry of Education and
Research of Germany in the framework of the research project ‘‘L2O:
Learning to Optimize’’ (01IS20013A). Appendix A. Modified undersupply probability calculation
The following formula shows the probability of more demand than
supply in a given zone based on the Poisson distribution:
𝑝undersupply =

∞
∑
𝑑 𝑘 𝑒−𝑑
𝑘! 𝑘=𝑠+1

=1−

𝑠
∑
𝑑 𝑘 𝑒−𝑑
𝑘=0

𝑘! In larger instances, the term 𝑘! can get bigger than most inbuilt
datatypes are able to handle. To prevent this problem, we replaced the
term 𝑘! with Stirling’s approximation. To prevent division by zero, we
only replace 𝑘! for 𝑘 > 0:
( )𝑘
√
𝑘
𝑘! ≈ 2𝜋𝑘
)
( 𝑒
𝑠
𝑑 0 𝑒−𝑑 ∑ 𝑑 𝑘 𝑒−𝑑
𝑝undersupply = 1 −
+
0! 𝑘! 𝑘=1

Fig. 8. Zone overlap using Manhattan distances. matching is close to zero, when there are only few requests (because of the small demand-supply-ratio and/or the short waiting
period for more requests).

---

**LLM Contextual Output:**

Analysis of the provided text chunk:

**Exact technical details, parameters, or processes described:**

* The formula to calculate the undersupply probability using Poisson distribution:
  - `𝑝undersupply = 1 − ∑( 𝑑 𝑘! (𝑘 = 0) / 𝑘!)`
  - `Stirling’s approximation: (𝑘/√𝑘)! ≈ 2𝜋𝑘`
* The formula to calculate the zone overlap using Manhattan distances:
  - `Fig. 8. Zone overlap using Manhattan distances.`

**Connection to or building upon the surrounding context:**

This chunk is part of a larger section discussing optimization techniques for ride-hailing systems, specifically focusing on dynamic trip-vehicle assignment, spatio-temporal demand forecasting, and fleet management. The text is building upon concepts introduced in earlier sections related to machine learning techniques and their application in optimizing shared autonomous vehicle fleets.

**Requirements, conditions, or constraints mentioned:**

* No specific requirements are mentioned for the readers; this is a technical analysis of existing research.
* The Federal Ministry of Education and Research of Germany provided funding for the research project '‘L2O: Learning to Optimize’’ (01IS20013A), which implies that there may be further funding or resources available for future studies.
