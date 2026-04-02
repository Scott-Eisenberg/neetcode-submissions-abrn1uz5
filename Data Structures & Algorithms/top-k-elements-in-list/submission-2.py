class Solution:
    def topKFrequent(self, nums:List[int], k:int) -> List[int]:
        count = {} #num -> frequency (unsorted). 
        freq = [[] for i in range(len(nums) + 1)]#frequency(unsorted) -> sort
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        ret = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                ret.append(num)
                if len(ret) == k:
                    return ret



            

        
        