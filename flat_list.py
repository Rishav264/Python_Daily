#nested list to flat list
ans = [] #if this is delclared inside the fucntion with  recusrion it will become empty with each iteration 
def flat_l(list1):
    for i in list1:
        if type(i) == list:
            flat_l(i)
        else:
            ans.append(i)
    return ans        

list1 = [1,2,[3,4,5,6],7,[8,9]]
print(flat_l(list1))