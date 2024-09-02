class two_sum:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target
    # 采用哈希表的形式
    def Solution1(self):
        hashmap = {}
        for i, num in enumerate(self.nums):
            if self.target - num in hashmap:
                return [hashmap[self.target - num], i]
            hashmap[num] = i
        return []
# 时间复杂度O(n),空间复杂度O(n)

nums = [2,7,11,15]
target = 22


two_sum = two_sum(nums, target)
print(two_sum.Solution1())