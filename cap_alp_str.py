def cap_even_idx(str1):
    ans =""
    for i in range(len(str1)):
        if i%2 == 0:
            ans += str1[i].upper()
        else:
            ans += str1[i].lower()
    return ans             

str1 = input("enter the string: ")
print(cap_even_idx(str1))