#longest substring without repating alphabete

def uniq_str(s):
    check = "" 
    for char in s:
        if char not in check:
            check = check + char
    return len(check) == len(s)

def gener_sub(s):
    max = 0
    for i in range(len(s)):
        for j in range(i,len(s)):
            ele = s[i:j+1]
            if uniq_str(ele):
                if len(ele) > max:
                    max = len(ele)
    return max

s = input("enter the string: ")
print(gener_sub(s))                        