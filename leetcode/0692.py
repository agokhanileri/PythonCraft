# 692. Top K Frequent Words
# Given an array of strings words and an integer k, return the k most frequent strings.
# Return the answer sorted by the frequency from highest to lowest. 
# Sort the words with the same frequency by their lexicographical order.

# ----------------------------------------------------------------------
# Clarifications:
Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.


# Inputs:
words = ["i","love","leetcode","i","love","coding"], k = 2  # out = ["i","love"]
# words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4 # out = ["the","is","sunny","day"]

# ----------------------------------------------------------------------
# Sol1: O() / O()


# ----------------------------------------------------------------------
# Submit: Sol1, O() / O()
class Solution:
    def 
    
        return 

# --------------
# Test:
sol = Solution()
print(sol.YYYY(x))


# 
import os
from collections import Counter, deque
import heapq as hq
         
## Q: Find top 10 most repeated words in that file with a lot of repeated words separated with single space
 

# Control Params
k = 10                      # top k words control param

# Read Words
fname = 'textinput.txt'
fpath = os.getcwd() + '\\' + fname
file = open(fpath, 'r+')  
data = file.read()  
words = data.split()        # default separator is any whitespace
# print(words)
n = len(words)

if (n == 0) or (k <= 0):    # if no words or bad k, no solution
    ans = []

# Create Dict    
dic = {}                    # else, build a dictionary or word counts
for w in words:             
    if w not in dic:        # if new entry
        dic[w] = 1          # cnt is 1
    else:               
        dic[w] = dic[w] + 1    # else, incr cnt

ans = []
if len(dic) <= k:            # if less than k distinct words, all of them are the solution
    for key in dic:
        ans.append(key)        
        
# Method 1: Create sortedList using values (item[1]), -1 factor because default is minSort and need maxSort
sortedList = sorted(dic.items(), key=lambda item: -item[1]) 
for i in range(k):
    ans.append(sortedList[i][0])   # get the words (1st element) of the tuple for top K items            
# print(ans)    

# Method 2: Create maxHeap, similarly -1 factor because default is minHeap and need maxHeap
ans = []
maxHeap = [(-value, key) for key, value in dic.items()] 
hq.heapify(maxHeap)        # build the heap
# print(maxHeap)
for i in range(k):
    ans.append(hq.heappop(maxHeap)[1])     # pop top(max) K words (2nd element of tuples)               
print(ans)               

#----------------
# Solution as a method, O(n)
class Tesla:
    def topKwords(self, words, k):
        # Boundary Check
        if (n == 0) or (k <= 0):    # if no words or bad k, no solution
            return []

        # Create Dict, time: O(n), space: O(m), n: # of words, m: # of distinct words
        dic = {}                    # else, build a dictionary or word counts
        for w in words:             
            if w not in dic:        # if new entry
                dic[w] = 1          # cnt is 1
            else:               
                dic[w] = dic[w] + 1    # else, incr cnt
         
        # Shortcut Solution        
        ans = []
        if len(dic) <= k:           # if less than k distinct words, all of them are the solution
            for key in dic:
                ans.append(key)
            return ans
                
        # Create maxHeap, O(log1+log2+...+logk)=O(logk!)=O(klogk) in worst case
        maxHeap = [(-value, key) for key, value in dic.items()] 
        hq.heapify(maxHeap)        # build the heap
        for i in range(k):
            ans.append(hq.heappop(maxHeap)[1])     # pop top K words one by one, O(logk)         
        return ans            

# Test the method
sol = Tesla()
print(sol.topKwords(words, k))

# Time: O(n*logk), assumung k < n, where n: dict size, k: heap size
# Space: O(n+k)

