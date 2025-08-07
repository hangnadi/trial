from itertools import groupby

S = input().rstrip()
group = []
key = []

for k, g in groupby(S):
    group.append(list(g))
    key.append(k)

for i in range(len(group)):
    group_length = len(group[i])
    k = int(key[i])
    print((group_length, k), end=" ")