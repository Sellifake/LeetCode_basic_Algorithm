class max_beauty:
    def solution1(nums, k):
        nums.sort()
        left = ans = 0
        for right in range(len(nums)):
            while nums[right] - nums[left] > 2 * k:
                left += 1
            ans = max(ans, right - left + 1)
        return ans

nums = [4,6,1,2]
k = 2
print(max_beauty.solution1(nums, k))
