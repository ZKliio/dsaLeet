def zero(ls):   
    l = 0
    r = len(ls)-1
    new = []
    for r in range(len(ls)):

        if ls[r] != 0:
            new.append(ls[r])
            r-=1

        # if ls[l] != 0:
        #     new.append(ls[l])
        #     l+=1

        # if ls[l] == 0:
    
        #     ls.append(ls[l])
        #     ls.remove(ls[l])
        #     l+=1
           
        if ls[r] == 0:

            ls.append(ls[r])
            ls.remove(ls[r])   
            r-=1 


        
            
            
            
    print(new)     
    return ls        











#ls = [0,1,0,3,12] #[0 1 0 3 12 0 0]
#ls = [10, 10, 0]

ls = [22, 12, 43, 56, 0]

#ls = [73348,66106,-85359,53996,18849,-6590,-53381,-86613,-41065,83457,0]
print(zero(ls))