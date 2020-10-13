class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        result = []
        for i in range(len(nums)):
            diff = target - nums[i]
            if(diff in d):
                result.append(i)
                result.append(d[diff])
                return result
            else:
                d[nums[i]] = i
        return result