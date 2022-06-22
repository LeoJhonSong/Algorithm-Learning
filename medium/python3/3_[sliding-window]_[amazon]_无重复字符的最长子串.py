# @before-stub-for-debug-begin
from python3problem3 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 维护变量
        max_len = 0
        head, tail = 0, 0
        while tail <= len(s):
            window = s[head:tail]
            if len(window) == len(set(window)):
                max_len = max(max_len, len(window))
                tail += 1
            else:
                head = head + window.index(window[-1]) + 1
        return max_len
# @lc code=end
