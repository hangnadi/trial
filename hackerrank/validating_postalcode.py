regex_integer_in_range = r"^[1-9][0-9]{5}$"	# Do not delete 'r'.
# regex_integer_in_range = r"^[1-9][0-9][0-9][0-9][0-9][0-9]$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(?=([0-9])[0-9]\1)"	# Do not delete 'r'.
# regex_alternating_repetitive_digit_pair = r"(\d)\1+"	# Do not delete 'r'.

import re
P = input()

X = bool(re.match(regex_integer_in_range, P))
Y = len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2
# print (f'x= {X} and y= {Y}')
print (X and Y)