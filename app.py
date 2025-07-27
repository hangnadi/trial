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
    # result = ""
    # for i in range(len(text)):
    #     if text[i].islower(): 
    #         result = f'{result + text[i].swapcase()}'
    #     else :
    #         result = f'{result + text[i]}'
        
    # return result

    # BEST ANSWER
    # return text.title()
    # OR
    # words = text.split()
    capitalized = []
    for char in text:
        capitalized.append(char[0].upper() + char[1:].lower())
    return " ".join(capitalized)

# print(f'{capitalize_words("Hello World!")}')

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

def multiply_all(nums: list[int]) -> int:
    # Question
    # multiply_all([1, 2, 3, 4]) → 24

    # your code here
    if not nums:
        return 0

    result = nums[0]
    for i in range(1, len(nums)):
        result = result * nums[i]

    return result

# print(f'{multiply_all([1, 2, 3, 4, 5])}')

def is_anagram(s1: str, s2: str) -> bool:
    # Question
    # is_anagram("listen", "silent") → True
    # is_anagram("hello", "world") → False

    # your code here
    # if len(s1) != len(s2): return False
    # set1 = set(s1)
    # set2 = set(s2)
    # return len(set1) == len(set2)
    # FAIL -> input aab vs abb

    # Best Answer
    return sorted(s1) == sorted(s2)
    # OR
    # count1 = {} -> defind empty dict
    # count2 = {}

    # for char in s1:
    #     if char in count1:
    #         count1[char] += 1
    #     else:
    #         count1[char] = 1

    # for char in s2:
    #     if char in count2:
    #         count2[char] += 1
    #     else:
    #         count2[char] = 1

    # return count1 == count2

# print(f'{is_anagram("hello", "olleh")}')

def majority_element(nums: list[int]) -> int:
    # Question
    # majority_element([3,3,4,2,3,3,5]) → 3

    # your code here
    max_count = 0
    most_frequent_num = None
    unique_nums = set(nums)
    
    for unique_num in unique_nums:
        count = 0
        for num in nums:
            if num == unique_num: count+=1
        
        if max_count < count: 
            max_count = count
            most_frequent_num = unique_num

    return most_frequent_num

    # BEST ANSWER
    # return Counter(nums).most_common(1)[0][0]
    # most_common(1)[0] → (3, 3)
    # most_common(1)[0][0] → 3 ← element
    # most_common(1)[0][1] → 3 ← frequency

# print(f'{majority_element([1, 2, 3, 3, 3, 2, 1])}')

def count_uppercase(text: str) -> int:
    # Question    
    # count_uppercase("Hello World") → 2
    # count_uppercase("python") → 0
    
    count = 0
    for i in range(len(text)):
        if text[i].isupper(): 
            count+=1

    return count

# print(f'{count_uppercase("Hello World")}')

def sum_digits(input: int) -> int:
    # QUESTION
    # sum_digits(1234) → 10
    # sum_digits(505) → 10
    result = 0
    text = str(input)

    for i in range(len(text)):
        result = result + int(text[i])

    return result

    # BEST ANSWER
    # return sum(int(d) for d in str(input))
    # OR
    # for digit in str(input):
    #     result += int(digit)
    # return result

# print(f'{sum_digits(50105)}')