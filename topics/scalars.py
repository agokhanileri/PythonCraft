"""Content: Numbers, Arithmetic, Boolean, Bits, Casting, Strings
See bit_ops.py for bytes and MathCraft repo for math."""

import math

# =================================================================================================
print("\n1) Numbers:")
print(int("3"), int(-3.9))  # 3 as int/str, -3 (truncates toward 0)
a = 3; b = 3  # # noqa: E702, can declare multiple vars in 1 line despite ruff/PEP8 warning
a, b = 3, 6
c = d = 0
d += 9  # assignment op, no return
e = a + \
    b  # multi-line, note that we can't comment after '\'
print(a, b, c, d, e)  # = 3, 6, 0, 9, 9

print(isinstance(3, float), isinstance(3.0, float))  # False, True
"33.3".isdigit()  # = False, due to the dot
"66.6".isdecimal()  # = False, //

# Arithmetic:
f, g = 9, 6
print(f"sum: {a + b}, diff: {a - b}, product: {a * b}, quotient: {a / b}")
print(f"remainder: {a // b}, modulus: {a % b}, exponent: {a ** b} or pow(a, b)")
print(f"root: {a ** 0.5} --> Throw valueError for negative float # --> need to use cmath")
print(f"constants: pi = {math.pi}, e = {math.e}, ln = {math.log(math.e)}")
# -------------------------------------------------------------------------------------------------
x = -3.69
print(f"Rounding {x}")
print(f"abs: {abs(x)}, round: {round(x, 1)}, floor: {math.floor(x)}, ceil: {math.ceil(x)}")

# =================================================================================================
print("\n2) Boolean:")
print(int(True), bool(0))  # 1, False
print(0.1 + 0.2 == 0.3)  # False, due to floating-point rounding
bool(-2)  # = True, only 0 is False

not (False or True)  # = not True = False, boolean (logical) op
2 in [1, 2, 3]  # = True, there exists or not
False + True + 5  # = 0+1+5 = 6, boolean literals, OR-like
2 != 4 > 2  # = (2 != 4) AND (4 > 2) = TRUE

all([1, 0, 1])  # = False, AND operation
any([False, True, False])  # = True, OR operation
print(any([]), all([]))  # = False, True

a = b = 1
a is b  # = True, same memory location (pointer to 1)
a = b = [1, 2, 3]
a is b  # = False, different memory allocations for arrays
print(0 < a >= b)  # = (0 < a) AND (a >= b) = TRUE (doesn't check for 0 < b)


char1 = "4"
int1 = 11
int2 = 3
str1 = "101"
type(char1)  # type of both char and string is str
i = ord(char1)  # = 4
b = int(str1, 2)  # = 5
f = float(str1)  # = 101.0
h = hex(int1)  # = 0xb
c = complex(int1, int2)
s = str(int1)  # "int1"
print("i=%, b=%, f=%, h=%, c=%, s=%", i, b, f, h, c, s)


print(0x10C, 0b1001)  # 268 (hex), 9 (binary). Both types are still 'int'

# =================================================================================================
print("\n3) Bits: Arithmetic, Shifting, Sign")
bin(0b0110 + 0b0010)  # gives int by default, so need to cast
bin(0b0110 + 0b0101)  # = 0001
bin(0b0011 - 0b0010)  # = 0001
bin(0b0110 - 0b0011)  # = 0011
bin(0b1000 - 0b0110)  # = 0010
bin(0b0011 * 0b0101)  # = 0011 + 100 + 1000 = 1111
bin(0b0011 * 0b0011)  # = 0110
bin(0b1101 ^ 0b0101)  # = XOR = 1000
bin(0b1101 ^ 0b0101)  # = OR = 1000
bin(0b0100 * 0b0011)  # = 1100 (4x = by 2)

# Bit shifting
x = 5  # = 101 (3 bits)
# Arihmetic shift (>>): keeps the sign bit (MSB)
# Logical shift (>>>): push a 0 on the left (MSB)
# x >>> 1  # = 0+10 = 2     --> no logical shift in Python
x >> 1  # 101 >> 010 = 3 but Python only has Logical shift with but prefers unsigned
# if you logical shift a negative number too much it'll be -1-1-1... = -1 signed int

bin(0b1101 >> 2)  # = push 0s on left: --> 0110 --> 0011
# 2's complement
~0  # = inv(b00) = b11 = -1, bitwise op
~1  # = inv(b01) = b10 = -2 = operator.xor_(0, 1)
~x  # = -(x+1) = -6 --> assumes signed


# =================================================================================================
print("\n2) Strings: Only char type, immutable, create by "", access by [] (no slicing)")
print(f"Char conversion: ord(a) = {ord("B")} and vice versa chr(66) = {chr(66)}")
print(f"Char encoding: café = {"café".encode()}")
print("- Py2 used ASCII, Py3 uses UTF-8, others are for testing and foreign text.\n")
a = "asd"
b = b"asd"  # string and variables are case sensitive, bytes are not
c = a.encode("ASCII")  # string to byte, via ascii or utf-8  --> c=b
d = c.decode("ASCII")  # decode back to string --> d=a
# -------------------------------------------------------------------------------------------------
print(str(3.0))
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

print("\nFormatting, f-strings, and bytes")
name, score = "Ada", 97.457
print(f"Hello {name}, score {score:.1f}")
escaped = "Line1\nLine2\tTabbed"
print(escaped)
print(r"Raw strings keep escapes: Line1\nLine2")
