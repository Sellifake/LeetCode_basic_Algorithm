class recieve_rainwater():
    @property
    def divide_and_conquer(num):
        n = len(num)

        pro_max = [0] * n  
        pro_max[0] = num[0]
        for i in range(1, n):
            pro_max[i] = max(pro_max[i - 1], num[i])

        suf_max = [0] * n
        suf_max[n - 1] = num[n - 1]
        for i in range(n - 2, -1, -1):
            suf_max[i] = max(suf_max[i + 1], num[i])
        
        res = 0
        for h, pre, suf in zip(num, pro_max, suf_max):
            res += min(pre, suf) - h

        return res

    def double_pointer(num):
        n = len(num)
        left = ans = pre_max = suf_max = 0
        right = n - 1
        while left < right:
            pre_max = max(pre_max, num[left])
            suf_max = max(suf_max, num[right])
            if pre_max < suf_max:
                ans += pre_max - num[left]
                left += 1
            else:
                ans += suf_max - num[right]
                right -= 1
        return ans
    


num = [0,1,0,2,1,0,1,3,2,1,2,1]
a = recieve_rainwater.divide_and_conquer
print(a)


