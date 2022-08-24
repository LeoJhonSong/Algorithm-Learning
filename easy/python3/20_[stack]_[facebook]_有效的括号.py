#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
pairs = {
    '(': ')',
    '{': '}',
    '[': ']'
}


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for token in s:
            if token in list(pairs.keys()):
                stack.append(token)
            else:
                try:
                    if token == pairs[stack[-1]]:
                        stack.pop()
                    else:
                        # 括号不匹配
                        return False
                except IndexError:
                    # 有多的右括号
                    return False
        return True if len(stack) == 0 else False
# @lc code=end

