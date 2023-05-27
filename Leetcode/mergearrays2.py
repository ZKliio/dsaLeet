def mergeTwoLists(list1, list2, m, n):
    l1 = list1
    l2 = list2
    i = m-1
    j = n-1
    z = len(l1) - 1
    while i >= 0 and j >= 0:
        print(l1)
        print(l2)

        if l1[i] >= l2[j]:
            # tmp = l1[i] 
            # l1[i] = l1[z]
            # l1[z] = tmp
            (l1[i], l1[z]) = (l1[z], l1[i])
            z-=1
            i-=1
        else:
            # tmp = l2[j]
            # l2[j] = l1[z]
            # l1[z] = tmp
            (l2[j], l1[z]) = (l1[z], l2[j])
            z-=1
            j-=1
        #print(l1)
        #print(f"i:{i}, j:{j}, z:{z}")
        
    if z == i:
        return l1
    else:
        while z >= 0:
            tmp = l2[j]
            l2[j] = l1[z]
            l1[z] = tmp
            z-=1
            j-=1
            print(l1)
        return l1



    


# l1 = [4, 0, 0, 0, 0, 0]
# m = 1
# l2 = [1, 2, 3, 5, 6]      
# n = 5

# l1 = [3, 5, 6, 0, 0, 0]
# m = 3
# l2 = [1, 2, 10]  
# n = 3      

l1 = [1, 2, 3, 0, 0, 0]
m = 3
l2 = [2, 5, 6]
n = 3


# l1 = [0]
# m = 0
# l2 =[1]
# n = 1

# l1 = [2, 0]
# m = 1
# l2 = [1]
# n = 1

# l1 = [1,2,4,5,6,0]
# m = 5
# l2 = [3]
# n = 1

# l1 = [0, 0, 3, 0, 0, 0, 0, 0, 0, 0]
# m = 3
# l2 = [-1, 1, 1, 1, 2, 3 ,3]
# n = 7
print(mergeTwoLists(l1, l2, m ,n))