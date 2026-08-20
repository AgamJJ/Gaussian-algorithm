# Gaussian Elimination Algorithm
## Objective 
To implement a generalized python program for solving systems of linear equations using the Gaussian Elimination algorithm.
## Methodology

The program follows these steps:

1. Accept the coefficient matrix and RHS vector from the user.
2. Create the augmented matrix.
3. Apply partial pivoting to select a suitable pivot.
4. Perform forward elimination to convert the matrix into upper triangular form.
5. Use back substitution to calculate the unknown variables.
6. Verify the obtained solution using the original equations.
7. Handle invalid dimensions, zero pivots, and systems without a unique solution.
## Features

- Works with general n × n systems of linear equations.
- Uses partial pivoting for numerical stability.
- Performs Gaussian forward elimination.
- Uses back substitution to obtain the solution.
- Verifies the calculated solution.
- Detects invalid matrix dimensions.
- Handles zero pivots and non-singular system requirements.
 ## How to Run

1. Make sure Python 3 is installed.
2. Open the project folder in VS Code or a terminal.
3. Run the following command:

python gaussian_elimination.py

4. Enter the number of variables.
5. Enter the coefficient matrix.
6. Enter the RHS vector.
7. The program will display the augmented matrix, matrix after forward elimination, solution, and verification results.
## Example

Input:

3
2 1 -1
-3 -1 2
-2 1 2
8 -11 -3

Expected Solution:

x1 = 2
x2 = 3
x3 = -1
## Results

The program successfully solves systems of linear equations using Gaussian Elimination.

For the tested 3 × 3 system, the solution obtained was:

x1 = 2
x2 = 3
x3 = -1

The solution was verified by substituting the calculated values into the original equations, and all equations were successfully verified.
## Testing

The program was tested with different types of input systems.

### Test Case 1: 2 × 2 System
- The program successfully performed forward elimination.
- Back substitution produced the solution.
- The solution was successfully verified.

### Test Case 2: 3 × 3 System
- The program successfully handled a 3 × 3 system.
- The calculated solution was verified using the original equations.

### Error Testing
- Invalid matrix dimensions were tested.
- Zero pivot and non-unique systems were tested.
- The program displayed an appropriate error message instead of producing an incorrect solution.
## Conclusion

The Gaussian Elimination algorithm was successfully implemented in Python as a generalized and modular program. The program performs forward elimination, partial pivoting, back substitution, and solution verification. Different test cases were used to verify the correctness and reliability of the program.