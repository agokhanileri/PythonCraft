# 0136. Single Number
# Given a non-empty array of integers nums, every element appears twice except for one. Find it in O(n)/O(1) sol.

# ----------------------------------------------------------------------
# Clarifications:
# 1 <= nums.length <= 3 * 104;  -3 * 104 <= nums[i] <= 3 * 104

# Inputs:
nums = [4,1,2,1,3, 2, 4]

# ----------------------------------------------------------------------
# Sol1: Using dict as hashset O(n) / O(n)
n = len(nums)
if n == 1:
    ans = nums[0]
else:
    dic = {}
    for i in nums:
        if i not in dic:        # 
            dic[i] = 1          # count of that number
        else:
            del dic[i]          # instead of increasing the count, delete the whole key
    ans = list(dic.keys())[0]   # so the remaning item will be the singleNumber

# ----------------------------------------------------------------------
# Sol2: Using Bitwise, O(1) / O(1)
#n = len(nums)
ans = 0                        
for i in nums:                  # if we keep XORing every binary #, dublicates will converge to 0
        ans ^= i                # bitwise XOR all nunmbers, single number will remain uncancelled
ans


# ----------------------------------------------------------------------
# Submit: Sol2, O(1) / O(1)
class Solution:
    def singleNumber(self, nums: list):
        ans = 0                     # will also work for singleNumber == 0 case
        for i in nums:              # if we keep XORing every binary #, dublicates will converge to 0
            ans ^= i                # bitwise XOR all nunmbers, single number will remain uncancelled        
        return ans

# --------------
# Test:
sol = Solution()
print(sol.singleNumber(nums))



