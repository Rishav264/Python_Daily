#neon number
def neon_num(num):
    sq = str(int(num)**2)
    sum1 = 0
    for i in sq:
        sum1 = sum1 + int(i)
    if sum1 == int(num):
        return True
    else:
        return False

num = input("enter the number: ")
print(neon_num(num))
    