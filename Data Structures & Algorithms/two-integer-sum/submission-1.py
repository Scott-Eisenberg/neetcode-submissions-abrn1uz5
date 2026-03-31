class Solution:
    def twoSum(self, nums:List[int], target:int) -> List[int]:
        seen = {} #hash map (dictionaries in python are hash)
        for i,j in enumerate(nums): #where i is index, and j is value
            difference = target - j
            if difference in seen: #return seen[diff], i
                return [seen[difference], i]
            seen[j] = i


        