class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash ={}
        if len(s)!=len(t):
            return False
        else:
            for i in range(len(s)):
                if s[i] not in hash:
                    hash[s[i]]=1
                else:
                    hash[s[i]]+=1
            
            for i in range(len(t)):
                if t[i] not in hash or hash[t[i]]==0:
                    return False
                hash[t[i]]-=1
                
        return True
                    