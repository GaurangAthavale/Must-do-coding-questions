def trap(self, heights: List[int]) -> int:
    if(len(heights)==0):
        return 0
    else:
        left = [0]*len(heights)
        right = [0]*len(heights)
        left[0] = heights[0]
        right[-1] = heights[-1]
        for i in range(1,len(heights)):
            if(heights[i]>left[i-1]):
                left[i] = heights[i]
            else:
                left[i] = left[i-1]
        for i in range(len(heights)-2,-1,-1):
            if(heights[i]>right[i+1]):
                right[i] = heights[i]
            else:
                right[i] = right[i+1]
        # print(left)
        # print(right)
        count = 0
        for i in range(len(heights)):
            count+=(min(left[i],right[i])-heights[i])
        # print(count)
        return count
