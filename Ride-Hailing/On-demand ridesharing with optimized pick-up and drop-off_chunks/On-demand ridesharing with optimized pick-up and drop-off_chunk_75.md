## On-demand ridesharing with optimized pick-up and drop-off - Chunk 75

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

walking time between contiguous nodes
Max walking time between contiguous nodes
Total number of requests
Av. in-vehicle time between origin and destination
Max in-vehicle between origin and destination
Min in-vehicle between origin and destination
Mean number of passengers per request
Max number of passengers per request
Median {|WD(u)| : u ∈ 𝒱}

53.7 [min]
4.7 [h]
34 [s]
349 [s]
89 [s]
31 [min]
9970
11.61 [min]
43.5 [min]
3 [min]
2.1
6
116 nodes

Max {|WD(u)| : u ∈ 𝒱}

246 nodes

• Searching for the PUDO nodes does not reduce the running time much, and it increases both users’ and operators’ costs: in this
simple graph, the number of feasible nodes is small, so an exhaustive search is fast and better. It should be recalled, however that
this heuristic is meant for very granular graphs, as explained in Section 2.4. All in all, the heuristics prove useful. When we deal with a large instance of the problem in the following subsections, we are using
all the heuristics. 3.1.3.

---

**LLM Contextual Output:**

This text chunk appears to be describing technical details related to ridesharing and mobility-on-demand systems, specifically focusing on the use of heuristic optimization techniques.

**Technical Details:**

* The concept of "walking time" refers to the average travel time between two contiguous nodes in a graph.
* The variables mentioned include:
	+ `Max walking time`: the maximum allowed walking time between any two contiguous nodes.
	+ `Total number of requests`: the total number of ride requests made by users.
	+ `Av. in-vehicle time`: the average time spent in an in-vehicle (i.e., a vehicle traveling between two locations) for each request.
	+ `Max in-vehicle time`: the maximum allowed time spent in an in-vehicle for any request.
	+ `Min in-vehicle time`: the minimum allowed time spent in an in-vehicle for any request.
* The variable `|WD(u)|` represents the distance (or "walking" distance) between two nodes `u` and `v`.

**Context:**

The surrounding context provides a summary of key themes and papers related to ridesharing and mobility-on-demand systems. This includes:

* A list of 10 papers, each addressing a specific aspect of these systems.
* A brief summary of the key papers mentioned in the reference list.

This text chunk is connecting to or building upon the surrounding context by describing the technical details used in heuristic optimization techniques for ridesharing systems. The use of variables such as `Max walking time`, `Av. in-vehicle time`, and `Min in-vehicle time` suggests a focus on optimizing ride request allocation, which is a key aspect of ridesharing systems.

**Requirements, Conditions, or Constraints:**

There are no explicit requirements, conditions, or constraints mentioned in this text chunk. However, the use of heuristic optimization techniques implies that the system is expected to perform well under various scenarios and with varying levels of demand, which may impact performance and efficiency.
