#find the missing postive integer in the list 
# like [0,1,3,4,5] missing integer = 2
def missing_val(list1):
    for i in range(len(list1)-1):
        if list1[i+1]!=list1[i]+1:
            print(list1[i]+1)

list1 = list(map(int,input("enter the list: ").split()))
missing_val(list1)