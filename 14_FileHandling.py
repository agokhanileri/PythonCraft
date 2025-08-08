"""Contents: File Read/Write."""
import math
import os
import sys
from pathlib import Path

for name in dir():
    if not name.startswith('_'):
        del globals()[name]
for var in dir():
    if not var.startswith('_'):
        del globals()[var]

# Given:


# -----------------------------------
current_dir = os.getcwd()   #'/Users/agi'

file = '14_FileHandling.py'

script_dir = os.path.dirname(os.path.abspath(__file__))


cwd = Path().resolve()
print(cwd)