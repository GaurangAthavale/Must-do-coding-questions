class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if(len(matrix)>0):
            a = []
            top = 0
            bottom = len(matrix)-1
            left = 0
            right = len(matrix[0])-1
            size = len(matrix)*len(matrix[0])
            while(len(a)<size):
                if(len(a)<size):
                    for i in range(left,right+1):
                        a.append(matrix[top][i])
                    top+=1
                    
                if(len(a)<size):
                    for i in range(top,bottom+1):
                        a.append(matrix[i][right])
                    right-=1
                    
                if(len(a)<size):
                    for i in range(right, left-1, -1):
                        a.append(matrix[bottom][i])
                    bottom-=1
                    
                if(len(a)<size):
                    for i in range(bottom, top-1, -1):
                        a.append(matrix[i][left])
                    left+=1

            return a
        else:
            return []
                