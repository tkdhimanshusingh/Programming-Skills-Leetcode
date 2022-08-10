class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderLst = list(order)
        counter = 0
        dict = {}
        for i in orderLst:
            dict[i] = counter
            counter += 1
        wordsLst = []
        for k in words:
            kValueLst = []
            for j in k:
                kValueLst.append(dict[j])
            wordsLst.append(kValueLst)
        result = True
        for y in range(len(wordsLst)-1):
            if wordsLst[y] > wordsLst[y+1]:
                result = False
        return result