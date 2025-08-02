import re
# Enter your code here. Read input from STDIN. Print output to STDOUT
# ^              # Start of the string
# [\w\.-]+       # One or more word characters (a-z, A-Z, 0-9, _), dot (.), or hyphen (-)
# @              # The @ symbol
# [\w\.-]+       # One or more word characters, dot, or hyphen
# \.             # A literal dot
# \w+            # One or more word characters (for domain like .com, .org)
# $              # End of the string

count = int(input())
pattern = r'^\w+[\w\.-]+@[\w\.-]+\.\w+$'

for _ in range(count):
    valid = False
    key_input = input().split()
    email = key_input[1].strip("<>")
    
    if re.match(pattern, email):
        print(f'{key_input[0]} {key_input[1]}')        
    
    
