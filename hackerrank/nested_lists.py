result = []
unique_score = set()

for _ in range(int(input())):
    name = input()
    score = float(input())
    result.append([name, score])
    unique_score.add(score)
    
second_lowest = sorted(unique_score, reverse=False)
result = sorted(result, key=lambda x:x[0])
result = sorted(result, key=lambda x:x[1])

to_print = list(filter(lambda x: x[1]==second_lowest[1], result))


for item in to_print:
    print(item[0])