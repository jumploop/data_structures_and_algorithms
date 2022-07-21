from typing import List


class Solution:
    # 寻找右侧边界的二分搜索
    def right_bound(self, nums: List[int], target: int) -> int:
        # write code here
        if len(nums) == 0:
            return -1
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
        return left - 1

    def right_bound2(self, nums: List[int], target: int) -> int:
        # write code here
        left, right = 0, len(nums) - 1
        # 搜索区间为 [left, right]
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                # 这里改成收缩左侧边界即可
                left = mid + 1
            elif nums[mid] > target:
                # 搜索区间变为 [left, mid-1]
                right = mid - 1
            elif nums[mid] < target:
                # 搜索区间变为 [mid+1, right]
                left = mid + 1
        # 这里改为检查 right 越界的情况，见下图
        if right < 0 or nums[right] != target:
            return -1
        return right

if __name__ == '__main__':
    solution = Solution()
    print(solution.right_bound([1, 2, 2, 2, 4], 2))
