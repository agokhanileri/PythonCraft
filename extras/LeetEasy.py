import math

#import numpy as np



# -----------------------------------
# LeetCode 796: String Rotation: Check if s2 is a rotation of s1
# Q: same length? --> no, need to check
    # case sensitive? --> yes
# Given:
str1 = "abcde"
str2 = "deabc"      # out = true
len1 = len(str1)
len2 = len(str2)

# Sol: try to find a fixed delay, O(n1+n2)
out = False
str3 = 2*str2   # str1 has to be a substring of str3
cnt, i, delay = 0, 0, 0
if (len1 == len2) and (len1>0):
    while (delay <= len1) and (i<len1):
        print(delay, i, cnt, str1[i], str3[i+delay])
        if str1[i] == str3[i+delay]:
            cnt += 1
            if cnt == len1: # if enough count reached
                out = True  # quit
                break
            i += 1
else:
            cnt = 0     # reset same char counter
            delay += 1  # try a different
out


##-----------------------------------
# LeetCode 217: Contains Duplicate, determine if a list/string has all unique characters
# Q:
# Given:
str1 = 'abcd123'       # out = True
str2 = 'abcd12a'       # out = False
n = len(str1)

# Sol1: 2 for loops O(n^2)

# Sol2: Convert to set and compare the lenghts, O(n)
myset = set(str1)
if n == len(myset):
    out = True
else:
    out = False
print(out)

# Sol3: map each (256) char to ASCI, O(n)
ascii_chars = 256*[0]
out = True
if n > 256:
    out = False             # there has to be a repetition
else:
    for char in str2:
        if ascii_chars[ord(char)] == 0: # if not encountered before
            ascii_chars[ord(char)] = 1
        else:       # same char seen earlier
            out = False
            break
print(out)




##-----------------------------------
# Leetcode 917: Reverse Only Letters (without affecting special chars)
s = ",Ab,c,c,ed"     # --> s = "ed,c,c,bA,"
n = len(s)

# Sol: 2ptr, O(n)/O(n) --> Can process the string in less then O(n) space?
arr = list(s)
i, j = 0, n-1
while i < j:
    if not arr[i].isalpha():    # iterate till a char
        i = i + 1
    if not arr[j].isalpha():
        j = j - 1
    arr[i], arr[j] = arr[j], arr[i]     # swap
    i = i + 1
    j = j - 1
s = ''.join(arr)


##-----------------------------------
# LeetCode 242: Valid anagram
s1 = "anagram"; t1 = "nagaram"            # --> True
s2 = "rat"; t2 = "car"                    # --> False

# Sol:
def isAnagram(word1, word2):
    n1 = len(word1); n2 = len(word2)
    if n1 != n2:
        return False
    #elif (n1==0) or (n2==0):
    #    return True
    if sorted(word1) == sorted(word2):  # works with empty words too
        return True
    else:
        return False
isAnagram(s1, t1)
isAnagram(s2, t2)


##-----------------------------------
# LeetCode 266: Palindrome Permutation
# -Determine if a permutation of the string could form a palindrome.
# Q: non letters? --> yes
# Given:
s = "carerac"   # --> racecar --> true
n = len(s)

# Sol: Can use array as hashmap
h = 256*[0]      # hash array of ascii chars
for ch in s:
    h[ord(ch)] += 1
odds = 0
for num in h:   # only 1 odd pair is allowed (mid char)
    if num % 2 == 1:
        odds += 1
if odds <= 1:
    ans = True
else:
    ans = False
print(odds, ans)


##-----------------------------------
# LeetCode 346: Moving Average from Data Stream
# Q:
# Given:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(arr)

# Sol: O(n)/O(1)
def update_avg(avg_old, num, n):
    avg_new = (avg_old*n + num)/(n+1)
    return avg_new

def get_avg(arr):
    avg = 0
    for i in range(len(arr)):
        avg = update_avg(avg, arr[i], i)
        print('i = ', i, ',avg =', avg)
    return avg

get_avg(arr)


##-----------------------------------
# LeetCode 66: Plus One (assume the array represent a #)
# Q:
  # is integer from 0 to 9? --> yes
  # can be empty? --> no
  # edge case --> 999 + 1 = return 1000
# Given:
arr = [1, 9, 9, 9, 8]
n = len(arr)

# Sol1:
carry = 1                       # since adding 1
for i in range(n-1, -1, -1):
    #print(i, arr[i], carry, arr)        # --> tester1
    if (arr[i] ==9)  and(carry==1):      # if still carry
        arr[i] = 0
        if i == 0:      # it at last element
            arr = [1] + arr
            #break
        carry = 1       # if mid elements, carry the overflow
    else:
        arr[i] = arr[i] + carry       # just add 1 regularly
        carry = 0
# if (carry == 1:
print(arr)


##-----------------------------------
# LeetCode 628: Maximum Product of Three Numbers
# Q:
  # Sorted --> No, you can't sort actually
  # Negative --> Yes
  # <3? --> Yes
  # return abs max or signed max? --> Signed
# Given:
arr = [-30, 10, -10, 3, 5, 6, 20]
n = len(arr)

# Sol1: O(n^3) / O(1)
if n < 3:
  print("size too small")
else:
  maxp = -float('Inf')
  for i in range(0, n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                maxp = max(maxp, arr[i]*arr[j]*arr[k])
print(maxp)

# Sol2: Sort and compare last 3 and first 2+last --> O(nlogn) / O(1)

# Sol3: Find max, 2nd max, 3rd max O(n) / O(1)
max1, max2, max3 = -float('Inf'), -float('Inf'), -float('Inf')
min1, min2, min3 = +float('Inf'), +float('Inf'), +float('Inf')
if n >= 3:
  for i in range(n):
    if arr[i] > max1:
      max3 = max2
      max2 = max1
      max1 = arr[i]
    elif max1 > arr[i] > max2:
      max3 = max2
      max2 = arr[i]
    elif max2 > arr[i] > max3:
      max3 = arr[i]

    if arr[i] < min1:
      min3 = min2
      min2 = min1
      min1 = arr[i]
    elif min1 < arr[i] < min2:
      min3 = min2
      min2 = arr[i]
    elif min2 < arr[i] < min3:
      min3 = arr[i]

# mins can result in bigger product if min1st and min2nd are negative
maxp = max(max1*max2*max3, min1*min2*max1)
print(maxp)


##-----------------------------------
# LeetCode 443: String Compression as letters and their counts
# Q: Char range? --> Assume a-Z
# Given:
string = "aabcdecaaa"  # out = a2b1c5a3
n = len(string)

# Sol:
i = 0
cnt = 1
out = ''
while i < n:
    i += 1
    if i == n:                  # last char
       out = out + string[i-1] + str(cnt) # dump
    elif string[i] == string[i-1]:
        cnt += 1                #
    else:                       # char change occured
        out = out + string[i-1] + str(cnt) # dump, O(n^2) op
        cnt = 1                 # reset to 1 (not 0)
if len(out) > len(string):
    out = string
out


##-----------------------------------
# LeetCode 1: Two Sum: Find all pairs from each array whose sum is equal to x. --> FIX
# Q: sorted? --> no
    # duplicate elements? --> no
    # same size? --> no
# Given:
arr1 = [1, 2, 4, 5, 7]
arr2 = [5, 6, 3, 4, 8, 2]
x = 9       # out = [[1, 8], [4, 5], [5, 4], [7, 2]]
n1, n2 = len(arr1), len(arr2)

# Sol 1: Brute force, O(n^2)
pairs = []
for num1 in arr1:
    for num2 in arr2:
        if num1 + num2 == x:
            pairs.append([num1,num2])
print(pairs)

# Sol 2: Shortcut, O(n^2)
print([(x-k,k) for k in arr2 if (x-k) in arr1])

# Sol 3: Hash 1st arr first, then search in arr2, O(n1 + n2)
    # no need to keep the order (index), so need of hashtable, just use hashset
    # if number range is limited, can use hash list, o.w. dict is better
d = dict()      # hash it as {element, comp} --> could just use HashSet infact
pairs = []   # results list
for i in range(n1):
    d[arr1[i]] = x - arr1[i]
    #d[str(arr1[i])] = ''   #open the key
print(d)

for j in range(len(arr2)):
    if arr2[j] in d.values():   # if matching found
        #d.get(arr2[j])
        pairs.append([x-arr2[j], arr2[j]]) # add the finding as a pair list into the results list
pairs


# Mod: Can be duplicate now but don't return the same results
arr1 = [1, 2, 3, 2, 3]
arr2 = [5, 5, 6, 5, 6, 7]
# Sol: just keep results in a set


##-----------------------------------
# Leetcode X (Google): Find the pairs in a sorted array that add up to a given sum
# Q: can it be same index? like 5 + 5 = 10 --> no
    # repeating elements? --> yes
    # can it be duplicate result? like (8,2) and (2,8) --> no, return one of them
    # can it return multiple results? like (8,2), (9,1) --> yes
    # can be they negative? --> yes, o.w. could stop searching if it exceeds target
    # integers? --> yes, but irrelevant
# Given
arr = [-1, -1, 1, 2, 7, 10, 10, 15]
x = 9          # --> out = [[2,7], [-1, 10]
n = len(arr)

# Sol: 2ptr if sorted, O(n) + sort = O(nlogn)
li = 0
ri = n - 1
pairs = set()
while li < ri:
    if arr[li] + arr[ri] < x:
        li = li + 1
    elif arr[li] + arr[ri] > x:
        ri = ri - 1
    elif (arr[li] + arr[ri]) == x:
        pairs.add((arr[li], arr[ri]))     # record the matches
        li = li + 1
        ri = ri - 1
pairs

# Mod: Unsorted
# Given
arr = [1, 2, 7, -1, 10, -1, 15]
n = len(arr)
# Sol 1: Brute Force, O(n^2)
matches = 0
i = 0
pairs = set()
for i in range(n):
    for j in range(i+1, n):
       if (arr[i] + arr[j] == x) and ((arr[j], arr[i]) not in pairs):
           matches += 1          # if want to return match or not, break after first match
           #print(matches, [i, j])
           pairs.add((arr[i], arr[j]))    # can't give a list to set
pairs

# Sol 2: HashSet, O(n)
 #carr = list(map(lambda x: x - summ, arr))  #  using map
 #carr = [x - summ for x in arr]              # more neat
 #carr = []*max(arr)  # max is O(n)
s = set()      # hashset
pairs = set()   # results list
for i in range(n):
    print(s)
    if (arr[i] in s) and ((x - arr[i], arr[i]) not in pairs):   # if complement found
        print("found at", i)
        pairs.add((arr[i], x - arr[i])) # add as a pair list into the results list
    else:   # otherwise, edtend the hashset
        s.add(x - arr[i])      # open a new entry
pairs


##-----------------------------------
# LeetCode 836: Rectangle overlap, 2 rectangles given with 2 coordinates
# Q: can it be sharing a line? --> yes, count it as no-overlap
    # guaranteed tr > bl? --> yes
    #
# Given: bottom left and top right in [x y]
bl1, tr1 = [0, 0], [5, 3]
bl2, tr2 = [6, 2], [10, 6]      # out = True

# Sol:
if (bl2[0] > tr1[0]) and (bl2[1] > tr1[1]):
    out = False
else:
     out = True

out


##-----------------------------------
# LeetCode 204: Count Primes, count the number of prime # between n1 and n2
# Q: Can n be negative? --> no
# Given:
n1 = 3
n2 = 12      # out = 4 (3, 5, 7, 11)

# Sol 1: O(n^2)/O(1)
def isprime(i) :
    if i == 1  or i % 2 == 0:
        return 0
    for j in range(2, 1 + math.floor(math.sqrt(i))) : # no need to scan beyond the sqrt(n)
        if (i % j) == 0 :  # if found a divisor
            return 0        # not a prime
    return 1        # if no divisor found

def countprimes(n1, n2) :
    if n1 > n2 :
        return 0
    if n1 < 2 :
        n1 = 2
    #primes = []     # solution set
    cnt = 0
    for i in range(n1, n2) :
       if isprime(i):
           cnt += 1
           #primes.append(i)
    return cnt
countprimes(n1, n2)


#----------------------
# LeetCode 485: Max Consecutive Ones, in a binary array
# Q:
# Given:
arr = [1, 1, 0, 1, 1, 1, 0, 0, 0, 0]
n = len(arr)

# Sol 1:
max_cnt = 0
cnt = 0
for i in range(n):
    if arr[i] == 1 :
        cnt += 1
        if cnt > max_cnt :
            max_cnt = cnt
    else :
        cnt = 0
max_cnt


#----------------------
# LeetCode 283: Move Zeroes, in place with minimal ops
# Q:
# Given:
arr = [0,1,0,3,12]      # out = [1,3,12,0,0]
n = len(arr)

# Sol:
zero_cnt = 0
i = 0
while i < (n - zero_cnt) :
    if arr[i] == 0:
        arr.pop(i)
        zero_cnt += 1
    i += 1
arr = arr + [0]*zero_cnt


#----------------------
# LeetCode 35: Search Insert Position
# Return the index of x in a sorted array, or return the index where it would be if it's inserted.
# 1 <= nums.length <= 10^4, -10^4 <= nums[i] <= 10^4, distinc values, -10^4 <= target <= 10^4
arr = [1, 3, 5, 6]
x1 = 2      # --> out = 1
x2 = 7      # --> out = 4
n = len(arr)

# Sol:
def sip(arr, x):
    i = 0
    while i < n :
        if x == arr[i]:
            return i    # return and be done
        elif x > arr[i]:
            i = i + 1
        else : # x < arr[i]: # increment until overflow
            return i
    return n    # if x > arr[-1], gotta place it at the end
sip(arr, x1)
sip(arr, x2)


#----------------------
# LeetCode 349: Intersection of Two Arrays
# Q: sorted --> yes
    # in increasing order? --> Google: yes
    # duplicates? --> yes
# Given:
arr1 = [1, 4, 4, 4, 5, 6, 7]
arr2 = [2, 3, 4, 6, 7]         # res = [4, 6, 7]
n1, n2 = len(arr1), len(arr2)

# Sol: O(n)/O(n), where n = max(n1, n2)
h = []  # common elements
i, j = 0, 0
while (i < n1) and (j < n2):
     if arr1[i] == arr2[j] :
         if h == []:
             h.append(arr1[i])      # record 1st common no matter what
         elif arr2[j] != h[-1]:     # for next, check if it's there
             h.append(arr1[i])
         i = i + 1
         j = j + 1
     elif arr1[i] > arr2[j]:
         j = j + 1
     else:
         i = i + 1
h

# Mod: Union     --> res = [1, 2, 3, 4, 5, 6, 7]
h = []
i, j = 0, 0
while (i < n1) and (j < n2):
     if arr1[i] < arr2[j] :     # place the smallest first and inc
         place = arr1[i]
         i = i + 1
     elif arr1[i] > arr2[j] :
         place = arr2[j]
         j = j + 1

     else : # arr1[i] == arr2[j]
         place = arr1[i]
         i = i + 1
         j = j + 1

     if h == [] or place != h[-1]:
         h.append(place)
h


#----------------------
# LeetCode 387: First Unique Character in a String
# Q: string type? --> all lowercase letters
# Given:
s = "coddec"    # o --> 1
n =  len(s)

# Sol: Hashtable
# h = [0]*(ord('z')-ord('a')) #
d = {}           # # get the counts in htable
for i in range(n):
    if s[i] not in d.keys():
        d[s[i]] = 1         # open a record
    else:
        d[s[i]] += 1        # inc the record
for key in d.keys():    # now scan the keys of the dict
    #print(key, d[key])
    if d[key] == 1:
        first_unique = key
        break
first_unique


##-----------------------------------
# LeetCode 100: Same Tree
# Given: root1, root2 --> need to create
# Sol: Recur with DFS and try to find a difference, O(min(n1,n2))/O(1)
def sametree(node1, node2):
    if node1== None and node2 == None:       # True if both are none
        return True
    if  node1 != None and node2 != None:   # gotta try to find a mismatch and return False
        print(node1.data, node2.data)
        if node1.data == node2.data:    # if same, recur for children
            left_check = sametree(node1.left, node2.left) # left branch same
            right_check = sametree(node1.right, node2.right) #
            return left_check and right_check  # signal OK from bottom to top
    return False      # if can't return true for all paths, then False
# sametree(root1, root2)


#----------------------
# LeetCode 252: Meeting Rooms, determine if a person can attend all the meetings
    # Start end times are given as array
# Q: can assume a day time such as 100? --> no
    # can assume Tend > Tstart --> yes
# Given:
arr = [[0,30],[5,10],[15,20]]  # --> False
n = len(arr)

# Sol: Sort, O(nlogn)/O(n)
def can_attend(arr):
    Tstart, Tend = [],[]
    for i in range(n):
        Tstart = Tstart + [arr[i][0]] # same as append
        Tend = Tend + [arr[i][1]]

    Tstart.sort()
    Tend.sort()
    print(Tstart, Tend)
    for i in range(n-1):
        print(i, Tstart[i+1], Tend[i] )
        if Tstart[i+1] < Tend[i]:
            return False
    return True
can_attend(arr)


#----------------------
# LeetCode 326: Power of Three
# Q:
# Given:
x = 81  # --> true

# Sol 1: Check if n % 3^(log3(max_int)) == 0
# Sol 2: Check if (Math.log10(n) / Math.log10(3)) % 1 == 0
# Sol 3:
def sol1(n):
    while n > 2 and n % 3 == 0:
        n = n // 3  # quotient, but same as / in this case
    return n == 1   # eventually it'll be like ..27/3, 9/3, 3/3 = 1
sol1(x)



#----------------------
# LeetCode 70: Climbing Stairs, find the distinct ways can you climb to the top
 # It takes n steps to reach to the top. Each time you can either climb 1 or 2 steps.
# Q: overflow? --> no needs exact landing
# Given:
n = 6       # 1+1+1, 1+2, 2+1 --> out = 3
s1 = 1      # step1
s2 = 2      # step2

ops = 0     # operation count
# Sol 1: Recursion, O(2^n) / O(1)
def climb(pos, n): # no need to carry counter as climb(pos, cnt, n)
    global ops
    if n <= 0:
        return 0
    else:
        if pos == n:
            #cnt = cnt + 1
            return 1
        elif pos < n:
            #print(pos)
            ops = ops + 1
            return climb(pos + s1, n) + climb(pos + s2, n)  # OR operation --> Addition
        else:
            return 0
climb(0, n)

# Sol 2: Add memoization, O(n) / O(n)
vmax = math.floor(n/s1)       # max iters vertically
memo = vmax*[None]   # pre init
def climb(pos, n, memo): # no need to carry counter as climb(pos, cnt, n)
    global ops
    if n == 0:
        return 0
    else:
        if pos == n:
            #cnt = cnt + 1
            return 1
        elif pos < n:
            #print(pos)
            if memo[pos] == 'None':
                memo[pos] = climb(pos + s1, n, memo) + climb(pos + s2, n, memo)
                ops = ops + 1
            else:
                return memo[pos]    # otherwise, no calculation
        else:
            return 0

climb(0, n, memo)

# Mod1: n = 9, step1,2 = 2, 5



#----------------------
# LeetCode 121: Best Time to Buy and Sell Stock, find the max profit
 # Given array whose i-th element is the price of a given stock on day i.
 # Max 1 buy/sell
# Q: Can you sell before you buy ? --> no
  # Can be negative? --> yes
  # can buy/sell at the same date? --> yes
# Given:
arr = [4, 7, 2, 6, 1, 2, 6, 2, 8, 4]        # profit
n = len(arr)

#Sol1: Brute force, for each day, scan the rest of days --> O(n^2)
#Sol2: Sort, and scan for the max delta O(n*nlogn), O(n) space for hashing days during sort
#Sol3: O(n)/O(1), 24ms
minn = arr[0]
maxx = arr[0]
max_profit = 0
n = len(arr)
if n < 2:
   profit = 0
else:
    for i in range(1, len(arr)):
        if prices[i] < minn:
            minn = arr[i]
            maxx = minn
            #maxx = arr[i]
        elif arr[i] > arr[i-1] :
            maxx = arr[i]
            profit = max(profit, maxx - minn)
        print(i, minn, maxx, profit)
print(profit)


#----------------------
# LeetCode 122: This time, buy/sell as many times
#Sol: O(n)/O(1)
buy = arr[0]
profit = 0
for i in range(1, len(arr)):
    if arr[i] < arr[i-1]:  # if down trend is observed, there's a local peak
        sell = arr[i-1]    # sell at the local peak
        profit += sell - buy  # add to the profit
        buy = arr[i]      # buy again
    print(i, profit)


#----------------------
# LeetCode 246: Strobogrammatic Numbe
# -Determine if a number (given as string) looks the same when rotated 180 degrees, like 69, 818
num = "1690691"  # --> True:
n= len(num)

# Sol: O(n)/O(5)
ans = True
d = {'0': '0', '1':'1', '8':'8', '6':'9', '9':'6'}
print(d.keys(), d.values())
for i in range(n):
    if num[i] not in d.keys():
        ans = False
    else:
        if num[-1-i] != d[num[i]]:
            ans = False
print(ans)





#----------------------
# LeetCode 276:	Paint Fence
n = 4; k = 2                               # --> 6

# Sol:
if k == 0 or n == 0:
    ways = 0
elif n == 1:
    ways = k
elif n == 2:
    ways = k*(k-1)
else:
    same = k
    diff = k*(k-1)
    for i in range(3,n+1):
    #print(i)
        same, diff = diff, (same + diff) * (k-1)

total = same + diff
print(total)



# -----------------------------------
# Leetcode 225: Implement Stack using Queues
# - should support all the functions of a normal stack (push, top, pop, and empty)


# -----------------------------------
# LeetCode 232: Implement Queue using Stacks


# ----------------------
# LeetCode 1025: Divisor Game
# Return True if and only if Alice wins the game for sure
# - Also, if a player cannot make a move, they lose the game. Alice goes next.
# - Choosing any x with 0 < x < N and N % x == 0, assuming both players play optimally.
# Q: N limits? --> yes, 1 <= N <= 1000
# N integer? --> yes
# Sol: Canwin if Bob loses --> canwin(N) = !canwin(N-x), O(n^2)/O(n)
def canwin(n, cache):  # cache is the boolean record of solutions
    print(cache)
    if n <= 1:
        return True  # no integer to pick between 0 < x < 1
    if cache[n - 1]:  # memoization part: if there's a solution
        print("omemo")
        return cache[n - 1]  # use it instead

    for x in range(1, round(n / 2 + 1)):  # no need to go all the way since max divisor is < n/2
        if (n % x) == 0:  # for a divisible number
            print("found divisor")
            if not canwin(n - x, cache):  # send it to backtracking,
                cache[n - 1] = True  # if Bob can't win, true, save the sol.
                return True
        # cache[n] = False    # not needed since below line covers it
    cache[n - 1] = False  # o.w. False
    return False


canwin(2, 2 * [None])  # a1 --> win  --> FIX
canwin(3, 3 * [None])  # a1 --> b1 --> lose
canwin(4, 4 * [None])  # a2 --> b1 --> lose but 1 --> a1 --> b1 --> a1 --> win
canwin(5, 5 * [None])  # can't do -1 -1, bob will win --> a1 --> b1 --> a2
canwin(6, 6 * [None])  # a2 --> b1 --> lose but 1 --> a1 --> b1 --> a1 --> win









