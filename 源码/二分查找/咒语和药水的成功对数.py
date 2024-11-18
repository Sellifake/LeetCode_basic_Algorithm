class successfulPairs:
    def solution1(potions, success):
        def binary_search(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] * target >= success:
                    right = mid - 1
                else: 
                    left = mid + 1
            return left
        
        potions.sort()
        ans = [0] * len(spells)
        for i in range(len(spells)):
            index = binary_search(potions, spells[i])
            ans[i] = len(potions) - index
        return ans

spells = [5,1,3]
potions = [1,2,3,4,5]
success = 7
print(successfulPairs.solution1(spells, potions, success))
