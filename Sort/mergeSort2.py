#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/9 22:41
# @Author  : 一叶知秋
# @File    : mergeSort2.py
# @Software: PyCharm

def merge_sort(arr):
    def merge(left, right):
        result = []
        while left and right:
            result.append((left if left[0] <= right[0] else right).pop(0))
        return result + left + right

    length = len(arr)
    if length < 2:
        return arr
    mid = length >> 1
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    result = merge(left, right)
    return result


if __name__ == '__main__':
    a = [7, 6, 8, 5, 2, 1, 3, 4, 0, 9, 10]
    print(a)
    print(merge_sort(a))
