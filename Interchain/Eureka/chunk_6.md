## Chunk 6

**Original Text:**

For the quickest and easiest integration, you can integrate the Widget in minutes! For more control over the UI you provide your users, the Client Library is the way to go. The integration provides a one-click experience for users to transfer assets across the Eureka ecosystem and beyond in a single integration (via Skip Go’s aggregation and composability engine). ​
Current Skip Go Integrator
Ensuring Eureka works with your Skip Go integration is the same easy process as any other bridge! Changes are as follows:

eureka_transfer Operation type to be expected to be returned from the /route and /msgs_direct endpoints
eureka_transfer Transfer type to be expected to be returned from the /status endpoint in the transfer sequence
eureka bridge type returned from the /bridges endpoint
To keep Eureka opt-in, integrators must pass eureka into the experimental_features array in the /route and /msgs_direct calls to enable Eureka routing
What this looks like for each type of Skip Go integration:

If you’re using the Widget, make sure you’re updated to version 3.5.0 or above and pass in eureka to the experimentalFeatures prop.

---

**LLM Contextual Output:**

This appears to be a documentation about the integration process for the Skip Go service with the Eureka protocol. Specifically, it explains the changes required for integrators to use the Skip Go bridge with Eureka.

To summarize:

* The /route and /msgs_direct endpoints will now expect eureka in their return operations.
* The /status endpoint will also expect eureka transfer type in its response.
* The eureka bridge type returned from the /bridges endpoint will require passing eureka to the experimental_features array.

For users of the Widget, this implies that:

* To take advantage of Eureka's aggregation and composability engine for asset transfers, they must update their integration version to 3.5.0 or above.
* They need to pass `eureka` as an option in their /route and /msgs_direct calls to enable Eureka routing.

It seems that the current Skip Go integrator has been updated to accommodate Eureka's changes, allowing for a more seamless experience with Eureka integration.
