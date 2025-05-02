#happy num
def happy_num(n) -> bool:
    ans = 0
    for i in n:
        ans =  ans + int(i)**2
    if ans == 1 :
        return True
    elif ans == 4:
        return False
    else:
        return happy_num(str(ans))
num = input("enter the num: ")
print(happy_num(num))