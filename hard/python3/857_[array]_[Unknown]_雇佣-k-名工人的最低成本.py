# @before-stub-for-debug-begin
from python3problem857 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=857 lang=python3
#
# [857] 雇佣 K 名工人的最低成本
#


# @lc code=start
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        # 一些预处理
        rate = list(map(lambda w, q: w / q, wage, quality))
        pair = sorted(list(zip(rate, quality, wage)), key=lambda item: item[0])  # 按rate从小到大
        # 从第k-1项开始遍历, 直到结束
        total_w_list = []
        for i in range(k - 1, len(rate)):
            highest = pair[i]
            q_rest = [item[1] for item in sorted(pair[:i], key=lambda item: item[1])[:k - 1]]
            total_q = sum(q_rest + [highest[1]])
            total_w_list.append(total_q * highest[0])
        return min(total_w_list)

# @lc code=end
