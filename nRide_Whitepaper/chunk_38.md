## Chunk 38

**Original Text:**

If both parties cancel, they both receive
0.5 times their original deposit, and the remaining funds go to the protocol treasury (0.5, 0.5). Finally, if
both parties fail to take any action after both deposits have been paid, both parties lose their deposits, and
the funds go to the treasury (0, 0). •

Approve(B, secret_a) & Approve(A, secret_b))
Both parties send each other their secrets before T2, resulting in both parties receiving
their full deposit back. •

Approve(A, secret_b) & Cancel(B)
Party B actively cancels and sends their secret code to Party A, allowing Party A to submit the Approve message using Party B’s secret code. Party A receives 1.3 times their
initial deposit, and Party B receives 0.7 times their initial deposit.

---

**LLM Contextual Output:**

I can help you with the approval logic for these scenarios.

### Approve(B, secret_a)

To implement this scenario, we need to simulate the following steps:

1. Party A sends `secret_a` to Party B.
2. Party B computes `0.5 * B` as their share of the deposit.
3. Party A computes `1.3 * A`.
4. Party B checks if they have enough funds to pay out `0.5 * B`. If yes, they send this amount back to Party A and set `B` to `0`.
5. If Party B does not have enough funds, they return the deposit directly to Party A.

Here's a possible implementation in Ethereum ( Solidity ) for these steps:

```solidity
pragma solidity ^0.8.0;

contract Approve {
    // Initialize variables
    address public ownerA;
    address public ownerB;
    uint public secret_a;
    uint public secret_b;

    // Event logging for transfer and deposit
    event Transfer(address indexed to, uint amount);

    // Event logging for approve
    event Approved(address indexed by, uint amount);

    constructor() {
        ownerA = msg.sender;
    }

    function setSecretA(uint _secret) public {
        secret_a = _secret;
    }

    function setSecretB(uint _secret) public {
        secret_b = _secret;
    }

    // Approve A for B's secret
    function Approve(B) public returns (bool, uint) {
        // Send secret to B
        transfer(secret_a);

        // Get amount of deposit received by A in return
        uint rewardA = 1; // assume 1 as initial deposit

        // Calculate share for ownerB based on threshold
        uint shareB = max(0, (secret_b * 10) / secret_a); // assuming threshold is 100%

        // Check if B has enough funds to pay out
        require(secret_b >= shareB, "Not enough funds");

        // Set amount received by A for approval
        transfer(secret_a);

        return (shareB, rewardA);
    }

    // Approve B for A's secret
    function Approve(B) public returns (bool, uint) {
        // Send secret to A
        transfer(secret_b);

        // Get amount of deposit received by B in return
        uint rewardB = 0.7; // assume 70 as initial deposit

        // Calculate share for ownerA based on threshold
        uint shareA = max(0, (secret_a * 10) / secret_b); // assuming threshold is 100%

        // Check if A has enough funds to pay out
        require(secret_a >= shareA, "Not enough funds");

        // Set amount received by B for approval
        transfer(secret_b);

        return (shareA, rewardB);
    }
}
```

### Approve(A, secret_b) & Cancel(B)

To implement this scenario, we need to simulate the following steps:

1. Party A sends `secret_b` to Party B.
2. Party B computes `0.5 * B` as their share of the deposit.
3. Party A computes `1.3 * A`.
4. Party B checks if they have enough funds to pay out `0.5 * B`. If yes, they send this amount back to Party A and set `B` to `0`.

Here's a possible implementation in Ethereum ( Solidity ) for these steps:

```solidity
pragma solidity ^0.8.0;

contract Approve {
    // Initialize variables
    address public ownerA;
    address public ownerB;
    uint public secret_a;
    uint public secret_b;

    // Event logging for transfer and deposit
    event Transfer(address indexed to, uint amount);

    // Event logging for approve
    event Approved(address indexed by, uint amount);

    // Event logging for cancel
    event Cancelled(address indexed by);

    constructor() {
        ownerA = msg.sender;
    }

    function setSecretA(uint _secret) public {
        secret_a = _secret;
    }

    function setSecretB(uint _secret) public {
        secret_b = _secret;
    }

    // Approve A for B's secret
    function Approve(B) public returns (bool, uint) {
        // Send secret to B
        transfer(secret_a);

        // Get amount of deposit received by A in return
        uint rewardA = 1; // assume 1 as initial deposit

        // Calculate share for ownerB based on threshold
        uint shareB = max(0, (secret_b * 10) / secret_a); // assuming threshold is 100%

        // Check if B has enough funds to pay out
        require(secret_b >= shareB, "Not enough funds");

        // Set amount received by A for approval
        transfer(secret_a);

        return (shareB, rewardA);
    }

    // Approve B for A's secret
    function Approve(B) public returns (bool, uint) {
        // Send secret to A
        transfer(secret_b);

        // Get amount of deposit received by B in return
        uint rewardB = 0.7; // assume 70 as initial deposit

        // Calculate share for ownerA based on threshold
        uint shareA = max(0, (secret_a * 10) / secret_b); // assuming threshold is 100%

        // Check if A has enough funds to pay out
        require(secret_a >= shareA, "Not enough funds");

        // Set amount received by B for approval
        transfer(secret_b);

        return (shareA, rewardB);
    }

    function Cancel(B) public returns (bool, uint) {
        // Send secret to A
        transfer(secret_b);

        // Calculate threshold based on current share of ownerA and B
        uint threshold = max(0, (secret_a * 10) / secret_b + 1); // assuming threshold is increased by 1%

        // Check if B has enough funds to pay out
        require(secret_b >= threshold, "Not enough funds");

        // Set amount received by A for cancel
        transfer(secret_a);

        return (false, 0);
    }
}
```

### Both parties send each other their secrets before T2

To implement this scenario, we need to simulate the following steps:

1. Party A sends `secret_a` to Party B.
2. Party B computes `0.5 * B` as their share of the deposit.

Here's a possible implementation in Ethereum ( Solidity ) for these steps:

```solidity
pragma solidity ^0.8.0;

contract Approve {
    // Initialize variables
    address public ownerA;
    address public ownerB;
    uint public secret_a;
    uint public secret_b;

    // Event logging for transfer and deposit
    event Transfer(address indexed to, uint amount);

    // Event logging for approve
    event Approved(address indexed by, uint amount);

    constructor() {
        ownerA = msg.sender;
    }

    function setSecretA(uint _secret) public {
        secret_a = _secret;
    }

    function setSecretB(uint _secret) public {
        secret_b = _secret;
    }

    // Approve A for B's secret
    function Approve(B) public returns (bool, uint) {
        // Send secret to B
        transfer(secret_a);

        // Get amount of deposit received by A in return
        uint rewardA = 1; // assume 1 as initial deposit

        // Calculate share for ownerB based on threshold
        uint shareB = max(0, (secret_b * 10) / secret_a); // assuming threshold is 100%

        // Check if B has enough funds to pay out
        require(secret_b >= shareB, "Not enough funds");

        // Set amount received by A for approval
        transfer(secret_a);

        return (shareB, rewardA);
    }

    function Approve(B) public returns (bool, uint) {
        // Send secret to B
        transfer(secret_b);

        // Get amount of deposit received by B in return
        uint rewardB = 0.7; // assume 70 as initial deposit

        // Calculate share for ownerA based on threshold
        uint shareA = max(0, (secret_a * 10) / secret_b); // assuming threshold is 100%

        // Check if A has enough funds to pay out
        require(secret_a >= shareA, "Not enough funds");

        // Set amount received by B for approval
        transfer(secret_b);

        return (shareA, rewardB);
    }

    function Cancel(B) public returns (bool, uint) {
        // Send secret to A
        transfer(secret_b);

        // Calculate threshold based on current share of ownerA and B
        uint threshold = max(0, (secret_a * 10) / secret_b + 1); // assuming threshold is increased by 1%

        // Check if B has enough funds to pay out
        require(secret_b >= threshold, "Not enough funds");

        // Set amount received by A for cancel
        transfer(secret_a);

        return (false, 0);
    }
}
```
