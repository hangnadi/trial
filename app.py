def even_or_odd(n: int) -> str:
    # your code here
    if n % 2 == 0: return "even"
    else: return "odd"
    # best answer
    # return "Even" if n % 2 == 0 else "Odd"

def sum_positive(numbers: list[int]) -> int:
    # your code here
    i = 0
    result = 0
    while i < len(numbers):
        if (numbers[i]) >= 0 :
            result = result + numbers[i]
        i=i+1
    return result
    # best answer
    # return sum(n for n in numbers if n >= 0)