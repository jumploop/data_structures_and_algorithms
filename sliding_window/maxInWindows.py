#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
BM45 滑动窗口的最大值

描述
给定一个长度为 n 的数组 nums 和滑动窗口的大小 size ，找出所有滑动窗口里数值的最大值。

例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}； 针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个： {[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}， {2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。

数据范围： 1 \le size \le n \le 100001≤size≤n≤10000，数组中每个元素的值满足 |val| \le 10000∣val∣≤10000
要求：空间复杂度 O(n)O(n)，时间复杂度 O(n)O(n)

"""
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param num int整型一维数组
# @param size int整型
# @return int整型一维数组
#
from typing import List


class Solution:

    def maxInWindows(self, num: List[int], size: int) -> List[int]:
        # write code here
        res = []
        #窗口大于数组长度的时候，返回空
        if size <= len(num) and size != 0:
            from collections import deque
            #双向队列
            dq = deque()
            #先遍历一个窗口
            for i in range(size):
                #去掉比自己先进队列的小于自己的值
                while len(dq) != 0 and num[dq[-1]] < num[i]:
                    dq.pop()
                dq.append(i)
            #遍历后续数组元素
            for i in range(size, len(num)):
                res.append(num[dq[0]])
                while len(dq) != 0 and dq[0] < (i - size + 1):
                    #弹出窗口移走后的值
                    dq.popleft()
                #加入新的值前，去掉比自己先进队列的小于自己的值
                while len(dq) != 0 and num[dq[-1]] < num[i]:
                    dq.pop()
                dq.append(i)
            res.append(num[dq[0]])
        return res
