#!/bin/python3

import math
import os
import random
import re
import sys

# Tsi
# h%x
# i #
# sM 
# $a 
# #t%
# ir!

# Tsih%xi #sM $a #t%ir! -> This is Matrix#  %!
# T%Mic&h%axr%iit#p!ssrst& -> This isMatrix scrpt&%!&



first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0]) # 7

m = int(first_multiple_input[1]) # 3

matrix = []

step_1 = []

pattern = r'[a-zA-Z0-9][\W\s]+[a-zA-Z0-9]'

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

# STEP 1 : read column vertically
for i in range(m):
    for j in range(n):
        step_1.append(matrix[j][i])

result_first_step = ''.join(step_1)
print(result_first_step) # Output : This$#is% Matrix#  %!

# SKIP or DELETE 
# causing the checking system fail because it has word if
                # # STEP 2 : If there are symbols or spaces between two alphanumeric characters, replaces them with a single space '' 
                # result_second_step = re.findall(pattern, result_first_step)    
                # print(result_second_step) # Output : ['s$#i', 's% M']
    
# STEP 3 : Replace them
result = re.sub(pattern, lambda m: m.group(0)[0] + " " + m.group(0)[-1], result_first_step)
print(result)
    
# expected  : This is Matrix#  %!
# output    : This is Matrix#  %!