class Solution:
    def isPalindrome(self, s: str) -> bool:
        str = "".join(s.split()).strip().lower()
        i=0
        j=len(str)-1

        while i<j:
            while (not str[i].isalnum() or not str[j].isalnum()) and (i<j):
                if not str[i].isalnum():
                    i+=1
                if not str[j].isalnum():
                    j-=1
            
            if str[i]==str[j] and (i<j):
                i+=1
                j-=1
            elif str[i]!=str[j] and (i<j):
                return False
        
        return True