class most_contain():
    def __init__(self, nums):
        self.nums = nums
    
    def max_area(self):
        num = self.nums
        left = 0 
        right = len(num) - 1
        max_area = 0

        while left < right:
            cur_area = min(num[left, num[right]]) * (right - left)
            max_area = max(max_area, cur_area)
            if num[left] < num[right]:
                left += 1
            else:
                right -= 1