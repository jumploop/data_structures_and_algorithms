from typing import List


class Solution:
    # 寻找左侧边界的二分搜索
    def left_bound(self, nums: List[int], target: int) -> int:
        # write code here
        if len(nums) == 0:
            return -1
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                right = mid
            elif nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
        return left

    def left_bound2(self, nums: List[int], target: int) -> int:
        # write code here
        left, right = 0, len(nums) - 1
        # 搜索区间为 [left, right]
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                # 收缩右侧边界
                right = mid - 1
            elif nums[mid] > target:
                # 搜索区间变为 [left, mid-1]
                right = mid - 1
            elif nums[mid] < target:
                # 搜索区间变为 [mid+1, right]
                left = mid + 1
        # 检查出界情况
        if left >= len(nums) or nums[left] != target:
            return -1
        return left


if __name__ == '__main__':
    solution = Solution()
    print(solution.left_bound([1, 2, 2, 2, 4], 2))
