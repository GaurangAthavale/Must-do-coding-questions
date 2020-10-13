class Solution:
    def threeSumClosest(self, a: List[int], target: int) -> int:
        n = len(a)
        a.sort()
        result = a[0] + a[1] + a[n-1]
        for i in range(n):
            l = i+1
            h = n-1
            while(l<h):
                current = a[i] + a[l] + a[h]
                if(current>target):
                    h-=1
                else:
                    l+=1
                if(abs(current-target)<abs(result-target)):
                    result = current
        return result