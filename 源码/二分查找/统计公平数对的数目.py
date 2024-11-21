from bisect import bisect_left, bisect_right


class countFairPairs:
    def solution1(nums, lower, upper):
        nums.sort()
        ans = 0
        for index, x in enumerate(nums):
            left = bisect_left(nums, lower - x, index)
            right = bisect_right(nums, upper - x, index)
            ans += right - left
        return ans

nums = [0,1,7,4,4,5]
lower = 3
upper = 6
print(countFairPairs.solution1(nums, lower, upper))