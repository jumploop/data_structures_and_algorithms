"""
给你一个非负整数 x ，计算并返回 x 的 算术平方根 。

由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。

注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。

"""


class Solution:
    def mySqrt(self, x: int) -> int:
        # 注意边界 0, 1
        left = 0
        right = x // 2 + 1
        # 根据上面的公式进行计算
        # 开始进行二分查找
        while left < right:
            # 取中间值
            # 这里要取右中间值，不然会进入死循环
            mid = (left + right + 1) // 2
            square = mid * mid
            if square == x:
                return mid
            elif square > x:
                right = mid - 1
            else:
                left = mid
        return left

    def mySqrt2(self, x: int) -> int:
        # 注意边界 0, 1
        left = 0
        right = x
        # 根据上面的公式进行计算
        # 开始进行二分查找
        while left <= right:
            # 取中间值
            # 这里要取右中间值，不然会进入死循环
            mid = (left + right) // 2
            square = mid * mid
            if square == x:
                return mid
            elif square > x:
                right = mid - 1
            else:
                left = mid + 1
        return right