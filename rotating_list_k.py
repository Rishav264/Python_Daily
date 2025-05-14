#roataing the list by k steps
#[1,2,3,4,5] roatae by 2 -> [4,5,1,2,3]
def roating_list(list1,k):
    n = len(list1)
    k = k%n
    for i in range(k):
        last = list1.pop()
        list1.insert(0,last)
    return list1    
        
list1 = list(map(int,input("enter the list: ").split()))
k = int(input("enter k: "))
print(roating_list(list1,k))