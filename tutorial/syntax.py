"""Content: Zen, Quotes, Identifiers, Indents, Comments, Spaces, Namespaces, Imports."""

import this  # noqa: F401

# =================================================================================================
# The Zen of Python says explicit/flat/sparse is better than implicit/nested/dense

# -------------------------------------------------------------------------------------------------
# Quotes: 'strings', "special_strings", """"multi-line strings and docstrings"""
# - For triple-quoted strings, always use double quote chars
print(
    """She said "hi!" to me.
         Then I said "hi" back to him."""
)  # multi-line style

# -------------------------------------------------------------------------------------------------
# Import: Group and order as standard libs > related 3party libs > local/user libs
# - Order: Module name > docstring > from __future__ > dunders > imports
# -- module dunders are __all__, __version__, __author__ etc.
# - lookup order: current dir > PYTHONPATH > default path

# -------------------------------------------------------------------------------------------------
# Identifiers: No special chars, separate by "_", no starting with digits
# - my_var, my_method, MyClass, MY_CONSTANT --> no My_Constant (ugly)
# - Don't use 'l', 'O', 'I' letters --> confusing
# - Name the exceptions as ***_error

# -------------------------------------------------------------------------------------------------
# Indents: 4 spaces (no tab)
# - Python 3 disallows mixing spaces with tabs
# - Don't try to align operators with extra spaces like my_var   = 1
income = 3 + 4  # new line before the operator  # operator aligned with the 1st input

# -------------------------------------------------------------------------------------------------
# Comments: Should always start with single space
# - Start with capital if full line comment, lowercase if partial line.
# - Wrapping at 100 is default but 80 is safer --> I choose 99

# -------------------------------------------------------------------------------------------------
# Spaces:
# - Surround binary operators with 1 space, ex: a >= b, a and b etc.
# - No space when slice params are omitted, ex: ham[1::3]
# - No space around = when used to indicate a keyword arg or a default, ex: complex(r=real, i=imag)
# - 2 blank lines before/after classes and top function, 1 blank line for methods
# - Try to avoid trailing whitespace anywhere since they are invisible


def myfunc():  # use self for the 1st arg in instance methods
    """Func is dope."""  # starts with capital, ends with dot


class MyClass:
    """Class is dope."""


print(myfunc.__doc__)
print(MyClass.__doc__)


# -------------------------------------------------------------------------------------------------
# Namespaces: lookup order is Local > Enclosed > Global > Built-in

# -------------------------------------------------------------------------------------------------
# Encoding: Python2 used ASCII, whereas Python3 uses UTF-8. Other encodings are for testing or foreign chars

# -------------------------------------------------------------------------------------------------
# Py8 guidelines:
