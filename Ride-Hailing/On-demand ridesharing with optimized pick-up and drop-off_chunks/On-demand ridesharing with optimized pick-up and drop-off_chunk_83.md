## On-demand ridesharing with optimized pick-up and drop-off - Chunk 83

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

Computational time can be further reduced by
tightening β in the Filtering vehicles heuristic. Let us analyze the results in more detail, focusing on the base scenario admitting walks. Fig. 6 shows histograms corresponding to
the waiting time, walking time and delay for each request. In Fig. 6b), we only include requests that do walk. There are a few requests
with negative delay, which happens because walking the first or last leg might reduce total traveling time in some very specific
conditions, e.g., when an arc can be toured faster walking than by car. Fig. 6a) shows that some passengers have negligible waiting
time, and that the histogram then decreases towards the maximum waiting time (5 [min]) but slowly, such that there are about one
thousand of requests in the highest categories. Figs. 6b), on the other hand, reveal that walking time and total delays tend to
concentrate much more around lower values. This suggests that Ωw plays the most relevant role determining the rejected requests.

---

**LLM Contextual Output:**

This specific text chunk is explaining how to optimize vehicle rebalancing in ridesharing systems using a heuristic called Filtering vehicles.

Here's a focused analysis of what this chunk is explaining:

1. **Technical details:** The technique being described is filtering, which involves selecting requests based on certain criteria, such as walking time and waiting time.
2. **Contextual connection:** This chunk builds upon the surrounding context by providing more information about ridesharing systems, optimization strategies, and mathematical frameworks used in the field of transportation.
3. **Requirements and conditions:** The requirements for using this technique are that requests must walk (i.e., move on foot or cycle) and there should be a certain threshold (β) for filtering vehicles.

This chunk can be further broken down into specific details:

* Filtering vehicles heuristic: A common optimization strategy used in ridesharing systems to reduce wait times.
* Parameters:
	+ β (beta): A parameter that determines the minimum waiting time for requests before they are filtered out.
	+ Walking time and walking distance: Variables that affect travel time, which are likely calculated based on user input or historical data.
* Examples of successful scenarios: The text shows examples of how filtering works in practice by highlighting successful cases where walking reduces total traveling time.
* Limitations and considerations: The text mentions some potential limitations and considerations for using this technique, such as the need to balance between walkability and travel speed.

In terms of connecting to or building upon the surrounding context:

* This chunk is part of a broader discussion on ridesharing systems and optimization strategies.
* It builds upon previous discussions about mathematical frameworks (e.g., modeling, simulation) used in transportation systems.
