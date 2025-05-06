#reverse a string
def rev_str(str1) -> bool:
    rev =""
    for char in str1:
        rev = char + rev
    return rev    
    
st1 = input("enter the string: ")
print(rev_str(st1))