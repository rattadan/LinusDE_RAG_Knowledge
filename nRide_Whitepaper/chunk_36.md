## Chunk 36

**Original Text:**

3.2. Possible Outcomes
The following table contains the 16 possible end states of an escrow:

Approve(A,s_b)
Cancel(A)
T1(A)
T2(A)

Approve(B,s_a)
(1, 1)
(0.7, 1.3)
x
(0.5, 1.5)

Cancel(B)
(1.3, 0.7)
(0.5, 0.5)
(0, 1)
(0, 0.5)

T1(B)
x
(1, 0)
x
(1, 0)

T2(B)
(1.5, 0.5)
(0.5, 0)
(0, 1)
(0, 0)

In this table, the columns represent the four possible actions that can be taken by party B, while the rows
represent the four possible actions that can be taken by party A. Each cell in the table represents the outcome of the escrow mechanism for the combination of actions taken by both parties. The table lists the coefficients that determine how much of the escrow funds each party receives in each
possible outcome. For example, if both parties approve the transaction and exchange secrets, they both receive the same amount of funds they originally deposited (1, 1).

---

**LLM Contextual Output:**

To find the possible outcomes for the escrow mechanism, we need to multiply the coefficients in each cell by the corresponding row and column values.

Let's start with the first row:

* Cell (0.7, 1.3) multiplied by:
	+ Row A: Approve(A)
	+ Row B: Cancel(B), T1(B), T2(B)
= 0.7 * (1 + 1.3) = 1.9
* Cell (0, 0.5) multiplied by:
	+ Row A: Approve(A)
	+ Row B: Cancel(B), T1(B), T2(B)
= 0 * (1 + 0.5) = 0

Now, let's move to the second row:

* Cell (1, 0) multiplied by:
	+ Row A: Approve(A)
	+ Row B: Cancel(B), T1(B), T2(B)
= 1 * (0 + 0) = 0
* Cell (1, 0) multiplied by:
	+ Row A: Approve(A)
	+ Row B: Cancel(B), T1(B), T2(B)
= 1 * (1 + 0) = 1

Next, let's move to the third row:

* Cell x (1, 0) multiplied by:
	+ Row A: Approve(A)
	+ Row B: Cancel(B), T1(B), T2(B)
= x
* Cell (1, 0) multiplied by:
	+ Row A: Approve(A)
	+ Row B: Cancel(B), T1(B), T2(B)
= 1 * (1 + 0) = 1

Now, let's move to the fourth row:

* Cell (1.5, 0.5) multiplied by:
	+ Row A: Approve(A)
	+ Row B: Cancel(B), T1(B), T2(B)
= 1.5 * (0 + 0.5) = 0.75
* Cell (0.5, 0) multiplied by:
	+ Row A: Approve(A)
	+ Row B: Cancel(B), T1(B), T2(B)
= 0.5 * (0 + 0) = 0

Finally, let's move to the fifth row:

* Cell (0, 1) multiplied by:
	+ Row A: Approve(A)
	+ Row B: Cancel(B), T1(B), T2(B)
= 0 * (1 + 0.5) = 0
* Cell (0, 0.5) multiplied by:
	+ Row A: Approve(A)
	+ Row B: Cancel(B), T1(B), T2(B)
= 0 * (0 + 0.5) = 0
