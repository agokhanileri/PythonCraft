# =================================================================================================
# Problem: 0020. Valid Parentheses
# Link: https://leetcode.com/problems/valid-parentheses
# Tags: Stack, String
# Complexity: O(n) / O(n)
#
# Task: Return True if brackets in s are properly matched and nested.
# Hints:
# (1) s consists of parentheses only '()[]{}'.
# (2) 1 <= s.length <= 10^4


# =================================================================================================
# Solution:
class Solution:
    def isValid(self, s: str) -> bool:
        """Stack approach: O(n) / O(n)"""
        # No need to check length since it's given n >=1, also we return not stack anyway
        # pairs = {")": "(", "]": "[", "}": "{"}  # can also define as dict
        stack = []  # stack to keep/check the order
        for ch in s:
            # print(ch, stack, ans)
            if ch in ["(", "[", "{"]:  # opening --> push
                stack.append(ch)
            elif ch in [")", "]", "}"]:  # closing --> pop
                if stack == []:  # no open brackets yet --> False
                    return False
                popped = stack.pop()
                if (  # o.w. pop the last open pharanthesis and compare
                    (ch == ")" and popped != "(")
                    or (ch == "]" and popped != "[")
                    or (ch == "}" and popped != "{")
                ):
                    return False  # no pair matched --> False
                else:  # ignore other chars
                    pass

        return not stack  # True if all pass, False if any open brakcets left


# =================================================================================================
# Complexity:
# Time: n loops × (dict_lookup + list_push/pop + compare) = n × (1+1+1) --> O(n)
# Space: at most n/2 open brackets in stack --> O(n)

# =================================================================================================
# Testing:
CASES = [
    ("", True),
    ("()", True),
    ("()[]{}", True),
    ("(]", False),
    ("([)]", False),
    ("{([])]}", False),
    ("{[]}", True),
    ("(((((((((())))))))))", True),
    ("[", False),
    ("]", False),
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
