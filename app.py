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

def longest_common_prefix(words: list[str]) -> str:
    # question
    # longest_common_prefix(["flower", "flow", "flight"]) → "fl"
    # longest_common_prefix(["dog", "racecar", "car"]) → ""
    # words = ["flow", "flower", "flee"]
    
    # your code here
    prefix = words[0]
    for i in range(1, len(words)):
        while not words[i].startswith(prefix):
            prefix = prefix[:-1]
            if not prefix: 
                return""
    return prefix        

    # best answer
    # if not words:
    #     return ""

    # # Start with the first word as reference
    # prefix = words[0]

    # for word in words[1:]:
    #     # Shrink prefix until it matches the start of the current word
    #     while not word.startswith(prefix):
    #         prefix = prefix[:-1]
    #         if not prefix:
    #             return ""
    # return prefix

    # FOOTNOTE
    # | Syntax        | Meaning                                 | Example Result                 |
    # | ------------- | --------------------------------------- | ------------------------------ |
    # | `words[1:]`   | From index 1 to the end                 | `["flow", "flight"]`           |
    # | `words[:2]`   | From start up to index 2 (not included) | `["flower", "flow"]`           |
    # | `words[1:3]`  | From index 1 to 3 (not included)        | `["flow", "flight"]`           |
    # | `words[-1]`   | Last item                               | `"flight"`                     |
    # | `words[:-1]`  | Everything except last                  | `["flower", "flow"]`           |
    # | `words[::-1]` | Full list in reverse                    | `["flight", "flow", "flower"]` |


# print(f' answer: {longest_common_prefix(["reflow", "reflower", "refuse"])}')

def count_vowels(text: str) -> int:
    # Question
    # count_vowels("hello") → 2

    # your code here
    vowels = ["a","i","u","e","o"]
    # result = []
    # for vowel in vowels:
    #     for item in text:
    #         if vowel in item.lower():
    #             result.append(item)
    # return len(result)

    # Best Answer
    count = 0
    for char in text.lower():
        if char in vowels:
            count+=1

    return count

# print(f'Answer: {count_vowels("hello world ooooooooooooo")}')

def reverse_string(text: str) -> str:
    # Question
    # reverse_string("hello") → "olleh"

    # your code here
    # result = ""
    # length = len(text)
    # while length >= 0:
    #     length-=1
    #     result = f"{result + text[length]}"

    # Best answer
    # Use Slicing
    return text[::-1]
    # OR
    # result = ""
    # index = len(text) - 1
    # while index >= 0:
    #     result += text[index]
    #     index -= 1
    # return result

# print(f'Answer: {reverse_string("hello")}')