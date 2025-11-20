# 0013. Roman to Integer
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D, M
# L = 50, C = 100, D = 500, M = 1000
# ----------------------------------------------------------------------
# Clarifications:
# 1 <= s.length <= 15 
# s contains only roman characters and is the range [1, 3999]

# ----------------------------------------------------------------------
# Inputs:
#s = "LVIII"   # ans = 58
s = "MCMXCIV"  # ans = 1000 + 900 + 90 + 4 = 1994

# ----------------------------------------------------------------------
# Sol1: O(1) / O(1)
# Negative numbers can only occur in a pair AB if A < B
# So we can slide [AB] left to right
n = len(s)
d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

res = 0     # will be summed left to right, ignoring the last element
for i in range(n-1):    # scan characters L2R in sliding windows of 2 (AB)
    if d[s[i]] < d[s[i+1]]:  # if A<B it means A is neg.
        res -= d[s[i]]
    else: 
        res += d[s[i]]
res += d[s[-1]]     # last element has no follower --> always pos.
res


# ----------------------------------------------------------------------
# Submit: 2ptr, O(n) / O(1)
class Solution:
    def maxProfit(self, prices: list[int]) -> int:        
        n = len(prices)
        l = 0       # buy day#
        r = 1       # sell day# (always on the right)
        max_profit = 0                           # default return value
        while r < n: 
            if (prices[l] < prices[r]):         # scan to find a better sell price
                profit = prices[r] - prices[l]  # calculate the temp profit
                max_profit = max(max_profit, profit)  # update the main profit
            else:                       # if a new losing sell date found           
                l = r                   # move the buy ptr to the new local minima found
            r += 1
                
        return max_profit
    
# --------------
# Test:
sol = Solution()
print(sol.maxProfit(prices))

