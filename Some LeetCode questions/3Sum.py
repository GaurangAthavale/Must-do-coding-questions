class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(0,len(nums)-2):
            if(i == 0 or (i>0 and nums[i]!=nums[i-1])):
                left = i+1
                right = len(nums)-1
                sum1 = -1*nums[i]
                while(left<right):
                    a = []
                    if(nums[left] + nums[right] == sum1):
                        a.append(nums[left])
                        a.append(nums[right])
                        a.append(nums[i])
                        while(left<right and nums[left] == nums[left+1]):
                            left+=1
                        while(left<right and nums[right] == nums[right-1]):
                            right-=1 
                        left+=1
                        right-=1
                        ans.append(a)
                    elif(nums[left] + nums[right] > sum1):
                        right-=1
                    else:
                        left+=1
        return ans   
                
                