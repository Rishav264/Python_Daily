#so we have list and we have a target we have to return those elemnt in form of tuple like
# [1,2,3,4,5] k=6 the answer should be (2,4)(1,5)
def sum_tuple(list1,k):
    for i in range(len(list1)-1):
        for j in range(i+1,len(list1)):
            if list1[i] + list1[j] == k:
                print((list1[i],list1[j]))
list1 = list(map(int,input("enter the list: ").split()))
k = int(input("enter the target: "))
sum_tuple(list1,k)