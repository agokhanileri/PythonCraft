"""Content: Bubble, Quick, Merge, Insertio, Selection, Heap, Counting, Radix, Bucket."""


# =================================================================================================
# BubbleSort: O(n^2)/O(1), best for fixing few items in a big array, worst for reverse sorted
def bubble_sort(arr):
    for i in range(len(arr)):
        swapped = False  # for optimization
        for j in range(0, len(arr) - i - 1):  # i is used only here to define the range
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if swapped == False:  # if carrying a j didn't cause any swaps along the way,
            break  # the rest of the array is sorted already, break
    # for j in range(n) :
    # print (arr[j], end=' ')            #
    # print ("%d" %arr[j], end=' ')      # alternatively


# -------------------------------------------------------------------------------------------------
# QuickSort: O(n^2)/O(n+k), D&C algo, good for Arrays since need random access as x + i*4
def part(arr, left, right):
    i = left - 1  # index to place the vals found, start at -1
    # j = left                                  # index to compare to pivot
    for j in range(left, right):  # pivot is the R
        # print(left, right, i, j, arr)
        if arr[j] < arr[right]:  # if smaller value found     # removed <=
            i = i + 1  # prepare it's index (i)
            arr[j], arr[i] = arr[i], arr[j]  # switch it with (j)
            # arr[j] = arr[i]                # places smaller elements to left of pivot and vv.
            # arr[i] = temp                  #
    temp = arr[right]  # since 0-i contains smaller than pivot,
    arr[right] = arr[i + 1]  # place pivot at i+1
    arr[i + 1] = temp
    # print(left, right, i, j, arr)  # double check the pivot placement
    return i + 1  # pivot is placed at i, it's sorted!


def quick_sort(arr, left, right):  # recursion to divide, real issue is to merge
    if left < right:
        pivot = part(arr, left, right)
        quick_sort(arr, left, pivot - 1)  # sort left
        quick_sort(arr, pivot + 1, right)  # sort right


# -------------------------------------------------------------------------------------------------
# 3) MergeSort: O(nlogn)/O(?), D&C algo, good for LLs since mid-insert O(1)
def merge_sort(arr):  # recursion to divide, real issue is to merge
    if len(arr) > 1:  # no need of n since calculates length recursively
        mid = len(arr) // 2  # quotient --> last ones: 3/2 = 1 --> [n0], [n1 n2]
        lefthalf = arr[:mid]  # exclusive (n0)
        righthalf = arr[mid:]  # inclusive (n1, n2)
        merge_sort(lefthalf)  # recursion
        merge_sort(righthalf)  # sort till the bottom branch complete
        i, j, k = 0, 0, 0  # indexes of arrL/arrR/arr_merged
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:  # if n0 < n1
                arr[k] = lefthalf[i]  # place n0 to k = 0
                # print("Merging i=", i, arr)
                i = i + 1
            else:
                arr[k] = righthalf[j]  # o.w. pick n1 for k = 0
                # print("Merging j=", j, k, arr)
                j = j + 1
            k = k + 1  # always inc

        while i < len(lefthalf):  # if left lenght is smaller, won't exec
            arr[k] = lefthalf[i]  #
            # print("Bypassing i=", i, arr)
            i = i + 1
            k = k + 1  # left bypass completed
        while j < len(righthalf):  # j = 1, n2 remaining, bypasses
            arr[k] = righthalf[j]  # copied over n2, since n2>n1 in prev step
            # print("Bypassing j=", j, arr)
            j = j + 1
            k = k + 1  # right bypass completed


# -------------------------------------------------------------------------------------------------
# 4) InsertionSort: O(n^2)/O(1), maintains a sorted sublist in the low part, good for kinda sorted
def insert_sort(arr):
    for i in range(1, len(arr)):  #
        for j in range(0, i):  # scan a sublist
            if arr[i] < arr[j]:  # if found a smaller element
                temp = arr[i]  # save it
                arr[i] = arr[j]  # insert it
                arr[j] = temp  # finish the swap
                # break
            print(i, j, arr)
            # else : # arr[j] >= arr[j+1] :   # o.w. carry on to find a bigger right neighbor


def insert_sort2(arr):  # instead of swapping i/j, just insert i
    for i in range(1, len(arr)):  # this will cause a shift though
        for j in range(0, i):  # scan a sublist
            if arr[i] < arr[j]:  # if found a smaller element
                arr.insert(j, arr.pop(i))  # insert ith to jth location
                # break
            # print(i, j, arr)
            # else : # arr[j] >= arr[j+1] :   # o.w. carry on to find a bigger right neighbor
    return arr


# -------------------------------------------------------------------------------------------------
# 5) SelectionSort: O(n^2)/O(1), 1 exchange per pass, n−1  passes, good for reverse sorted
def select_sort(arr):  #
    for i in range(0, len(arr)):  #
        jmax = 0  # temp max index = assume 1st element is max
        for j in range(1, len(arr) - i):  # scan till the last sorted sublist
            # print(i, j, jmax, arr)
            if arr[j] > arr[jmax]:  # if found a smaller element
                jmax = j  # update max      # //        index

        temp = arr[len(arr) - i - 1]  # save the last element (before the subarray)
        arr[len(arr) - i - 1] = arr[jmax]  # place vmax on it
        arr[jmax] = temp  # swap the last element with the max element found


# -------------------------------------------------------------------------------------------------
# 6) HeapSort O(nlogn)/O(1), fixed speed regardless of i.c., can be iterative

# 7) Counting Sort: O(?)/O(n+k), no comparison, goof if input is bounded by [1 k], sort by digits,

# 8) RadixSort: O(logb(k)*(n+b))/O(?), no comparison, good if input is bounded by [1 k^2]
# - Better than QuickSort if log2n bits/digits (binary)
# - b = base (10 for decimals), k = sqrt(bound), n = input size

# 9) Bucket Sort: O(?)/O(?)


# =================================================================================================
# Test:
arr = [9, 9, 7, 8, 8, 5, 4, 0, 1, 2, 7, 7]
arr_org = arr
bubble_sort(arr)
print(arr)
quick_sort(arr, 0, len(arr) - 1)
print(arr)
merge_sort(arr)
print(arr)
insert_sort2(arr)
print(arr)
select_sort(arr)
print(arr)
# heap_sort(arr);   print(arr)
# count_sort(arr);  print(arr)
# radix_sort(arr);  print(arr)
# bucket_sort(arr);  print(arr)
