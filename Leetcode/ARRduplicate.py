def containsDuplicate(nums):
    nums = sorted(nums)
    i = 0
    for j in range(1, len(nums)):
        if nums[i] == nums[j]:
            return True
        else:
            i+=1
            j+=1
    return False
    






nums =[0,1,2,3,4]
print(containsDuplicate(nums))

# nums = sorted(nums)
#     start = 0 
#     for i in range(len(nums)):
#         start +=1
#         for j in range(start,len(nums)):
#             if nums[i] == nums[j]:
#                  return True
     
        
            
#     return False
