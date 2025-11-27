# =================================================================================================
# Problem: 0001. Two Sum
# Link: https://leetcode.com/problems/two-sum/
# Tags: Array, Hash Table
# Complexity: O(n) / O(n)
#
# Task: Return indices of the 2 numbers in a given integer array (nums) that add up to a target.
# Hints:
# (1) Assume there is only 1 sol, can't use the same element twice, can return in any order.
# (2) 2 <= nums.length <= 10e4, -10e9 <= nums[i] <= 10e9, -10e9 <= target <= 10e9
# Ex: nums = [3, 2, 5, 6, 5], target = 7 --> ans = [1, 2]


# =================================================================================================
# Solution:
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """Hash map using enum: O(n) / O(1)"""
        seen: dict[int, int] = {}  # keep a reversed dict for O(1) lookup
        for i, x in enumerate(nums):
            y = target - x
            if y in seen:
                return [seen[y], i]
            seen[x] = i
        return []  # just in case if n = 0 or no sol

    def twoSum_brute(self, nums: list[int], target: int) -> list[int]:
        """Brute force: O(n^2) / O(1)"""
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                # print(i, j)
                if (nums[i] + nums[j]) == target:
                    return [i, j]
        return []  # if no sol


# =================================================================================================
# BigO:
# Time: n loops x (dict_lookup + dict_insert + subtraction + comparison) = n x (1+1+1+1) = O(n)
# Space: Stores up to n key->index pairs --> O(n)

# =================================================================================================
# Testing:
CASES = [  # [(args, expect)]  — can be a tuple of inputs or a single value
    (([2, 7, 11, 15], 9), [0, 1]),  # Example 1
    (([3, 2, 4], 6), [1, 2]),  # Example 2
    (([3, 3], 6), [0, 1]),  # Example 3
    # Edge cases
    (([1, 2], 3), [0, 1]),  # minimal length
    (([1, 2, 3, 4, 5], 10), []),  # no valid pair
    (([-1, -2, -3, -4, -5], -8), [2, 4]),  # negative values
    (([0, 4, 3, 0], 0), [0, 3]),  # zero sum
    (([1, 1, 1, 1], 2), [0, 1]),  # repeated values
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

# Fallback primitive test if CLI test fails
# nums = [2, 7, 11, 15]
# target = 18
# sol = Solution()
# print(sol.twoSum(nums, target))
# print(sol.twoSum_brute(nums, target))
