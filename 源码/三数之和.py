class threeSum:
    def __init__(self, nums):  
        self.nums = nums
    
    def solution1(self):
        self.nums.sort()
        ans = []
        n = len(self.nums)
        for i in range(n - 2):
            if self.nums[i] + self.nums[i + 1] + self.nums[i + 2] > 0:
                break
            if self.nums[i] + self.nums[n - 2] + self.nums[n - 1] < 0:
                continue
            if i > 0 and self.nums[i] == self.nums[i - 1]:
                continue
            j = i + 1
            k = n - 1
            while j < k:
                s = self.nums[i] + self.nums[j] + self.nums[k]
                if s < 0:
                    j += 1
                elif s > 0:
                    k -= 1
                else:
                    ans.append([self.nums[i], self.nums[j], self.nums[k]])
                    j += 1
                    if j < k and self.nums[j] == self.nums[j - 1]:
                       j += 1
                    k -= 1
                    if j < k and self.nums[k] == self.nums[k + 1]:
                        k -= 1
        return ans

nums = [-1, 0, 1, 2, -1, -4]
s = threeSum(nums)
print(s.solution1())
