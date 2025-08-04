import numpy as np


N = int(input())
A = []
B = []
for _ in range(N):
    list_of_integers = list(map(int, input().rstrip().split()))
    A.append(list_of_integers)

for _ in range(N):
    list_of_integers = list(map(int, input().rstrip().split()))
    B.append(list_of_integers)

npa = np.array(A)
npb = np.array(B)

print(np.dot(npa, npb))