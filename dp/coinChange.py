#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
凑零钱问题

322. 零钱兑换

给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。

计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。

你可以认为每种硬币的数量是无限的。

 

示例 1：

输入：coins = [1, 2, 5], amount = 11
输出：3
解释：11 = 5 + 5 + 1
示例 2：

输入：coins = [2], amount = 3
输出：-1
示例 3：

输入：coins = [1], amount = 0
输出：0

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/coin-change
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        meme = {}

        # 题目要求的最终结果是 dp(amount)
        def dp(coins, amount, meme):
            # 定义：要凑出金额 n，至少要 dp(coins, n) 个硬币
            # base case
            if amount == 0:
                return 0
            if amount < 0:
                return -1
            if amount in meme:
                return meme[amount]
            res = float('inf')
            for coin in coins:
                # 计算子问题的结果
                subProblem = dp(coins, amount - coin, meme)
                # 子问题无解则跳过
                if subProblem == -1:
                    continue
                # 在子问题中选择最优解，然后加一
                res = min(res, subProblem + 1)
            meme[amount] = -1 if res == float('inf') else res
            return meme[amount]

        return dp(coins, amount, meme)


if __name__ == '__main__':
    s = Solution()
    print(s.coinChange(coins=[1, 2, 5], amount=11))
