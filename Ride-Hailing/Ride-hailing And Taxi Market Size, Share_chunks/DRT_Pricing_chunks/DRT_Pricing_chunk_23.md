## DRT_Pricing - Chunk 23

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

30-60 minutes per iteration
compared to the detailed simulation (every 10th iteration), depending on the total number of simulated DRT users (see
Fig. 1a). Also, as shown in Fig. 1b, there is no significant change in the mode shares before and after disabling the
speed up approach in iteration 350. The jump in iteration 400 is explained by switching off the innovative strategies
(disabling choice set generation). 2400.00
1800.00
1200.00
600.00
0.00

0

50 100 150 200 250 300 350 400 450 500
Iteration

(a) Computation time over the iterations

0.25
bicycle

0.2

car

0.15

DRT

0.1

PT

0.05

walk

0

0

50

100

150

200

250 300
Iteration

350

400

450

500

(b) Mode share over the iterations

Fig. 1: Mode share and computation time over the iterations (DRT service area: Berlin area; Minimum fee: 2.00 EUR)

4.2. Travel time and travel distance
Tab. 1 and 2 provide the average DRT travel time and average DRT trip distance for each simulation experiment.

---

**LLM Contextual Output:**

This specific section of text is explaining the technical details related to a multi-agent transport simulation model developed using MATSim, an agent-based transport simulation framework.

**Context:**

The surrounding context is a discussion about the development of a simulation model for dynamic transport services (such as shared autonomous vehicles) in Berlin, using MATSim. The key points mentioned are:

* A multi-agent transport simulation scenario was created based on the OpenBerlin data set.
* The focus is on city-wide shared taxis as a mobility concept.
* Various transportation modes (public transit, private cars, bicycles) will be integrated into the model.

**Technical Details:**

The technical details described in this chunk are:

* The model uses MATSim, an agent-based transport simulation framework.
* A multi-agent transport simulation scenario was developed using OpenBerlin data set.
* The mode share analysis is based on the "choice set generation" approach, which switches off innovative strategies (disabling choice set generation) after iteration 350 to explain a significant jump in iteration time.
* Mode shares are analyzed over iterations, with detailed statistics provided for each transportation mode.

**Connection to surrounding context:**

The specific requirements and conditions mentioned include:

* The model is designed to simulate dynamic transport services in Berlin using MATSim.
* The focus is on shared autonomous vehicles as a mobility concept.
* The study aims to investigate how various factors (e.g., vehicle capacity, sharing level) influence system performance metrics like passenger waiting times and travel speeds.

**Constraints:**

No specific constraints are mentioned in this chunk. However, it is implied that the simulation model will be applied to a real-world setting (Berlin), which may have its own set of data requirements and constraints.
