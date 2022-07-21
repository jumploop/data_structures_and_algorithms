"""
150. 逆波兰表达式求值

根据 逆波兰表示法，求表达式的值。

有效的算符包括 +、-、*、/ 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。

注意 两个整数之间的除法只保留整数部分。

可以保证给定的逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/evaluate-reverse-polish-notation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    def evalRPN(self, tokens: List[str]) -> int:

        def comp(num1, num2, op):
            if op == '+':
                return num1 + num2
            if op == '-':
                return num1 - num2
            if op == '*':
                return num1 * num2
            if op == '/':
                abs_result = abs(num1) // abs(num2)
                return abs_result if num1 * num2 > 0 else -abs_result

        stack = []
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(comp(num1, num2, token))
            else:
                stack.append(int(token))
        return stack[0]