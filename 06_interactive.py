"""Contents: Printing, PrettyPrint, Prompting, FileHandling, ContextManagers."""

import os

# from pathlib import Path

# =================================================================================================
# Printing:
help("print")  # = print(value, sep=' ', end='\n', file=sys.stdout, flush=False)
print(1, 2, 3, sep=" ", end="#")  # = 1 2 3#
print(lst=[1, 2, 3], end="#")  # = [1, 2, 3]#, container items default sep=' '
print("hi" * 2)  # = hihi = print('hi' + 'hi')

# formatting - %d/%i: signed, %u: unsigned, %X: hex_caps, %E: eform_caps, %G: float_short
print("{Who} <3 {food}".format(food="chicken", Who="I"))  # = I <3 chicken
c, s, d, u, f, x, X, e, g = "c", "str", 10, 10, 10, 10, 10, 100.22456, 100.22456
print(f"Formats: {c} {s} {d} {u} {f:.6f}")  # c str  10 10  10.000000
print(f"Formats: {x:x} {X:X} {e:e} {g:g}")  #  a A 1.002246e+02 100.225
print(f"{5.256:3.2f}, {6.2:3.0f}")  # = 5.26, 6

# escaping - common: \t, \n, \r, \u
print("He said \"hey\" 'look'\fa")
print(r"C:\\Temp")  # = C:\\Temp, rawstring to disable escaping
unicode = "\u00dcnic\u00f6de"  # unicode for non ASCII support


# --Print_Advanced
# escaping - other: \a = Alert, \b = Backspace, \e = Esc, \cx = Control+X, \x = unicode Esc
from pprint import pprint  # to process inputs from other API

data1 = {
    "status": "OK",
    "results": [
        {"components": [{"long_name": "Raj-path", "types": ["route"], "short_name": "Raj-path"}]}
    ],
}
print(data1)
pprint(data1)  # more user friendly


# -------------------------------------------------------------------------------------------------
# User I/O: Read 2 ages from user (with a space separator) and print
a, b = (int(x) for x in input("Enter ages: ").split())  # returns string, need to cast
print(f"Ages are {a}, {b}")  # = Ages are 4, 5

str = input("Enter your input: ")  # enter [x*5 for x in range(2,10,2)]
inp = eval(str)
print(inp)  # [10, 20, 30, 40]

# -------------------------------------------------------------------------------------------------
# File I/O: Read integers from a text file (one int per line), then add one in the end
# - open(file [, mode][, buffering]), 'r' = read, 'r+': read/write
work_dir = os.getcwd()
file_name = "integers.txt"
file_path = work_dir + "/inputs/" + file_name

# a) Legacy: just for illustration
file = open(file_path, "r+")  # # noqa: SIM115, read + append
file.name  # ../Dropbox/GosuML/sw_python/data/integers.txt'
file.mode  # = 'r' = default access mode
try:
    data = file.read()  # read the whole thing
finally:
    file.close()  # auto-close in case of an error

items = data.split()  # ['1', '3', '4'], default: whitespace and newline
file.write("50")  # writes at the end by default
file.tell()  # we are at 13th char
file.seek(0)  # return to the byte 0 (beginning)
file.readline()  # = '10\n', line by line reading
file.seek(3)  # = '\n',
file.readline()  # = ' \n', every char is 2 byte --> hard to track
file.seek(2)  # go back to empty 2nd line
file.write("\n20\n")  # write there
file.close()  # fhandle still exists but can't R/W anymore

# b) Context Manager: modern, safer, simpler
with open(file_path) as file:  # read-only (default: 'r')
    data = file.read()
print(file.read().split())  # = ['10', '20', '30', '40', '50']
file.close()
data1 = file.readlines()
data1[1] = "20\n"
data1.append("50\n")

with open(file_path, "w") as file:
    data = file.read()
file.writelines(data1)
del file  # better to del handle too
# os.rename("./data/integers.txt", "./data/numbers.txt")
# os.remove("./data/numbers.txt")  # hope you saved it!


# -----------------------------------
# QUESTIONS
# -----------------------------------
# File I/O: Count the occurrences of each word in given text file using dictionary
fname = "words.txt"
fpath = workdir + indir + "/" + fname
fhandle = open(fpath)
data = fhandle.read()
import string

data = str(data)
for char in string.punctuation:
    data = data.replace(char, "")
words = data.lower().split()  # first lowercase, then split in a list
d = dict()
for w in words:
    d[w] = d.get(w, 0) + 1  # returns 0 if N/A
print(d)
