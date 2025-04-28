## On-demand ridesharing with optimized pick-up and drop-off - Chunk 78

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

We will consider one hour of the operation of the
system, just after 1 pm of January 15th, 2013, to have a large number of requests but avoiding the peak, in which trips have a quite
specific direction; we filter those requests in which the origin and destination are too close (less than 3 min by car), as they rarely occur
in real-world on-demand systems (Liu et al., 2019). The system is analyzed over a graph that reproduces the road network of Man­
hattan with 9453 edges and 4092 nodes, that represent the intersections and dead-ends of the streets. Fig. 5 shows heatmaps corre­
sponding where each request departs (left) and arrives (right): the concentration of origins and destinations is much higher in the
center of the network. In-vehicle times represent the real ones at 1 pm. Walking times are calculated proportional to the length of each arc, which are
known as the Manhattan graph provides the geographical coordinates of each node.

---

**LLM Contextual Output:**

The current text chunk is explaining how to analyze a ridesharing system over time, specifically focusing on one hour in January 2013.

### Technical Details:

1. **Graph Representation**: The system is modeled using a graph that represents the road network of Manhattan with 9453 edges and 4092 nodes.
2. **Heatmaps**: Heatmaps are used to represent where each request departs (left) and arrives (right), highlighting high concentrations of origins and destinations in the center of the network.

### Parameters/Processes:

1. The system operates over a specific time frame, one hour from January 15th, 2013.
2. A graph is created to model the road network and simulate ride requests.

### Contextual Connection and Requirements:

This chunk builds upon the surrounding context by providing an overview of ridesharing systems, modeling methodologies (graph representation), and analytical techniques (heatmaps). It also sets the stage for further analysis or application development in ridesharing technologies. The specific requirements mentioned are not explicitly stated but can be inferred from the context:

- **Understanding ride requests**: The text assumes some prior knowledge of how to analyze ride requests, such as identifying high concentrations of origins and destinations.
- **Analyzing system performance**: By analyzing one hour of operation, the reader is prompted to consider real-world on-demand systems and their potential applications.
- **Using graph representation and heatmaps**: The use of a graph-based model (Manhattan network) and heatmaps for visualization suggests that the text aims to explore various techniques in ridesharing system analysis.
