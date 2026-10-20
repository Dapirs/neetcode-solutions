class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash={}
        anagram=[]
        for str in strs:
            sorted_str = ''.join(sorted(str))
            if sorted_str not in hash:
                hash[sorted_str]=[]
            hash[sorted_str].append(str)
        
        for str in hash:
            anagram.append(hash[str])
        
        return anagram