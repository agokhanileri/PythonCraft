# 0344. Reverse String
# Write a function that reverses a string. The input string is given as an array of characters s in-place (O(1) space).

# ----------------------------------------------------------------------
# Clarifications:

# Inputs:
s = ["H","a","n","n","a","h"]

# ----------------------------------------------------------------------
# Sol1: O() / O(1)
n = len(s)
mid = n // 2       
for i in range(0, mid):
    temp = s[-i - 1]
    s[-i - 1] = s[i]
    s[i] = temp
    

# ----------------------------------------------------------------------
# Submit: Sol1, O() / O()
class Solution:
    def reverseString(self, s):
        """Do not return anything, modify s in-place instead."""
        mid = len(s) // 2
        for i in range(0, mid):
            temp = s[-i - 1]
            s[-i - 1] = s[i]
            s[i] = temp
            
# --------------
# Test:
sol = Solution()
sol.reverseString(s)
print(s)

