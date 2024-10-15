class max_ones_III():
    def solution1(nums, k):
        left = ans = count = 0
        for right, x in enumerate(nums):
            count += 1 - x
            while count > k:
                count -= 1- nums[left]
                left += 1
            ans = max(ans, right - left + 1)
        return ans

nums = [1,1,1,0,0,0,1,1,1,1,0]
K = 2
print(max_ones_III.solution1(nums, K))
