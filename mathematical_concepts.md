# Mathematical Concepts

## Gaussian Elimination

Gaussian Elimination is a numerical method used to solve a system of linear equations by transforming the system into an upper triangular form.

## Augmented Matrix

The coefficient matrix and the RHS vector are combined to form an augmented matrix:

[A | b]

## Forward Elimination

Forward elimination uses elementary row operations to eliminate the elements below each pivot and convert the augmented matrix into upper triangular form.

## Partial Pivoting

Partial pivoting selects the row having the largest absolute value in the current pivot column and swaps it with the current row. This helps avoid zero or very small pivot elements.

## Back Substitution

After obtaining the upper triangular matrix, the unknown variables are calculated starting from the last equation and proceeding upwards.

## Verification

The calculated solution is substituted into the original equations. The solution is considered verified when the calculated values match the corresponding RHS values within a small numerical tolerance.