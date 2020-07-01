#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/1 11:53
# @Author  : 一叶知秋
# @File    : MinStack.py
# @Software: PyCharm
"""
155. 最小栈
设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) —— 将元素 x 推入栈中。
pop() —— 删除栈顶的元素。
top() —— 获取栈顶元素。
getMin() —— 检索栈中的最小元素。


示例:

输入：
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

输出：
[null,null,null,null,-3,null,0,-2]

解释：
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.


提示：

pop、top 和 getMin 操作总是在 非空栈 上调用。
"""


# 思路：用两个栈实现，一个最小栈始终保证最小值在顶部
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = []
        self.stack = []

    def push(self, x: int) -> None:
        min = self.getMin()
        if x < min:
            self.min.append(x)
        else:
            self.min.append(min)
        self.stack.append(x)

    def pop(self) -> None:
        if not self.stack:
            return
        self.stack = self.stack[:len(self.stack) - 1]
        self.min = self.min[:len(self.min) - 1]

    def top(self) -> int:
        if not self.stack:
            return 0
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        if len(self.min) == 0:
            return 1 << 31
        min = self.min[len(self.min) - 1]
        return min

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
