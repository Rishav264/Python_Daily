#moving all the zeros to end like [1,0,2,0,3,0] -> [1,2,3,0,0,0]
def moving_zero(list1):
    ans = []
    zero=[]
    for char in list1:
        if int(char) == 0:
            zero.append(char)
        else:
            ans.append(char)
    sol = ans + zero
    return sol            

list1 = list(map(int,input("enter the list: ").split()))
print(moving_zero(list1))