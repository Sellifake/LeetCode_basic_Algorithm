class twosum_sort_num:

    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    # 两数之和，采用暴力循环的方法
    def Solution1(self):
        for i in range(len(self.nums)):
            for j in range(i+1,len(self.nums)):
                if self.nums[i] + self.nums[j] == self.target:
                    return [i,j]

    # 针对已经排好序的数组，采用双指针的方法
    def Solution2(self):
        i = 0
        j = len(self.nums) - 1
        while i < j:
            if self.nums[i] + self.nums[j] == self.target:
                return [i,j]
            if self.nums[i] + self.nums[j] < self.target:
                i += 1
            else:
                j -= 1
        return None



nums = [2,7,11,15]
target = 9

two_sum = twosum_sort_num(nums, target)
print(two_sum.Solution2())
