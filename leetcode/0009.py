# =================================================================================================
# Problem: 0009. Palindrome Number
# Link: https://leetcode.com/problems/palindrome-number
# Tags: Math
# Complexity: O(log(n)) / O(1)
#
# Task: Given an integer x, return True if x is a palindrome.
# Hints:
# (1) -2^31 <= x <= 2^31 - 1
# (2) Follow-up: Solve without converting to a string.
# (3) Single-digit → palindrome
# (4) Negatives → not palindrome
# (5) Numbers ending with 0 (but not 0 itself) → not palindrome


# =================================================================================================
# Solution:
class Solution:
    def isPalindrome(self, x: int) -> bool:
        """Reverse half of the number | O(log(n)) / O(1))"""
        if (x < 0) or (x % 10 == 0 and x != 0):  # using (4) and (5)
            return False
        rev = 0
        while x > rev:
            rev = rev * 10 + x % 10  # append last digit of x to rev (left shift)
            x //= 10  # remove last digit from x (right shift)
        return x == rev or x == rev // 10

    def isPalindrome2(self, x: int) -> bool:
        """Conver to string : O(n) / O(n))"""
        intstr = str(x)  # integer string
        n = len(intstr)
        if n == 1:
            return True
        elif (x < 0) or (intstr[-1] == "0"):
            return False  # no left zero padding allowed
        else:
            for i in range(0, n // 2):  # will miss the mid number if n is odd, but no problem
                if intstr[i] != intstr[-1 - i]:
                    return False  # 1 violation is enough to conclude
        return True  # if no violations yet


# =================================================================================================
# Testing:
CASES = [
    (121, True),
    (-121, False),
    (10, False),
    (0, True),
    (1221, True),
    (12321, True),
    (1001, True),
    (100, False),
    (11, True),
    (-101, False),
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
