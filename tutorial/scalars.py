"""Content: Numbers, Boolean, Strings, Arithmetic."""  # See bit_ops.py and math.py for more

import math

# =================================================================================================
# Numbers:
print(int("3"), str(3.0), int(-3.9))  # 1, 4.5, -3 (casts by rounding close to 0)
print(0x10C, 0b1001)  # 268 (hex), 9 (binary). Both types are still 'int'
print(isinstance(3, float), isinstance(3.0, float))  # False, True

# a = 3; b = 3  # can declare multiple in 1 line but PEP8 says no semicolumn
a, b = 3, 6
c = d = 0
e = a + b  # multi-line, can't comment after '\'
f = a + b  # multiline declaration 2, more explicit
d += 1  # assignment op, no return, so can't put it within the print
print(a, b, c, d, e, f)  # 3, 6, 0, 1, 9, 9
"333.3".isdigit()  # False
"666.6".isdecimal()  # False, dot disturbs

# -------------------------------------------------------------------------------------------------
# Boolean:
print(int(True), bool(0))  # 1, False


# -------------------------------------------------------------------------------------------------
# Strings: only char type, immutable, created by '', access by [] (no slicing)

# Character Encoding: Python 2 used ASCII, Python 3 uses UTF-8, others are for testing/foreign
print(ord("a"), chr(97))  # 97, a (ord converts char to ASCII, v.v. for chr)

str1 = "abc"
print(str1 * 2, str1 + str1)  # abcabc, abcabc
print("-".join(str1))  # a-b-c

str2 = "hello world"
str2.startswith("he")  # True
str2.isalpha()  # False (spaces and numbers disturb alphanumeric)
str2.islower()  # True
str2.capitalize()  # 'Hello world' (first letter only)
str2.count("o", 0, 9)  # 2 (counted in range 0 to 9)
str3 = str2.title()  # Hello World (capitalizes every 1st char)
str3.istitle()  # True
str3.swapcase()  # hELLO wORLD
str4 = "aa, bb, cc"

print(str4.split(","))  # ['aa', ' bb', ' cc']
print(str4.split(",", 1))  # ['aa', ' bb, cc'] (1 times, 1st comma by default)
print(str4.strip(","))  # 'aa, bb, cc' (removes it fully if not a special char)
print(str4.rstrip(" c"))  # 'aa, bb,' (removes if it is on the very right)
str4.index(",")  # 1 = str3.find(',') (only returns the 1st instance)
print(str1.center(5, "-"))  # --ab- (center in between '-', total 5 chars)
print(str1.rjust(5, "-"))  # ---ab (same but right adjusted)
print("--xyz---".rstrip("-"))  # ab (right stripped)

eval("3+4")  # 7 (evals to a string, will eval anything inside


# =================================================================================================
# Arithmetic:
a, b = 9, 2
print(f"sum: {a + b}, diff {a - b}")  # 11, 7 (add/substract)
print("product =", a * b)  # = 18 (multiply)
print("quotient =", a / b)  # 4.5 (divide)
print("remainder =", a // b)  # 1 (floordiv)
print("modulus =", a % b)  # 1 (mod)
print("exponent1 =", a**b)  # 81 (power)
print("exponent2 =", pow(a, b))  # alternative way
print("root =", math.sqrt(a))  # alternative way
print("pi =", math.pi, "e =", math.e)  # constants
print("ln =", math.log(math.e))  # log

# --- Rounding
x = -3.75
print(f"abs: {abs(x)}, round: {round(x, 1)}, floor: {math.floor(x)}, ceil: {math.ceil(x)}")
print(abs(x))
print(round(x, 1))
print(math.floor(x))
print(math.floor(x))

# --- Precision caution -------------------------------------------------------
print(0.1 + 0.2 == 0.3)  # False due to floating-point rounding
