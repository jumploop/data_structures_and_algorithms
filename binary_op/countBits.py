#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/6 13:47
# @Author  : 一叶知秋
# @File    : countBits.py
# @Software: PyCharm
"""
338. 比特位计数
给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。

示例 1:

输入: 2
输出: [0,1,1]
示例 2:

输入: 5
输出: [0,1,1,2,1,2]
进阶:

给出时间复杂度为O(n*sizeof(integer))的解答非常容易。但你可以在线性时间O(n)内用一趟扫描做到吗？
要求算法的空间复杂度为O(n)。
你能进一步完善解法吗？要求在C++或任何其他语言中不使用任何内置函数（如 C++ 中的 __builtin_popcount）来执行此操作。
"""
from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        result = []
        for n in range(num + 1):
            count = bin(n).count('1')
            result.append(count)
        return result

    def countBits2(self, num: int) -> List[int]:
        """
        动态规划
        """
        dp = [0] * (num + 1)
        for i in range(1, num + 1):
            if (i % 2 == 1):
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = dp[i // 2]
        return dp

    # 由二进制的两条性质得到递推公式：
    # dp[i]={ dp[i−1]+1
    #       { dp[i//2]
    # i为奇数
    # i为偶数
    # ​
    # i为奇数
    # i为偶数
    # 复杂度分析
    # 时间复杂度：O(n)O(n)
    # 空间复杂度：O(n)O(n)

    def countBits3(self, num: int) -> List[int]:
        result = []
        for i in range(num + 1):
            result.append(self.count(i))
        return result

    def count(self, n):
        count = 0
        while n != 0:
            n = n & (n - 1)
            count += 1
        return count

    def countBits4(self, num: int) -> List[int]:
        dp = [0] * (num + 1)
        for i in range(1, num + 1):
            # 上一个缺1的元素+1即可
            dp[i] = dp[i & (i - 1)] + 1
        return dp

if __name__ == '__main__':
    n = 13
    print(Solution().countBits(n))
    print(Solution().countBits2(n))
    print(Solution().countBits3(n))
    print(Solution().countBits4(n))
