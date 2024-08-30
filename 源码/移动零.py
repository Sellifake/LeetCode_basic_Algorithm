class MoveZero:
    def __init__(self, nums):
        self.nums = nums

    # 逆向思维，将非零元素移动到前面，count用来记录非零元素应该移动到的位置
    def solution1(nums):
        count = 0
        for i in range(len(nums)):
            if nums[i] :
                nums[count], nums[i] = nums[i], nums[count]
                count += 1
        return nums

    # 双指针法,实际上原理和逆向思维一样，只不过用两个指针来记录位置
    def solution2(nums):
        i = 0
        j = 0
        while j < len(nums):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
        return nums
    # 时间复杂度均为O(n)
    # 空间复杂度均为O(1)


num = [1, 2, 0, 1]
move = MoveZero(num)