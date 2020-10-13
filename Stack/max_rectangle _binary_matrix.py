class Solution:
    def MAH(self,heights):
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
        # print(left)
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
        # print(right)

        max1 = -1
        for i in range(len(heights)):
            # print()
            if((int(right[i])-int(left[i])-1)*int(heights[i])>max1):
                max1 = (int(right[i])-int(left[i])-1)*int(heights[i])
        # print(max1)
        return max1
    
    
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if(len(matrix) == 0):
            return 0
        else:
            max1 = -1
            # val = matrix[0]
            val = [int(i) for i in matrix[0]]
            ans = self.MAH(val)
            max1 = max(ans,max1)
            for i1 in range(1,len(matrix)):
                for j1 in range(len(matrix[i1])):
                    if(matrix[i1][j1] == "0"):
                        val[j1] = 0
                        # print("hi")
                    else:
                        val[j1]+=int(matrix[i1][j1])
                    # print("val",val)
                ans = self.MAH(val)
                max1 = max(ans,max1)
            return max1                