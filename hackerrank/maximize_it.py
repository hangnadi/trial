"""
Title     : Maximize It
Subdomain : 
Domain    : Python
Author    : Hang Nadi
Created   : 4 August 2025
Problem   : https://www.hackerrank.com/challenges/maximize-it/problem?isFullScreen=true
"""

import itertools 

# Enter your code here. Read input from STDIN. Print output to STDOUT

input_format = list(map(int, input().rstrip().split()))
Smax = 0
K, M = input_format[0], input_format[1]
list_numbers=[]


for _ in range(K):
    N = list(map(int, input().rstrip().split()))
    list_numbers.append(N[1:len(N)])

cm = itertools.product(*list_numbers)

for item in cm:
    Smax = max(sum(n ** 2 for n in item) % M, Smax)

print(Smax)
