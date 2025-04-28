## On-demand ridesharing with optimized pick-up and drop-off - Chunk 31

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

This issue can be quite relevant: for instance, numerical simulations by Fielbaum and Alonso-Mora (2020) show that more than 30% of
the passengers face some change before completing their trips, with some users facing up to six changes, and that forbidding any
route’s update that increases a previous passenger’s waiting time might yield a relative increase on the rejection rate of about 45%. There are different ways to face this trade-off, all of them compatible with the general method we are explaining here. When we run
the numerical simulations (Section 3), we explain the specific rules that we assume. Throughout the paper, we use tw (r, v, i, j, o, d) to denote the waiting time experienced by request r if it is inserted in the vehicle v,

6
In this reference, they call trip what we define below as a group, and they include the requests in the graph, which implies that the respective
graph is denoted RTV instead of GV

6

Transportation Research Part C 126 (2021) 103061

A. Fielbaum et al.

---

**LLM Contextual Output:**

This specific text chunk appears to be explaining a technical detail related to ridesharing systems, specifically how they can be optimized using mathematical modeling and simulation techniques.

Here's a focused analysis of the technical details:

* **Numerical simulations**: The text mentions that numerical simulations (Section 3) are used to analyze the impact of changing routes on passenger waiting times. Specifically, Fielbaum and Alonso-Mora (2020) conducted numerical simulations that showed how changes in route updates can affect passenger waiting times.
* **Waiting time representation**: The text explains that the waiting time experienced by a request is denoted as "tw" (r, v, i, j, o, d). In this context, "r" represents the request, "v" represents the vehicle, "i" and "j" represent the location of the request and the route it belongs to, "o" and "d" represent the origin and destination of the trip.
* **Graph representation**: The text also mentions that a graph is used to represent the trips and their connections. In this context, the graph RTV represents the trips and their corresponding requests.

Regarding how this chunk connects to or builds upon the surrounding context:

The current text chunk is connected to the broader context by highlighting the importance of mathematical modeling and simulation techniques in optimizing ridesharing systems. This is because the issue can be relevant for understanding the impact of changing routes on passenger waiting times, which is a critical aspect of ridesharing.

Additionally, this chunk builds upon the surrounding context by providing technical details about numerical simulations, graph representations, and waiting time models. These concepts are essential for analyzing the complexities of ridesharing systems and developing effective optimization strategies.

Finally, the text chunk also sets the stage for further analysis or application development in ridesharing technologies. The inclusion of meeting points is highlighted as a significant factor for improving efficiency and user satisfaction in these systems, which suggests that there may be opportunities for exploring new approaches to optimizing routes and managing passenger wait times.
