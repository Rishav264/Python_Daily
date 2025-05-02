def check_prime(n) -> bool:
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

def interval_print(start,end):
    for i in range(start,end):
        if check_prime(i):
            print(i)

num1 = int(input("enter the starting point: "))
num2 = int(input("enter the ending point: "))
interval_print(num1,num2)