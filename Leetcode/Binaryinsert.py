def searchInsert(nums, target):
        lo = 0 
        hi = len(nums)-1

        while (hi-lo)>1:
            mid = (lo + hi)//2
            if target < nums[mid]:
                hi = mid
            elif target > nums[mid]:
                lo = mid+1
            elif target == nums[mid]:
                return mid
        if target == nums[lo]:
            return lo
        elif target == nums[hi]:
            return hi
        elif target < nums[lo]:
            nums.insert(lo, target)
            return lo
        elif target< nums[hi]:
            nums.insert(lo+1, target)
            return lo+1
        elif target > nums[hi]:
            nums.append(target)   
            return hi+1     
        

nums = [1,3,5,6]

print(searchInsert(nums, 7))