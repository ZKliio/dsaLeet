def zero(ls):   
    counter = 0
    new = []
    for r in range(len(ls)):

        if ls[r] != 0:
            new.append(ls[r])
        elif ls[r] == 0:
            counter+=1
        

    for i in range(counter):
        new.append(0)
    ls = new
    return ls



ls = [0,1,0,3,12] #[0 1 0 3 12 0 0]
#ls = [10, 10, 0]

#ls = [22, 12, 43, 56, 0]
#ls = [0, 0, 1]
#ls = [73348,66106,-85359,53996,18849,-6590,-53381,-86613,-41065,83457,0]
print(zero(ls))        