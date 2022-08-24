#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] 逆波兰表达式求值
#

# @lc code=start


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ['+', '-', '*']:
                stack = stack[:-2] + [str(eval(stack[-2] + token + stack[-1]))]
            elif token == '/':
                stack = stack[:-2] + [str(int(eval(stack[-2] + '/' + stack[-1])))]
            else:
                stack.append(token)
        return int(stack[-1])
# @lc code=end
