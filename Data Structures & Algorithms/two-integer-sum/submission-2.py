class Solution:
    def twoSum(self, nums: List[int], target:int) -> List[int]:
        prevMap = {}
        for i, n in enumerate(nums):
            curr = target - n
            if curr in prevMap:
                return [prevMap[curr], i]
            prevMap[n] = i


        