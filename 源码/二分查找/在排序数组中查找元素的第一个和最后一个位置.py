class binary_search:
    def solution1(nums, target):
        # 暴力做法
        start = end = -1
        for i in range(len(nums)):
            if nums[i] == target:
                end = i 
                if start == -1:
                    start = i        
        return [start, end]
    
    def solution2(nums, target):
        # 二分查找
        left, right = 0, len(nums) - 1 # 闭区间[left, right]
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1 # [mid + 1, right]
            else:
                right = mid - 1 # [left, mid - 1]
        return left

nums = [5,7,7,8,8,10]
target = 8
start = binary_search.solution2(nums, target)
if start == len(nums) or nums[start] != target:
    start = -1
end = binary_search.solution2(nums, target - 1)
# return [start, end]