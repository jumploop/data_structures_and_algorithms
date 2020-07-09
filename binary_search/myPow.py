#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/9 8:38
# @Author  : 一叶知秋
# @File    : myPow.py
# @Software: PyCharm
"""
50. Pow(x, n)
实现 pow(x, n) ，即计算 x 的 n 次幂函数。

示例 1:

输入: 2.00000, 10
输出: 1024.00000
示例 2:

输入: 2.10000, 3
输出: 9.26100
示例 3:

输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25
说明:

-100.0 < x < 100.0
n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x ** n

    def myPow2(self, x: float, n: int) -> float:
        if x == 0.0:
            return 0.0
        res = 1
        if n < 0:
            x, n = 1 / x, -n
        while n:
            if n & 1:
                res *= x
            x *= x
            n >>= 1
        return res

        #  算法流程：
        # 1.当 x = 0.0 时：直接返回 0.0 ，以避免后续 1 除以 0 操作报错。分析： 数字 0 的正数次幂恒为 0 ； 0 的 0 次幂和负数次幂没有意义，因此直接返回 0.0 即可。
        # 2.初始化 res = 1 。
        # 3.当 n < 0 时：把问题转化至 n≥0 的范围内，即执行 x = 1/x ，n = - n 。
        # 4.循环计算：当 n = 0时跳出。
        #   当 n&1=1 时：将当前 x 乘入 res （即 res *= x）。
        #   执行 x = x^2 （即 x *= x）。
        #   执行 n 右移一位（即 n >>= 1）。
        # 5.返回 res。
        #
        # 作者：jyd
        # 链接：https://leetcode-cn.com/problems/powx-n/solution/50-powx-n-kuai-su-mi-qing-xi-tu-jie-by-jyd/
        # 来源：力扣（LeetCode）
        # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


if __name__ == '__main__':
    x = 2
    n = 3
    print(Solution().myPow2(x, n))
