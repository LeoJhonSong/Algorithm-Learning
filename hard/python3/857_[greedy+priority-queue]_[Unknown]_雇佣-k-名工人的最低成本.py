# @before-stub-for-debug-begin
from python3problem857 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=857 lang=python3
#
# [857] 雇佣 K 名工人的最低成本
#
from math import inf
from heapq import heappush, heappop


# @lc code=start
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        # 一些预处理
        rate = list(map(lambda w, q: w / q, wage, quality))
        pairs = sorted(list(zip(rate, quality)), key=lambda item: item[0])  # 按rate从小到大
        total_q = 0
        h = []  # 用于维护优先队列的堆, 更多见: https://docs.python.org/zh-cn/3/library/heapq.html
        ret = inf
        # 先默认使用前k-1项,非最后一项项只影响total_q
        for _, q in pairs[:k - 1]:
            total_q += q
            heappush(h, -q)
        for r, q in pairs[k - 1:]:
            total_q += q
            heappush(h, -q)
            ret = min(ret, total_q * r)  # 更新总工资
            total_q += heappop(h)  # 弹出最小元素, 即最大q, 保持total_q最小
        return ret
# @lc code=end
