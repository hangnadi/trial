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

def capitalize_words(text: str) -> str:
    # your code here
    return""

def remove_duplicates(nums: list[int]) -> list[int]:
    # your code here
    results = []
    for num in nums:
        if num not in results: 
            results.append(num)

    return results
    # best answer
    # seen = set() -> use for setting the unique only
    # result = []
    # for num in nums:
    #     if num not in seen:
    #         result.append(num)
    #         seen.add(num)
    # return result
