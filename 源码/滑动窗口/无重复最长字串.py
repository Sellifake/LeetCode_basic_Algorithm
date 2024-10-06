class max_len():
    def silde_window(s):
        n = len(s)
        left = ans = 0
        window = set()
        for right in range(n):
            while s[right] in window:
                window.remove(s[left])
                left += 1
            window.add(s[right])
            ans = max(ans, right - left + 1)
        return ans
    

s = "pwwkew"
print(max_len.silde_window2(s))