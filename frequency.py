def freq(s):
    s = s.split()
    frq = {}
    for char in s:
        if char not in frq:
            frq[char] = 1
        else:
            frq[char]+=1
    for char,value in frq.items():
        print(char,value)
str1 = input("enter the string: ")
freq(str1)