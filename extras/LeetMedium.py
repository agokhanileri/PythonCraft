import math

# import numpy as np

for name in dir():
    if not name.startswith('_'):
        del globals()[name]


# -----------------------------------
# LeetCode 161: One Edit Distance (prem)
str1, str2 = "abcd", "abdc"             # --> True

n1, n2 = len(str1), len(str2)
out = True                              # if diff <=1
diff = 0
i1, i2 = 0, 0
if abs(n1 - n2) > 1:                    # if +1 diff, then no way
    out = False
else:  # if it's doable, check if only 1 op
    while (i1 < n1) and (i2 < n2):
        if str1[i1] != str2[i2]:
            diff += 1
            print("diff", i1, i2)
            if n1 > n2:
                i1 += 1
            elif n2 > n1:
                i2 += 1
            else:
                i1 += 1
                i2 += 1
        else:
            i1 += 1
            i2 += 1
        if diff > 1:                    # scan for an early decision
            out = False
            print("break", i1, i2)
            break

print(out)


# -----------------------------------
# LeetCode 40: Given sorted, repetitive, find nums summing to summ --> FIX
numm = list(range(0, 1000+1))
summ = 1500
n = len(numm)

# Sol1: linear * dec_linear --> O(n^2) / O(?)
for i in range(0, n):
    for j in range(i + 1, n):
        if numm[ i ] + numm[ j ] == summ:
            break
    if numm[ i ] + numm[ j ] == summ:
        print('Yes, 1st pair summing to', summ, ': ', numm[ i ], numm[ j ])
        break

# Sol2:
i = 1
j = n-1
while i < j :
    s = numm[i] + numm[j]
    if s == summ:
        print('Yes, 1st pair summing to', summ, ': ', numm[ i ], numm[ j ])
        break
    elif s > summ:
        i = i + 1
    else: # s < summ
        j = j - 1

# Sol3: Covers unsorted (binary search = nlogn)
numm = np.array([10, 0, 0, 9, 9, 1, 8, 2, 7, 3, 6, 4, 5, 5])
summ = 15

n = len(numm)
numd = summ - numm
i = 1
j = 2
for i in range(0, n):
    for j in range(i + 1, n):
        pass
        # if numd[j] == summ[i]:
        # s = numm[i] + numm[j]
    if numm[i] + numm[j] == summ:
        print('Yes, 1st pair summing to', summ, ': ', numm[ i ], numm[ j ])
        break
    elif s > summ:
        i = i + 1
    else: # s < summ
        j = j - 1


# -----------------------------------
# LeetCode 136: Find the 2 non-repeating numbers in an integer array
arr = [2, 4, 7, 8, 4,  8, 2]  # Output: 7
n = len(arr)

# Sol1: Sort and compare with adjacent elements O(nlogn) / O(1)

# Sol2: Use XOR O(n) / O(1)
xor = 0   # 0^x = x
for i in range(0, n):
  xor = xor^arr[i]
print(xor)


# Mod1: What if there are 2 non-repeating elements instead?
arr = [2, 4, 3, 8, 5, 4,  8, 2]  # Output: 3, 5
n = len(arr)

# Sol3:
xor, x, y = 0, 0, 0
for i in range(0, n):
  xor = xor^arr[i]
  set_bit_no = xor & ~(xor-1)   # get the rightmost set bit

for i in range(0, n):
  if arr[i] & set_bit_no:     # compare with xor set bit
    x = x ^ arr[i]              # xor of first set
  else:
    y = y ^ arr[i]            # xor of 2nd set

print(x, y)


# -----------------------------------
# LeetCode 48: Rotate an n*n image 90deg clockwise in-place
# Q: image value range? --> doesn't matter, say 0-100
mat = [[1,2,3,4],           # [7,4,1]
       [5,6,7,8],           # [8,5,2]
       [9,10,11,12],
       [13,14,15,16]]       # [9,6,3]
# m, n = len(mat), len(mat[0])
n = len(mat)

# Sol1:
off = 0
while off < int(n/2 - n%2/2):
    for i in range(0+off, n-1-off):
            mat[off][i], mat[i][n-1-off], mat[n-1-off][n-1-i], mat[n-1-i][off] = \
            mat[n-1-i][off], mat[off][i], mat[i][n-1-off], mat[n-1-off][n-1-i]
    off = off + 1
mat

# Mod1: Rotate clockwise by 1 element only (Google)
# Sol2: assume one line as [1 2 3 4 8 12 11 10 9 5]
off = 0
while off < int(n/2 - n%2/2):
    for i in range(0+off, n-1-off):
        if i == off:
            mat[i][i], mat[i][n-1-off], mat[n-1-i][n-1-i], mat[n-1-i][i] = \
            mat[i+1][i], mat[i][n-2-off], mat[n-2-i][n-1-i], mat[n-2-i][i]
        #elif (i == n-1-off):
            #mat[off][i], mat[i][n-1-off], mat[n-1-off][n-1-i], mat[n-1-i][off] = \
            #mat[n-1-i][off], mat[off][i], mat[i][n-1-off], mat[n-1-off][n-1-i]
        #else :      # i in [1 n-1-off]:
            #mat[off][i], mat[i][n-1-off], mat[n-1-off][n-1-i], mat[n-1-i][off] = \
            #mat[n-1-i][off], mat[off][i], mat[i][n-1-off], mat[n-1-off][n-1-i]
    off = off + 1
mat


# -----------------------------------
# LeetCode 54: Spiral Matrix
# - print a given matrix in spiral form
mat = [
      [1, 2, 3, 4],
      [5, 6, 7, 8],
      [9,10,11,12]
     ]              # out = [1,2,3,4,8,12,11,10,9,5,6,7]
m = len(mat)
n = len(mat[0])

# Sol: O(m*n) / O(1)
m1, n1 = 0, 0           # starting row/col
m2, n2 = m, n           # ending row/col
while m1 < m2 and n1 < n2:
    for i in range(n1, n2):        # first row from the remaining m1
        print(mat[m1][i], end = " ")
    m1 += 1

    for i in range(m1, m2):        # last col ...
        print(mat[i][n2 - 1], end = " ")
    n2 -= 1

    if m1 < m2:
        for i in range(n2 - 1, (n1 - 1), -1):      # last row ...
            print(mat[m2 - 1][i], end = " ")
        m2 -= 1

    if n1 < n2:
        for i in range(m2 - 1, m1 - 1, -1):        # first col
            print(mat[i][n1], end = " ")
        n1 += 1


# -----------------------------------
# LeetCode 324: Wiggle Sort II
# - Given an unsorted array sort as nums[0] <= nums[1] >= nums[2] <= ...
nums = [3, 5, 2, 1, 6, 4]   # --> ex:  [1, 6, 2, 5, 3, 4].
n = len(nums)   # fix if odd

# Sol:
for i in range(2, n, 2) :
    print(i)
    if nums[i-1] < nums[i-2]:
        print("first swap i =", i)
        temp = nums[i-1]
        nums[i-1] = nums[i-2]
        nums[i-2] = temp

    if nums[i] > nums[i-1]:
        print("second swap i =", i)
        temp = nums[i]
        nums[i] = nums[i-1]
        nums[i-1] = temp
    # else :  # do nothing

for i in range(0, n) :      # test
    print(nums[i], end=" ")
print("\n")



# -----------------------------------
# LeetCode 73: Set Matrix Zeroes
# - if an element is 0, its entire row/col set to 0
mat = [[0, 0,  3],
       [0, 0,  4],
       [7, 8,  9],
       [7, 11, 7]]
m = len(mat)    # rows
n = len(mat[0]) # columns

# Sol: keep a row/col enable (to nullify), clear one of them in outer loop only
r, c = 0, 0
row_en, col_en = [], []
for i in range(m):
    row_en = row_en + [1]
for i in range(m):
    col_en = col_en + [1]

for c in range(n):
    for r in range(m):
        if mat[r][c] == 0:
            if row_en[r]:
                for i in range(n):     # repeat for the column
                    mat[r][i] = 0
                row_en[r] = 0   # row r is cleared
                col_en[c] = 0   # col c should be cleared too (in outer loop)
        print(c,r)
        print(mat)
        print(row_en, col_en, "\n ")
    if col_en[c]==0:            # if col c is marked to be cleared
        for i in range(m):      # nullify that row
            mat[i][c] = 0       # then, disable that row/col
mat


# -----------------------------------
# LeetCode 567: Permutation in String: Check if one string is a permutation of the other.
# Q: Consider repeating chars? --> yes
     # Consider white spaces --> yes
     # Consider case --> yes
     # Q: Duplicates? --> Yes --> sets won't work like (set1 == set2) and (len(str1)==len(str2))
     # Ascii? --> yes --> Nchar = 256
str1 = 'Abc cbbc'
str2 = 'c Abccbb'       # --> True
Nchar = 256

# Sol1: Use a ascii_chars counter, O(n)
str1_chars = Nchar*[0]
str2_chars = Nchar*[0]        # can't use = str1_chars
if len(str1) != len(str2):
    ans = False
else:
    for i in range(len(str1)):
        str1_chars[ord(str1[i])] += 1
        str2_chars[ord(str2[i])] += 1
    if str1_chars == str2_chars :
        ans = True
    else:
        ans = False
ans

# Mod1: Check if str2 contains permutation of s1 (LeetCode)
# Sol2: Scan for str2_chars > str1_chars
str1 = 'Abc cbbcd'
str2 = 'c Abccbbdg'     # --> True
str1_chars = Nchar*[0]
str2_chars = Nchar*[0]
if len(str1) > len(str2):                       # str2 can't be shorter
        ans = False
else:
    for i in range(len(str1)):                  # fill in the char arrays
        str1_chars[ord(str1[i])] += 1
    for i in range(len(str2)):
        str2_chars[ord(str2[i])] += 1

    ans = True
    for i in range(Nchar):
        if str1_chars[i] > str2_chars[i]:       # if str1 has more of any char
            str1_chars[i]
            str2_chars[i]
            ans = False
            break
ans


# -----------------------------------
# LeetCode 287: Find the Duplicate Number --> FIX
# Q: only one duplicate --> yes
arr = [7, 8, 3, 4, 7, 8, 5]
n = len(arr)

# Sol1: sort and find dup, O(nlogn)/O(1)

# Sol2: impement hash with dict
def hinsert(htable, key):
  htable[key] = htable[key] + 1
  #htable.append(key)

myset = set()
for i in range(n):
    myset.add(arr[i])
print(myset)
#htable = len(myset)*[None]   # init hash table
htable = len(myset)*[0]   # init hash table

for i in range(n):
    if htable[ arr[i] ] == 0 :  # 0 count yet
        # htable(arr[i]) = 'Y'
        hinsert(htable, arr[i])
        # hash_table.append((key, arr[i])) # key, value
    else:   # exists already
        ans = arr[i]
        break
print("htable = " + str(htable))
print("i = " + str(i) + ", ans = " + str(arr[i]))

keys = ['A', 'B']
values = [1, 2]
ahmet = dict(keys, values)
for i in range(n):
    if ahmet[ arr[i] ] in dict():
        pass


# -----------------------------------
# Leetcode 15: 3Sum
# - Count triplets with sum equal to 0 in  O(n^2)
# Q: Repeating? --> yes   Can return duplicate triplets? --> no
arr = [-1, 0, 1, 2, -1, -4]     # out =   [-1, 0, 1], [-1, -1, 2]
n = len(arr)

# Sol1: Run 3 loops brute force --> O(n^3)
# Sol2: Sort + use 3 indexes --> O(n^3)
arr.sort()          # O(nlogn)
trips = []       # list of lists
for i1 in range(n-2) :  # O(n2) since while loop also scans --> dominates sort
    i2 = i1 + 1         # start scanning right after
    i3 = n - 1          #
    while i2 < i3:   #
        summ = arr[i1] + arr[i2] + arr[i3]
        if summ == 0: # if a sol found
            print('found:', i1, i2, i3)
            if len(trips) == 0 or trips[-1] != [arr[i1], arr[i2], arr[i3]]:       # if 1st finding
                trips.append([arr[i1], arr[i2], arr[i3]])
            i2 = i2 + 1     # move both pointers regardless of unique or not
            i3 = i3 - 1     # since moving one can only find a repeating sol
        elif summ > 0:
            i3 = i3 - 1
        else: # (summ < 0)
            i2 = i2 + 1
trips


# -----------------------------------
# Leetcode 16: 3Sum Closest
# Q: Multiple solutions possible? --> no
arr = [-1, 2, 1, -4]

# Sol:
def sum3closest(arr, x):
    n = len(arr)
    arr.sort()          # = [-4 -1 1 2]
    import sys
    closest = sys.maxsize
    trips = []
    for i1 in range(n-2) :
        i2 = i1 + 1         # start scanning right after
        i3 = n - 1
        while i2 < i3:
            summ = arr[i1] + arr[i2] + arr[i3]
            if summ == x:  # if a perfect sol found
                print('perfect sol:', summ, i1, i2, i3)
                trips = [arr[i1], arr[i2], arr[i3]]
                return trips
                #break
            elif abs(x - summ) < abs(x - closest):  # if a better sol found
                print('better sol:', summ, i1, i2, i3)
                closest = summ
                trips = [arr[i1], arr[i2], arr[i3]]
                if summ < x :
                    i2 = i2 + 1     # move both pointers regardless of unique or not
                else :
                    i3 = i3 - 1     # since moving one can only find a repeating sol
    return trips

sum3closest(arr, 1)         # out = -1 + 2 + 1 = 2
sum3closest(arr, -4)        # out = -4 -1 + 1 = -4


# -----------------------------------
# Leetcode 259: 3Sum Smaller
x = 1   # ans = [[-4, -1, 2], [-4, -1, 1], [-1, -1, 2], [-1, 0, 1]]

# Sol: just change summ < x


# -----------------------------------
# LeetMedium 33: Search an element in a sorted and rotated array in O(logn)
# Q: duplicates? --> no, doesn't work with duplicates

arr = [4, 5, 6, 7, 1, 2, 3]
n = len(arr)
x = 2       # out = 5th index

# Sol: Recurion --> O(logn)
def search(arr, l, r, x):
    if l > r:               # stops recursion
        print("key not found")
        return -1
    mid = (l + r) // 2      # Find middle (pivot of rotation)
    if arr[mid] == x:     # if we got lucky, return it, o.w. shift the pivot
        return mid

    if arr[l] <= arr[mid]:  # means it's monotonic (sorted) till the mid
        if arr[l] <= x <= arr[mid]:  # check if key is in left half
            return search(arr, l, mid-1, x)
        return search(arr, mid+1, r, x)  # else shift the pivot right
    # else : no need becuase of the returns
        # it has to be monotonic after the mid
    if arr[mid] <= x <= arr[r]:
        return search(arr, mid+1, r, x)
    return search(arr, l, mid-1, x)
print( search(arr, 0, n, 2) )


# -----------------------------------
# LeetCode 253: Meeting Rooms II, find min # of conf room
# Q: can assume a day time such as 100? --> no
    # can assume Tend > Tstart --> yes

arr = [[0,30],[5,10],[15,20]]  # --> 2
n = len(arr)

# Sol: Sort --> O(nlogn)/O(n)
def can_attend(arr):
    if (arr == None) or (n == 0):
        return 0
    Tstart, Tend = [],[]
    for i in range(n):
        Tstart = Tstart + [arr[i][0]] # same as append
        Tend = Tend + [arr[i][1]]
    Tstart.sort()
    Tend.sort()
    print(Tstart, Tend)
    rooms = 0
    for i in range(n-1):
        print(i, Tstart[i], Tend[i] )
        if Tstart[i+1] < Tend[i]:
            return False
    return rooms
can_attend(arr)


# -----------------------------------
# LeetCode 365: Water and Jug Problem  --> FIX
# - Determine whether you can measure d liters of water
# - Can empty/fill any of the jugs completely with water.
# - Can pour water from one jug into another till the other jug is completely full or the first
# jug itself is empty.
jug1, jug2, target = 3, 5, 4   # out = True

# Sol: equation ax + by = d which is solvable if and only if gcd(a, b) divides d
def gcd(a, b):
    if b==0:
       return a
    return gcd(b, a % b)
gcd(3,5)

jug1w = jug1    # max fill
jug2w = 0       # empty at start
steps = 1
while (jug1w != target) and (jug2w != target) :  # continue if no found
    print(jug1w, jug2w, gcd(jug1, jug2w))
    # jug1 is full of
    water = min(jug1w, jug2 - jug2w)    # max that can be transferred from jug1 to jug2
    print(steps, jug1w, jug2w)
    if (jug1w == target) or (jug2w == target):     # if one of the jugs have the solution
        break
    if jug1w == 0:      # if 1st jug becomes empty, fill it
        jug1w = jug1
        steps += 1
    if jug2w == jug2:   # if 2nd jug becomes full, empty it
        jug2w = 0
        steps += 1


# -----------------------------------
# LeetCode 64: Minimum Path Sum
# - Find a path from top left to bottom right which minimizes the sum filled with non-negative
# - numbers. Can only move down or right
mat = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]   # -->  1 3 1 1 1 = 7

# Sol:
def find_min(mat, x,y):
#   if
   return mat[x][y] + min(find_min(mat, x+1, y), find_min(mat, x, y+1))


find_min(mat, 0, 0)


# -----------------------------------
# Leetcode 78: Subsets: Return the power set  --> IMRPOVE
arr = [1, 2 , 3]   # out = [], [1], [2], [2, 3], [1 [2, 3]]
n = len(arr)

# Sol1: O(n^2) --> Or O(n^2 / 2)?
sublist = [[]]      # start with empty list
for i in range(n+1):
    for j in range(i+1, n+1):
        sub = arr[i:j]
        sublist.append(sub)
sublist

# Sol2: ?, O(n) needed?


# -----------------------------------
# LeetCode 442: Find All Duplicates in an Array --> FIX
# - some elements appear twice and others appear once.
arr = [4,3,2,7,8,2,3,1]     # out = [2,3]
n = len(arr)

# Sol:


# -----------------------------------
# Leetcode 1143: Longest Common Subsequence (LCS)
arr1 = ['a', 'b', 'c', 'd', 'e', 'f']   # columns (n)
arr2 = ['a', 'c', 'b', 'c', 'f']        # rows (m) --> a, b, c, f --> 4
n, m = len(arr1), len(arr2)

# Sol1: Get all subsequences (2^n) and check the commonality (n) --> O(n*2^n)
# Sol2: Dynamic, O(n^2), convert into matrix
zeros = [0]*(n+1)       # copy the column vector zeros
mat = []
for r in range(m+1):    # for each row
    mat.append(zeros)
    #for c in range(n+1):
        #mat[r][c] = 0
# mat
# res = 0
for r in range(1, m+1):             # scan each row starting from the 2nd element
    if arr2[r-1] == arr1[0]:          # calc the start of that row
        mat[r][1] = mat[r-1][1] + 1 # inc cnt if common element found
    else:
        mat[r][1] = mat[r-1][1]     # o.w. copy over the cnt
    for c in range(1, n+1):            # now scan each col
        if arr2[r-1] == arr1[c-1]:      # if common element found
            if r == 1:
                mat[r][c] = 1 + max(mat[r-1][c], mat[r][c-1])  # cnt is 1 + max(previous)
            else:
                mat[r][c] = max(mat[r-1][c], mat[r][c-1])   # cnt is max(previous)
        else:
            mat[r][c] = mat[r][c-1] # copy over from previous column
        print(r,c, mat[r][c])

#mat[r+1][c+1]   # last matrix element has traveled through each array


#----------------------
# LeetCode 309: Best Time to Buy and Sell Stock with Cooldown
 # After you sell, you cannot buy stock on next day. (ie, cooldown 1 day)
# Q:
# Given:
arr = [4, 7, 2, 6, 1, 2, 6, 2, 8, 4]        # profit =
n = len(arr)
cooldown = 1

#Sol:
    # Cooldown should not miss the super low buy: Check
buy = arr[0]
profit = 0
for i in range(1, len(arr)):
    while arr[i] > arr[i-1]:  # as long as gaining, hold on

        sell = arr[i-1]    # sell at the local peak
        profit += sell - buy  # add to the profit
        buy = arr[i]      # buy again
    print(i, profit)


# -----------------------------------
# Leetcode 1618: Maximum Font to Fit a Sentence in a Screen
# - Find the best font size given min/max, W,H, text string
# Q: Word breaks? --> perform word warping using spaces
minFont = 10
maxFont = 29
fontWx = 1  # for simplicity,  should be +1 to account for spacing
fontHx = 1  # for simplicity, , should be +2 to account for capitals and spacing
W = 400
H = 40
text = "He was coming to the office while I was leaving quietly, but then someone came in."

# Sol: If we don't care word warping, solution is simple: max_n = w/(font*fontWx) * h/(font*fontHx)
# Speed: O(nlogn)*O(k) / O(1), n is the font range, k is the # of rows needed in the textbox
def textFits(text, font, fontWx, fontHx, W, H):   # helper func to check if a text can fit
    i = 0  # col index, acts like a text cursor
    j = 0  # row index
    i_max = W // (font * fontWx)  # chars_per_row, note the quotient division
    j_max = H // (font * fontHx)  # chars_per_col

    fits = False
    while text and (fits == False) and (j <= j_max):  #
        if len(text) <= i_max:  # can fit all in one line
            fits = True
        else:  # need to line break at a space character
            i = i_max
            if text[i] == ' ':  # if the line ended at a space char luckily
                j = j + 1  # line break and keep the k there
                #print(text[0:i + 1])  # show the written text so far
                text = text[i + 1:]
                # print(text)
                i = 0
            else:  # o.w., search backwards for space char
                while (i >= 0) and (text[i] != ' '):
                    i = i - 1
                    # print(text[i])
                j = j + 1
                #print(text[0:i + 1])  # and line break right after the space
                text = text[i + 1:]  # remaining text
                i = 0
        #print(j, fits)
    return fits

def bestFont(text, minFont, maxFont):       # bsearch to find the optimal font
    L = minFont
    R = maxFont
    while L < R-1:                          # has to end with r = l + 1, not r > l (font is an int)
        font = math.floor((R + L) / 2)      # try the mid-level font size
        if textFits(text, font, 1, 1, W, H):    # if it fits
            L = font                            # ignore all fonts that are smaller
        else:
            R = font
        #print(l, r)
    return font

bestFont(text, minFont, maxFont)



# -----------------------------------
# LeetCode 63: Strobogrammatic Number II, Find all strobo nums that are length n
# - Ex: n = 2, return ["11","69","88","96"]
# Q: is 00 included? --> No
n = 3

# Sol: O(?)/O(?)
nums = []
d = dict({'0': '0', '1':'1', '8':'8', '6':'9', '9':'6'})
nd = len(d)

if n == 1:
    for i in range(nd):
        nums.append(d.keys[i])
    print(nums)

elif n // 2 == 1:
    eo = 'odd'
else:
    eo = 'even'

print(d.keys(), d.values())

for i in range(n):
    if num[i] not in d:
        ans = False
    else:
        if num[-1-i] != d[num[i]]:
            ans = False
print(ans)



# -----------------------------------
# LeetCode 249: Group Shifted Strings
# - group s.t. all strings in a group are shifted versions of each other: S[i] = T[i] + K for
# - all lowercase given, 1 <= i <= S.length, K is constant integer
strings = {"acd", "dfg", "wyz", "yab", "mop", "bdfh", "a", "x", "moqs"}
# - ans = a x, acd dfg wyz yab mop bdfh moqs, bdfh moqs

# Sol: O(?)/O(?)
nset = len(strings)  # set length
d = dict()
for string in strings:
    n = len(string)
    if n not in d.keys():
        d[n] = string

d
strings.keys()


# -----------------------------------
# LeetCode 198:	House Robber
# - Max profit of robbery, houses will call the police if two adjacent houses were broken into
# Q: Constraints, 1 <= nums.length <= 100, 0 <= nums[i] <= 400
# Q: Cyclic? meaning first/last houses are not neighbors? --> No
stashes = [2, 10, 9, 3, 1, 10]      # -->
max_robbed = 0

# Sol1: O(n)
n = len(stashes)
if n < 1:
    robbed = 0
elif n == 1:
    max_robbed = stashes[0]
elif n == 2:
    max_robbed = sum(stashes)
else:
    rob_even = sum(stashes[0: :2])
    rob_odd = sum(stashes[1: :2])
    max_robbed = max(rob_even, rob_odd)
print(max_robbed)


# -----------------------------------
# LeetCode 93: Restore IP Addresses
# - Given a string containing only digits, restore it by returning all possible valid IP combo
# - A valid IP is A.B.C.D, in range of 0-255
# Q: Can be 0 prefixed? --> No      Number length too short/long? --> no
given = "25011255255"
     # = 25525511135

# Sol1: generate all possible, then split with dot --> kinda linear
res = set()  # different sols ==> use set
for dots[0] in range(1, 4):
    for dots[1] in range(dots[0]+1, dots[0]+4):
        for dots[2] in range(dots[1]+1, len(given)-1):
            print(dots)
            if (dots[2]-dots[1] <= 3) & (len(given)-dots[2] <= 3):
                if (given[dots[0]] != '0') & (given[dots[1]] != '0') & (given[dots[2]] != '0'):
                    # if no 0 start
                    sol = given[0:dots[0]] + "." + given[dots[0]:dots[1]] + "." \
                          + given[dots[1]:dots[2]] + "." + given[dots[2]:]
                    #print(sol)
                    res.add(sol)
res

# Sol2: DFS + roll back, O(n*2^n) --> IMPROVE


# -----------------------------------
# LeetCode 62: Unique Paths
# - Count all possible paths from top left to bottom right of a mXn matrix.
# - Can either move right or down
# Q: print paths too? --> Yes
     # can it temporarily go out of matrix area? --> No
# m, n = 3, 2  # o/p = 28
m, n = 3, 5  # o/p = 3
# 1. Right -> Right -> Down
# 2. Right -> Down -> Right
# 3. Down -> Right -> Right

# Sol1: Recursion
def find_paths1(i, j, paths):
    print(i, j, paths)
    #if (i < 1) or (j < 1):
    #   return None
    if (i == 0) and (j == 0):
        paths.add((i, j))    # path reached
        return paths

    if ((i-1, j) not in paths)  and (i-j) <= 1:
    #return numberOfPaths(m-1, n) + numberOfPaths(m, n-1)
        paths = paths | find_paths1(i-1, j, paths) # try coming from left
    elif ((i, j-1) not in paths) and (i-j) >= 1:
        paths = paths | find_paths1(i, j-1, paths) # // coming from top

    return paths
find_paths1(m, n, paths)


def find_paths2(i, j):
    #paths.append(str(i)+","+str(j))
    if (i == 1) or (j == 1):  # if reached to first row or col, solution is trivial
        return 1
    paths = find_paths2(i-1, j) + find_paths2(i,j-1)
    return paths
find_paths2(m, n)

# Sol 2: DP, avoid recomputation using a temp count array in a bottom up manner, O(mn)/O(mn)
def find_paths3(m, n):
    count = [[0 for x in range(m)] for y in range(n)]
    for i in range(m):   # Count of paths to reach any cell in first column is 1
        count[i][0] = 1
    for j in range(n):
        count[0][j] = 1

    for i in range(1, m):   # recur bottom up
        for j in range(n):
            count[i][j] = count[i-1][j] + count[i][j-1]
            print(i, j, count)
    return count[m-1][n-1]
find_paths3(m, n)

# Mod (Google): Start from bottom left, can move either to right, top-right, bottom-right
# Given a:  same --> out = ..
         # (1,0), (1,1), (1,2)
         # ....., (0,1), .....
         # try with m,n = 3,4 to see bottom right cases too


# Sol: should be O(mn)/O(m)
 # target is to reach (m-1, n-1), at at m-1 already
 # BFS: find 1st steps first, then 2nd steps
routes = []
loc = [m-1, 0]

# for i = 0: m-1
#    for j = 0: n-1
#        if


# -----------------------------------
# LeetCode 63: Unique Paths II: Same things except obstacles in m*m grid
# - Obstacles marked as 1/0

# Sol:

# Mod (Google): Same as Google mod of LeetCode 62 except trenches given as a list
m, n = 4, 3
trench =[(3,1), (1,2)]

# Sol:

# Mod (Google): A horizontal line splits North and South, find # of ways it steps in the North
north = 1   # north is just the top row --> then try with north = 3 rows

# Sol: should be O(m*n)/O(m)





