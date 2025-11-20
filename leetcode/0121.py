# 0121. Best Time to Buy and Sell Stock
# Given prices[i] is the price of a given stock on the i-th day.
# Return the max profit by choosing single day for buy and sell.
# If no profit possible (monotinacally decreasing), return 0.
# ----------------------------------------------------------------------
# Clarifications:
# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104

# ----------------------------------------------------------------------
# Inputs:
prices = [7,1,5,3,6,4]   # ans = 5
# prices = [7,6,4,3,1]  # ans = 0

# ----------------------------------------------------------------------
# Sol1: BruteForce, O(n^2) / O(1), Can't sort ince we need to keep the days, 
n = len(prices)
profit = 0
for i in range(n):
    j = i + 1
    profit_temp = 0
    while j < n:
        profit_temp = max(profit_temp, prices[j] - prices[i])
        print(i, j, profit_temp, profit)
        j = j + 1 
    print(i, profit_temp, profit)        
    profit = max(profit, profit_temp)    

# ----------------------------------------------------------------------
# Sol2: 2ptr, O(n) / O(1)
n = len(prices)
l = 0   # buy index
r = 1   # sell index
# buy_price = prices[i]
max_profit = 0                           # default return value 
#for i in range(1, n-1):                 # can't buy at the last day
while r < n:
    if (prices[l] < prices[r]):         # if there is a better buy price found
        profit = prices[r] - prices[l]  # calculate the temp profit
        max_profit = max(max_profit, profit)  # update the main profit
    else:                       # vice verse if better sell price found            
        l = r                   # move the buy ptr to the new local minima found
    r += 1              
max_profit

# ----------------------------------------------------------------------
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

        