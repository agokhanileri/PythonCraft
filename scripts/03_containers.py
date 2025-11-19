"""Content: Lists, Tuples, Sets, Dictionary, Stacks/Queues, Collections."""

import array as ar
import collections as col
from collections import ChainMap, Counter, OrderedDict

# =================================================================================================
# Lists: mutable, any type, create and access by []
str1 = "abc"
lst1 = list(str1)  # ['a', 'b', 'c'] (casts string to list)
del lst1[1:3]  # ['a']
lst1 = lst1 + ["b"]  # ['a', 'b'] (concats)
lst1.append("c")  # ['a', 'b', 'c']
lst1.insert(1, "e")  # ['a', 'e', 'b', 'c'] (shifts the rest)
lst1.pop()  # 'c' (removes and returns the last element)
lst1.pop(0)  # 'a' (// first element)
lst1.clear()  # []

lst2 = list(range(1, 11))  # need to cast to list at Python 3x
print(lst2[-5:-3])  # [6, 8) w/ 1x inc --> [6, 7] (arr[-1] = arr[end])
print(lst2[3:9:2])  # [4, 10) w/ 2x inc --> [4, 6, 8]
print(lst2[9:3:2])  # [10, 4) w/ 2x inc --> []
print(lst2[:6:-1])  # = (7, 10] w/ 1x dec --> [10, 9, 8]

lst3 = [1, 2, 3]
lst3.insert(1, 0)  # insert at 1st pos, shift the rest
print(lst3)  # [1, 0, 2, 3]
lst3.remove(2)  # remove the first occurrence of 2
print(lst3)  # [1, 0, 3]
lst3.reverse()
print(lst3)  # [3, 0, 1]
lst3.sort()
print(lst3)  # [0, 1, 3]
lst3 = lst3 + list("ab")  # = [3, 0, 1, 'a', 'b'], can't sort now due to chars
lst3.count(3)  # = 1, count 3s
[1, 7, 3, 7, 5].index(
    7,
    2,
)  # = 3, returns the index of 2nd encounter of 7
lst3.extend([1, 2])  # = [3, 0, 1, 'a', 'b', 1, 2], like a multi append
lst3w = lst3  # pointer is wrong, will get updated each time lst3 changes
lst3c = lst3.copy()  # returns a shallow copy
lst3f = lst3[:]  # fastest copy method by slicing

lst4 = [1, 2, 3]
print(sum(lst4))  # = 6
lst4[0] = lst4[2] = 4
print(lst4)  # = [4, 2, 4]

print([2**x for x in range(1, 11)])  # single line declaration


# -------------------------------------------------------------------------------------------------
# Sets: mutable, only str/nums, no duplicates, create by {}
# only add/remove/lookup, no access/order/index
set1 = {"a", "b", "c"}  # = {'a', 'b', 'c'}
set1.add("d")
print(set1)  # = {'b', 'd', 'a', 'c'}, random order
set1.remove("d")
print(set1)  # = {b', 'a', 'c'}
lst = list(set1)  # = [b', 'a', 'c']
set2 = frozenset(["c", "d", "e"])  # immutable, can't do set2.add('a')

set3 = set1 | set2
print(set3)  # = = set1.union(set2) = {'b', 'c',  'a', 'e'}
set4 = set1 & set2
print(set4)  # = set1.intersection(set2) = {'c'}
set5 = set1 - set2
print(set5)  # = set1.difference(set2) = {'b', 'a'}
print(set1.isdisjoint(set3))  # = no intersection? =  FALSE
set5.clear()  # same as list

print(set1 != set2)  # = True
print(set1 < set2)  # = is proper subset of = False
print(set1 ^ set2)  # = !(set1 & set2) = {'e', 'b', 'd', 'a'}

set1.update({"d", "e"})  # will simply add 'd' and 'e' if not present in set1 already
print(set1)  # {'e', 'a', 'd', 'b', 'c'}


# -------------------------------------------------------------------------------------------------
# Tuples: any type, immutable (fast), create by (), access by []
tup1 = (1,)
tup2 = ("a", "b")  # need to use comma to create 1-element tuple
print(tup1 + tup2)  # = (1, 'a', 'b'), concat like a list
tup3 = (tup1, tup2)  # = ((1,), ('a', 'b')), nest like a list
tuple(range(1, 4))  # = (1, 2, 3)
print(tup1 * 2)  # = (1, 1)
max(tup2)  # = 'b'
print((3, 1) > (2, 2))  # = True, checks the first item only
# any set of vars seperated with comma but no pharanthesis will default to a tuple


# -------------------------------------------------------------------------------------------------
# Dictionaries: any type, mutable, create by {} or [[]], access by keys()/values()/get()
# - Just like Hashmap: keys can't be duplicate and should be hashabel (str, int, float, object)
# - key/value pairs can be Null, if we use special dict classes (see advanced section)
# - O(1) access, if we know missing keys
dic1 = {}  # empty dict
dic1["a"] = 1  # 1st way
dic1["b"] = 2  # //
dic1 = dict([["a", 1], ["b", 2]])  # 2nd way
dic1 = {"a": 1, "b": 2}  # 3rd way

len(dic1)  # = 2
str(dic1)  # = "{'a': 1, 'b': 2}", converts the whole thing to string
print(dic1)  # = {'A': 123, 'B': 345}
print(dic1.keys())  # = dict_keys(['A', 'B'])
print(dic1.values())  # = dict_values([123, 345])
print(dic1.items())  # = dict_items([('A', 123), ('B', 345)])

for k in dic1:  # iter keys
    print(f"{k} {dic1[k]}")
    # print("%s %s" % (k, dic1[k]))
for k, v in dic1.keys(), dic1.values():  # iter both key/value, more explicit
    print(f"{k}, {v}")
    # print("%s %s" % (k, v))
for k, v in dic1.items():  # alternative
    print(f"{k} {v}")

del dic1["a"]  # delete one record
print("b" in dic1)  # = True, dic1.has_key('b') is N/A
print(dic1.get("a", "N/A"))  # = N/A, alternative check with a default get
print(dic1.setdefault("a", "None"))  # = A: None, puts it in the end
print(dic1["a"], dic1["b"])  # = None 2

dic1.setdefault("C", "None")  # syntax: (key, def_value)
dic1.get("C", "None")  # = 'None'
str5 = "abc"
dic1.get("b")  # = 2
dic1.get(str5[1])  # = 'None'

str(dic1)
dic1.clear()  # = {}, empties it, doesn't delete
del dic1  # full delete


# -------------------------------------------------------------------------------------------------
# Stacks (LIFO): O(1) insert/remove, O(n) access (same as arrays)
stack = [1, 2, 3]
stack.pop()  # = [1, 2]
stack.append("a")  # = [1, 2, 'a']


class Stack:
    def __init__(self):
        self.arr = []

    def is_empty(self):
        return self.arr == []

    def push(self, x):
        self.arr.append(x)

    def pop(self):
        if self.size() == 0:
            return None
        else:
            return self.arr.pop()

    def peek(self):
        return self.arr[-1]

    def print(self):
        return self.arr

    def size(self):
        return len(self.arr)

    def get_min(self, s):
        if s.isEmpty() == []:
            return -1
        minn = s.pop()
        for i in range(s.size()):  # fix unused i
            x = s.pop()
            if x < minn:
                minn = x
        return minn


s = Stack()
s.push(3)
s.push(4)
s.push(1)
s.push(2)
s.print()  # = [3, 4, 1, 2]
print(s.size(), s.peek(), s.min())  # = 4, 2, 1


# -----------------------------------
# Queues: (FIFO, O(n) access still but a little slower during removal (shifting)
from collections import deque  # so employ deque that can do fast ops from start/end

queue = deque([1, 2, 3])  # = ([1, 2, 3]) --> deque object
queue.append(4)  # = ([1, 2, 3, 4])
queue.popleft()  # = 1, queue = ([2, 3, 4])

# =================================================================================================
# Collections
# ChainMap encapsulates dicts like a bookshelf
dic1 = {"a": 1, "b": 2}
dic2 = {"c": 3, "d": 4}
dd = ChainMap(dic1, dic2)
print(dd)  # = ChainMap({'a': 1, 'b': 2}, {'c': 3, 'd': 4})

# Counter is a container where values = counts by default
dic3 = dic2
dic3.update(dic1)  # = {'c': 3, 'd': 4, 'a': 1, 'b': 2}, adds dic1 contents
dic4 = Counter("aabbbbc")
print(dic4)  # = Counter({'b': 4, 'a': 2, 'c': 1}), already sorted
dic4.most_common(2)  # = [('b', 4), ('a', 2)], most 2 common items/counts
cntr1 = Counter({"x": -3, "y": 3, "z": -2})
cntr2 = Counter({"x": 2, "y": 4})
cntr2["y"] = 5
print(cntr2)  # Counter({'x': 2, 'y':5}), can access/update easily
cntr1 + cntr2  # = Counter({'y': 8}), only shows positive counts
cntr1 - cntr2  # = Counter(), all negative
cntr1 & cntr2  # = Counter({'y': 3}), min/pos values
cntr1 | cntr2  # = Counter({'y': 5, 'x': 2}), max/pos values

# Handling missing keys
d = col.defaultdict(lambda: "N/A")  # sets the default once and for all
d["B"] = 123
d["A"] = 345
print(d["C"])  # = N/A
print(d)  # = {'B': 123, 'A': 345, 'C': 'N/A'})

dord = OrderedDict([["B", 2], ["C", 4], ["D", 3]])
del dord["B"]
dord["B"] = 2
print(dord)  # = OrderedDict([('C', 4), ('D', 3), ('B', 2)])
dord.move_to_end("B", False)  # moves back to the beginning
print(dord)  # = OrderedDict([('B', 2), ('C', 4), ('D', 3)])

dord["A"] = 1
for key in sorted(dord):
    dord.move_to_end(key)
print(dord)  # = OrderedDict([('A', 1), ('B', 2), ('C', 4), ('D', 3)])

for key, _ in sorted(dord.items(), key=lambda item: item[1]):
    dord.move_to_end(key)
print(dord)  # = OrderedDict([('A', 1), ('B', 2), ('D', 3), ('C', 4)])

for value in sorted(dord.values()):
    pos = dord.values().index(value)
    print(value, pos)

dnorm = dict([["B", 2], ["C", 4], ["D", 3]])
dnorm.values().index(4)
print(dord)  # = OrderedDict([('A', 1), ('B', 2), ('C', 4), ('D', 3)])


# -------------------------------------------------------------------------------------------------
# Arrays: similar to list except single type, mutable
arr1 = ar.array("i", [1, 2, 3])  # = array('i', [1, 2, 3])
print(arr1.typecode)  # = i
print(arr1.itemsize)  # = 4, (byte)
print(arr1.buffer_info())  # = (4474546816, 3), mem address
print(arr1.count(2))  # = 1, occurrences
arr1.extend([4, 5])
print(arr1)  # = [1, 2, 3, 4, 5]
arr2 = ar.array("i", [])
print(arr2.fromlist([1, 2, 3]))  # = array('i', [1, 2, 3]), cast to ar
print(arr2.tolist())  # = [1, 2, 3], cast back
print(arr1[1:3])  # = array('i', [2, 3])
