# Enter your code here. Read input from STDIN. Print output to STDOUTfrom itertools import permutations
from itertools import *

x = input().rstrip().split()

for item in list(combinations_with_replacement(sorted(x[0]), int(x[1]))):
        print("".join(item))
    