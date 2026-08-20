# Algorithm / Pseudocode

1. Start
2. Read the number of variables (n).
3. Read the coefficient matrix A.
4. Read the RHS vector b.
5. Create the augmented matrix [A | b].
6. Apply partial pivoting to select the largest pivot element.
7. Swap rows if required.
8. Perform forward elimination to convert the matrix into upper triangular form.
9. Check for zero pivots and systems without a unique solution.
10. Perform back substitution to calculate the unknown variables.
11. Verify the calculated solution using the original equations.
12. Display the solution and verification results.
13. Stop.