#O(1) space
#initial thought -> brute force. check every pair -> unoptimal
#two pointers, l and r. 
#ex:
#[1,2,3,4], target = 3. cursum = 4
#l    r
class Solution:
    def twoSum(self, numbers:List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            cursum = numbers[r] + numbers[l] #5
            if cursum > target:
                r -= 1
            elif cursum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []

    

        