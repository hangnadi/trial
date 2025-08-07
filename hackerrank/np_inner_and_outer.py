import numpy as np

npa, npb = np.array(list(map(int, input().rstrip().split()))), np.array(list(map(int, input().rstrip().split())))

print(np.inner(npa, npb))
print(np.outer(npa, npb))
