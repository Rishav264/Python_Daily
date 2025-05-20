#counting palindrome substring in string
def check_pali(s):
    ans = ""
    for char in s:
        ans = char + ans
    return ans == s

def genrate_sub(s):
    count = 0
    for i in range(len(s)):
        for j in range(i,len(s)):
            str1 = s[i:j+1]
            if check_pali(str1):
                count+=1
    return count               

s = input("enter the string: ")
print(genrate_sub(s))