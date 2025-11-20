# 0009. Palindrome Number
# Given an integer x, return true if x is a palindrome

# ----------------------------------------------------------------------
# Clarifications:
# If one digit? --> Palindrome
# Can pad with 0s s.t. 120 & 021? --> No, not Palindrome
# Negative number? --> Can't be Palindrome

# Inputs:
x = 1221 # --> True

# ----------------------------------------------------------------------
# Sol1: O(n) / O(1)
strx = str(x)                     # integer as string
n = len(strx)
if n == 1:
    ans = True            # no need
elif (x < 0) or (strx[-1] == '0'):
    ans = False             # no left zero padding allowed
else:
    for i in range(0, n // 2):      # n//2 will miss the mid number if n is odd, but we don't care
        print(i, strx[i], strx[-1-i])
        if strx[i] != strx[-1 - i]:
            ans = False             # 1 violation is enough to conclude
            break
    ans = True                      # no violations --> set True

# ----------------------------------------------------------------------
# Submit: Sol1, O(n) / O(1)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        intstr = str(x)
        n = len(intstr)
        if n == 1:
            return True
        elif (x < 0) or (intstr[-1]=='0'):
            return False
        else:
            for i in range(0, n//2):
                if intstr[i] != intstr[-1-i]:
                    return False
        return True

# --------------
# Test:
sol = Solution()
print(sol.isPalindrome(x))
