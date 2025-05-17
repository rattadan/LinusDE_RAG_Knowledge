## Chunk 43

**Original Text:**

Call a contract on a remote chain after purchasing a cw20 asset (e.g. since this requires an IBC transfer under the hood)
Chain 1 is the origin chain, where the token can be used freely for post-route actions, but it cannot be used in post-route actions on other chains. Chain 1 is the origin chain, where the token can be used freely for post-route actions, but it cannot be used in post-route actions on other chains. IBC transfer from a remote chain to the CW20’s origin chain then perform a swap or any other post-route action on that chain
Chain 2 is the origin chain. The token can be transferred back there, but it can't be used or swapped for anything in the same transaction.

---

**LLM Contextual Output:**

So you want to set up an on-chain / off-chain interaction between two different chains (a "remote chain" and a "CW20's origin chain") using Inter-Chain Communication (ICC) techniques, specifically with the goal of enabling an IBC (Inter-Blockchain Communication) transfer from a remote chain to CW20's origin chain. 

Here's a general outline of how you could set this up:

**Remote Chain to CW20 Origin Chain**

1.  You create a contract on CW20's origin chain that performs an IBC transfer from the remote chain.
2.  Once the IBC transfer is initiated, the remote chain uses its native token for post-route actions and can't use it in any other transaction on CW20.

**CW20 Origin Chain to Remote Chain**

1.  The contract you created above is deployed on CW20's origin chain as well.
2.  This contract will be used to receive IBC transfer requests from the remote chain, perform the necessary checks (e.g., token ownership, valid destination), and then execute the post-route action.

**Post-Route Action**

1.  The contract on CW20 performs a specific post-route action (e.g., swap tokens) using the received IBC transfer request.
2.  This action can now be used in conjunction with other transactions on the remote chain, allowing for seamless interaction between the two chains.

Here's some sample code to illustrate this concept:

```solidity
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/AbiUtil.sol";

contract RemoteContract {
    // Define the CW20 contract address
    address cw20;

    // Define the IBC transfer settings
    uint256 cw20Address;
    uint256 destinationChainId;
    uint256 tokenType;

    constructor(address _cw20, address _destinationChain, uint256 _tokenType) public {
        cw20 = _cw20;
        destinationChainId = _destinationChain;
        tokenType = _tokenType;
    }

    // IBC transfer function
    function ibcTransfer() external payable returns (bool) {
        // Check if the contract is on CW20's origin chain
        require(msg.sender == cw20, "Only CW20's origin chain can perform IBC transfers");

        // Perform checks for valid destination and token transfer
        require(destinationChainId == cw20Address, "Invalid destination chain");
        require(tokenType != 0, "No token type specified");

        // Check if the contract has sufficient balance on CW20
        require(msg.value > 1 * 10**18, "Insufficient balance on CW20 for IBC transfer");

        // Execute the post-route action
        (bool success, address[] memory _destinations) = executePostRouteAction();
        require(success, "IBC transfer failed");
        return success;
    }

    // Execute a specific post-route action using an IBC transfer request
    function executePostRouteAction() internal returns (bool success, address[] memory _destinations) {
        // Get the destination chain's native token contract
        address _destinationContract = IWbcSwapV2.cw20.toTokenAddress(_tokenType);

        // Create a data structure for the IBC transfer request
        bytes32 _ibcRequest = abi.encodeWithSignature("IBCRequest", _destinationChainId, cw20Address, destinationChainId, cw20Address, _destinationContract, msg.value);
        return (true, [_ibcRequest]);
    }
}

// CW20 contract
pragma solidity ^0.8.0;

contract CW20 {
    // Define the address of the remote chain's contract
    address remoteContract;

    // Define the IBC transfer settings
    uint256 cw20Address;
    uint256 destinationChainId;
    uint256 tokenType;

    constructor(address _cw20, address _destinationChain, uint256 _tokenType) public {
        cw20 = _cw20;
        destinationChainId = _destinationChain;
        tokenType = _tokenType;
    }

    // IBC transfer function
    function ibcTransfer() external payable returns (bool) {
        // Check if the contract is on CW20's origin chain
        require(msg.sender == cw20, "Only CW20's origin chain can perform IBC transfers");

        // Perform checks for valid destination and token transfer
        require(destinationChainId == cw20Address, "Invalid destination chain");
        require(tokenType != 0, "No token type specified");

        // Check if the contract has sufficient balance on CW20
        require(msg.value > 1 * 10**18, "Insufficient balance on CW20 for IBC transfer");

        // Execute the post-route action
        (bool success, address[] memory _destinations) = executePostRouteAction();
        require(success, "IBC transfer failed");
        return success;
    }

    // Execute a specific post-route action using an IBC transfer request
    function executePostRouteAction() internal returns (bool success, address[] memory _destinations) {
        // Get the destination chain's native token contract
        address _destinationContract = IWbcSwapV2.cw20.toTokenAddress(tokenType);

        // Create a data structure for the IBC transfer request
        bytes32 _ibcRequest = abi.encodeWithSignature("IBCRequest", destinationChainId, cw20Address, destinationChainId, cw20Address, _destinationContract, msg.value);
        return (true, [_ibcRequest]);
    }
}

// IWbcSwapV2 contract
pragma solidity ^0.8.0;

contract IWbcSwapV2 {
    // Define the address of the CW20 contract
    address cw20;

    // Define the IBC transfer settings
    uint256 destinationChainId;
    uint256 tokenType;

    constructor(address _cw20, uint256 _tokenType) public {
        cw20 = _cw20;
        destinationChainId = 0; // We'll use a placeholder for now
        tokenType = _tokenType;
    }

    // IBC transfer function
    function ibcTransfer() external payable returns (bool) {
        // Check if the contract is on CW20's origin chain
        require(msg.sender == cw20, "Only CW20's origin chain can perform IBC transfers");

        // Perform checks for valid destination and token transfer
        require(destinationChainId != 0, "No destination chain specified");
        require(tokenType != 0, "No token type specified");

        // Check if the contract has sufficient balance on CW20
        require(msg.value > 1 * 10**18, "Insufficient balance on CW20 for IBC transfer");

        // Execute the post-route action
        (bool success, address[] memory _destinations) = executePostRouteAction();
        require(success, "IBC transfer failed");
        return success;
    }

    // Execute a specific post-route action using an IBC transfer request
    function executePostRouteAction() internal returns (bool success, address[] memory _destinations) {
        // Get the destination chain's native token contract
        address _destinationContract = CW20.cw20.toTokenAddress(tokenType);

        // Create a data structure for the IBC transfer request
        bytes32 _ibcRequest = abi.encodeWithSignature("IBCRequest", 0, cw20Address, destinationChainId, cw20Address, _destinationContract, msg.value);
        return (true, [_ibcRequest]);
    }
}
```
