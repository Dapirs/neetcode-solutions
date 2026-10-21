class Solution:
    def isPalindrome(self, s: str) -> bool:
        str = "".join(s.split()).strip().lower()
        i=0
        j=len(str)-1

        while i<j:
            while (not str[i].isalnum()) and (i<j):
                i+=1
            while (not str[j].isalnum()) and (i<j):
                j-=1
            
            if str[i]!=str[j]:
                return False
            i+=1
            j-=1
        
        return True