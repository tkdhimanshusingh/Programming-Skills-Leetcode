class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum = 0 
        ln = len(mat)
        for row in range(ln):
            sum += mat[row][row] + mat[row][ln - row - 1]
        
        if ln % 2 != 0:
            sum -= mat[ln//2][ln//2]
        return sum