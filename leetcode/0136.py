# =================================================================================================
# Problem: 0136. Single Number
# Link: https://leetcode.com/problems/single-number
# Tags: Bits
# Complexity: O(n) / O(1)
#
# Task: Return the only number in a non-empty array of integers that does not appeat twice.
#
# Hints:
# (1) 1 <= nums.length <= 3 * 104
# (2) -3 * 104 <= nums[i] <= 3 * 104


# =================================================================================================
# Solution:
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        """Hashset approach | O(n) / O(1)"""
        n = len(nums)
        if n == 1:
            return nums[0]
        else:
            dic = {}
            for i in nums:
                if i not in dic:  # O(1) look up
                    dic[i] = 1  # mark it as 1 (found)
                else:
                    del dic[i]  # delete the whole key (don't inc count)

        ans = list(dic.keys())[0]  # so the remaning item will be the single number
        return ans

    def singleNumber2(self, nums: list[int]) -> int:
        """XOR approach | O(n) / O(1)"""
        res = 0  # accumulator
        for x in nums:
            res = res ^ x  # every duplicate cancels itself because XOR(a,a) = 0
        return res


# =================================================================================================
# Complexity:
# Time: n x (lookup + add/del) = n x (1+1) --> O(n)
# Space: 1 integer accumulator --> O(1)

# =================================================================================================
# Testing:
# Simple test:
sol = Solution()
sol.singleNumber([1, 3, 2, 3, 1])
sol.singleNumber2([1, 3, 2, 3, 1])

# Batch test:
CASES = [
    ([2, 2, 1], 1),
    ([4, 1, 2, 1, 2], 4),
    ([1], 1),
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
            # print(expect, got)
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
