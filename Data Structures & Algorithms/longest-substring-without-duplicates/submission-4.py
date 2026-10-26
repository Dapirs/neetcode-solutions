class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lemon=set()
        j=0
        max_length=0
        for i in range(len(s)):
            while s[i] in lemon:
                lemon.remove(s[j])
                j+=1
            lemon.add(s[i])
            max_length = max(max_length, i-j+1)
        return max_length
        