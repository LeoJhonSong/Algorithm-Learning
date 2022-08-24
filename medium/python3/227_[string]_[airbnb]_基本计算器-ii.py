#
# @lc app=leetcode.cn id=227 lang=python3
#
# [227] 基本计算器 II
#

# @lc code=start

# 优先级图省事依据cppreference设置
operators = {
    '*': {
        'precedence': 5,
        'operation': lambda x, y: x * y
    },
    '/': {
        'precedence': 5,
        'operation': lambda x, y: int(x / y)
    },
    '+': {
        'precedence': 6,
        'operation': lambda x, y: x + y
    },
    '-': {
        'precedence': 6,
        'operation': lambda x, y: x - y
    }
}


class Solution:
    def calculate(self, s: str) -> int:
        # 将s解析为中缀表达式列表
        s = s.replace(' ', '')
        for token in list(operators.keys()):
            s = s.replace(token, f' {token} ')
        tokens = s.split(' ')
        # 中缀表达式转换为逆波兰表达式
        operator_stack = []
        rpn_stack = []
        for token in tokens:
            if token in list(operators.keys()):
                try:
                    # 将运算符栈的栈顶运算符弹出压到逆波兰表达式栈, 直到当前token优先级高于运算符栈栈顶运算符的
                    while operators[token]['precedence'] >= operators[operator_stack[-1]]['precedence']:
                        rpn_stack.append(operator_stack.pop())
                    operator_stack.append(token)
                except IndexError:
                    # 最后一个token不可能是运算符, 因此运算符栈空了直接把当前token直接加入运算符栈继续运算
                    operator_stack.append(token)
            else:
                rpn_stack.append(token)
        # 将运算符栈所有运算符依次压到逆波兰表达式栈
        for i in range(len(operator_stack)):
            rpn_stack.append(operator_stack.pop())
        # 计算逆波兰表达式
        stack = []
        for token in rpn_stack:
            if token in list(operators.keys()):
                stack = stack[:-2] + [str(operators[token]['operation'](int(stack[-2]), int(stack[-1])))]
            else:
                stack.append(token)
        return int(stack[-1])
# @lc code=end
