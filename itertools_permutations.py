from itertools import permutations

x = input().rstrip().split()
for item in sorted(list(permutations(x[0], int(x[1])))):
    print("".join(item))
