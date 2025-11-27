# =================================================================================================
# Problem: 0021. Merge Two Sorted Lists
# Link: https://leetcode.com/problems/merge-two-sorted-lists
# Tags: LL, 2ptr
# Complexity: O(m+n) / O(1)
#
# Task: Given the heads of 2 sorted LLs list1 and list2, merge them into 1 sorted list by splicing
# together the nodes of the 2 lists. Return the head of the merged linked list.
# Hints:
# (1) -100 <= Node.val <= 100
# (2) The number of nodes in both lists is in the range [0, 50]
# (3) Optional[T] = Union[T, None] --> value can either be of type T or None --> test for None


# =================================================================================================
# Solution:
class ListNode:
    """Definition for singly-linked list."""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # If either lists is None or empty, return the other
        if not list1 or not list2:
            return list1 or list2

        merged = ListNode()  # original pointer to return the head when merger is complete
        merged_aux = merged  # aux pointer to the same head, just to fill the merged LL
        while list1 and list2:  # until one of the list is finished
            if list1.val < list2.val:  # attach smaller node
                merged_aux.next = list1
                list1 = list1.next  #  to next node
            else:
                merged_aux.next = list2
                list2 = list2.next
            merged_aux = merged_aux.next  # advance aux pointer

        merged_aux.next = list1 or list2  # appends all remaining nodes of the longer list
        # Now merged_aux is pointing to the tail node while merged still points to the head

        return merged.next  # we obtain the head


# =================================================================================================
# Testing:
CASES = [
    ([], [], []),
    ([], [0], [0]),
    ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
    ([1, 2, 4], [1, 3, 4, 5, 6], [1, 1, 2, 3, 4, 4, 5, 6]),
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
