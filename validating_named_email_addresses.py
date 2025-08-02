import re
# Enter your code here. Read input from STDIN. Print output to STDOUT
# ^              # Start of the string
# [a-zA-Z0-9]    # Start character with a-z, A-Z, 0-9
# [\w\.-]+       # One or more word characters (a-z, A-Z, 0-9, _), dot (.), or hyphen (-)
# @              # The @ symbol
# [\w\.-]+       # One or more word characters, dot, or hyphen
# \.             # A literal dot
# \w+            # One or more word characters (for domain like .com, .org)
# [a-zA-Z]{0,3}  # One up to Three character a-z dan A-Z
# $              # End of the string

count = int(input())
pattern = r'^[a-zA-Z0-9][\w\.-]+@[a-zA-Z]+\.[a-zA-Z]{0,3}$'

for _ in range(count):
    valid = False
    key_input = input().split()
    email = key_input[1].strip("<>")
    
    if re.match(pattern, email):
        print(f'{key_input[0]} {key_input[1]}')        
    
    
