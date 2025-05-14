#anagram 
def ana(str1,str2):
    str1 = list(str1)
    str2 = list(str2)
    return str1.sort() == str2.sort()
    
str1 = input("enter the string: ")
str2 = input("enter the string: ")
print(ana(str1,str2))