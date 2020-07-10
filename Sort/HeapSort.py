#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/9 22:58
# @Author  : 一叶知秋
# @File    : HeapSort.py
# @Software: PyCharm
# 堆排序

def heap_sort(arr):
    #  1、无序数组arr
    #  2、将无序数组arr构建为一个大根堆
    length = len(arr)
    for i in range(length // 2 - 1, -1, -1):
        sink(arr, i, length)
    # 3、交换arr[0]和a[len(arr)-1]
    # 4、然后把前面这段数组继续下沉保持堆结构，如此循环即可
    for i in range(length - 1, 0, -1):
        # 从后往前填充值
        arr[0], arr[i] = arr[i], arr[0]
        # 前面的长度也减一
        sink(arr, 0, i)
    return arr


def sink(arr, i, length):
    while True:
        # 左节点索引(从0开始，所以左节点为i * 2 + 1)
        left = i * 2 + 1
        # 右节点索引
        right = i * 2 + 2
        # idx保存根、左、右三者之间较大值的索引
        idx = i
        # 存在左节点，左节点值较大，则取左节点
        if left < length and arr[left] > arr[idx]:
            idx = left
        # 存在有节点，且值较大，取右节点
        if right < length and arr[right] > arr[idx]:
            idx = right
        # 如果根节点较大，则不用下沉
        if idx == i:
            break
        # 如果根节点较小，则交换值，并继续下沉
        arr[i], arr[idx] = arr[idx], arr[i]
        # 继续下沉idx节点
        i = idx


if __name__ == '__main__':
    a = [7, 6, 8, 5, 2, 1, 3, 4, 0, 9, 10]
    print(a)
    print(heap_sort(a))
