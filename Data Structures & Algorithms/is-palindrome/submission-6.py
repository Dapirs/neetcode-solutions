class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=''.join(s.split()).strip().lower()
        new = ""
        for i in range(len(s)):
            if s[i].isalnum():
                new+=s[i]
        if new==new[::-1]:
            return True
        return False
