class Solution:
    def topKFrequent(self, nums: List[int], target:int) -> List[int]:
        count = {} #key is number, val is frequency
        for num in nums:
            count[num] = 1 + count.get(num,0) #count = number -> freq (unsorted). freq -> result(sorted)
        freq = [[] for i in range(len(nums) + 1)]
        for key, val in count.items():
            freq[val].append(key)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == target:
                    return res


            

        
        