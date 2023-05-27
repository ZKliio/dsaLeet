def mergeTwoLists(list1, list2):
    #l3 = list1+list2
    l = []
    i = 0
    j = 0
    
    
    if list1 == [] or list2 == []:   
        return list1+list2
    
    length = len(list1) + len(list2)
    z = 1 
    while z < length:
        # print(i, "i")
        # print(j, "j")
        if list1[i] <= list2[j]:
            l.append(list1[i])
            #print(l)
            i+=1
            z+=1

        elif list1[i] > list2[j]:
            l.append(list2[j])
            #print(l)
            j+=1
            z+=1
   
    for i in l:
        print(i)
    
    return l
        

list1 = [1,2,4]
list2 = [1,2,3,4]        

# list1= []
# list2 = []
print(mergeTwoLists(list1, list2))

            
    













#print(mergeTwoLists(list1 = [1,2,4], list2 = [1,3,4]))