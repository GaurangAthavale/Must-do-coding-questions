def largestRectangleArea(self, heights: List[int]) -> int:
    if(len(heights) == 0):
        return 0
    else:
        left = [-1]
        right = [len(heights)]
        s = []
        s.append(0)
        for i in range(1,len(heights)):
            # s.append(heights[i])
            if(heights[i]>heights[s[-1]]):
                left.append(s[-1])
                s.append(i)
            else:
                while(len(s)>0 and heights[i]<=heights[s[-1]]):
                    s.pop()
                if(len(s)>0):
                    left.append(s[-1])
                else:
                    left.append(-1)
                s.append(i)
        print(left)
        s = []
        s.append(len(heights)-1)
        for i in range(len(heights)-2,-1,-1):
            # s.append(heights[i])
            if(heights[i]>heights[s[-1]]):
                right.append(s[-1])
                s.append(i)
            else:
                while(len(s)>0 and heights[i]<=heights[s[-1]]):
                    s.pop()
                if(len(s)>0):
                    right.append(s[-1])
                else:
                    right.append(len(heights))
                s.append(i)
        right = right[::-1]
        print(right)

        max1 = -1
        for i in range(len(heights)):
            # print()
            if((right[i]-left[i]-1)*heights[i]>max1):
                max1 = (right[i]-left[i]-1)*heights[i]
        # print(max1)
        return max1