class minimum_operations:
    def solution1(nums, x):
        target = sum(nums) - x
        if target < 0:
            return -1
        left = s = 0
        ans  = -1
        n = len(nums)
        for right, val in enumerate(nums):
            s += val
            while s > target:
                s -= nums[left]
                left += 1
            if s == target:
                ans = max(ans, right - left + 1)
        return -1 if ans < 0 else n - ans