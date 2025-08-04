A = int(input()) # the number of students who have subscribed to the English newspaper.
list_A = input().rstrip().split() # ids of those students.
B = int(input()) # the number of students who have subscribed to the French newspaper.
list_B = input().rstrip().split() # ids of those students.

# Find union
print(len(set(list_A).symmetric_difference(set(list_B))))


