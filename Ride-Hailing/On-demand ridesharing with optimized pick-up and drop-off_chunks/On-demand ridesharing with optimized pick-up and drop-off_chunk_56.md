## On-demand ridesharing with optimized pick-up and drop-off - Chunk 56

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

This heuristic reduces
the set of pick-up candidates to the nodes u that, besides being walking-reachable (tw (or , u)⩽Ωa ), verify the following condition:
there exists a path P = x0 , …, xκ , with x0 = or and xκ = u, such that
c(r, v, i, j, xi+1 , d)⩽c(r, v, i, j, xi , d), ∀i = 0, …, κ − 1
I.e., there is a walking path that, assuming no walking in the drop-off, diminishes the induced cost in every step. The set of can­
didates for the drop-off can be expressed analogously. Algorithm 3. Local search to decide drop-off’s position given pick-up’s position. 1: ji = i + 1

2: forj = i + 2…l + 2do
3: %l is the number of stops prior to this insertion
′

4: if Vehicle v was not full between j − 1 and j ∧ cost(r, v, i, j , or , dr )⩽cost(r, v, i, j − 1, or , dr )
′

′

′

′

5: ji = j ;
6: else
7: break;
8: end if
9: end for
′

Algorithm 4. Local search to decide PUDO points. 1: CO = CD = ∅; o = or , d = dr ;%CO and CD will be the candidates set for the pick-up and the drop-off point, respectively.

---

**LLM Contextual Output:**

This specific text chunk is explaining a heuristic algorithm used in ridesharing systems to reduce the number of potential pick-up candidates.

**Technical Details:**

The algorithm reduces the set of pick-up candidates based on a condition that there exists a walking path (P = x0 , …, xκ , with xi+1 , such that c(r, v, i, j, xi+1 , d)⩽c(r, v, i, j, xi , d), ∀i = 0, …, κ − 1. This means it considers the cost of reaching a potential pick-up candidate from the current position.

**Connectivity to surrounding context:**

This chunk is building upon the understanding that in ridesharing systems, the key challenge lies in efficiently selecting a set of potential pick-up candidates from a larger pool. By considering walking paths, this algorithm helps narrow down the selection process.

**Specific requirements and constraints:**

The algorithm requires:

- The ability to compute walking costs (c(r, v, i, j , or , dr ))
- A way to determine whether there is a path with minimal cost (≤ Ωa ) between two nodes u and v.
- The ability to handle different types of vehicles (r) and locations (or ).
- The capacity constraint for vehicles (d).
- The presence of drop-off points (v), which are often determined by the system's design.

The algorithm is designed to reduce the number of potential pick-up candidates, making it a crucial step in efficient ridesharing optimization.
