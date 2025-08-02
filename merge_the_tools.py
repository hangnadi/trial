def merge_the_tools(string, k):
    # your code goes here
    unique = []
    seen = set()
    i = 0
    while i + k <= len(string):
        element = string[i:i+k]
        unique.clear()
        seen.clear()
        
        for char in element:
            if char not in seen:
                seen.add(char)
                unique.append(char)
                
        print(''.join(unique))
        i = i + k

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)