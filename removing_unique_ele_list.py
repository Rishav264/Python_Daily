def unq_rmv(list1):
    ans =[]
    for char in list1:
        if char not in ans:
            ans.append(char)
    return ans        

list1 = list(map(int,input("enter the list: ").split()))
print(unq_rmv(list1))