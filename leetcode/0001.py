# 0001. Two Sum
# Return indices of the two numbers such that they add up to target. Only 1 valid answer exists.

# ----------------------------------------------------------------------
# Clarifications:
# Assume there will be exactly 1 sol. You can't use the same element twice.
# 2 <= nums.length <= 10e4, -10e9 <= nums[i] <= 10e9, -10e9 <= target <= 10e9

# Inputs:
nums = [3, 2, 5, 6, 5]; target = 7   # ans = [1, 2]
n = len(nums)

# ----------------------------------------------------------------------
# Sol1: Brute force, O(n^2) / O(1)
ans = [-1, -1]
for i in range(n):
    for j in range(i+1, n):
        print(i, j)
        if (nums[i] + nums[j]) == target:
            ans = [i, j]
            break

print(ans)

# ----------------------------------------------------------------------
# Sol2: Hashtable, need to keep a reversed dict for O(1) lookup, or use enumarate. O(n) / O(1)
ans = [-1, -1]
ht1 = dict()             # can't use hset since we need the report the index
ht2 = dict()
j = 0
for i in range(n):
    print(i, ht1, ht2)
    if (target - nums[i]) in ht1.values():   # since there's 1 sol, check for it first so we are done
        print('match found, quitting')
        j = ht2[(target - nums[i])]         # can overwrite j since we are gonna finish the loop anyway\
        ans = [j, i]                # report right away and stop
        break
    if nums[i] not in ht1.values():          # if not seen before
        print('not found, adding')
        ht1[j] = nums[i]
        ht2[nums[i]] = j            # form the reverse hash table for easy lookup
        j = j + 1

print(ans)


# ----------------------------------------------------------------------
# Submit: Sol2, O(n) / O(1)
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        ht1 = dict()        # {indx: num}, can't use hset since we need the report the indx
        ht2 = dict()        # {num: indx}, so we use a reversed version to access indexes in O(1)
        j = 0
        for i in range(n):
            print(i, ht1, ht2)
            if (target - nums[i]) in ht1.values():  # if there's a match, we are done
                j = ht2[(target - nums[i])]         # obtain the index of first pair,
                # can overwrite j since we are done anyway
                return [j, i]                       # report and quit since there is only 1 sol

            if nums[i] not in ht1.values():         # if not seen before
                ht1[j] = nums[i]
                ht2[nums[i]] = i                    # form the reverse htable
                j = j + 1                           # length counter for both htables

        return [-1, -1]                             # if n = 0 or no sol, return -1s

# Test:
# nums = [3, 2, 1, 0, 1, 5, 6, 5]; target = 7   # ans = [5, 1]
nums = [1,1,1,1,1,4,1,1,1,1,1,7,1,1,1,1,1];  target = 11   # ans = [5, 11]
sol = Solution()
print(sol.twoSum(nums, target))


