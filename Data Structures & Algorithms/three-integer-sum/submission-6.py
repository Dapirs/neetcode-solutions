class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        output=[]
        for i in range(len(nums)-2):
            j=i+1
            k=len(nums)-1
            while (j<k):
                if nums[i]+nums[j]+nums[k]>0:
                    k-=1
                elif nums[i]+nums[j]+nums[k]<0:
                    j+=1
                else:
                    output.append([nums[i],nums[j],nums[k]])
                    k-=1
                    j+=1
        
        for i in range(len(output)):
            output[i]=sorted(output[i])
            output[i]=tuple(output[i])
        
        output = list(set(output))

        for i in range(len(output)):
            output[i]=list(output[i])
        
        return output

    # this algo doesnt detect duplicates but removes them later with extra loops so it may be inefficient