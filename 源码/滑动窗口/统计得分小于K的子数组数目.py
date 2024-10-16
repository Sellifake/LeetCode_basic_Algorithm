class subarray_Scores_less_than_k:
    def solution1(nums, k):
        ans = s = left = 0
        for right, num in enumerate(nums):
            s += num
            while s * (right - left + 1) >= k:
                s -= nums[left]
                left += 1
            ans += right - left + 1
        return ans
    
nums = [2,1,4,3,5]
k = 10
print(subarray_Scores_less_than_k.solution1(nums, k))