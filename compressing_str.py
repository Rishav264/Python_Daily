#aaabbbcc -> a3b3c2
def compress_str(s):
    uq = uniq_str(s)
    ans =""
    for char in uq:
        ans = ans + char + str(s.count(char))
    return ans    

def uniq_str(s):
    uq =""
    for char in s:
        if char not in uq:
            uq = uq + char
    return uq        

str1 = input("enter the string: ")
print(compress_str(str1))