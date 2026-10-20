class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash={}
        maximum=[]
        origin=0
        for num in nums:
            if num not in hash:
                hash[num]=1
            else:
                hash[num]+=1
        
        bucket = [[] for x in range(len(nums)+1)]
        for num in hash:
            bucket[hash[num]].append(num)
        
        for i in range(len(bucket)-1,0,-1):
            for num in bucket[i]:
                maximum.append(num)
                if len(maximum)==k:
                    return maximum