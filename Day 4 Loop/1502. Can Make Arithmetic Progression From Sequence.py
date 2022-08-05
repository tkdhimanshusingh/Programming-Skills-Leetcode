class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff=arr[0]-arr[1]
        for i in range(1,len(arr)):
            if not (diff==arr[i-1]-arr[i]):
                return False
        return True
        