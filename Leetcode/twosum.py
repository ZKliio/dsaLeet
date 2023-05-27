
def twoSum(nums, target):
    hashmap = {}
    
    for index, ele in enumerate(nums):
        
        diff = target - ele
        if diff in hashmap:
            print(hashmap)
            return [hashmap[diff], index]
        else:
            hashmap[ele] = index
            print(hashmap)
    




nums = [2,7,11,15]
print(twoSum(nums, 22))