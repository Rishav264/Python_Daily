#removing all the element from list which are divisible by a given number
def removing_ele(list1,k):
    ans =[]
    for char in list1:
        if int(char)%k != 0:
            ans.append(char)
    return ans        
list1 = list(map(int,input("enter the list: ").split()))
k = int(input("enter the number whose divisble number u want to remove: "))
print(removing_ele(list1,k))