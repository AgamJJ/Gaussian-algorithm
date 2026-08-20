# Results and Observations

## Test Case 1: 2 × 2 System

The program successfully accepted a 2 × 2 coefficient matrix and RHS vector.

The program performed:
- Augmented matrix formation
- Partial pivoting
- Forward elimination
- Back substitution
- Solution verification

The obtained solution was successfully verified.

## Test Case 2: 3 × 3 System

The program was tested with a 3 × 3 system to confirm that it works for a general system and is not limited to a 2 × 2 example.

The obtained solution was:

x1 = 2.0  
x2 = 3.0  
x3 = -1.0

All three equations were successfully verified.

## Error Handling Test

A singular system was also tested. The program detected the zero pivot and displayed an appropriate error message indicating that the system does not have a unique solution.

## Overall Observation

The program successfully implements the Gaussian Elimination algorithm and performs the required elimination, back substitution, verification, and error handling operations.