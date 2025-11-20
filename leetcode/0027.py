# 0027. Remove Element
# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place and return k, # of remaining elements.
# First k elements of nums contain the elements (order irrelevant) which are not equal to val. Remaining elements aren't important

# ----------------------------------------------------------------------
# Clarifications:
# Inputs:
nums = [1, 2, 3, 4, 2, 5, 2];   # input array
val = 2;                        # value to remove --> nums = [1, 3, 4, 5, _,_,_] --> k = 4

# ----------------------------------------------------------------------
# Sol1: O(n) / O(1)
n = len(nums)
k = n
i = 0
while i <= k: 
    if nums[i] == val:
        nums.pop(i)
        print(nums)
        k = k - 1 
    else:
        i = i + 1

print(i, k, nums)

# ----------------------------------------------------------------------
# Submit: Sol1, O(n) / O(1)
class Solution:
    def removeElement(self, nums, val) -> int:
        n = len(nums)
        k = n
        i = 0
        while i < k: 
            if nums[i] == val:
                nums.pop(i)
                print(i, k, nums)
                k = k - 1 
            else:
                i = i + 1

        print(i, k, nums)
    
        return i     

# --------------
# Test:
sol = Solution()
print(sol.removeElement(nums, val))

# Judge
expectedNums = [1, 3, 4, 5] # The expected answer with correct length.
k = sol.removeElement(nums, val); # Calls your implementation
assert k == len(expectedNums)
nums.sort() # Sort the first k elements of nums
#for i in range(len(expectedNums)):
    #assert nums[i] == expectedNums[i]