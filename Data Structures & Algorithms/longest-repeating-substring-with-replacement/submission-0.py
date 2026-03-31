class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} #char -> frequency
        res = 0 #maximum valid window length so far
        l = 0 #left pointer
        maxf = 0 #count of the most frequent char in the current window
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])
            while (r-l+1) - maxf > k: #r-l +1 is window size - maxf = how many chars need replacement:
                count[s[l]] -= 1
                l+= 1
            res = max(res,r-l+1)
        return res



        