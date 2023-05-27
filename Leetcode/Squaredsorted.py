# from nums import nums
def squareSort(nums):
    new = []
    l = 0
    r = len(nums)-1

    while l<= r:
        
        if (nums[l]*nums[l]) > (nums[r]*nums[r]):
            new.append(nums[l]*nums[l])
            l+=1
            print(f"this is l:{l}")
        else:
            new.append(nums[r]*nums[r])
            r-=1
            print(f"this is r:{r}")
    
    return new[::-1]




nums = [-4, -2, 0, 1, 3, 5]
print(squareSort(nums))