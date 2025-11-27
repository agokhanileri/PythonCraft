# =================================================================================================
# Problem: 0007. Reverse Integer
# Link: https://leetcode.com/problems/reverse-integer
# Tags: Math
# Complexity: O(log(n)) / O(1)
#
# Task: Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes
# the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Hints:
# (1) ...
# (2)


# =================================================================================================
# Solution:
class Solution:
    def reverse(self, x: int) -> int:


# =================================================================================================
# Testing:
CASES = [
    (121, True),
    (-121, False),
]

METHODS = [
    name
    for name in dir(Solution)
    if not name.startswith("_") and callable(getattr(Solution, name))
]


def _call(func, args):
    # Normalize args: allow raw value or tuple
    if not isinstance(args, tuple):
        args = (args,)
    return func(*args)


def test_pass():
    sol = Solution()
    for name in METHODS:
        func = getattr(sol, name)
        for args, expect in CASES:
            # CHANGE: reuse _call to avoid duplicate arg normalization
            assert _call(func, args) == expect


if __name__ == "__main__":  # simple CLI smoke test
    import sys

    sol = Solution()
    methods = METHODS if isinstance(METHODS, (list, tuple)) else [METHODS]

    ok = True
    for name in methods:
        fn = getattr(sol, name)
        for args, expect in CASES:
            got = _call(fn, args)
            if got != expect:
                print("❌FAIL")
                print(f"method: {name}")
                print(f"args:   {args}")
                print(f"expect: {expect}")
                print(f"got:    {got}")
                ok = False
                break
        if not ok:
            break

    print("✅PASS" if ok else "❌FAIL")

    # avoid SystemExit in Spyder/IPython, but keep exit code in normal Python runs
    in_ipy = bool(getattr(sys, "ps1", None)) or "ipykernel" in sys.modules
    if not in_ipy:
        sys.exit(0 if ok else 1)
