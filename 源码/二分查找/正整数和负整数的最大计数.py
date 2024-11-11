from bisect import bisect_left, bisect_right


class max_pos_or_neg:
    def sloution1(nums):
        pos = neg = 0
        for i, x in enumerate(nums):
            if x > 0:
                pos += 1
            elif x <0:
                neg += 1
        return max(neg, pos)
    
    def solution2(nums):
        def find_max_neg(num):
            left, right = 0, len(nums) - 1
            while left < right:
                mid = (left + right) // 2
                if num[mid] < 0:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        

        def find_min_pos(num):
            left, right = 0, len(num) - 1
            while left < right:
                mid = (left + right) // 2
                if num[mid] > 0:
                    right = mid - 1
                else:
                    left = mid + 1
            return left
        
        max_neg = find_max_neg(nums)
        min_pos = find_min_pos(nums)
        return max(max_neg, (len(nums) - min_pos))
    

    def solution3(nums):
        neg = bisect_left(nums, 0)
        pos = len(nums) - bisect_right(nums, 0)
        return max(neg, pos)

nums = [-2,-1,-1,1,2,3]
print(max_pos_or_neg.solution2(nums))



