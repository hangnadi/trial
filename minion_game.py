def minion_game(string):
    # your code goes here
    vowel = ['A', 'I', 'U', 'E', 'O']
    score_stuart = 0
    score_kevin = 0
 
    if 0 <= len(string) <= 10 ** 6:
        n = len(string)
        total_substring = (n * (n + 1)) / 2
        
        print(total_substring)
            
        # unique = set()
        for start in range(len(string)):
            for end in range(start + 1, len(string) + 1):
                if string[start] not in vowel:
                    score_stuart+=1
                else:
                    score_kevin+=1
                # unique.add(string[start:end])
                
        if score_stuart > score_kevin:
            print(f'Stuart {score_stuart}')
        elif score_kevin > score_stuart:
            print(f'Kevin {score_kevin}')
        else:
            print('Draw')

    # BEST ANSWER
    # vowels = ['A', 'I', 'U', 'E', 'O']
    # score_stuart = 0
    # score_kevin = 0
 
    # if 0 <= len(string) <= 10 ** 6:
    #     n = len(string)
        
    #     for i in range(n):
    #         if string[i] in vowels:
    #             score_kevin += n - i
    #         else:
    #             score_stuart += n - i
                
    #     if score_stuart > score_kevin:
    #         print(f'Stuart {score_stuart}')
    #     elif score_kevin > score_stuart:
    #         print(f'Kevin {score_kevin}')
    #     else:
    #         print('Draw')
    # Simuluation
    # | Index `i` | Character | Substrings starting at `i`      | Count     |
    # | --------- | --------- | ------------------------------- | --------- |
    # | 0         | B         | B, BA, BAN, BANA, BANAN, BANANA | 6 = 6 - 0 |
    # | 1         | A         | A, AN, ANA, ANAN, ANANA         | 5 = 6 - 1 |
    # | 2         | N         | N, NA, NAN, NANA                | 4 = 6 - 2 |
    # | 3         | A         | A, AN, ANA                      | 3 = 6 - 3 |
    # | 4         | N         | N, NA                           | 2 = 6 - 4 |
    # | 5         | A         | A                               | 1 = 6 - 5 |
