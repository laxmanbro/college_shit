import cvxpy as cp

# Create two scalar optimization variables.
x1 = cp.Variable()
x2 = cp.Variable()

# Create two constraints.
constraints = [x1+x2-18 >= 0]

# Form objective.
obj = cp.Minimize(((x1 - 8)**2)+((x2-6)**2))

# Form and solve problem.
prob = cp.Problem(obj, constraints)
prob.solve()  # Returns the optimal value.
print("status:", prob.status)
print("optimal value", prob.value)
print("optimal var", x1.value, x2.value)