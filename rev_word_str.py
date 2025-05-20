# i love python --> python love i
def rever_word(s):
    sl = s.split()
    ans = []
    for i in range(len(sl)-1,-1,-1):
        ans.append(sl[i])
    return ' '.join(ans)

s = input("enter the string: ")
print(rever_word(s))    

