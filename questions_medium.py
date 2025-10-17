import math


##-----------------------------------
# AlgoHard 02: Write function to sum the odd numbers from 1 to 100.
# Q: none
# Given: none

# Sol: Sum of numbers between [n1 n2] = ((n2-n1)*(n2+n1)+1)/2
n1, n2 = 1, 99
n = (n2 - n1)/2 + 1           # number count
odd_sum = (n*(n+1)/2)*2      # multiply back with 2 since goes in 2s

odd_sum2 = 0
for i in range(101):
    if (i % 2) == 1:
        odd_sum2 = odd_sum2 + i

print(str(odd_sum) + ", " + str(odd_sum2))


##-----------------------------------
# AlgoHard 04: Find GCD of 2 numbers
# Q:
# Given:
num1, num2 = 60, 24     # o/p = 12
# num1, num2 = 60, 7    # o/p = 1
# Sol1: Recur
def gcd(a, b):       # 
    if a == 0:      
        return b    # 0 divides everything, so b becomes GCD
    elif b == 0:
        return a
    elif a == b:    
        return a    # or b
    else:           # here we go
        if a > b :
            #print("a greater -->", a%b, b)
            return gcd(a % b, b)
        else : # b > a :
            #print("b greater -->", a, b%a)
            return gcd(a, b % a)
gcd(num1, num2)         # test     


##-----------------------------------
# AlgoHard 05: Find LCM of 2 numbers  # --> FIX
# Q:
# Given:
num1, num2 = 6, 8       # simpler ex

# Sol: LCM(a,b) = (a*b)/GCD(a,b) 
def lcm(a, b):
    return (a*b) / gcd(a, b)
lcm(num1, num2)         

# Mod: Can't use GCD     
# Sol: Recur again
def lcm2(a, b):            
    if (a == 0) or (b == 0):
        return 1
    elif a == b:
        return a    # or b
    elif a > b:    
        return lcm2(a + a%b, b)
    else : # b > a :
        return lcm2(a, b + b%a)
lcm2(num1, num2)




##-----------------------------------
# AlgoHard 08: Find a max and min in an array simultaneously w/ min comparisons
# Q: 
# Given:
arr = [3, 2, 1, 6, 5, 4, 8, 7]  # out = 1, 8
n = len(arr)

# Sol 1: Linear, O(n), T(n) = 2(n-1) at worst case (ascending)
 # ex: 1 2 3 --> 2<1? --> no --> 2>1 --> yes --> 3<1? --> no --> 3>2? --> yes -->? 4 comp = 1 + 2
 #from numpy import inf
 #minn = +float(inf)
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
print('n', 'min', 'max') 
def minmax(arr, n):
    if n == 1:
        minn = arr[0]
        maxx = arr[0]
        print(n, minn, maxx) 
        return [minn, maxx]     # carry a list 
    elif n == 2:                # simple comparison
        if arr[1] >= arr[0]:
            minn = arr[0]
            maxx = arr[1]
        else:
            minn = arr[1]
            maxx = arr[0]
        print(n, minn, maxx)   
        return [minn, maxx] 
    else:   # n > 2
        arr_left = arr[0: math.ceil(n/2)]   # [1 2 3 4 5] --> [0 3) + [3, 5)
        arr_right = arr[math.floor(n/2): ]  
        minmax_left = minmax(arr_left, len(arr_left))
        minmax_right = minmax(arr_right, len(arr_right))
            
        if minmax_left[0] < minmax_right[0] :   # compare mins of L/R first
            minn = minmax_left[0]
        else:                           # equals don't matter 
            minn = minmax_right[0]     
        if minmax_left[1] > minmax_right[1] :   # same thing for maximums of L/R
            maxx = minmax_left[1]
        else:                           
            maxx = minmax_right[1]
        print(n, minn, maxx)   # 3, 2, 1, 6   /  5, 4, 8, 7  --> 1, 6 vs 4, 8 --> 1, 8  
        return [minn, maxx]
minmax(arr, n)


# -----------------------------------
# AlgoHard 09: Given 3 numbers, tell the # of ways you can form N sum with them,
# Q: number reuse? --> yes      different combinations --> yes
arr = [1, 3, 5]
n = len(arr)        # irrelevant
x = 7               # 1 + 3 + 8 = 12

# Sol1: Dynamic
    # sum3(2): (1+1) + 5 --> 1x
    # sum3(4): (1+3) + 3, (3+1) + 3, (1+1+1+1) + 3 --> 3x
    # sum3(6): (1+1+1+1+1+1) + 1, (1+1+1+3) + 1, .., (3+3) + 1, (1+5) + 1.. --> 8x
# Thus: sum3(n) = sum3(n-1) + sum3(n-3) + sum3(n-5)
size = int(max(0, x+1))
table = size*[None]
def sum3d(n) :
   if n < 0:
      return 0
   if n == 0:
      return 1   
   return sum3d(n-1) + sum3d(n-3) + sum3d(n-5)
sum3d(x)

# Sol1: Dynamic + memo
def sum3dm(n):
    if n < 0:        # let's say no negative #
      return 0 
    if n == 0:       # subset with no elements sum to 0
      return 1
    print(n, table)
    if table[n] != None :
        return table[n]    
    return sum3dm(n-1) + sum3dm(n-3) + sum3dm(n-5)    
sum3dm(x) 


# -----------------------------------
# AlgoHard 10: Towers of Hanoi, move all disks to another rod
# - 3 rods, n disks
 
# Sol: Recur O(n^2) --> 2 calls = n^2 
def hanoi(n, A, C, B):  # (from, to, aux)
    if n == 1: 
        print("Move disk", n, "from", A, "to", C)
        return              # means function end
    hanoi(n-1, A, B, C)     # move n-1 disks from A to B
    print("Move disk", n, "from", A, "to", C)
    hanoi(n-1, B, C, A)     # recur when A-C reversed 
hanoi(3, 'A', 'C', 'B')     #


# -----------------------------------
# AlgoHard 11: Multiply two integers recursively
    # no loops, multiplication, division and bitwise operators
# Q:
# Given:    
a, b = 6, 5

# Sol: Recur, prod = prod + multiply(x-1, y)
def rec_multiply(x, y, product):
    if x == 0:              # base condition reached
        return product 
    elif x > 0 :        
        product += y + rec_multiply(x-1, y, product) 
    else: 
        x = x + 1
        product += y + rec_multiply(x-1, y, product) 
    print(x, product)   
    return product

rec_multiply(a, b, 0)   


##-----------------------------------
# AlgoHard 12:: Remove Alternate Duplicate characters from a char array 
# Q: Small letter? --> no, any characters
# Given:
arr = ['a', 'b', 'c', ' ', 'c', 'd', 'c', 'd', 'e']   # --> abc dce
n = len(arr)

# Sol: Hashtable of counts, O(n)/O(128)
h = 128*[0]
i = 0
while i < n:  
    h[ord(arr[i])] += 1         # update encounter
    if h[ord(arr[i])] == 2:     # when duplicate found
        print("i = ", i, "removed", arr[i]) # echo it
        h[ord(arr[i])] = 0      # reset counter --> can use modulus?
        del arr[i]              # delete it         
        n = n - 1               # inplace = dynamic size --> dec n             
    else :
        i = i + 1
arr


##-----------------------------------
# AlgoHard 13: Break sentence into words using a given dict of valid words
# Q:
# Given: 
s = "shoppingwithflipkartiseasy"  # --> out = shopping with flipkart is easy
n = len(s)

# Sol: My idea
d = {"shopping":1, "with":1, "flipkart":1, "is":1, "easy":1}
# out = "" # =( 
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
out = ' '.join(out)     
out



##-----------------------------------
# AlgoHard 15: Longest Repeated Subsequence (LRS)
    # LRS(str) = LCS(str,str) where str pointers are different
# Q: 
# Given:
str = 'AABEEEBCDD' # --> ABD

# Sol: Dynamic



##-----------------------------------
# AlgoHard 16: Longest Increasing Subsequence (LIS)
   # Find the length of longest sub that is in increasing order
# Q:
# Given:
arr = [10, 22, 9, 33, 21, 50, 41, 60]   # m = 5( 10,22,33,50,60)
n = len(arr)

# Sol: Recur, m(i) = 1 + max(m(j)) for j<i, and arr[j]<arr[i]

 

