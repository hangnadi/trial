# Enter your code here. Read input from STDIN. Print output to STDOUTfrom itertools import permutations
from itertools import combinations

x = input().rstrip().split()
for i in range(1, int(x[1]) + 1):    
    for item in list(combinations(sorted(x[0]), i)):
        print("".join(item))