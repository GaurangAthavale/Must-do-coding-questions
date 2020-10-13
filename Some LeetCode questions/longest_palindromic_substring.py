def expand(s,left,right):
    if(len(s) == 0 or right<left):
        return 0
    
    while(left>=0 and right<len(s) and s[left] == s[right]):
        left-=1
        right+=1
    
    return right - left - 1

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if(len(s) == 0):
            return ""
        
        start = 0
        end = 0
        
        for i in range(len(s)):
            l1 = expand(s,i,i)
            l2 = expand(s,i,i+1)
            length = max(l1,l2)
            
            if(length > end-start):
                start = i - (length-1)//2   # because i is in the middle. Therfeore, we subtract (length-1)//2 from i for start
                end = i + length//2         #and add (length)//2 to i for end
            
        return s[start:end+1]