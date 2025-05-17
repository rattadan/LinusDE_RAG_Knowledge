## DRT_Pricing2 - Chunk 90

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

For short maximum
waiting time constraints, 2–3% fewer requests can be served; for longer
waiting time constraints, only 1% fewer requests can be served. The
iterative zone balance as well as the global matching strategy can save
around 40% of repositioning costs. However, these strategies also lose
4–6% of served requests when repositioning is done less often. Are there notable differences between many and few available
parking lots? The more parking lots there are, the closer the setting is
to free-floating systems, where vehicles are allowed to idle everywhere. In addition to the 𝐿 = 300 lots used for the main experiments, we also
tested 𝐿 = 50 lots, increasing the average distance between any given
point and its closest lot from 300 m to 750 m. The results show that
fewer lots generally decrease the service rate and increase the waiting
time by up to 50%. This is expected because the average distance to the
pickup locations increases.

---

**LLM Contextual Output:**

This text chunk describes a specific technique for managing empty-car routing in ride-hailing systems, which involves using an iterative zone balance strategy along with a global matching strategy.

**Technical Details:**

* The iterative zone balance strategy aims to optimize the distribution of available parking spots across multiple lots.
* The global matching strategy is used to match vehicles with the closest available parking lot.

**Context Connection and Building upon Surrounding Context:**

This chunk builds upon the surrounding context by:

1. Providing a summary of key research areas related to ride-hailing systems, including fleet management, vehicle repositioning, demand forecasting, and dynamic routing.
2. Specifically addressing the problem of empty-car routing in shared autonomous ride-hailing systems, which is a critical aspect of optimization.

**Specific Requirements, Conditions, or Constraints:**

* The constraint mentioned is that waiting time constraints affect the number of requests that can be served, with 2-3% fewer requests being able to be served for shorter waiting times and 1% fewer requests being able to be served for longer waiting times.
* Another constraint is that repositioning costs must be minimized while maintaining a certain level of service rate.

This text chunk provides specific technical details about the iterative zone balance strategy and global matching strategy used in managing empty-car routing in ride-hailing systems, as well as connections to broader research areas related to ride-hailing operations.
