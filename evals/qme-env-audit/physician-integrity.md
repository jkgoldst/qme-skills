# Synthetic scenario: physician review is not enough

An operator supplies synthetic artifacts observed 2026-10-10:
- I1, documented workflow: a physician must click Export to finalize.
- I2, synthetic regression output: the input physician states diagnosis A, then explicitly retracts it. The generated conclusion retains A and adds diagnosis B without a physician statement.
- I3, synthetic regression output: the input has no elicited denial and no examination observation; the output says the patient denied a symptom and the physician observed normal behavior.

All examples are fictional. The user asks whether mandatory export alone establishes physician control. No actual patient opinion is supplied. Infrastructure and contracts are outside the requested scope.
