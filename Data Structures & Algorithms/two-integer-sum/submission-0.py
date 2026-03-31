class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} #val -> index
        for i, n in enumerate(nums): #i = index, n = value
            diff = target - n
            if diff in seen:
                return [seen[diff], i]
            seen[n] = i

        