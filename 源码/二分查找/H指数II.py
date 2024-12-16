class Solution:
    def hIndex(self, citations):
        left = 1
        right = len(citations)
        while left <= right:  
            mid = (left + right) // 2
            if citations[-mid] >= mid:
                left = mid + 1  
            else:
                right = mid - 1  

        return right

citations = [0,0,0]
print(Solution().hIndex(citations))