#armstrong
def arm_strong(n) -> bool:
    ans = 0
    for i in n:
        ans = ans + int(i)**3
    if int(n) == ans:
        return True
    else:
        return False

num = input("enter the num: ")
print(arm_strong(num))