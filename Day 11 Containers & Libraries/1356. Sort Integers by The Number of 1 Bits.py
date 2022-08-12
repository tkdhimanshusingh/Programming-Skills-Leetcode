class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        l = []
        arr.sort()
        for i in arr:
            l.append(bin(i))
        l.sort(key= lambda x: len([i for i in x if i=="1"]))
        res = []
        for i in l: res.append(int(i,2))
        return res