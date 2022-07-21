#!/usr/bin/env python
# -*- coding: utf-8 -*-
def fib(n):
    # base case
    if n == 0 or n == 1:
        return n
    # 递推关系
    prev, cur = 0, 1
    for i in range(2, n + 1):
        prev, cur = cur, prev + cur
    return cur


def fib2(n):
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)


def fib3(n):
    memo = {}
    return helper(memo, n)


def helper(memo, n):
    if n == 0 or n == 1:
        return n
    # 已经计算过，不用再计算了
    if n in memo:
        return memo[n]
    memo[n] = helper(memo, n - 1) + helper(memo, n - 2)
    return memo[n]


if __name__ == '__main__':
    print(fib(4))
    print(fib2(4))
    print(fib3(4))
