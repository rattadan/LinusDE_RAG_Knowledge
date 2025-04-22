## Chunk 56

**Original Text:**

The data bytes will be interpreted according to the application-binary-interface (ABI) of the contract that’s being interacted with. If this field is empty, it means the transaction is sending funds to an address, rather than calling a contract. required_erc20_approvals: The permissions that must be granted to a specific smart contract to spend or transfer a certain amount of their ERC-20 tokens on behalf of the end user. This allows smart contracts to execute expressive flows that may involve moving some amount of the user’s ERC-20 tokens
Skip Go will always return this field if there are any erc20 approvals needed for the route. It is the client’s responsibility to check if the user’s approval is already at or above the returned approval needed (for example, if the integrator allows for max approvals).

---

**LLM Contextual Output:**

This text explains how the data bytes of a transaction will be interpreted in terms of the application-binary-interface (ABI) used by the contract being interacted with. It highlights two specific fields:

1. `required_erc20_approvals`: This field indicates whether smart contracts are required to grant certain permissions (approvals) before they can execute actions, such as spending or transferring ERC-20 tokens on behalf of the user.
2. `Skip Go will always return this field if there are any erc20 approvals needed for the route.`: This implies that when a transaction is executed, this field is checked and returned to the client as part of the transaction's data bytes. It suggests that smart contracts must explicitly grant these required permissions before they can proceed with executing certain actions.
