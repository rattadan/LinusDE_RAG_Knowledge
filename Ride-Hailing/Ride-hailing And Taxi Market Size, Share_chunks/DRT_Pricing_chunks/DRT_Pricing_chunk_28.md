## DRT_Pricing - Chunk 28

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

In contrast, a larger DRT service area increases the modal shift from
car to DRT. The setup in which DRT vehicles operate inside the entire Berlin area, a higher minimum fee translates
into a higher share of users switching from car to DRT. Nevertheless, the share of users switching from car to DRT is
rather minor compared to the number of users switching from PT to DRT. (a) Minimum fee: 0.00 EUR
No car toll
DRT trips: 255,030

(b) Minimum fee: 2.00 EUR
No car toll
DRT trips: 28,680

(c) Minimum fee: 3.00 EUR
No car toll
DRT trips: 3,770

(d) Minimum fee: 3.00 EUR
With car toll
DRT trips: 6,560

Fig. 2: Previously chosen mode by DRT users – DRT service area: Inner-city Berlin area

(a) Minimum fee: 0.00 EUR
No car toll
DRT trips: 502,0401

(b) Minimum fee: 2.00 EUR
No car toll
DRT trips: 88,390

(c) Minimum fee: 3.00 EUR
No car toll
DRT trips: 35,340

(d) Minimum fee: 3.00 EUR
With car toll
DRT trips: 88,650

Fig.

---

**LLM Contextual Output:**

**Technical Details and Parameters:**

The current text chunk is discussing the setup of a Dynamic Retail Transport (DRT) service area in Berlin, with specific details about the minimum fees associated with using DRT vehicles versus traditional public transit (PT) services.

- **Minimum fee:** The minimum fee for using DRT vehicles is set at 0.00 EUR.
- **No car toll:** There is no car toll associated with using DRT trips.
- **DRT trips:**
  - With the minimum fee: 502,040 trips
  - Without the minimum fee: 88,390 trips

**Connection to or Building Upon Surrounding Context:**

This chunk builds upon and expands on the initial text by providing specific data about the setup of a DRT service area in Berlin. This information is crucial for understanding how different scenarios affect system performance metrics such as passenger waiting times and travel speeds.

The text also establishes the context for evaluating welfare effects of shared autonomous vehicles at scale, which is mentioned later in the paper (point 8). The discussion on minimum fees and their impact on DRT trips serves as a foundation for exploring more complex aspects of mobility services in urban areas with emerging technologies like self-driving cars and ride-sharing fleets.

**Specific Requirements, Conditions, or Constraints:**

- **Data accuracy:** The text assumes the availability of data from the OpenBerlin dataset.
- **Minimum fee consistency:** The minimum fee is consistently applied across different scenarios (a-d).
- **Model assumptions:** The model's behavior, such as car tolls and service area coverage, are assumed without explicit explanations or justifications.

Overall, this chunk provides technical details about the setup of a DRT service area in Berlin and its implications for mobility services.
