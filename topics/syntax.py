"""Content: Zen, Comments, Quotes, Identifiers, Spacing, Imports, Namespaces."""

# =================================================================================================
print("\nPythonCraft: Syntax & Style Tutorial\n" + "-" * 80)
print("\n0) Zen: Prefer explicit over implicit; flat over nested; sparse over dense.")
print("Ex: import this  (displays Zen of Python full text")

# =================================================================================================
print("\n1) Commenting:")
print("- Full-line comments start with capital and end with a period when a full sentence.")
print("- Inline (trailing) comments have two spaces before '#', then start lowercase.")
print("- May utilize inline TODO:, FIXME:, NOTE: for reminders; may include owner or ticket.")

# =================================================================================================
print("\n2) Docstrings:")
print("- Wrapped inside triple quotes; used to describe modules, classes, and functions.")
print("- Start with an imperative verb phrase and end with a period.")
print("- First line ≤ 72 chars summary, then a blank line, then details/sections as needed.")
print("- Prefer Google-style sections: Args, Returns, Raises, Examples.")
print("Ex:")
print(
    '''\
def resample(signal, rate):
    """Resample a signal to the target rate.

    Args:
      signal: 1-D float samples.
      rate: Target sampling rate in Hz.

    Returns:
      Resampled 1-D float array.

    Raises:
      ValueError: If rate <= 0 or signal is empty.
    """
'''
)

# =================================================================================================
print("\n3) Indenting:")
print("- Use 4 spaces per indent level since Python 3 disallows mixing spaces with tabs.")
print("- One blank line between related blocks; two between top-level defs.")
print("- Don't try to align operators with extra spaces like my_var   = 1")
print("- Align continued lines with (again) 4 spaces under an opening delimiter.")
print("Ex:")
print(
    """\
items = [
    "alpha",
    "beta",
]
"""
)

# =================================================================================================
print("\n4) Spacing:")
print("- Surround all binary operators with one space. Ex: a >= b; a or b")
print("- No space when slice params are omitted, ex: mylist[1::3])")
print("- No space around '=' when used to indicate a default/keyword arg. Ex: z(r=real, i=imag)")
print("- 2 lines before/after classes and the top function; 1 line before/after methods.")
print("- Avoid trailing whitespace everywhere because they are invisible.")

# =================================================================================================
print("\n5) Quoting:")
print("- Use double quotes for all strings, since strings may already contain single quotes")
print("- Use triple double quotes for docstrings.")
print("- Use triple single quotes for quoting a string.")
print("Ex:")
print('''str = "Can't connect: retrying"''')

# =================================================================================================
print("\n6) Wrapping:")
print("- Default is 80; this project uses 99.")
print("- Break BEFORE operators (and, or etc.) in LONG expressions to keep diffs tidy.")
print(
    """\
is_valid = (
    lower_bound <= value
    and value <= upper_bound
)
"""
)

# =================================================================================================
print("\n7) Naming:")
print("- Modules/Functions: snake_case, Classes: CapWords, Constants: UPPER_SNAKE")
print("- Ex: my_var, my_method, MyClass, MY_CONSTANT")
print("- No special chars, separate by '_', no starting with digits.")
print("Don't use ambigous 'l', 'O', 'I' letters.")
print("Use type hinting and Protocol for duck typing.")
print("- Booleans should mean a clear yes/no: is_ready, has_value, should_update.")
print("- Avoid abbreviations unless they are obvious or industry-standard or covered in README.")
print("Ex:")
print(
    """\
MAX_RETRIES = 3

class FrameDecoder:
    def is_ready(self) -> bool:
        return True
"""
)


# =================================================================================================
print("\n8) Importing:")
print("- Coarse order: stdlib → 3rd-party → user/local. Fine order: Alphabetical.")
print("- Prefer explicit imports over wildcard imports.")
print("- Use relative imports only within a package and only one level deep.")
print("- Import as __all__ for public APIs to avoid surprises.")

# =================================================================================================
print("\n9) Error handling")
print("- Validate inputs at boundaries and raise ValueError/TypeError early.")
print("- Preserve tracebacks with 'raise ***_error from e' when adding context.")
print("Ex:")
print(
    """\
def divide(a, b):
    #  Compute safe division with input validation.
    if b == 0:
        raise ValueError("b must be nonzero")
    try:
        return a / b
    except Exception as e:
        raise RuntimeError("division failed") from e
"""
)

# =================================================================================================
print("\n10) Overall:")
print("- Use ruff/black/pre-commit locally to keep diffs minimal.")
print("- Namespaces lookup order: Local > Enclosed > Global > Built-in")
print("- File lookup order: current dir > PYTHONPATH > default path")

# 1) Module docstring (if any)

# 2a) __future__ imports (must be here, after docstring, before anything else)

# 2b) Standard library imports
# 2c) Third-party imports
# 2d) Local/package imports

# 3) Module dunders and metadata: __all__, __version__, __author__, etc.

# 4) Constants (UPPER_SNAKE)

# 5) Public classes/functions
# 6) Internal helpers prefixed with _

# 7) CLI entry guard __main__ (if executable and want to mask printing)
print("\nEx: Enchancing a function")
print("Before:")
print(
    """\
def run(a,b): #process
  if not a: raise Exception("bad")
  r=f(a,b) # calc
  return r
"""
)
print("After:")
print(
    '''\
def run(a: int, b: int) -> int:
    """Process validated inputs and return the computed result."""

    if a is None:  # reject missing primary operand
        raise ValueError("a must be provided")
    result = f(a, b)  # compute core transform

    return result
'''
)
