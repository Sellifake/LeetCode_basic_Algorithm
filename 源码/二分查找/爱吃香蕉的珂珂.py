class minEatingSpeed:
    def solution1(nums, h):
        n = len(nums)
        left = 1
        right = max(nums)
        while left <= right:
            mid = (left + right) // 2
            if sum((p - 1) // mid for p in nums) <= h - n:
                right = mid - 1
            else:
                left = mid + 1
        return left

