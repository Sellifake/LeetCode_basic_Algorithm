class less_than_target():
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def solution1(self):
        self.nums.sort()
        left = 0
        right = len(nums) - 1
        count = 0
        while left < right:
            if self.nums[left] + self.nums[right] < self.target:
                count += right - left
                left += 1
            else:
                right -= 1
        return count

nums = [-6,2,5,-2,-7,-1,3]
target = -2

less_than_target = less_than_target(nums, target)
print(less_than_target.solution1())