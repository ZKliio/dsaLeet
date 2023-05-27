def mergeTwoLists(list1, list2, m, n):
    l1 = list1
    l2 = list2
    # if len(l1) == 1:
    #         print(69)
    #         for _ in range(len(l1)):
    #            l1[_] = l2[_]
    #         return l1
    # elif len(l2) == 1:
    #         print(69)
    #         return l1
    
    z = len(l1)-1

    # i = len(l2)-1
    # j = len(l2)-1
    i = m
    j = n 

    while z > 0 and i>=0:
        print(i)
        print(z)
        if l1[i] == 0:
              i-=1
        elif l1[i] >= l2[j]:
                tmp = l1[i]
                l1[i] = l1[z]
                l1[z] = tmp
                i-=1
                z-=1
                print(l1)
                print(l2)
        elif l2[j] >= l1[i]:
                tmp = l2[j]
                l2[j] = l1[z]
                l1[z] = tmp
                j-=1
                z-=1
                print(l1)
                print(l2)
    print(f"sort ended, z:{z}, i:{i}")
    # _i = 0
    
    
    if i != 0:
        while z > -1: #and _j < len(l2):
            # print(_i)
            # print(_j)
            
            print(l1)
            print(l2)
            tmp = l1[z]
            l1[z] = l2[z]
            l2[z] = tmp
            z-=1
        print(f"final l1:{l1}")
        print(f"final l2:{l2}")
        return l1
    else:
        print(f"final l1:{l1}")
        print(f"final l2:{l2}")
        return l1
        
    #while   
    


# l1 = [4, 0, 0, 0, 0, 0]
# l2 = [1, 2, 3, 5, 6]      

# l1 = [3, 5, 6, 0, 0, 0]
# l2 = [1, 2, 10]        

# l1 = [1, 2, 3, 0, 0, 0]
# m = 3
# l2 = [2, 5, 6]
# n = 3


# l1 = [0]
# l2 =[1]

# l1 = [2, 0]
# l2 = [1]

l1 = [1,2,4,5,6,0]
m = 5
l2 = [3]
n = 1

print(mergeTwoLists(l1, l2, m ,n))