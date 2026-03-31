class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #at each index of the input, the corresponding output index
        #should be the product of the val at said index from the left
        #multiplied, by the val of said index from the right
        res = [1] * len(nums) 
        #first, handle the lefthand pass
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix  
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
#[1,2,3,4], res = [1, 1, 2, 6] -> [24, 12, 8, 6]
        