#Find all elements that appear more than once but less than three time
def ele_count(list1):
    char_li = []
    count_li = []
    for i in list1:
        if i not in char_li:
            char_li.append(i)
            count_li.append(1)
        else:
            idx = char_li.index(i)
            count_li[idx] += 1
    ans = []        
    for k in range(len(count_li)):
        if count_li[k] > 1 and count_li[k] < 3:
            ans.append(char_li[k])
    return ans        
        
list1 = list(map(int,input("enter the list: ").split()))
print(ele_count(list1))