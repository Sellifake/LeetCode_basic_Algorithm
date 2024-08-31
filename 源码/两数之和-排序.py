class twosum:

    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    # 两数之和，采用暴力循环的方法
    def Solution1(nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

    # 针对已经排好序的数组，采用双指针的方法
    def Solution2(nums, target):
        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[i] + nums[j] == target:
                return [i,j]
            if nums[i] + nums[j] < target:
                i += 1
            else:
                j -= 1
        return None



nums = [2,7,11,15]
target = 9

two_sum = twosum(nums,target)
print(two_sum.Solution2)
