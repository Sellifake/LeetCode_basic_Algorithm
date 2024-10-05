class minSubArrayLen:
    def brute_force(nums, target):
        n = len(nums)
        ans = n+1
        for i in range(n):
            total = 0
            for j in range(i,n):
                total += nums[j]
                if total >= target:
                    ans = min(ans, j-i+1)
        return ans if ans <= n else 0
    
    def sliding_window(nums, target):
        n = len(nums)
        ans = n+1
        left = 0
        s = 0
        for right,x in enumerate(nums):
            s += x
            while s >= target:
                ans = min(ans, right-left+1)
                s -= nums[left]
                left += 1
        return ans if ans <= n else 0
nums = [1,4,4]
target = 1
a = minSubArrayLen.sliding_window(nums, target)
print(a) 
