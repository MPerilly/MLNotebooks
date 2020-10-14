import numpy as np

p = 3
n = 5

X = np.zeros((n, p))
print(X)
X[0][0] = 1
X[0][1] = 1
X[0][2] = 1
print(X)
print(X[0] * 5)
X[0] = X[0] * 5
print(X)