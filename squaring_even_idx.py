#replacing every even index ele with square
def even_square(list1):
    if len(list1) <=1:
        return list1
    for i in range(0,len(list1),2):
        list1[i] = list1[i]**2
    return list1    
        
list1 = list(map(int,input("enter the list: ").split()))
print(even_square(list1))