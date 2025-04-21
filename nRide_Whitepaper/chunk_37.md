## Chunk 37

**Original Text:**

The table lists the coefficients that determine how much of the escrow funds each party receives in each
possible outcome. For example, if both parties approve the transaction and exchange secrets, they both receive the same amount of funds they originally deposited (1, 1). If one party cancels and the other approves
using the cancelling party’s secret, the approving party receives 1.3 times their original deposit, while the
cancelling party receives 0.7 times their original deposit (1.3, 0.7). If both parties cancel, they both receive
0.5 times their original deposit, and the remaining funds go to the protocol treasury (0.5, 0.5). Finally, if
both parties fail to take any action after both deposits have been paid, both parties lose their deposits, and
the funds go to the treasury (0, 0).

---

**LLM Contextual Output:**

Based on the table you provided, here's a breakdown of how the escrow funds are allocated in each possible outcome:

1. Both parties approve the transaction and exchange secrets:
   - Party A receives 1.3 times their original deposit.
   - Party B receives 1.3 times their original deposit.

2. One party cancels and the other approves using the cancelling party's secret:
   - Party A receives 1.3 times their original deposit (since they were approved, but also received a secret that cancelled them out).
   - Party B receives 0.7 times their original deposit.
   - The remaining funds go to the protocol treasury.

3. Both parties cancel:
   - Both receive 0.5 times their original deposit each.

4. Both parties fail to take any action after both deposits have been paid, and the funds go to the treasury:
   - Both lose their deposits of 0, and the funds are transferred to the protocol treasury.
