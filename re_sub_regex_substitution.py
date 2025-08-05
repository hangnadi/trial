import re
import sys 

pattern_and = r"(?<= )(&&)(?= )"
pattern_or = r"(?<= )(\|\|)(?= )"

n = int(input())
for line in sys.stdin:
    string_and = re.sub(pattern_and, "and", line)
    string_or = re.sub(pattern_or, "or", string_and)
    print(string_or, end="")