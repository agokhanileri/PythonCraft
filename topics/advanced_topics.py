"""Contents: Keywords, Mutation/Override, Zip, Map/Reduc/Struct, Itertools, Fraction, RegEx."""

import functools
import itertools
import keyword  # keyword module
import operator
import re
import struct  # C structs represented as Python bytes objects

# =================================================================================================
# Keywords:
keyword.iskeyword("yield")


# -------------------------------------------------------------------------------------------------
# List mutation
a = [1, 2]
b = [3]
arr = [a, b]
b.append(4)
print(arr)  # = [[1, 2], [3, 4]], dynamically modifies


# -------------------------------------------------------------------------------------------------
# Set override
def f(x, s=set()):  # noqa: B006 (on purpose error to demo)
    s.add(x)
    print(s)


f(1)  # = {1}, s=set() is evaluated once, but nothing given
f(4)  # = {1, 4}, s is mutable, not constructed again
f(1, {2, 3})  # = {1, 2, 3}, {2, 3} overrides the set() init, constructing another copy
f(5)  # = {1, 4, 5}, continue with the original construction


# -------------------------------------------------------------------------------------------------
# Zip:
# By default, zip(a, b) silently stops at the shortest iterable.
# That can hide logic errors if your lists are unexpectedly different lengths.
# Python 3.10 introduced: zip(a, b, strict=True)


# -------------------------------------------------------------------------------------------------
# Map:
def square(x):
    #  """Test function."""
    return x**2


sq = map(square, range(5))  # applies a function to every member of iterable
print(list(sq))  # = [0, 1, 4, 9, 16]

# -------------------------------------------------------------------------------------------------
# Reduce:
arr = [1, 3, 5, 6, 2]
# reduce(fun, seq) --> apply fun to all sequence elements
sum1 = functools.reduce(lambda a, b: a + b, arr)  # (n1 + n2)+  n3 ... = 17
sum2 = functools.reduce(operator.add, arr)  # avoid lambda using op --> more readable!
sum3 = itertools.accumulate(arr, lambda a, b: a + b)  # [n1 n1+n2 n1+n2+n3 ..] = [1, 4, 9, 15, 17]
print(sum1, sum2, list(sum3))  # last element of accu = reduce()

# -------------------------------------------------------------------------------------------------
# Struct:
# struct.pack(format, v1, v2, ...)  # format specifies the expected layout when packing/unpacking
print(struct.pack("hhl", 1, 2, 3))  # h/l is long/short in C, so hhl is short/short/long
print(struct.pack("iii", 1, 2, 3))  # 8 bit per integer --> all long


# -------------------------------------------------------------------------------------------------
# Itertools: Used for speed, list, tuple, set, string, dict are all built-in iters
# method(iter, func)  # execute function for each, default is addition
lis = [1, 2, 3]  #
lis1 = list(itertools.accumulate(lis))  # = 1, 1+2, 1+2+3 = [1, 3, 6]
lis2 = list(itertools.accumulate(lis, operator.mul))  # = [1, 2, 6]
print(list(itertools.chain(lis1, lis2)))  # chain = print together
list(itertools.compress(lis1, [1, 0, 1, 1]))  # = [1, 6], filtering with boolean list
print(list(itertools.dropwhile(lambda x: x > 3, lis1)))  # prints after the func returns false
print(list(itertools.takewhile(lambda x: x <= 2, lis1)))  # opposite, prints till // // //
print(list(itertools.filterfalse(lambda x: x <= 2, lis1)))  # = [3, 4], prints when it's false
print(list(itertools.islice(lis1, 1, 4, 2)))  # selective print (start, stop, step) --> [2 4]
print(list(itertools.starmap(min, lis1)))  #
print(list(itertools.product("AB", "12")))  # cartesian product
print(list(itertools.permutations("ABC", 2)))  # all possible permutations of size n
print(list(itertools.repeat(25, 4)))  # repeats n times --> 25 25 25 25
# print(list(iterator.count(5, 2)))  # infinite iter: start, step --> 5,7,9,11.. (error)
# print(list(iterator.cycle([1, 2, 3, 4])))  # // but cyclic --> 1 2 3 4 1 2 3 4 .. (error)


# -------------------------------------------------------------------------------------------------
# Regular Expressions: Seeks pattern in the string with flag modifiers set by bitswise OR (|)
# - Returns None if no match, returns group() if match. Raises the exception re.error
# Syntax: re.match(pattern, string, flags=0)
# re.I = case-insensitive
# re.M = Makes ^/$ match the start/start of the line instead of the string
# re.S = Makes a period (dot) match any character, including a newline.
# Control chars: (+ ? . * ^ $ ( ) [ ] { } | \) --> can be escaped with a "\"
# []    : char class
# ^/$   : matches beginning vs end
# +/*   : >=1 vs any occurrences
# .     : matches any character except newline
# ?     : matches 0 vs 1 occurrences
# |     : matches with any of the characters separated by it
# \d \D : matches any digit vs non-digit
# \s \S : matches any space vs non-space (tabs are different)
# \w \W : matches any alphanumeric vs non-alphanumeric

p = re.compile("[a-e]")  # creates regular expression of char class [a-e] --> [a,b,c,d, e]
print(p.findall("AfedcBa"))  # = [e, d, c, a], case sensitive
str1 = "I went to him at 11 A.M. on 4th July 1886"
p = re.compile(r"\d")  # decimal RE class [0-9]
print(p.findall(str1))  # = [1, 1, 4, 1, 8, 8, 6]
p = re.compile(r"\d+")  # same but in groups of +=1
print(p.findall(str1))  # = ['11', '4', '1886'] --> good to extact meta data over internet

print(re.split(r"\W+", str1))  # = [.. 'him', 'at', '11', 'A', 'M', 'on', '4th', 'July', '1886']
# re.match(pattern, string, flags=0)    # matches a pattern to a whole string

line = "Cats are smarter than dogs"
match1 = re.match(r"cats", line, re.M | re.I)  # checks at the beginning
print(match1.group())
match2 = re.match(r"dogs", line, re.M | re.I)  # check at the beginning
# print(match2.group())                 # no match since dogs is at the end

search1 = re.search(r"dogs", line, re.M | re.I)  # searches through all
print(search1.group())
search2 = re.search(r"(.*) are (.*?) .*", line, re.M | re.I)
print(search2.group() + " / " + search1.group(1) + " / " + search1.group(2))

# re.sub(pattern, repl, string, max=0)    # replace pattern with repl
phone = "2004-959-559 # This is Phone Number"
num = re.sub(r"#.*$", "", phone)  # . = match all chars, $ = new line,
print(num)  # comments deleted
num = re.sub(r"\D", "", phone)  # \D = match nondigits
print(num)  # dashes removed
