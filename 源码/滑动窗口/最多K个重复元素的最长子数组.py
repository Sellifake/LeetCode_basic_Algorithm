from collections import Counter


class Solution:
    def maxSubarrayLength(nums, k):
        ans = left = 0
        cnt = Counter()
        for right, x in enumerate(nums):
            cnt[x] += 1
            while cnt[x] > k:
                cnt[nums[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans

nums = [1,2,1,2,1]
k = 2
Solution.maxSubarrayLength(nums,k)
