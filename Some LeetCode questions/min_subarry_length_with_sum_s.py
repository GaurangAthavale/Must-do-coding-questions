class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        left = 0
        result = float("inf")
        current = 0
        
        for i in range(len(nums)):
            current += nums[i]
            
            while(current >= s):
                result = min(result, i-left+1)
                current-=nums[left]
                left+=1
            
        if(result == float("inf")):
            return 0
        else:
            return result