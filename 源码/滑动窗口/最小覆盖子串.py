from collections import Counter, defaultdict


class min_sub_cover_str:
    def solution1(s, t):
        ans_left, ans_right = -1, len(s)
        cnt_s = Counter()
        cnt_t = Counter(t)

        left = 0
        for right, c in enumerate(s):
            cnt_s[c] += 1
            while cnt_s >= cnt_t:
                if right - left < ans_right - ans_left:
                    ans_left, ans_right = left, right
                cnt_s[s[left]] -= 1
                left += 1
        return "" if ans_left < 0 else s[ans_left: ans_right + 1]
    
    def solution2(s, t):
        ans_left, ans_right = -1, len(s)
        cnt = defaultdict(int)
        for ele in t:
            cnt[ele] += 1
        less = len(cnt)
        
        left = 0
        for right, c in enumerate(s):
            cnt[c] -= 1
            if cnt[c] == 0:
                less -= 1
            while less == 0:
                if right - left < ans_right - ans_left:
                    ans_left, ans_right = left, right
                x = s[left]
                if cnt[x] == 0:
                    less += 1
                cnt[x] += 1
                left += 1
        return "" if ans_left < 0 else s[ans_left: ans_right + 1]

s = "ADOBECODEBANC"
t = "ABC"
print(min_sub_cover_str.solution2(s, t))

