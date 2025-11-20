# 0628. Maximum Product of Three Numbers
# Given an integer array nums, find three numbers whose product is max and return the max product.

# ----------------------------------------------------------------------
# Clarifications:
# 3 <= nums.length <= 104, -1000 <= nums[i] <= 1000
# Distinct #? --> Not necessarily

# Inputs:
# nums = [-1,-4,3, 5, -2]  # -4*-2*5 = 40
nums = [7,3,1,0,0,6]  # -4*-2*5 = 40
# [1,2,3,2]

# ----------------------------------------------------------------------
# Sol1: Sort and then compare last3 vs first2*last, O(nlogn) / O(1)
n = len(nums)
if n ==3:
    maxprod = nums[0]*nums[1]*nums[2]
else:
    nums.sort()  # nums = [-4, -2, -1, 3, 5] 
    if (nums[0] >= 0) or (nums[-1] <= 0): # all pos/neg --> choose biggest/smallest (last) 3 #
        maxprod = nums[-1]*nums[-2]*nums[-3]  
    else:  # both pos/neg --> choose either last 3 #, or (first 2 neg # and last pos #)    
        maxprod = max(nums[0]*nums[1]*nums[-1], nums[-3]*nums[-2]*nums[-1])
    
maxprod    

# ----------------------------------------------------------------------
# Sol2: Dynamically update min1,2, max1,2,3 and compare in the end, O(n) / O(1)
n = len(nums)
if n ==3:
    maxprod = nums[0]*nums[1]*nums[2]
else:  # assume min1 < min2 ... max3 < max2 < max1 
    min1, min2 = 1000, 1000
    max1, max2, max3 = -1000, -1000, -1000  
    for i in range(n):
        if nums[i] <= min1:     # new absolute min
            min2 = min1         # previous min1 is now our 2nd min
            min1 = nums[i]      # update(lower) min1                        
        elif nums[i] <= min2:   # found the 2nd min, <= instead of < because it could 2 abs mins
            min2 = nums[i]      # update(lower) min2
            
        if nums[i] >= max1:     # new absolute max
            max3, max2 = max2, max1 # previous max3/max2 is now max max2/max1 (shifted)
            max1 = nums[i]      # update(raise) max1                    
        elif nums[i] >= max2:   # found the 2nd max
            max3 = max2         # previous max2 is now max3
            max2 = nums[i]      # update(raise) max2          
        elif nums[i] >= max3:    # found the 3rd max
            max3 = nums[i]            
        print(min1,min2,max3,max2,max1)
    maxprod = max(max1*min1*min2, max1*max2*max3)
    print(maxprod)

# ----------------------------------------------------------------------
# Submit: Sol1, O() / O()
class Solution:
    def maximumProduct(self, nums):        
        n = len(nums)
        if n ==3:
            return nums[0]*nums[1]*nums[2]
        else:  # assume min1 < min2 ... max3 < max2 < max1 
            min1, min2 = 1000, 1000
            max1, max2, max3 = -1000, -1000, -1000  
            for i in range(n):
                if nums[i] <= min1:      # new absolute min
                    min2 = min1         # previous min1 is now our 2nd min
                    min1 = nums[i]      # update(lower) min1                        
                elif nums[i] <= min2:    # found the 2nd min
                    min2 = nums[i]      # update(lower) min2
                    
                if nums[i] >= max1:      # new absolute max
                    max3, max2 = max2, max1 # previous max3/max2 is now max max2/max1 (shifted)
                    max1 = nums[i]      # update(raise) max1                    
                elif nums[i] >= max2:    # found the 2nd max
                    max3 = max2         # previous max2 is now max3
                    max2 = nums[i]      # update(raise) max2                
                elif nums[i] >= max3:    # found the 3rd max
                    max3 = nums[i]
                #print(min1,min2,max3,max2,max1)                
            return max(max1*min1*min2, max1*max2*max3)

# --------------
# Test:
sol = Solution()
sol.maximumProduct(nums)


