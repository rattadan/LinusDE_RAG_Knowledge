## On-demand ridesharing with optimized pick-up and drop-off - Chunk 53

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

Passenger A by itself could be
feasibly served by four vehicles, and some of them can also serve larger groups, including passengers B and C. The heuristic only
looks at the costs of transporting A alone (second column), leading to erase (marked as red in Table 1) v4 because its cost exceeds
mean({(1,1.5,1,2)}) + 1 ⋅ std({(1,1.5,1,2)}). Note that in the last row of the bottom matrix, the costs of the matching v4 with any
other group containing A are not even computed, which is why this heuristic saves computational time. • Limiting sequences: When calculating cost(τ,v), we limit the number of sequences even further (besides the insertion heuristic). To
decide the sequence, recall that we are inserting the requests one by one, so we should decide a position i for the pick-up in which
the vehicle is not full and a position j⩾i +1 for the drop-off.

---

**LLM Contextual Output:**

This text chunk describes a technical solution for optimizing ride-hailing systems, specifically focusing on how to serve multiple passengers using a minimum number of vehicles.

The exact technical details are as follows:

* The heuristic only looks at the costs of transporting one passenger alone (second column) and chooses not to transport them (`erase` flag `red`) due to high costs.
* When calculating the cost of matching two passengers with available vehicles (`cost(τ,v)`), a sequence limit is applied, where we decide the position for the pick-up (`i`) such that the vehicle is not full and a position `j⩾i +1` is chosen for the drop-off.

This chunk builds upon the surrounding context by:

* Providing specific details about the heuristic (looking at costs of transporting one passenger alone) and its limitations (limiting sequences).
* Showing how this solution applies to multiple passengers (` Passenger A by itself could be feasibly served by four vehicles...`) and can handle larger groups, including passengers B and C.

The context requires consideration of several requirements:

* Computational efficiency: The heuristic should save time computational.
* Flexibility: The system should be able to accommodate various passenger requests (four vehicles for one passenger).
* User satisfaction: Meeting points are highlighted as a key factor in improving user experience.
* Mathematical modeling and simulation: The solution relies on mathematical models (sequences, cost calculations) to optimize ride-hailing systems.

The context also mentions specific requirements and conditions:

* Mathematical modeling and decomposition methods should be used for ridesharing problems with flexible pickup and delivery locations.
* Meeting points are a significant factor in improving efficiency and user satisfaction in flex-route transit services.
