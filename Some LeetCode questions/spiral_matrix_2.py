class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        a = [[0 for i in range(n)] for i in range(n)]
        i1 = 1
        
        left = 0
        top = 0
        bottom = len(a)-1
        right = len(a[0])-1
        
        while(i1<=n**2):
            for i in range(left,right+1):
                a[top][i] = i1
                i1+=1
            top+=1
            
            for i in range(top,bottom+1):
                a[i][right] = i1
                i1+=1
            right-=1
            
            for i in range(right,left-1,-1):
                a[bottom][i] = i1
                i1+=1
            bottom-=1
            
            for i in range(bottom,top-1,-1):
                a[i][left] = i1
                i1+=1
            left+=1
        return a