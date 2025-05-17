## DYNAMIC RIDE-SHARING IMPACTS OF GREATER TRIP DEMAND AND - Chunk 14

**Document Summary:**

Thank you for sharing this reference list on shared autonomous vehicle fleet performance. This appears to be a comprehensive collection of scholarly articles and reports that discuss various aspects of shared autonomous vehicles, including their potential impacts on urban transportation systems, consumer preferences, and operational strategies.

The references cover a range of topics such as:

1. Congestion pricing with self-driving cars
2. Parking needs for shared fleets 
3. Consumer preferences for ride-sharing vs individual vehicle use
4. Optimization techniques to improve ridesplitting services
5. Effects on vehicle ownership and emissions
6. The "peak car" phenomenon and electric mobility services

The timeframe spans from 2014 to 2020, capturing recent developments in the field. Key authors include K.M. Kockelman, J.W. Ward, M. Yan, T. Stoiber, et al.

If you need any specific information extracted or have questions about these references, please let me know! I'd be happy to provide more details on particular studies or analyze trends across the papers.

**Original Text:**

If an SAV was not idle, a measure of
directionality was calculated as the angle between the Euclidian OD lines joining the ongoing
and proposed trips using XY coordinates. A threshold for angle between these two Euclidian
lines was provided as an input to the model. If the ongoing trip was picking up or dropping off
another traveler near the new request, the requirement was waived. If more than one occupant
was riding the SAV, then the ongoing trip was based on the current SAV task (either a pickup or
a dropoff). This instantaneous match was supported by a Euclidian distance-based constrained shortest path
across all assigned pickups and drop-offs. Each time a new traveler was added to the traveling
party, an R-tree implementation was used to construct the ordering of pickups and drop-offs that
minimized total distance while taking into account whether travelers were picked up before they
are dropped off.

---

**LLM Contextual Output:**

This specific section is explaining the technical details behind calculating directionality in shared autonomous vehicle (SAV) fleets, specifically using Euclidean OD lines joining ongoing trips.

Here's a focused analysis:

**Technical Details:**

* The calculation uses X and Y coordinates to create Euclidean OD lines.
* A threshold angle between these lines is provided as input to the model.
* If an SAV is not idle or picking up/dropping off another traveler near the new request, the requirement for instantaneous matching is waived.

**Connection to Surrounding Context:**

This chunk connects to the surrounding context by providing a detailed description of how directionality calculations are performed in shared autonomous vehicle fleets. It sets the stage for understanding how these calculations relate to other aspects of SAV operations, such as ride-splitting services and peak car theory.

**Requirements, Conditions, or Constraints:**

* The requirement for instantaneous matching when an SAV is not idle or picking up/dropping off another traveler near the new request implies that this calculation must be performed rapidly in response to changes in trip dynamics.
* The use of a Euclidean distance-based constrained shortest path across all assigned pickups and drop-offs suggests that this calculation may be sensitive to the distribution of travelers within the fleet.

By analyzing this section, we can gain insights into the technical details involved in calculating directionality in shared autonomous vehicle fleets, as well as the context in which these calculations are performed.
