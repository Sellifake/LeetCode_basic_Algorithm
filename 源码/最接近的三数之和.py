class nearestSum:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target
    
    def solution(self):
        self.nums.sort()
        difference = float('inf')

        for i in range(len(self.nums) - 2):
            
            if i > 0 and self.nums[i] == self.nums[i - 1]:
                continue

            left = i + 1
            right = len(self.nums) - 1

            max_sum = self.nums[i] + self.nums[right] + self.nums[right - 1]
            if max_sum < self.target and abs(max_sum - self.target) > abs(difference):
                continue

            min_sum = self.nums[i] + self.nums[i + 1] + self.nums[i + 2]
            if min_sum > self.target and abs(min_sum - self.target) > difference:
                break

            while left < right:

                sum = self.nums[i] + self.nums[left] + self.nums[right]
                if sum == self.target:
                    return self.target

                if abs(sum - self.target) < difference:
                    difference = abs(sum - self.target)
                    ans = sum 
                if sum < self.target:
                    left += 1
                else:
                    right -= 1
        return ans


nums = [1, 1, 1, 0]
target = -100
nearestSum = nearestSum(nums, target)
print(nearestSum.solution())
