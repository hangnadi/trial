import numpy as np

list_integers = list(map(float, input().rstrip().split()))
x = int(input())

print(np.polyval(list_integers, x))