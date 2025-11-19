"""Content: Medium level practice questions."""

import math

for name in dir():
    if not name.startswith("_"):
        del globals()[name]
for var in dir():
    if not var.startswith("_"):
        del globals()[var]

# =================================================================================================
# Q: Reverse sort (in place) tuples by its 2nd float element (Lambda)
t = [("1", "9.4"), ("2", "16.9"), ("3", "5.5"), ("4", "4.2"), ("5", "7.3")]

# Sol: Use advanced sort w/ key + reverse
t.sort(key=lambda x: float(x[1]), reverse=True)
print(t)


# -------------------------------------------------------------------------------------------------
# Q: Write function to sum the odd numbers from 1 to 100.

# Sol: Sum of numbers between [n1 n2] = ((n2-n1)*(n2+n1)+1)/2
n1, n2 = 1, 99
n = (n2 - n1) / 2 + 1  # number count
odd_sum = (n * (n + 1) / 2) * 2  # multiply back with 2 since goes in 2s

odd_sum2 = 0
for i in range(101):
    if (i % 2) == 1:
        odd_sum2 = odd_sum2 + i

print(str(odd_sum) + ", " + str(odd_sum2))


# -------------------------------------------------------------------------------------------------
# Q: Find GCD of 2 numbers (Recursion)
num1, num2 = 60, 24  # o/p = 12


# Sol1: Recursion
def gcd(a, b):  #
    if a == 0:
        return b  # 0 divides everything, so b becomes GCD
    elif b == 0:
        return a
    elif a == b:
        return a  # or b
    else:  # here we go
        if a > b:
            # print("a greater -->", a%b, b)
            return gcd(a % b, b)
        else:  # b > a :
            # print("b greater -->", a, b%a)
            return gcd(a, b % a)


gcd(num1, num2)  # test


# -------------------------------------------------------------------------------------------------
# Q: Find LCM of 2 numbers  # --> FIX
num1, num2 = 6, 8


# Sol1: LCM(a,b) = (a*b)/GCD(a,b)
def lcm(a, b):
    return (a * b) / gcd(a, b)


lcm(num1, num2)


# Sol2: Recursion without using GCD
def lcm2(a, b):
    if (a == 0) or (b == 0):
        return 1
    elif a == b:
        return a  # or b
    elif a > b:
        return lcm2(a + a % b, b)
    else:  # b > a :
        return lcm2(a, b + b % a)


lcm2(num1, num2)


# -------------------------------------------------------------------------------------------------
# Q: Find a max and min in an array simultaneously w/ min comparisons
arr = [3, 2, 1, 6, 5, 4, 8, 7]  # out = 1, 8

# Sol 1: Linear, O(n), T(n) = 2(n-1) at worst case (ascending)
# ex: 1 2 3 --> 2<1? --> no --> 2>1 --> yes --> 3<1? --> no --> 3>2? --> yes -->? 4 comp = 1 + 2
# from numpy import inf
# minn = +float(inf)
n = len(arr)
minn = arr[0]
maxx = arr[0]
for i in range(1, n):
    if arr[i] < minn:
        minn = arr[i]
    elif arr[i] > maxx:
        maxx = arr[i]
print(minn, maxx)

# Sol 2: Divide and Conquer, O(n) but  T(n) = T(floor(n/2)) + T(ceil(n/2)) + 2
minn = arr[0]
maxx = arr[0]
print("n", "min", "max")


def minmax(arr, n):
    if n == 1:
        minn = arr[0]
        maxx = arr[0]
        print(n, minn, maxx)
        return [minn, maxx]  # carry a list
    elif n == 2:  # simple comparison
        if arr[1] >= arr[0]:
            minn = arr[0]
            maxx = arr[1]
        else:
            minn = arr[1]
            maxx = arr[0]
        print(n, minn, maxx)
        return [minn, maxx]
    else:  # n > 2
        arr_left = arr[0 : math.ceil(n / 2)]  # [1 2 3 4 5] --> [0 3) + [3, 5)
        arr_right = arr[math.floor(n / 2) :]
        minmax_left = minmax(arr_left, len(arr_left))
        minmax_right = minmax(arr_right, len(arr_right))

        if minmax_left[0] < minmax_right[0]:  # compare mins of L/R first
            minn = minmax_left[0]
        else:  # equals don't matter
            minn = minmax_right[0]
        if minmax_left[1] > minmax_right[1]:  # same thing for maximums of L/R
            maxx = minmax_left[1]
        else:
            maxx = minmax_right[1]
        print(n, minn, maxx)  # 3, 2, 1, 6   /  5, 4, 8, 7  --> 1, 6 vs 4, 8 --> 1, 8
        return [minn, maxx]


minmax(arr, n)


# -------------------------------------------------------------------------------------------------
# Q: Given 3 numbers, tell the # of ways you can form N sum with them,
# number reuse? --> yes      different combinations --> yes
arr = [1, 3, 5]
n = len(arr)  # irrelevant
x = 7  # 1 + 3 + 8 = 12

# Sol1: Dynamic
# sum3(2): (1+1) + 5 --> 1x
# sum3(4): (1+3) + 3, (3+1) + 3, (1+1+1+1) + 3 --> 3x
# sum3(6): (1+1+1+1+1+1) + 1, (1+1+1+3) + 1, .., (3+3) + 1, (1+5) + 1.. --> 8x
# Thus: sum3(n) = sum3(n-1) + sum3(n-3) + sum3(n-5)
size = int(max(0, x + 1))
table = size * [None]


def sum3d(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return sum3d(n - 1) + sum3d(n - 3) + sum3d(n - 5)


sum3d(x)


# Sol1: Dynamic + memo
def sum3dm(n):
    if n < 0:  # let's say no negative #
        return 0
    if n == 0:  # subset with no elements sum to 0
        return 1
    print(n, table)
    if table[n] != None:
        return table[n]
    return sum3dm(n - 1) + sum3dm(n - 3) + sum3dm(n - 5)


sum3dm(x)


# -------------------------------------------------------------------------------------------------
# Q: Towers of Hanoi, move all disks to another rod
# - 3 rods, n disks


# Sol: Recur O(n^2) --> 2 calls = n^2
def hanoi(n, a, b, c):  # (from, to, aux)
    if n == 1:
        print("Move disk", n, "from", a, "to", c)
        return  # means function end
    hanoi(n - 1, a, b, c)  # move n-1 disks from a to b
    print("Move disk", n, "from", a, "to", c)
    hanoi(n - 1, b, c, a)  # recur when a and c reversed

hanoi(3, "a", "b", "c")


# -------------------------------------------------------------------------------------------------
# Q: Multiply two integers recursively
# - no loops, multiplication, division and bitwise operators
# Given:
a, b = 6, 5

# Sol: Recur, prod = prod + multiply(x-1, y)
def rec_multiply(x, y, product):
    if x == 0:  # base condition reached
        return product
    elif x > 0:
        product += y + rec_multiply(x - 1, y, product)
    else:
        x = x + 1
        product += y + rec_multiply(x - 1, y, product)
    print(x, product)
    return product

rec_multiply(a, b, 0)


# -------------------------------------------------------------------------------------------------
# Q: Remove Alternate Duplicate characters from a char array
# - Small letter? --> no, any characters
arr = ["a", "b", "c", " ", "c", "d", "c", "d", "e"]  # --> abc dce
n = len(arr)

# Sol: Hashtable of counts, O(n) / O(128)
h = 128 * [0]
i = 0
while i < n:
    h[ord(arr[i])] += 1  # update encounter
    if h[ord(arr[i])] == 2:  # when duplicate found
        print("i = ", i, "removed", arr[i])  # echo it
        h[ord(arr[i])] = 0  # reset counter --> can use modulus?
        del arr[i]  # delete it
        n = n - 1  # inplace = dynamic size --> dec n
    else:
        i = i + 1
arr


# -------------------------------------------------------------------------------------------------
# Q: Break sentence into words using a given dict of valid words
# Given:
s = "shoppingwithflipkartiseasy"  # --> out = shopping with flipkart is easy

# Sol: My idea
n = len(s)
d = {"shopping": 1, "with": 1, "flipkart": 1, "is": 1, "easy": 1}
out = []
i, j = 0, 1
while i < j:
    for j in range(i, n):
        if s[i:j] in d.keys():
            out.append(s[i:j])
            # out = out + ''.join(s[i:j]) + " " # either firstt or last element is space =(
            i = j
            j = j + 1
            continue
    i = i + 1

out = " ".join(out)
print(out)


# -------------------------------------------------------------------------------------------------
# Q: Longest Repeated Subsequence (LRS)
# - LRS(str) = LCS(str,str) where str pointers are different
str = "AABEEEBCDD"  # --> ABD

# Sol: Dynamic


# -------------------------------------------------------------------------------------------------
# Q: Longest Increasing Subsequence (LIS) - Find the length
arr = [10, 22, 9, 33, 21, 50, 41, 60]  # m = 5( 10,22,33,50,60)

# Sol: Recur, m(i) = 1 + max(m(j)) for j<i, and arr[j]<arr[i]
n = len(arr)


# -------------------------------------------------------------------------------------------------
# Q: Deck of Cards, how to subclass the DS to implement blackjack? (OOP)
# Sol:
class Deck:
    def card(value, suit):
        # c_value = value
        # c_suit = suit


# -------------------------------------------------------------------------------------------------
# StackQueue: Sort Stack s.t. smallest items are on the top
# Q: Can use additional stack? --> yes but not array
# Given: s = [2, 1, 4, 3] --> [4, 3, 2, 1]

# Sol: O(n^2)/O(n)
def s_sort(s):
    # n = s.size()
    r = Stack()  # result stack
    while not s.isEmpty():
        tmp = s.pop()
        while (not r.isEmpty()) and (r.peek() > tmp):  # if can't reach smaller elements yet
            s.push(r.pop())  # keep pouring over the s
        r.push(tmp)  # when done, insert the next min to r
        # max element in s and will be inserted in r too in the end
    while not r.isEmpty():  # now r is sorted but in descending order
        s.push(r.pop())  # so pour r back to s


s_sort(s)
s.print()  # done

# Sol:
from queue import Queue

qq1 = Queue()
qq2 = Queue()


def sq_push(q1, q2, x):
    q2.put(x)
    while not q1.empty():
        q2.put(q1.queue[0])
        q1.get()  # no return for push
    qtemp = q1  #
    q1 = q2
    q2 = qtemp


def sq_pop(q):
    return q.get()


def sq_print(q1, q2):
    arr1, arr2 = [], []
    for i in range(q1.qsize()):
        arr1.append(q1.get())
        arr2.append(q2.get())
    return arr1, arr2


sq_push(qq1, qq2, "a")
sq_push(qq1, qq2, "b")
sq_push(qq1, qq2, "c")

sq_print(qq1, qq2)

sq_pop(q1)


# -----------------------------------
# StackQueue: Animal Shelter
# FIFO basis, people select cat/dog but have to adopt the oldest
# Sol:
class Animal:
    def __init__(self):
        self.dogs = []
        self.cats = []

    # def isEmpty(self):
    #    return self.arr == []


#     def enqueue():

#     def dequeueAny():

#     def dequeueDog():

#     def dequeueCat():


# -----------------------------------
# StackQueue: Stack of Plates:
# Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
# Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
# threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be
# composed of several stacks and should create a new stack once the previous one exceeds capacity.
# SetOfStacks. push() and SetOfStacks. pop() should behave identically to a single stack
# (that is, pop () should return the same values as it would if there were just a single stack).
# FOLLOW UP
# Implement a function popAt(int index) which performs a pop operation on a specific substack.
# Q:
# Sol:

# -----------------------------------
# StackQueue: Three in One, implement three stacks in a single array.
# Given:    Hints: #2, #72, #38, #58
n = 10

# Sol1: Assign n/3 size to each stack
arr1 = n // 3 * []

# Sol2: Grow paritition size when one stack exceeds capacity
# also design the array circularly --> solution too long, do later


# -----------------------------------
# StackQueue: Reverse a stack without using extra space in O(n)
# Sol:
def s_reverse(s):
    ll = LinkedList()  # start an empty LL object
    node1 = Node(1)
    LL.head = node1
    node2 = Node(2)
    node1.next = node2
