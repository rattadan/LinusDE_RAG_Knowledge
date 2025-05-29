## Impact assessment of autonomous DRT system - Chunk 14

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

Since the focus in this paper is the public transport demand, the
original simulation model was reduced to only depict those agents using public transport, resulting in a synthetic
population of 11 000 agents.1 In the base case, all of them have at least one trip by public transit per day, whereas in
the policy cases, these were replaced by various forms of demand responsive transport. 3.2. Simulation of Demand responsive transport
MATSim provides a set of extensions to simulate various MaaS systems (?). These include taxi (?), SAVs (?) and
DRT (?). In this paper, the DRT extension is used, which performs a centralized, on-the-fly assignment of vehicles to
passengers as soon as a passenger requests to use the service. Usually, the request is assigned to the vehicle where the
insertion of the request into the planned route will cause the lowest additional vehicle operating time.

---

**LLM Contextual Output:**

**1. Technical Details:**
The chunk describes the simulation approach used in the study, which involves:

* Two types of DRT systems: stop-based and door-to-door.
* Evaluation metrics:
	+ Operational costs
	+ Travel times
	+ Vehicle utilization
* The simulation models use a specific transportation matrix (MATSim) to simulate various MaaS systems, including taxi, SAVs, and DRT.

**2. Context Connection and Building:**
This chunk connects to the surrounding context by:

* Providing an overview of the paper's focus on public transport demand.
* Introducing the simulation model as a key tool for evaluating the impact of DRT systems.
* Allowing readers to understand that the study is exploring how autonomous DRT services might reshape urban transportation landscapes.

**3. Requirements and Constraints:**
The requirements and constraints mentioned in this chunk are:

* The simulation model should be able to evaluate various MaaS systems, including taxi, SAVs, and DRT.
* The study assumes a synthetic population of 11,000 agents for the base case.
* Future studies should consider variations in service models, such as limited stop usage during peak hours.

Overall, this chunk provides technical details about the simulation approach used in the paper, its connection to the surrounding context, and the requirements and constraints mentioned.
