# 0217. Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, 
# Return false if every element is distinct.

# ----------------------------------------------------------------------
# Clarifications:
# 1 <= nums.length <= 105;  -109 <= nums[i] <= 109

# Inputs:
#nums = [1,1,1,3,3,4,3,2,4,2] # true
nums = [1,2,3,3]
nums = [1,2,3,2]
nums = [1,2,3,4]

# ----------------------------------------------------------------------
# Sol1: O(n) / O(n)
n = len(nums)
dic = {}
ans = False
for k in nums:
    print(k, list(dic.keys()))
    if k in dic.keys():                # if seen before
        ans = True        
    else:
        dic[k] =+ 1             # inc count
ans


# ----------------------------------------------------------------------
# Submit: Sol1 with hashset instead of dic, O() / O()
class Solution:
    def containsDuplicate(self, nums: list):
        #n = len(nums)
        hset = set()
        for k in nums:
            #print(k, hset)
            if k in hset:                # if seen before
                return True
            else:
            hset.add(k)
        return False                    # if no duplicates found

# --------------
# Test:
sol = Solution()
print(sol.containsDuplicate(nums))



