# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

word_counts = OrderedDict()
keyword = ""

for _ in range(int(input())):
    keyword = input()
    
    if keyword in word_counts:
        word_counts[keyword]+=1
    else:
        word_counts[keyword]=1

print(len(word_counts))
print(" ".join(str(count) for count in word_counts.values()))
    

