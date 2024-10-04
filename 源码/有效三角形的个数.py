class Effective_triangle():
    def __init__(self,nums):
        self.nums = nums
    
    def solution(self):

        ans = 0
        num = self.nums
        num.sort()
        n = len(num)

        for i in range(n-1, 1, -1):
            left = 0
            right = i-1
            while left < right:
                if num[left] + num[right] > num[i]:
                    ans += right - left
                    right -= 1
                else:
                    left += 1
        return ans
    
nums = [4,2,3,4]
a = Effective_triangle.solution(nums)

print(a.solution())

