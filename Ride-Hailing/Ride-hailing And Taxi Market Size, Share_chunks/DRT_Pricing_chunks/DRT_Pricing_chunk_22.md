## DRT_Pricing - Chunk 22

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

3 and the DRT service area is either set to (1) the inner-city Berlin area or (2) the entire
Berlin area. The DRT fare is set to a distance-based fare of 0.35 EUR/km, and the minimum fee is set to (a) 0.00,
(b) 2.00 or (c) 3.00 EUR. All simulation experiments are carried out for two pricing schemes for the car mode: i) no
tolling and ii) with a toll of 0.20 EUR/km. The toll is only imposed on car users and does not affect to DRT vehicles
or DRT users. The simulation results are compared to the base case continued in which there is no DRT mode and no
car toll. Ihab Kaddoura et al. / Procedia Computer Science 170 (2020) 807–812
I. Kaddoura et al. / Procedia Computer Science 00 (2020) 000–000

810
4

4. Results
4.1. DRT speed up

0.35

4200.00

0.3

3600.00
3000.00

Mode share

Computation time [sec]

Using the DRT speed up module has a significant impact on the computational performance. In iterations where the
DRT mode is simulated in a simplified way, the computation time is reduced by approx.

---

**LLM Contextual Output:**

This specific section of text chunk can be analyzed as follows:

1. **Technical details and parameters:** The key parameters mentioned in this chunk are:
   - Vehicle capacity
   - Sharing level
   - Service area coverage (specifically, the DRT service area being set to either Berlin's inner-city or entire city)

2. **Connections to the surrounding context:** This section builds upon the surrounding context by discussing specific aspects of dynamic transport services in Berlin and the development of a simulation model using MATSim for these services. The text also mentions external cost pricing as a mechanism for optimal operation, which is mentioned earlier in the context.

3. **Requirements and conditions:** The key requirement mentioned here is that the DRT speed up module should have a significant impact on computational performance, suggesting that efficient computation of this model would be beneficial or necessary for its use.

This chunk appears to explain how the simulation model's DRT mode affects computation time, specifically in relation to reducing it by approximating simplified scenarios. The analysis aims to provide insights into how the efficiency of the model is affected by the design parameters (vehicle capacity, sharing level, and service area coverage) and how these might be optimized for better computational performance.

Given the context provided, this section contributes to understanding how simulation models can efficiently run complex transportation systems like DRTs by highlighting an important parameter that can impact computation time.
