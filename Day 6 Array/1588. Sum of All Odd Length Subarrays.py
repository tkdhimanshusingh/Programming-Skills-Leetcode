class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0
        for l in range(1, n + 1, 2):
            for i in range(n - l + 1):
                ans += sum(arr[i:i + l])
        return ans