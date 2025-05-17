## Chunk 28

**Original Text:**

In contrast to [4], the proposed approximation approach accounts for the specific
characteristics of the DRT module (for example the DRT pricing scheme) and only approximates the DRT mode,
whereas, all other modes are simulated without any modification. During the first n iterations, the DRT mode is only
simulated in detail every k iterations. In between these iterations, the DRT mode is simulated in a simplified way
without running the assignment of DRT vehicles and users on the network. Instead, user costs are approximated as
follows:
• The DRT trip travel time is calculated based on the beeline distance and an average beeline speed which is obtained from the detailed DRT simulation. The average beeline speed is updated every k iterations and considers
the time passengers spend inside the DRT vehicles as well as the time passengers spend waiting for a DRT
vehicle.

---

**LLM Contextual Output:**

Here's a possible way to summarize this information:

The proposed approximation approach in contrast to the original method used in [4] differs in several key ways. Specifically, it only simulates the Detailed Real-Time (DRT) mode, while other modes are simulated with less detail or without modification. 

In particular, during the initial stages of the simulation, the DRT mode is simulated in greater depth at regular intervals (k iterations). However, once this initial phase is complete, the DRT mode is approximated and simplified to a lower level of detail, focusing on user costs rather than the assignment of vehicles and users on the network.
