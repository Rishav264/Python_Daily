# revrse vowel
def rever_vowel(str1) -> str:
    vowel = 'aeiouAEIOU'
    list1 = list(str1)
    i = 0;
    j = len(list1)-1
    while i < j:
        if list1[i] not in vowel:
            i = i+1
        if list1[j] not in vowel:
            j = j-1
        else:
            list1[i],list1[j] = list1[j],list1[i]
            i = i+1
            j = j-1
    return "".join(list1)        
str1 = input("enter the string: ")
print(rever_vowel(str1))