def zero(nums):   
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j]= temp
            j +=1


    return nums



nums = [0,1,0,3,12] #[0 1 0 3 12 0 0]
#ls = [10, 10, 0]

#nums = [22, 12, 43, 56, 0]
#nums = [0, 0, 1]
#nums = [73348,66106,-85359,53996,18849,-6590,-53381,-86613,-41065,83457,0]
print(zero(nums))        