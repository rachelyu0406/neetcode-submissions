class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # as you iterate through the array keep the first row (determines which col to set to 0) and first col without the first row as markers for what to set to zero for the rest of the array
        # have O(1) space boolean to know if first row should be set to 0
        # space = O(1)
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0

        
        