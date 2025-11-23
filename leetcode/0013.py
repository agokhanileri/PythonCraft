# 0013. Roman to Integer
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D, M
# L = 50, C = 100, D = 500, M = 1000
# ----------------------------------------------------------------------
# Clarifications:
# 1 <= s.length <= 15
# s contains only roman characters and is the range [1, 3999]

# ----------------------------------------------------------------------
# Inputs:
# s = "LVIII"   # ans = 58
# s = "MCMXCIV"  # ans = 1000 + 900 + 90 + 4 = 1994
s = "III"  # ans = 3

# ----------------------------------------------------------------------
# Sol1: O(1) / O(1)
# Negative numbers can only occur in a pair AB if A < B
# So we can slide [AB] left to right
n = len(s)
d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

res = 0  # will be summed left to right, ignoring the last element
for i in range(n - 1):  # scan characters L2R in sliding windows of 2 (AB)
    if d[s[i]] < d[s[i + 1]]:  # if A<B it means A is neg.
        res -= d[s[i]]
    else:
        res += d[s[i]]
res += d[s[-1]]  # last element has no follower --> always pos.
res


# ----------------------------------------------------------------------
# Submit: 2ptr, O(n) / O(1)
class Solution:
    def romanToInt(self, s: str) -> int:
        n = len(s)
        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        res = 0  # will be summed left to right, ignoring the last element
        for i in range(n - 1):  # scan characters L2R in sliding windows of 2 (AB)
            if d[s[i]] < d[s[i + 1]]:  # if A<B it means A is neg.
                res -= d[s[i]]
            else:
                res += d[s[i]]
            # print(i, res)  # testing
        res += d[s[-1]]  # last element has no follower --> always pos.
        return res



# --------------
# Test:
sol = Solution()
print(sol.romanToInt(s))
