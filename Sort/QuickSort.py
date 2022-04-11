#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/9 19:34
# @Author  : 一叶知秋
# @File    : QuickSort.py
# @Software: PyCharm
# 快速排序

# 思路：把一个数组分为左右两段，左段小于右段
import random


def quick_sort(arr):
    length = len(arr)
    if length < 2:
        return arr
    pivot_idx = random.randint(0, len(arr) - 1)
    pivot = arr.pop(pivot_idx)  # 递归条件,基准值
    less = [i for i in arr if i <= pivot]  # 由所有小于基准值的元素组成的子数组
    greater = [i for i in arr if i > pivot]  # 由所有大于基准值的元素组成的子数组
    return quick_sort(less) + [pivot] + quick_sort(greater)


if __name__ == '__main__':
    a = [7, 6, 8, 5, 2, 1, 3, 4, 0, 9, 10]
    print(a)
    print(quick_sort(a))
