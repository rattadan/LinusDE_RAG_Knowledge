## Chunk 57

**Original Text:**

This allows smart contracts to execute expressive flows that may involve moving some amount of the user’s ERC-20 tokens
Skip Go will always return this field if there are any erc20 approvals needed for the route. It is the client’s responsibility to check if the user’s approval is already at or above the returned approval needed (for example, if the integrator allows for max approvals). If this field is non-empty and the user does not have the approvals necessary, the approval must be granted, signed, and submitted before the EvmTx populated by the other fields in the response can be submitted to the network. Otherwise, it will fail to execute with a permission error. Skip’s ERC20Approval object has 3 fields that define approval: _ token_contract: The address of the ERC-20 token on which the approval is granted _ spender: The address of the contract to which the approval will grant spend authority * amount: The amount of token_contract tokens the approval will grant the spender to spend
Check out EIP-2612 for more information on ERC-20 approvals.

---

**LLM Contextual Output:**

It appears that you're working with smart contracts and the ERC-20 token standard, specifically focusing on executing expressive flows that require moving some amount of user-provided tokens. You also mention the `ERC20Approval` contract, which is used to manage approvals for token transfers.

To summarize:

1. The response from a smart contract, like Skip, indicates whether there are any `ERC20` approvals needed for a particular route.
2. If an approval is required and the user doesn't have it yet, the approved amount must be granted, signed, and submitted before the EVM transaction (Evem Transaction) can be sent to the network.
3. The `Skip` contract's response contains specific fields that control this process:
   - `skip.ERC20Approval.token_contract`: The address of the ERC-20 token being used for approval
   - `skip.ERC20Approval.spender`: The address of the contract that will grant spend authority on behalf of the spender
   - `skip.ERC20Approval.amount`: The amount of tokens being granted to the spender

To execute a flow that involves moving tokens, you would need to:

1. Check if an approval is required for the specific route.
2. If necessary, retrieve the current approval settings (e.g., token contract, spender, and amount).
3. Grant the required approvals, sign them, and submit them before submitting the EVM transaction.

Here's a high-level example in Solidity:
```solidity
pragma solidity ^0.8.0;

contract MyContract {
    function grantApproval() public {
        // Get current approval settings
        ERC20Approval[] memory approvals = skip.ERC20Approval;

        // Check if any approvals are needed
        bool needsApproval = false;
        for (uint256 i = 0; i < approvals.length; i++) {
            if (approvals[i].amount > 0) {
                needsApproval = true;
                break;
            }
        }

        if (!needsApproval) {
            // Handle no approval needed
            return;
        }

        // Grant the required approvals, sign them, and submit them
        for (uint256 i = 0; i < approvals.length; i++) {
            ERC20Approval memory approval = approvals[i];
            // ... grant or update approval settings ...
        }
    }
}
```
Please note that this is a simplified example and may not cover all edge cases. You should consult the specific EVM and smart contract documentation for more detailed information on executing approvals and managing token transfers in your specific use case.
