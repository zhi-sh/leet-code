#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        ret = res = ListNode(0)
        while (l1 is not None or l2 is not None):
            x = l1.val if l1 is not None else 0
            y = l2.val if l2 is not None else 0
            sums = carry + x + y
            carry = sums // 10
            res.next = ListNode(sums % 10)
            res = res.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry > 0:
            res.next = ListNode(carry)
        return ret.next
# @lc code=end
