class max_element_k:
    def solution(nums, k):
        max_ele = max(nums)
        ans = left = count = 0
        for x in nums:
            if x == max_ele:
                count += 1
            while count == k:
                if nums[left] == max_ele:
                    count -= 1
                left += 1
            ans += left
        return ans

nums = [1,3,2,3,3]
k = 2
print(max_element_k.solution(nums, k))