import cvxpy as cp
x1 = cp.Variable()
x2 = cp.Variable()
constraints = [3*x1+x2-8 == 0,15-2*x1-4*x2 >= 0]
obj = cp.Minimize(4*(x1**2)+2*(x2**2))
prob = cp.Problem(obj, constraints)
prob.solve()
print("status:", prob.status)
print("optimal value", prob.value)
print("optimal var", x1.value, x2.value)