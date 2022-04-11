#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/9 22:09
# @Author  : 一叶知秋
# @File    : mergeSort.py
# @Software: PyCharm
# 归并排序

def merge_sort(arr):
    length = len(arr)
    if length < 2:
        return arr
    # 分治法：divide 分为两段
    mid = length // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    # 两边数组合并游标
    l, r = 0, 0
    while l < len(left) and r < len(right):
        # 谁小合并谁
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    # 剩余部分合并
    result.extend(left[l:])
    result.extend(right[r:])
    return result


if __name__ == '__main__':
    a = [7, 6, 8, 5, 2, 1, 3, 4, 0, 9, 10]
    print(a)
    print(merge_sort(a))
