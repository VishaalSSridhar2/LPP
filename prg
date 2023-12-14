from scipy.optimize import linprog

# Coefficients of the objective function
c = [-4, -5]  # Since linprog minimizes and we want to maximize, we use negative coefficients

# Coefficients of the inequality constraints
A = [
    [2, 1],   # Coefficients of the first constraint (2x + y <= 20)
    [-4, 5]   # Coefficients of the second constraint (-(4x - 5y) <= 10)
]

# Constants on the right-hand side of the inequalities
b = [20, 10]

# Bounds for variables
x_bounds = (0, None)  # x >= 0
y_bounds = (3, None)  # y >= 3

# Solve the linear programming problem
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

# Display the results
print("Optimal values:")
print("x =", result.x[0])
print("y =", result.x[1])
print("Optimal objective function value (max Z) =", -result.fun)  # Note: Multiply by -1 to get the maximum value
