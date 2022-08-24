#
# @lc app=leetcode.cn id=875 lang=python3
#
# [875] 爱吃香蕉的珂珂
# 此处二分法用双指针实现
#

# @lc code=start
from math import ceil


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while True:
            mid = (left + right) // 2
            if left + 1 == right:
                return left if sum([ceil(p / left) for p in piles]) <= h else right
            if sum([ceil(p / mid) for p in piles]) <= h:
                right = mid
            else:
                left = mid
# @lc code=end
