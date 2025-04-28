## Impact assessment of autonomous DRT system - Chunk 15

**Document Summary:**

The paper discusses the potential impact of a fully automated Demand Responsive Transport (DRT) system on traditional public transport operations using Cottbus, Germany as a case study. Here's a summary of key points:

1. **Simulation Approach**:
   - The simulation models both stop-based and door-to-door DRT systems.
   - It evaluates the operational costs, travel times, and vehicle utilization.

2. **Travel Times and Costs Comparison**:
   - **Stop-Based System**: Lower operating costs but higher travel times compared to traditional public transport.
   - **Door-to-Door System**: Further reduced travel times for passengers, potentially cheaper to operate than traditional schedule-based transport when considering driverless operation.

3. **Operational Cost Analysis**:
   - Stop-based system: ~30,191 EUR daily operational cost.
   - Door-to-door system (assuming driverless): ~32,653 EUR daily operational cost.
   - Traditional public transport: Currently serving 5.5 million kilometers annually at a higher cost.

4. **Impact on Public Transport**:
   - The study suggests that DRT systems could operate more efficiently with lower costs, potentially disrupting traditional public transport operations due to competition from MaaS providers.

5. **Potential for Mode Choice and Optimized Operation**:
   - The model assumes users of other modes will remain constant.
   - Future studies should consider how an attractive DRT system might influence mode choice (e.g., drawing car users).

6. **Limitations and Further Research**:
   - The current modeling approach focuses on peak and commuting traffic, which may not fully capture the operational costs under all scenarios.
   - More variations in service models need to be evaluated, such as limited stop usage during peak hours.

7. **Conclusion**:
   - Fully automated DRT systems could be competitive with traditional public transport if designed optimally.
   - The paper highlights that a switch to DRT would require comprehensive planning and integration into broader mobility ecosystems.

Overall, the study provides insights into how autonomous DRT services might reshape urban transportation landscapes, particularly in comparison to existing public transport models.

**Original Text:**

However, this
is subject to two constraints:
• Firstly, the total travel time (= time from request to dropoff) for any other passenger also traveling on the same
vehicle needs to remain under a certain threshold tr ,
r
tr = α tdirect
+β,
r
denotes the direct ride time without detours nor waits, and α and β are parameters to model the
where tdirect
maximal time loss because of waiting, boarding and detours occurring due to the pick-up and drop-off of fellow
passengers. • Secondly, the expected waiting times for the other customers need to remain smaller than a defined time frame
twait . This ensures that customers do not have to wait too long. Note that idle vehicles are included into that computation and can thus be dispatched as a result. It is also possible to
add the new request at the end of an existing vehicle schedule, so that a pickup/dropoff is always possible even under
overload conditions, albeit possibly with a long waiting time. For the request itself, the constraints can be violated.

---

**LLM Contextual Output:**

**Technical Details and Parameters:**

The current text chunk describes two technical parameters:

* `α` and `β`: These are parameters used to model the maximal time loss due to waiting, boarding, and detours when a passenger requests another vehicle that is not immediately available.
* `twait`: This parameter represents the maximum allowed waiting time for other customers.

**Connections to or Building upon the Surrounding Context:**

The current text chunk builds upon the previous context by:

* Providing more details about the simulation approach used in the study, which includes models of stop-based and door-to-door DRT systems.
* Discussing travel times and costs comparison between different scenarios (stop-based vs. door-to-door), highlighting the benefits and drawbacks of each.
* Examining operational cost analysis, including estimates for operating costs under both scenarios.
* Explaining the potential impact on public transport operations, including disruption due to competition from MaaS providers.

The current text chunk also sets the stage for future studies that aim to optimize the operation of DRT systems, considering factors such as mode choice and the influence of attractive MaaS providers on user behavior.

**Specific Requirements, Conditions, or Constraints:**

* The study assumes certain parameters (e.g., `twait`, `α`, `β`) are known, which may require additional data collection or assumptions.
* The simulation models include constraints on travel times for other passengers, ensuring that waiting times remain smaller than a defined threshold (`twait`).
* The use of idle vehicles as part of the computation allows for efficient dispatching even under overload conditions.

Overall, this text chunk provides technical details and context necessary to understand the underlying mechanics of the simulation approach and its implications for public transport operations.
