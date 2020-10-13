class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # return [nums.count(2)]
        if(len(nums)>0):
            nums.sort()
            ans = [nums[0]]
            dp = [1 for i in range(len(nums))]
            max1 = 1
            print(nums)
            for i in range(1,len(nums)):
                # val = [nums[i]]
                for j in range(i):
                    if(nums[i]%nums[j] == 0):
                        if(dp[j]+1>dp[i]):
                            dp[i] = dp[j]+1

            print(dp)
            max1 = max(dp)
            prev = -1
            val = []
            for i in range(len(dp)-1,-1,-1):
                if(max1 == 0):
                    break
                else:
                    if(max1 == dp[i] and (prev%nums[i] == 0 or prev==-1)):
                        val.append(nums[i])
                        prev = nums[i]
                        max1-=1
            print(val)
            return val   

        else:
            return []