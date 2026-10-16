class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        hash = {}
        for i in range(len(arr)):
            max = 0
            for j in range(i+1,len(arr)):
                if arr[j]>max:
                    max = arr[j]
            arr[i] = max
            if i == len(arr)-1:
                arr[i] = -1

        return arr