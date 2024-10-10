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
        ans = n + 1  # 初始化答案为一个不可能的较大值（比数组长度还大）
        left = 0  # 窗口左边界，初始为0
        s = 0  # 当前窗口内的元素和
        
        # 遍历整个数组，right 是窗口右边界
        for right, x in enumerate(nums):
            s += x  # 将当前元素加入窗口和
            
            # 当窗口内的和大于等于目标值时，尝试收缩窗口
            while s >= target:
                # 更新最小长度
                ans = min(ans, right - left + 1)
                # 移动左边界，减少窗口内的和，以期寻找更小的满足条件的子数组
                s -= nums[left]
                left += 1

        # 如果 `ans` 没有被更新，返回 0，否则返回最小子数组的长度
        return ans if ans <= n else 0

    
nums = [1,4,4]
target = 1
a = minSubArrayLen.sliding_window(nums, target)
print(a) 
# 初始化一个空字符串