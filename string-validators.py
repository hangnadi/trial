if __name__ == '__main__':
    s = input()
    l = len(s)
    is_alnum = False
    is_alpha = False
    is_digit = False
    is_lower = False
    is_upper = False
    
    if 0 < l < 1000:
        
        for i in range(l):
            if s[i].isalnum():
                is_alnum = True
                break
        
        for i in range(l):
            if s[i].isalpha():
                is_alpha = True
                
        for i in range(l):
            if s[i].isdigit():
                is_digit = True
                break
        
        for i in range(l):
            if s[i].isupper():
                is_upper = True
                break
        
        for i in range(l):
            if s[i].islower():
                is_lower = True
                break
                            
        print(is_alnum)
        print(is_alpha)
        print(is_digit)
        print(is_lower)
        print(is_upper)
        