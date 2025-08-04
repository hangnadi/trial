import numpy as np

N = int(input())
A = []
for _ in range(N):
    list_numbers = list(map(float, input().rstrip().split()))
    A.append(list_numbers)

print(round(np.linalg.det(A), 2))