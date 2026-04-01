class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uni_chars = set()
        l = 0
        max_ = 0
        for r, n in enumerate (s):
            while n in uni_chars:
                uni_chars.remove(s[l])
                l+=1
            uni_chars.add(n)
            max_ = max(max_, r-l+1)
        return max_

        