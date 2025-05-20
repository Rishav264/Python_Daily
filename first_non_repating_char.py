#first non repating char in a string like aaabbbcdee -> c 
def f_non_rep_char(s):
    for char in s:
        if s.count(char) == 1:
            return char
    return '-1'

s = input('enter the string: ')
print(f_non_rep_char(s))    

