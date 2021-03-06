#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/1 14:50
# @Author  : 一叶知秋
# @File    : evalRPN.py
# @Software: PyCharm
"""
150. 逆波兰表达式求值
根据 逆波兰表示法，求表达式的值。

有效的运算符包括 +, -, *, / 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。



说明：

整数除法只保留整数部分。
给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。


示例 1：

输入: ["2", "1", "+", "3", "*"]
输出: 9
解释: 该算式转化为常见的中缀算术表达式为：((2 + 1) * 3) = 9
示例 2：

输入: ["4", "13", "5", "/", "+"]
输出: 6
解释: 该算式转化为常见的中缀算术表达式为：(4 + (13 / 5)) = 6
示例 3：

输入: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
输出: 22
解释:
该算式转化为常见的中缀算术表达式为：
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22


逆波兰表达式：

逆波兰表达式是一种后缀表达式，所谓后缀就是指算符写在后面。

平常使用的算式则是一种中缀表达式，如 ( 1 + 2 ) * ( 3 + 4 ) 。
该算式的逆波兰表达式写法为 ( ( 1 2 + ) ( 3 4 + ) * ) 。
逆波兰表达式主要有以下两个优点：

去掉括号后表达式无歧义，上式即便写成 1 2 + 3 4 + * 也可以依据次序计算出正确结果。
适合用栈操作运算：遇到数字则入栈；遇到算符则取出栈顶两个数字进行计算，并将结果压入栈中。
"""
from typing import List


# 思路：通过栈保存原来的元素，遇到表达式弹出运算，再推入结果，重复这个过程
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        symbol = ["+", "-", "*", "/"]
        stack = []
        if len(tokens) == 0:
            return 0
        for token in tokens:
            if token in symbol:
                if len(stack) < 2:
                    return -1
                # 注意：a为除数，b为被除数
                b = stack[len(stack) - 1]
                a = stack[len(stack) - 2]
                stack = stack[:len(stack) - 2]
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    stack.append(int(a / b))
            else:
                stack.append(int(token))
        return stack[0]

    def evalRPN2(self, tokens: List[str]) -> int:
        def comp(or1, op, or2):
            if op == '+':
                return or1 + or2

            if op == '-':
                return or1 - or2

            if op == '*':
                return or1 * or2

            if op == '/':
                abs_result = abs(or1) // abs(or2)
                return abs_result if or1 * or2 > 0 else -abs_result

        stack = []
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                or2 = stack.pop()
                or1 = stack.pop()
                stack.append(comp(or1, token, or2))
            else:
                stack.append(int(token))

        return stack[0]

    def evalRPN3(self, tokens: List[str]) -> int:

        symbol = ["+", "-", "*", "/"]
        recList = []

        if len(tokens) == 0:
            return 0
        else:
            for c in tokens:
                if c not in symbol:
                    recList.append(c)
                else:
                    b = int(recList.pop())
                    a = int(recList.pop())
                    if c == "+":
                        recList.append(str(a + b))
                    elif c == "-":
                        recList.append(str(a - b))
                    elif c == "*":
                        recList.append(str(a * b))
                    elif c == "/":
                        recList.append(str(int(a / b)))
            return int(recList[0])


if __name__ == '__main__':
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    print(Solution().evalRPN(tokens))
