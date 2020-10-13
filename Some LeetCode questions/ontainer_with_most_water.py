class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max1 = 0
        while(left<right):
            min1 = min(height[left],height[right])
            max1 = max(max1, min1*(right-left))
            if(height[left]>height[right]):
                right-=1
            else:
                left+=1
        return max1