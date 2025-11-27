# =================================================================================================
# Problem: 0089. Gray Code
# Link: https://leetcode.com/problems/gray-code
# Tags: Bits
# Complexity:
#
# Task: Return any valid n-bit gray code sequence.
#
# Hints:
# (1) [0, 2n - 1], binary representation of every pair of adjacent integers differs by 1 bit
# (2) 1 <= n <= 16


# =================================================================================================
# Solution: O(2ⁿ) / O(2ⁿ)
class Solution:
    def grayCode(self, n: int) -> list[int]:
        # n_bin = bin(n)[2:]  # to get the binary represenation of a number
        # Next gray code is found by XORing right shifted binary by itself
        # So, gray[i+1] = gray[i] XOR (gray[i]>>1)
        gray = [0]
        for i in range(1, 2**n):  # until 2ⁿ - 1
            gray.append(i ^ (i >> 1))  # calculate the next gray code with formula
        return gray


# =================================================================================================
# BigO:
# Time: 2ⁿ loops x (bit_shift + XOR + append) = 2ⁿ*(1+1+1) --> O(2ⁿ)
# Space: Stores 1 number per iter --> O(2ⁿ)

# =================================================================================================
# Testing:
# Simple test:
sol = Solution()
sol.grayCode(2)

# Batch test:
CASES = [0, 1, 2, 3, 4]  # extend n as needed

METHODS = [
    name
    for name in dir(Solution)
    if not name.startswith("_") and callable(getattr(Solution, name))
]


def _one_bit(a: int, b: int) -> bool:
    x = a ^ b
    return x != 0 and (x & (x - 1)) == 0  # power of two → one bit differs


def valid_gray(seq, n: int) -> bool:
    n_values = 1 << n
    if not isinstance(seq, (list, tuple)) or len(seq) != n_values:
        return False
    if set(seq) != set(range(n_values)):
        return False
    return all(_one_bit(seq[i], seq[i + 1]) for i in range(n_values - 1))


def _call(func, args):
    # Normalize args: allow raw value or tuple
    if not isinstance(args, tuple):
        args = (args,)
    return func(*args)


def test_pass():
    sol = Solution()
    if not hasattr(sol, "grayCode"):
        raise AttributeError("Solution.grayCode not implemented")
    for n in CASES:
        out = sol.grayCode(n)
        assert valid_gray(out, n), f"grayCode({n}) invalid: {out}"


if __name__ == "__main__":  # simple CLI smoke test
    import sys

    ok = True
    try:
        test_pass()
    except AssertionError as e:
        ok = False
        print("❌ FAIL")
        print(e)
    except Exception as e:
        ok = False
        print("❌ ERROR")
        print(e)
    if ok:
        print("✅ PASS")
    in_ipy = bool(getattr(sys, "ps1", None)) or "ipykernel" in sys.modules
    if not in_ipy:
        sys.exit(0 if ok else 1)

    print("✅PASS" if ok else "❌FAIL")

    # avoid SystemExit in Spyder/IPython, but keep exit code in normal Python runs
    in_ipy = bool(getattr(sys, "ps1", None)) or "ipykernel" in sys.modules
    if not in_ipy:
        sys.exit(0 if ok else 1)
