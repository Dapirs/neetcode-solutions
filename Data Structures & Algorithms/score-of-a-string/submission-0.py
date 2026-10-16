class Solution:
    def scoreOfString(self, s: str) -> int:
        hash={}
        for letter in s:
            hash[letter]=ord(letter)
        sum=0
        for i in range(1, len(s)):
            if hash[s[i]]>=hash[s[i-1]]:
                sum = sum + (hash[s[i]]-hash[s[i-1]])
            else:
                sum = sum + (hash[s[i-1]]-hash[s[i]])
        return sum