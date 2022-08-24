#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        s = 0
        while True:
            s = max(s, (right - left) * min(height[left], height[right]))
            if left + 1 == right:
                return s
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
# @lc code=end
