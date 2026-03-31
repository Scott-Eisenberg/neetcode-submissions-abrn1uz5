class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
    def decode(self, s: str) -> List[str]: #5#Hello5#World -> ["Hello", "World"]
        res = []
        i = 0 #where the chunk starts
        while i < len(s):
            j = i #i and j start at same position
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1 #in first run, now set to H / index 2
            j = i + length
            res.append(s[i:j])
            i = j
        return res






