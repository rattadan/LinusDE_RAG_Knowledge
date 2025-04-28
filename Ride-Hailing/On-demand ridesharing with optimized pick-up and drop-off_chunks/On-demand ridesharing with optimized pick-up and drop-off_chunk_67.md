## On-demand ridesharing with optimized pick-up and drop-off - Chunk 67

**Document Summary:**

This reference list covers a wide range of works from 2010 to 2020, focusing on various aspects of ridesharing and mobility-on-demand systems. Here's a summary of the key themes:

### Key Themes:
1. **Rebalancing Strategies**:
   - Wallar et al., van Engelen et al.
   - Wen et al.

2. **Modeling and Mathematical Frameworks**:
   - Zhao et al.
   - Stiglic et al.
   - Tirachini, A. & Gomez-Lobo (2020)
   - Tirachini, A. et al. (2010)

3. **Optimization Heuristics**:
   - Stiglic et al.

4. **Simulation and Service Design**:
   - Vosooghi et al.
   - Spieser et al., Samaranayake et al.

5. **Flexible Transport Services**:
   - van Engelen et al.

6. **Ride-Sharing Systems with Meeting Points**:
   - Zheng et al.

7. **Vehicle Rebalancing for Mobility-on-Demand Systems**:
   - Wallar et al.
   - Vosooghi et al.

8. **Flex-Route Services and Ride-Sharing**:
   - Zhao, M. et al.
   - Stiglic et al.

9. **Reinforcement Learning Approaches**:
   - Wen et al.

10. **Benefits of Meeting Points in Ride-Sharing Systems**:
    - Stiglic et al.
    - Zheng et al.

### Summary of Key Papers:

- **Vosooghi, R., Puchinger, J., Jankovic, M., Vouillon, A. (2019)**: Focuses on shared autonomous vehicle simulation and service design.
- **Zhao, M., Yin, J., An, S., Wang, J., Feng, D. (2018)**: Develops mathematical modeling and decomposition methods for ridesharing problems with flexible pickup and delivery locations.
- **Stiglic, M., Agatz, N., Savelsbergh, M., Gradisar, M. (2015)**: Analyzes the benefits of meeting points in ride-sharing systems.
- **Zheng, Y., Li, W., Qiu, F., Wei, H. (2019)**: Evaluates the benefits of introducing meeting points into flex-route transit services.

### Concluding Remarks:
The papers collectively address critical challenges and opportunities in ridesharing and mobility-on-demand systems through various methodologies, from heuristic optimization to advanced simulation techniques. The inclusion of meeting points is highlighted as a significant factor for improving efficiency and user satisfaction in these systems. The use of reinforcement learning and mathematical modeling further underscores the growing sophistication in managing such dynamic systems.

This reference list provides a comprehensive overview of current research trends and can serve as a basis for further analysis or application development in ridesharing technologies.

**Original Text:**

Each minute, the system accumulates all the requests that have arrived in that lapse, and solves AP considering the current state of
the vehicles. We consider two requests arriving every 15 s. In the base case, requests’ origins and destinations are random (uniformly
13

Transportation Research Part C 126 (2021) 103061

A. Fielbaum et al. Table 2
Results of SMoD with or without optimizing the PUDO points. All times are in minutes. Users’ costs are shown in proportion to the cost of one minute
over the vehicle. Scenario

Walks? Av. waiting

Av. walking

Av. delay

Rejections

Av. cU

VHT

Base

Yes
No
Yes
No
Yes
No
Yes
No

2.15
2.18
2.25
1.96
1.9
2.06
1.92
1.85

2.29
–
2.44
–
2.23
–
2.34
–

3.38
3
2.85
2.68
3.03
3.06
1.74
1.4

5.8%
15%
15%
24.4%
2.92%
4.58%
7.92%
12.1%

14.6
19.36
21.8
26.1
11.4
10.84
14.26
14.78

61.5
70.1
58.3
67.1
53.8
68.4
50.12
61.4

Non-uniform network
Concentrated demand
Non-uniform network &
concentrated demand

Table 3
Performance of the heuristics. All times are in minutes.

---

**LLM Contextual Output:**

**Technical Details and Parameters:**

The technical details mentioned in this chunk include:

* The system accumulates all requests that have arrived within a 15-second window, which is considered as one minute.
* The system considers two requests arriving every 15 seconds, with random origins and destinations for both the sender (requester) and receiver (vehicle).
* The base case scenario shows how users' costs are calculated based on their walking times.

**Context:**

The current text chunk appears to be discussing a ridesharing or mobility-on-demand system that uses a heuristic optimization approach to manage vehicle assignments. The system considers the time it takes for each request to arrive and calculates users' costs accordingly. The analysis is focused on understanding how this system works, particularly in terms of optimizing vehicle assignments.

The context suggests that this chunk may be part of a larger research paper or article that discusses various aspects of ridesharing systems, including their design, optimization techniques, and user experiences. The inclusion of specific papers (e.g., A. Fielbaum et al.) provides additional context and references to other studies on similar topics.

**Connections to Surrounding Context:**

The current text chunk builds upon the surrounding context by:

* Providing more details about the system's operations, including its time-dependent behavior and optimization approach.
* Discussing specific scenarios, such as the base case scenario mentioned earlier, which helps to illustrate how the system works.
* Including references to other studies on ridesharing systems, which suggests that this chunk is part of a broader research effort.

The connections are built through:

* Shared terminology (e.g., "requests," "vehicles," "time-dependent behavior") and concepts (e.g., optimization techniques).
* Familiarity with the context of mobility-on-demand systems and their design challenges.
* References to specific papers and studies, which helps to establish credibility and build upon existing knowledge.

**Requirements and Conditions:**

The requirements and conditions mentioned in this chunk include:

* The need for a system that can efficiently manage vehicle assignments based on time-dependent requests.
* A focus on optimizing user experiences by considering the waiting times for users when requesting transportation.
* The use of heuristic optimization techniques to find optimal solutions within a given time frame.

These requirements and conditions suggest that this chunk is part of a larger research project or paper focused on developing efficient ridesharing systems, where heuristics are used to optimize vehicle assignments in real-time.
