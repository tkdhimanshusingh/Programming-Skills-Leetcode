class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product=1
        for i in nums:
            product*=i
        return self.signFunc(product)
    def signFunc(self,p):
        if p>0:
            return 1
        elif p<0:
            return -1
        else:
            return 0