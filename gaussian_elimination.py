def verify_solution(A, b, solution):
    print("\nVerification:")

    for i in range(len(A)):
        calculated = 0.0

        for j in range(len(A[i])):
            calculated += A[i][j] * solution[j]

        print(f"Equation {i + 1}: Calculated = {calculated:.6f}, Expected = {b[i]:.6f}")

        if abs(calculated - b[i]) < 1e-9:
            print("Verified")
        else:
            print("Not Verified")
def back_substitution(matrix):
    n = len(matrix)
    solution = [0.0] * n

    for i in range(n - 1, -1, -1):
        sum_value = matrix[i][n]

        for j in range(i + 1, n):
            sum_value -= matrix[i][j] * solution[j]

        if abs(matrix[i][i]) < 1e-12:
            raise ValueError("Zero pivot encountered during back substitution.")

        solution[i] = sum_value / matrix[i][i]

    return solution
def forward_elimination(matrix):
    n = len(matrix)

    for i in range(n):

        # Partial pivoting
        max_row = i
        for k in range(i + 1, n):
            if abs(matrix[k][i]) > abs(matrix[max_row][i]):
                max_row = k

        # Swap rows
        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]

        # Check for zero pivot
        if abs(matrix[i][i]) < 1e-12:
            raise ValueError("Zero pivot encountered.")

        # Eliminate elements below pivot
        for k in range(i + 1, n):
            factor = matrix[k][i] / matrix[i][i]

            for j in range(i, n + 1):
                matrix[k][j] -= factor * matrix[i][j]

    return matrix
def get_input():
    n = int(input("Enter the number of variables: "))

    if n <= 0:
        raise ValueError("Number of variables must be positive.")

    print("Enter the coefficient matrix:")
    A = []

    for i in range(n):
        row = list(map(float, input().split()))

        if len(row) != n:
            raise ValueError("Invalid matrix dimensions.")

        A.append(row)

    print("Enter the RHS vector:")
    b = list(map(float, input().split()))

    if len(b) != n:
        raise ValueError("RHS vector dimension does not match the matrix.")

    return A, b

A, b = get_input()
# Create argumented matrix
augmented_matrix = []

for i in range(len(A)):
    augmented_matrix.append(A[i] + [b[i]])

print("\nAugmented Matrix:")
for row in augmented_matrix:
    print(row)    # Perform forward elimination
try:
    upper_matrix = forward_elimination(augmented_matrix)
except ValueError:
    print("\nError: The system does not have a unique solution.")
    print("Please provide a non-singular system.")
    exit()
print("\nMatrix after Forward Elimination:")
for row in upper_matrix:
    print(row)
    solution = back_substitution(upper_matrix)

print("\nSolution:")
for i, value in enumerate(solution):
    print(f"x{i + 1} = {value}")
    verify_solution(A,b,solution)

print("\nCoefficient Matrix:")
for row in A:
    print(row)

print("\nRHS Vector:")
print(b)