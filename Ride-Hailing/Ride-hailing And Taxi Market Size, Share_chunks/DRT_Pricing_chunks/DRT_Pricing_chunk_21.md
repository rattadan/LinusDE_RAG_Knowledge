## DRT_Pricing - Chunk 21

**Document Summary:**

This paper discusses the development of a simulation model for dynamic transport services (such as shared autonomous vehicles) in Berlin using MATSim, an agent-based transport simulation framework. The key points are:

1. A multi-agent transport simulation scenario was developed based on the OpenBerlin data set.

2. It focuses on city-wide shared taxis as a mobility concept.

3. The model includes integration of various transportation modes (public transit, private cars, bicycles).

4. Key parameters examined include vehicle capacity, sharing level, and service area coverage.

5. The study investigates how these factors influence system performance metrics like passenger waiting times and travel speeds.

6. External cost pricing is proposed as a mechanism for optimal operation in an autonomous vehicle future.

7. Case studies were conducted using the model to analyze specific scenarios.

8. The model can be used to test different dynamic routing algorithms for on-demand transport services.

9. It provides a basis for evaluating welfare effects of shared autonomous vehicles at scale.

The authors suggest their approach could help inform policy decisions regarding future mobility systems in urban areas with emerging technologies like self-driving cars and ride-sharing fleets.

Key references include:

- Fourie's chapter on multi-modeling in MATSim 
- Bösch et al. on cost analysis of AVs
- Horni et al. on the MATSim framework

The paper contributes to research on simulating autonomous mobility services, integrating various transport modes in city-wide models, and evaluating welfare impacts. If you need more details or specific citations from the text, let me know!

**Original Text:**

trip chains starting and ending at the same activity location, the transport mode
may be changed to only car, only bicycle (chain-based modes) or a combination of public transit, DRT and walk for
each trip within the sub-tour. The ride mode is fixed, i.e. transport users are not enabled to switch from or to the ride
mode. In this study, intermodal trips are not accounted for. Each agent’s choice sets is limited to 5 travel plans. All
simulation experiments are run for a total of 500 iterations. During choice set generation (first 400 iterations), in each
iteration the share of agents who change their mode, route and departure time (innovative strategies) is set to 5% per
choice dimension. In the final 100 iterations, all agents select from their choice sets based on a multinomial logit
model. Utility parameters for the different modes are set similar to [9]. Simulation experiments. In different simulation experiments, the DRT mode is added as an additional mode of transportation as described in Sec.

---

**LLM Contextual Output:**

**Technical Details and Parameters**

The current text chunk describes a specific technical detail within the context of simulating dynamic transport services (such as shared autonomous vehicles) using MATSim.

* **Trip chains**: The study focuses on trip chains that start and end at the same activity location, allowing for analysis of various transportation modes.
* **Transport mode change**: The transport mode can be changed to only one of the following: car, bicycle, or a combination of public transit, DRT (Direct Regional Transit), and walk. This is achieved through chain-based modes (i.e., changing between two specific modes within the same trip).
* **Ride mode fixedness**: The ride mode is fixed for each individual transport user, meaning they cannot switch from one mode to another.
* **Choice set limitations**: Each agent's choice set is limited to 5 travel plans. This limitation affects the innovative strategies explored in this study.

**Connection to and Building upon Surrounding Context**

This chunk builds upon the surrounding context by:

* Providing more details on the transportation modes included in the simulation (public transit, DRT, walk, car, bicycle)
* Explaining how these modes are integrated within trip chains
* Describing the fixed ride mode for transport users

**Requirements and Conditions**

The text requires:

* Access to the MATSim agent-based transport simulation framework for the purpose of simulating dynamic transport services in Berlin.
* The availability of the OpenBerlin data set, which is likely used as a basis for the multi-agent transport simulation scenario.
* A multinomial logit model (mentioned in section 7) that can be used for utility parameters.

In terms of conditions or constraints:

* The study assumes access to a suitable transportation data set and the necessary computational resources to run the simulation experiments.
* The authors likely require permission from relevant authorities to use the OpenBerlin data set, which may involve obtaining necessary licenses or permissions.
