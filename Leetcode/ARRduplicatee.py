def containsDuplicate(nums):
    hash = set()
    print(hash)
    for i in nums:
        if i in hash:
            return True
        else:
            hash.add(i)
            
    return False

nums =[0,1,2,3,4, 1]

print(containsDuplicate(nums))