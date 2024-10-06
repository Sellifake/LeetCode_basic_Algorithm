class multi_less_k:
    def sliding_window(nums, target):
        if target <= 1:
            return 0
        n = len(nums)
        left = 0
        ans = 0 
        multi = 1
        for right in range(n):
            multi *= nums[right]
            while multi >= target:
                multi /= nums[left]
                left += 1
            ans += right - left + 1
        return ans

nums = [10,5,2,6]
target = 100
print(multi_less_k.sliding_window(nums, target))
