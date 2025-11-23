"""Contents: If, For, While, Case, Continue/Break/Pass, Iterables."""

# =================================================================================================
# If:
a, b = 3, 5
if a > b:
    minn = b
elif a < b:
    minn = a
else:
    print("they're equal")

print(a if a < b else b)  # = a = 3, no ':' required for one-liners
{True: a, False: b}[a < b]  # = a, use dict for //
(b, a)[a < b]  # = a, use tuple for selecting
(lambda: b, lambda: a)[a < b]()  # = a, only 1 eval (most efficient), () to eval the expr
print(a < b and a or b)  # = (True & a) or b = a or b = a


# -------------------------------------------------------------------------------------------------
# For:
for ch in "abc":
    print(ch, end=" ")

for n in [1, 2, 3]:
    print(n, end=" ")
for n in range(1, 4):  # same thing
    print(n, end=" ")
else:
    print("finished")


# -------------------------------------------------------------------------------------------------
n = 1
while n < 4:  # same thing
    print(n, end=" ")
    n = n + 1


# -------------------------------------------------------------------------------------------------
# Continue/Break/Pass
print("j = ", end=" ")
for i in [1, 2]:
    for j in "abcde":
        if j == "b":
            continue
        elif j == "c":
            pass
        elif j == "d":
            break
        else:
            pass
        print(i, j, end=" ")  # = a c a c, skips b using continue, breaks at d


# -------------------------------------------------------------------------------------------------
# Case: like a dict
def f(x):
    return {
        1: 10,
        2: 20,
    }.get(
        x, 0
    )  # default get value to return


print(f(1), f(2), f(3))  # = 10, 20, 0


# -------------------------------------------------------------------------------------------------
# Iterables: used if we don’t need to modify the container, more concise and faster
# a) Reversed:
for i in reversed(range(1, 10, 3)):  # = 7 4 1,.
    print(i)

# b) Lambda: func that take many args but return 1 value as expression (can't print directly)
exp = lambda x, y: x**y  # lambda [arg1 [,arg2,.....argn]]: expression
exp(3, 2)  # = 9

# c) Filtering: used to filter iterables
[x**2 for x in [1, 2, 3] if x >= 2]  # = [4, 9], one-line list creation
all(x > 2 for x in [1, 2, 3])  # = False, due to 3

nums = [1, 2, 3]
fobj = filter(lambda x: x >= 2, nums)  # using filter func, usually uses lambda
for i in fobj:  # = 4, 9
    print(i**2)

# d) Enumerate: creates an enum object as an iterator
arr = ["a", "b", "c"]
for i, val in enumerate(arr, start=1):  # like a dict, where keys are 0,1,2.. by default
    print(i, val, end=" ")  # = 1 a 2 b 3 c
for item in enumerate(arr, start=1):  # alternative
    print(item[0], item[1], end=" ")  # = 1 a 2 b 3 c


# --Iterables_Advanced
# e) Zip: vertically maps between containers
xlist = [1, 2, 3]
ylist = ["a", "b", "c"]
for x, y in zip(xlist, ylist, strict=False):
    print(x, y, end=" ")  # = 1 a 2 b 3 c

# f) Chain: horizontally maps between containers
from itertools import chain  # using chain()

for item in chain(xlist, ylist):
    print(item, end=" ")  # 1 2 3 a b c

# Iteritems:  # like dict.items(), N/A for Python 3+


# -------------------------------------------------------------------------------------------------
# Counters: used to accumulate stats, count distinct elements of Containers
from collections import Counter  # a subclass of dict (unordered)

print(Counter(["B", "B", "A", "B", "C", "A"]))  # create with a sequence
print(Counter({"A": 2, "B": 3, "C": 1}))  # // with dictionary
print(Counter(A=2, B=3, C=1))  # // with keyword arguments

cntr = Counter()  # empty counter
cntr.update(["A", "B", "C"])  # 1st filling
cntr.update(["A", "A", "C"])  # 2nd filling
print(cntr)  # ={'A': 3, 'C': 2, 'B': 1}

comp = ["A", "B", "C", "D"]  # scans a premade Counter, D = 0
for i in comp:
    print(i, cntr[i])

print(list(cntr.elements()))  # get all elements
print(cntr.most_common(2))  # = A:3, C:2, 2 most common elements
