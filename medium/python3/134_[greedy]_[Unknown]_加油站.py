#
# @lc app=leetcode.cn id=134 lang=python3
#
# [134] 加油站
#

# @lc code=start
from itertools import accumulate  # 默认为前缀和, 可设置为前缀积func=operator.mul


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        n = len(gas)
        diff = [gas[i] - cost[i] for i in range(n)]  # 每次到达一站时油量
        # 方法一: 返回前缀和最小的下一个下标
        prefix = list(accumulate(diff))
        return (prefix.index(min(prefix)) + 1) % n
        # 方法二: 遍历找到
        # total = 0
        # start = 0
        # for i in range(n):
        #     total += diff[i]
        #     if total < 0:
        #         start = i + 1  # 遍历剪枝: https://leetcode.cn/problems/gas-station/solution/jia-you-zhan-by-leetcode-solution/
        #         total = 0
        # return start


# @lc code=end
