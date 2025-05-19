def pali(str1):
    check =""
    str1 = str1.lower()
    for char in str1:
        check = char + check
    return check == str1    

str1 = input('enter the string: ')
print(pali(str1))