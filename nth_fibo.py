# nth multiple of fibo series
# the fibo sreis will keep ongoing on till we will keep count how many num in fibo is divisible
# by m till n count then we will get the nth num which we will return 

def fibo_nth_mth_div(n,m) -> int:
    a=0
    b=1
    count = 0
    while True:
        a,b = b,a+b
        if b%m == 0:
            count+=1
        if count == n:
            return b
            break

n = int(input("enter the num: "))
m = int(input("enter the divisor: "))
print(fibo_nth_mth_div(n,m))