# @before-stub-for-debug-begin
from python3problem2 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1 = ''
        s2 = ''
        while True:
            s1 += str(l1.val)
            if l1.next is None:
                break
            l1 = l1.next
        while True:
            s2 += str(l2.val)
            if l2.next is None:
                break
            l2 = l2.next
        s3 = str(int(s1[::-1]) + int(s2[::-1]))
        s3 = s3[::-1]  # reversed to order for link
        ret = ListNode(val=int(s3[0]))
        end = ret
        for s in s3[1:]:
            end.next = ListNode(val=int(s))
            end = end.next
        return ret
# @lc code=end
