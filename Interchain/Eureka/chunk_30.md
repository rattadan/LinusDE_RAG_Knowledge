## Chunk 30

**Original Text:**

​
Execution Messages
Supports a “Swap Exact In” method where a user specifies an input asset and path to swap, and the module / contract swaps the given user asset to the user’s desired output asset and sends it to the user (see Osmosis for a module example, or Astroport for a contract example). Inputs into the swap:
An asset (Native cosmos coin or CW20 token, incl. denom and amount)
A path (can be a single pool, or multiple pools if designed like a router)
Outputs of the swap:
An asset
NICE TO HAVE (Optional): Supports a “Swap Exact Out” method where a user specifies a desired output asset, a path to swap through to achieve that asset, and a maximum amount of an input asset to swap, and the module / contracts swaps in the exact input asset needed to acquire the specified output asset and sends it to the user (see Osmosis for a module example). ​
Query Messages
Exposes a “Swap Exact In Simulation” method where a user can put the inputs that would be used in the “Swap Exact In” execution method, and gets a response from the query that specifies the asset they would receive if executing the method (see Osmosis for a module example, or Astroport for a contract example). Exposes a “Swap Exact Out Simulation” method where a user can input the asset desired and a given pool / path, and the query returns the asset required to swap in to receive the output asset desired (see Osmosis for a module example, or Astroport for a contract example).

---

**LLM Contextual Output:**

Here's an outline of the execution messages and support queries that this feature would entail:

**Execution Messages**

1. **Swap Exact In**: A message that requests a swap with specific input asset (`inputAsset`) and path to swap (`path`). The response should include:
	* `receiverAsset`: The desired output asset.
	* `amountIn`: The amount of the input asset to be swapped.
	* `inputs`: An object containing additional information about the swap, such as the `maxAmount` for maximum input asset amount swapping.

Example:
```json
{
  "id": "swapExactIn-1",
  "type": "Swap Exact In",
  "params": [
    {
      "asset": "inputAsset",
      "path": "path"
    }
  ],
  "result": {
    "receiverAsset": "outputAsset",
    "amountIn": "1000000.0",
    "inputs": {
      "maxAmount": "2000000.0"
    }
  }
}
```
2. **Swap Exact Out**: A message that requests a swap with specific output asset (`outputAsset`) and path to swap through to achieve it, as well as the maximum amount of input asset to swap.

Example:
```json
{
  "id": "swapExactOut-1",
  "type": "Swap Exact Out",
  "params": [
    {
      "asset": "outputAsset",
      "pathThrough": "pathThrough"
    },
    {
      "maxAmount": "1000000.0"
    }
  ]
}
```
**Support Queries**

1. **Swap Exact In Simulation**: A query that requests a simulation of the swap using the specified input asset and path.

Example:
```json
{
  "id": "swapExactInSimulation-1",
  "type": "Swap Exact In Simulation",
  "params": [
    {
      "inputAsset": "inputAsset"
    }
  ]
}
```
2. **Swap Exact Out Simulation**: A query that requests a simulation of the swap using the specified output asset and path through to achieve it, as well as the maximum amount of input asset to swap.

Example:
```json
{
  "id": "swapExactOutSimulation-1",
  "type": "Swap Exact Out Simulation",
  "params": [
    {
      "outputAsset": "outputAsset"
    },
    {
      "pathThrough": "pathThrough",
      "maxAmount": "1000000.0"
    }
  ]
}
```
