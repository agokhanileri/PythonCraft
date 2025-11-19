"""Content: LinearSearch, BinarySearch, JumpSearch, InterpolationSearch."""

import math


# =================================================================================================
# 1) LinearSearch (O(n), O(1))              # best if unsorted
def linear_search(arr, val):
    n = len(arr)
    cnt = 0
    for i in range(n):
        # print(i)
        if arr[i] == val:
            # break
            cnt = cnt + 1
            return i  # return the index of the finding
    return -1


# -------------------------------------------------------------------------------------------------
# 2) BinarySearch (O(logN), O(1))           # best if monotonic
def binary_search(arr, val):
    n = len(arr)
    i = int(round(n / 2, 0))
    cnt = 1
    while i < n:
        # print(i)
        if arr[i] == val:
            return i
        # break
        elif arr[i] > val:
            cnt = cnt + 1
            i = i - int(round((n / (2**cnt)), 0))

        else:  # arr[i] < val:
            cnt = cnt + 1
            # i = i - math.ceil(n/(2**(cnt)))\
            i = i + int(round((n / (2**cnt)), 0))
    return -1


# -------------------------------------------------------------------------------------------------
def binary_search2(arr, val):  # faster for large i/p, just +1 iter
    n = len(arr)
    l = 0
    r = n - 1  # left/right pointers of the region of interest
    cnt = 1  # iter counter
    # global i
    while l < r:  #
        i = math.floor((r + l) / 2)  # returns int anyway
        # print(cnt, i, l, r)
        if arr[i] < val:  # search right, or carry the left pointer to mid
            cnt = cnt + 1
            l = i + 1  # +1 because first index 0 convention
        else:  # arr[i] > val
            cnt = cnt + 1
            r = i
        return -1
    return l  # checks only when L = R, where the speed comes from


# -------------------------------------------------------------------------------------------------
# 3) JumpSearch (O(sqrtN), O(1)), AKA block search, slower but jumps back lesser (n/m jumps)
def jump_search(arr, val):
    n = len(arr)
    m = math.sqrt(n)  # jump step location set
    i = 0
    # r = n - 1
    cnt = 0
    while arr[i] < val:
        cnt = cnt + 1
        # print(cnt, i)
        i = i + round(m)  # move left pointer to next chunk
        if i >= n:  # if overflows, then target out of range
            return -1
        # else                               # i jumped over val, scan back previous chunk
    while arr[i] > val:  # scan backwards from current i
        cnt = cnt + 1
        # print(cnt, i)
        i = i - 1
    return i


# -------------------------------------------------------------------------------------------------
# 4) InterpolationSearch (O(loglogN)))      # shines if the elements are uniformly distributed
def interp_search(arr, val):
    n = len(arr)
    l = 0
    r = n - 1
    cnt = 0
    i = 0
    while (arr[i] < val) and (arr[l] < val < arr[r]):
        i = l + int((val - arr[l]) * (r - l) / (arr[r] - arr[l]))  # like my boost search
        cnt = cnt + 1
        # print(cnt, i)
        if arr[i] == val:  # if found, return
            return i
        elif arr[i] < val:
            l = l + 1
        else:  # arr[ i ] < val:
            r = r - 1
    return -1  # if the scan is complete and it's not found


# -------------------------------------------------------------------------------------------------
# 5) ExponentialSearch (?)
# 6) TernarySearch (?)
# 7) SublistSearch (?)
# 8) FibonacciSearch (?)
# ex) Ubiquitious BinarySearch (?)
# ex) Recursive LinearSearch (?)
# ex) Recursive Substring Search (?)
# ex) Unbounded BinarySearch (?)


# =================================================================================================
# -- Test
val = 8
arr = [1, 2, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10]  # sorted
# n = len(arr)
linear_search(arr, val)
binary_search(arr, val)
binary_search2(arr, val)  # failed for repeating numbers in arr
jump_search(arr, val)
interp_search(arr, val)
