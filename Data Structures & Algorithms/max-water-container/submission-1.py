class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # 2 pointers
        max_area=0
        i=0
        j=len(heights)-1
        while i<j:
            width = j - i
            height = min(heights[i], heights[j])
            area = height * width
            max_area = max(max_area, area)

            if heights[i]<heights[j]:
                i+=1
            elif heights[i]>heights[j]:
                j-=1
            elif heights[i]==heights[j]:
                i+=1
        
        return max_area