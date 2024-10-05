class four_sum:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target
    
    def solution(self):
        nums = self.nums
        target = self.target
        nums.sort()
        res = []

        for i in range(len(nums) - 3):  

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break

            if nums[i] + nums[len(nums) - 1] + nums[len(nums) - 2] + nums[len(nums) - 3] < target:
                continue

            for j in range(i + 1, len(nums) - 2):

                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break

                if nums[i] + nums[j] + nums[len(nums) - 1] + nums[len(nums) - 2] < target:
                    continue

                left = j + 1
                right = len(nums) - 1
                while left < right:
                    s = nums[i] + nums[j] + nums[left] + nums[right]
                    if s == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        right -= 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

                    elif s < target:
                        left += 1
                    else:
                        right -= 1
        return res            

nums = [1, 0, -1, 0, -2, 2]
target = 0
a = four_sum(nums, target)
print(a.solution())