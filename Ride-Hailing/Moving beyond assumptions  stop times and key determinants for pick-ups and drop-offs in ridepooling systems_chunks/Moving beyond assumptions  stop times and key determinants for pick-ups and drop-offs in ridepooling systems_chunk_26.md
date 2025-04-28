## Moving beyond assumptions  stop times and key determinants for pick-ups and drop-offs in ridepooling systems - Chunk 26

**Document Summary:**

The provided reference list appears to be a collection of citations for various research papers, articles, and reports related to ride-pooling services, with a focus on urban transport systems and sustainability. The references cover a range of years from 2013 to 2024, indicating ongoing research in this field.

### Key Themes and Topics:

1. **Ride-Pooling Services**:
   - Various studies discuss the implementation and efficiency of ride-pooling services in different urban contexts.
   - Some references focus on specific companies like Uber, Waymo, and Via Transportation.

2. **Urban Transport and Sustainability**:
   - Several papers explore how shared mobility can reduce traffic congestion and carbon emissions.
   - The sustainability aspect is discussed with a particular emphasis on the impact of platform services on reducing motorized traffic in cities.

3. **Simulation Studies**:
   - Multiple references indicate that simulation tools like MATSim are being used to model ride-pooling strategies and their operational aspects.
   - There is an interest in understanding how different service designs can influence urban ride-pooling systems.

4. **Disparities and Access**:
   - Some studies focus on the disparities in travel times for accessing non-work destinations using ride-hailing services.

5. **Technological Aspects**:
   - References to autonomous vehicles are included, suggesting a growing interest in how technology can influence ride-pooling services.
   - The use of advanced technologies like Waymo's app is highlighted as an example of how these services can be optimized.

### Notable Citations:

- **Tirachini, Alejandro. 2013**: This paper discusses the impact of fare collection systems and bus age on dwell times, which could be relevant for understanding operational aspects of ride-pooling services.
  
- **Zwick, Felix, Nico Kuehnel, Rolf Moeckel, and Kay W. Axhausen. 2021**: This study focuses on the impact of autonomous ride-pooling on traffic noise in a city-wide simulation.

- **Tikoudis et al., 2021**: This research provides evidence from 247 cities on how ridesharing services can reduce motorized traffic and CO2 emissions, highlighting the broader implications of these services for urban transport.

### Conclusion:
The references cover a comprehensive range of topics related to ride-pooling, from its operational aspects to its sustainability impacts. They reflect the current trends in research, including the use of advanced simulation tools and the integration of autonomous vehicles into urban transport systems. This collection would be valuable for researchers, policymakers, and industry professionals interested in understanding and improving shared mobility solutions in urban contexts.

**Original Text:**

in the case of strollers or bicycles)
Number of passengers boarding/alighting the vehicle
0: Passenger was on time at PUDO location
1: Passenger delay at a PUDO location

The variable xPax (Passengers) was treated as a continuous parameter, allowing us to analyze how each additional person boarding or alighting influences stop time. The variable
xWait (Waiting) was only included in the boarding model, as it is not relevant to alighting
stops. We employed a Generalised Linear Model (GLM) with a Gaussian regression to evaluate the impact of specific determinants on stop time, as the majority of the independent
variables included are categorical. Further we used an identity link function for fitting the
continuous dependent variable (stop time). Cumulative distribution
To account for the variability of stop times, the use of a cumulative distribution function
(CDF) can aid in generating a realistic set of stop times. This approach enables to assess the
probability of specific stop times occurring.

---

**LLM Contextual Output:**

**1. Technical details and parameters:**
The chunk provides detailed information about the technical aspects of ride-pooling services, specifically:

- The use of variables such as `xPax` (Passengers) for modeling stop time.
- The employment of a Generalized Linear Model (GLM) with a Gaussian regression to analyze the impact of specific determinants on stop time.
- The inclusion of an identity link function for fitting the continuous dependent variable (stop time).
- The use of a cumulative distribution function (CDF) to account for variability in stop times.

**2. Connection to surrounding context:**
The chunk connects to the surrounding context by:

- Discussing ride-pooling services as a form of shared mobility, which is a key theme in the document.
- Mentioning specific companies like Uber and Via Transportation, which are mentioned in the Key Themes and Topics section.
- Referencing simulation studies (e.g., MATSim) used to model ride-pooling strategies and their operational aspects.

**3. Requirements, conditions, or constraints:**
The chunk does not explicitly state any technical requirements or constraints, but it assumes:

- A familiarity with Generalized Linear Models (GLMs) and Gaussian regression.
- An understanding of the concept of cumulative distribution functions (CDFs).
- The availability of software such as R for data analysis.

To address these requirements or constraints, further discussion or explanations would be necessary.
