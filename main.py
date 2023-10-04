import numpy as np

def simplex_method(A, b, c):
    m, n = A.shape
    tableau = np.hstack((np.vstack((A, np.eye(m))), np.vstack((c, np.zeros(m)))))
    basic_vars = np.arange(n, n + m)
    
    while True:
        # Find the entering variable (pivot column)
        entering_var = np.argmax(tableau[-1, :-1])
        
        # If all values in the last row are non-positive, we have the optimal solution
        if tableau[-1, entering_var] <= 0:
            break
        
        # Find the departing variable (pivot row)
        ratios = tableau[:-1, -1] / tableau[:-1, entering_var]
        departing_var = np.argmin(ratios)
        
        # Perform pivot operation to update the tableau
        pivot_element = tableau[departing_var, entering_var]
        tableau[departing_var, :] /= pivot_element
        for i in range(m + 1):
            if i != departing_var:
                tableau[i, :] -= tableau[i, entering_var] * tableau[departing_var, :]
        
        # Update basic variables
        basic_vars[departing_var] = entering_var
    
    optimal_solution = tableau[-1, -1]
    basic_solution = np.zeros(n)
    for i, var in enumerate(basic_vars):
        if var < n:
            basic_solution[var] = tableau[i, -1]
    
    return optimal_solution, basic_solution

# Example usage
A = np.array([[2, 1], [1, 3]])
b = np.array([4, 6])
c = np.array([-3, -5])

optimal_value, solution = simplex_method(A, b, c)
print("Optimal Value:", optimal_value)
print("Optimal Solution:", solution)
