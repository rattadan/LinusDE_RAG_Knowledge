## Chunk 7

**Original Text:**

​
Current Skip Go Integrator
Ensuring Eureka works with your Skip Go integration is the same easy process as any other bridge! Changes are as follows:

eureka_transfer Operation type to be expected to be returned from the /route and /msgs_direct endpoints
eureka_transfer Transfer type to be expected to be returned from the /status endpoint in the transfer sequence
eureka bridge type returned from the /bridges endpoint
To keep Eureka opt-in, integrators must pass eureka into the experimental_features array in the /route and /msgs_direct calls to enable Eureka routing
What this looks like for each type of Skip Go integration:

If you’re using the Widget, make sure you’re updated to version 3.5.0 or above and pass in eureka to the experimentalFeatures prop. If you’re using the Client Library, make sure you’re updated to version 0.16.22 or above and pass in eureka to the experimentalFeatures param. If you’re integrated directly with the REST endpoints, you can find the relevant types in the API reference for the Route Operation and for the Lifecycle Tracking Transfer. Eureka
Security properties
Depending on where it is deployed, IBC Eureka might have different security properties compared to the ones in IBC Classic.

---

**LLM Contextual Output:**

It appears that there are some changes to the current Skip Go Integrator setup in relation to using Eureka with your integration:

1. **Operation type and transfer type**: Changes are required for the operation type and transfer type returned from `/route` and `/msgs_direct` endpoints.

2. **Eureka bridge type**: The eureka_bridge_type is now expected to be returned from the `/bridges` endpoint, which is different from the previous versions where it was passed directly as an argument in the routes and msgDirect calls.

3. **eureka opt-in**: To enable Eureka routing for your integration, you need to pass `eureka` into the `experimentalFeatures` prop (Widget) or `experimentalFeatures` param (Client Library). 

4. **Dependence on deployment location**: The security properties of Eureka might vary depending on where it is deployed.

To summarize:

- Update your code to match these changes:
    - For Widget: Pass `eureka` into the `experimentalFeatures` prop with a version higher than 3.5.0.
    - For Client Library: Use the `experimentalFeatures` param and pass `eureka` as an object with the required properties (version, etc.) and values.

By making these changes, you should be able to successfully integrate Skip Go with Eureka according to the current guidelines provided.
